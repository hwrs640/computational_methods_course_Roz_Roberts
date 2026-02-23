import numpy as np
from scipy.interpolate import interp1d

def make_forcing_interpolants(t_forcing, P_series, T_series,
                              kind="linear",
                              extrapolate=False):
    """
    Create callable functions P(t), T(t) from discrete forcing time series.

    Parameters
    ----------
    t_forcing : (N,) array
        Forcing times in the same units you will use in solve_ivp.
    P_series : (N,) array
        Precip forcing values at t_forcing.
    T_series : (N,) array
        Temperature (or other) forcing values at t_forcing.
    kind : str
        Interpolation kind for interp1d ('linear', 'nearest', 'previous', etc.).
    extrapolate : bool
        If True, extrapolate beyond forcing range. If False, hold end values.

    Returns
    -------
    P_of_t, T_of_t : callables
        Functions that accept scalar t (float) and return scalar forcing.
    """
    t_forcing = np.asarray(t_forcing, dtype=float)
    P_series = np.asarray(P_series, dtype=float)
    T_series = np.asarray(T_series, dtype=float)

    if t_forcing.ndim != 1:
        raise ValueError("t_forcing must be 1D")
    if P_series.shape != t_forcing.shape or T_series.shape != t_forcing.shape:
        raise ValueError("P_series and T_series must have the same shape as t_forcing")

    # Ensure sorted by time (interp1d expects increasing x)
    sort_idx = np.argsort(t_forcing)
    t_sorted = t_forcing[sort_idx]
    P_sorted = P_series[sort_idx]
    T_sorted = T_series[sort_idx]

    if extrapolate:
        fill = "extrapolate"
    else:
        # Hold constant at the ends if asked beyond the forcing range
        fill = (P_sorted[0], P_sorted[-1])
    P_of_t = interp1d(
        t_sorted, P_sorted,
        kind=kind,
        bounds_error=False,
        fill_value=fill,
        assume_sorted=True
    )

    if extrapolate:
        fillT = "extrapolate"
    else:
        fillT = (T_sorted[0], T_sorted[-1])
    T_of_t = interp1d(
        t_sorted, T_sorted,
        kind=kind,
        bounds_error=False,
        fill_value=fillT,
        assume_sorted=True
    )

    return P_of_t, T_of_t

def make_rhs(P_of_t, T_of_t, a, b, c, clamp_storage=True):
    """
    Returns a function f(t, y) that compute dS/dt using interpolated forcings.

    dS/dt = P(t) - a * max(T(t), 0) - b * S(t)^c
    """
    a = float(a)
    b = float(b)
    c = float(c)

    def rhs(t, y):
        # y is array-like; single state S is y[0]
        S = float(y[0])

        P = float(P_of_t(t))
        T = float(T_of_t(t))

        T_pos = max(T, 0.0)

        if clamp_storage:
            S_eff = max(S, 0.0)
        else:
            S_eff = S

        dSdt = P - a * T_pos - b * (S_eff ** c)

        return [dSdt]  # must be iterable length 1

    return rhs


from scipy.integrate import solve_ivp

# Example forcing
t_forcing = np.array([0, 1, 2, 3, 4, 5], dtype=float)
P_series  = np.array([0, 10, 0, 0, 5, 0], dtype=float)
T_series  = np.array([-2, 1, 3, -1, 0, 2], dtype=float)

P_of_t, T_of_t = make_forcing_interpolants(
    t_forcing, P_series, T_series,
    kind="previous",       # stepwise forcing (common for daily inputs)
    extrapolate=False
)

# Parameters
a = 0.8
b = 0.05
c = 1.2

rhs = make_rhs(P_of_t, T_of_t, a=a, b=b, c=c, clamp_storage=True)

# Integrate
t_span = (t_forcing[0], t_forcing[-1])
S0 = [0.0]

t_eval = np.linspace(t_span[0], t_span[1], 200)

sol = solve_ivp(
    rhs,
    t_span=t_span,
    y0=S0,
    t_eval=t_eval,
    method="RK45",
    rtol=1e-6,
    atol=1e-9
)
print(sol)
# sol.t -> times, sol.y[0] -> S(t)