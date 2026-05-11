import marimo

__generated_with = "0.20.4"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Redstart: A Lightweight Reusable Booster
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.image(src="public/images/redstart.png")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Project Redstart is an attempt to design the control systems of a reusable booster during landing.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In principle, it is similar to SpaceX's Falcon Heavy Booster.

    >The Falcon Heavy booster is the first stage of SpaceX's powerful Falcon Heavy rocket, which consists of three modified Falcon 9 boosters strapped together. These boosters provide the massive thrust needed to lift heavy payloads—like satellites or spacecraft—into orbit. After launch, the two side boosters separate and land back on Earth for reuse, while the center booster either lands on a droneship or is discarded in high-energy missions.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.center(
        mo.Html("""
    <iframe width="560" height="315" src="https://www.youtube.com/embed/RYUr-5PYA7s?si=EXPnjNVnqmJSsIjc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>""")
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Dependencies
    """)
    return


@app.cell
def _():
    import scipy
    import scipy.integrate as sci

    import matplotlib as mpl
    import matplotlib.pyplot as plt

    import numpy as np
    import numpy.linalg as la

    return np, plt, sci


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## The Model

    The Redstart booster in model as a rigid tube of length $\ell$ and negligible diameter whose mass $M$ is uniformly spread along its length. It may be located in 2D space by the coordinates $(x, y)$ of its center of mass and the angle $\theta$ it makes with respect to the vertical (with the convention that $\theta > 0$ for a left tilt, i.e. the angle is measured counterclockwise)

    This booster has an orientable reactor at its base ; the force that it generates is of amplitude $f \geq 0$ and the angle of the force with respect to the booster axis is $\phi$ (with a counterclockwise convention).

    We assume that the booster is subject to gravity, the reactor force and that the friction of the air is negligible.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.center(mo.image(src="public/images/geometry.svg"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Constants

    For the sake of simplicity (this is merely a toy model!) in the sequel we assume that:

    - the total length $\ell$ of the booster is 2 meters,
    - its mass $M$ is 1 kg,
    - the gravity constant $g$ is 1 m/s^2.

    This set of values is completely unrealistic, but very simple! It will simplify our computations and will not fundamentally impact the structure of the booster dynamics.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Getting Started
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Constants

    Define the Python constants `g`, `M` and `l` that correspond to the gravity constant, the mass and length of the booster.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### According to the model described above, we have:
    """)
    return


@app.cell
def _():
    g = 1.0      # gravity constant
    M = 1.0      # booster mass
    l = 2.0      # length of the booster
    return M, g, l


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Forces

    Compute the cartesian coordinates $f_x$ and $f_y$ of the force applied to the booster by the reactor, functions of $f$, $\theta$ and $\phi$.
    """)
    return


@app.cell
def _(np):
    def f_reactor(f, theta, phi):
        return np.array([
            -f * np.sin(theta + phi),
            f * np.cos(theta + phi),
        ])


    def fx(f, theta, phi):
        return f_reactor(f, theta, phi)[0]


    def fy(f, theta, phi):
        return f_reactor(f, theta, phi)[1]

    return fx, fy


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Center of Mass

    Give the ordinary differential equation that governs the evolution of the position $(x, y)$ of the center of mass of the booster.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    According to Newton's second law, the motion of the center of mass is governed by

    $$
    M\vec{a} = \sum \vec{F}.
    $$

    The booster is subject to two forces:

    - gravity, directed downward:

    $$
    M
    \begin{pmatrix}
    0 \\
    -g
    \end{pmatrix}
    $$

    - the reactor force:

    $$
    f
    \begin{pmatrix}
    -\sin(\theta+\phi) \\
    \cos(\theta+\phi)
    \end{pmatrix}
    $$

    Therefore, in Cartesian coordinates, we obtain

    $$
    M
    \begin{pmatrix}
    \ddot{x} \\
    \ddot{y}
    \end{pmatrix}
    =
    M
    \begin{pmatrix}
    0 \\
    -g
    \end{pmatrix}
    +
    f
    \begin{pmatrix}
    -\sin(\theta+\phi) \\
    \cos(\theta+\phi)
    \end{pmatrix}.
    $$

    Hence,

    $$
    \ddot{x}
    =
    -\frac{f}{M}\sin(\theta+\phi)
    $$

    and

    $$
    \ddot{y}
    =
    \frac{f}{M}\cos(\theta+\phi)-g.
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Moment of inertia

    Compute the [moment of inertia](https://en.wikipedia.org/wiki/Moment_of_inertia) $J$ of the booster and define the corresponding Python variable `J`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The booster is modeled as a thin rigid rod of total length \(\ell\), with negligible diameter. The rotation axis passes through the center of mass.

    Since the mass is uniformly distributed along the booster, the linear mass density is

    $$
    \lambda = \frac{M}{\ell}.
    $$

    The moment of inertia is therefore

    $$
    J = \int_{-\ell/2}^{\ell/2} x^2 \lambda \, dx.
    $$

    Thus,

    $$
    J = \int_{-\ell/2}^{\ell/2} x^2 \frac{M}{\ell} \, dx.
    $$

    So,

    $$
    J = \frac{M}{\ell}
    \int_{-\ell/2}^{\ell/2} x^2 \, dx.
    $$

    Now,

    $$
    \int_{-\ell/2}^{\ell/2} x^2 \, dx
    =
    \left[
    \frac{x^3}{3}
    \right]_{-\ell/2}^{\ell/2}.
    $$

    Therefore,

    $$
    \int_{-\ell/2}^{\ell/2} x^2 \, dx
    =
    \frac{\ell^3}{12}.
    $$

    Hence,

    $$
    J
    =
    \frac{M}{\ell}
    \cdot
    \frac{\ell^3}{12}
    =
    \frac{1}{12}M\ell^2.
    $$
    """)
    return


@app.cell
def _(M, l):
    J = (1 / 12) * M * l**2
    return (J,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Tilt

    Give the ordinary differential equation that governs the evolution of the tilt angle $\theta$.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The only force that creates a torque around the center of mass is the reactor force. Gravity does not create a torque because it is applied at the center of mass.

    The reactor is located at the base of the booster. Since \(\ell\) is the total length of the booster, the distance from the center of mass to the base is

    $$
    \frac{\ell}{2}.
    $$

    The torque generated by the reactor force is

    $$
    \tau
    =
    -\frac{\ell}{2} f \sin(\phi).
    $$

    The rotational equation of motion is

    $$
    J\ddot{\theta} = \tau.
    $$

    Therefore,

    $$
    J\ddot{\theta}
    =
    -\frac{\ell}{2} f \sin(\phi).
    $$

    Hence,

    $$
    \ddot{\theta}
    =
    -\frac{\ell f}{2J}\sin(\phi).
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Vector Field

    Denote

    - $v_x =\dot{x}$, $v_y = \dot{y}$ the components of the booster center of mass velocity,
    - $\omega = \dot{\theta}$ the angular velocity of the booster.


    What is is dimension $n$ of the state space?
    What is the state $s \in \R^n$ of the booster dynamics?
    Provide the definition of the function $F : \mathbb{R}^{n + 2} \to \mathbb{R}^n$ such that the system evolves
    according to

    $$
    \dot{s} = F(s, f, \phi).
    $$
    """)
    return


@app.cell
def _(J, M, fx, fy, g, l, np):
    def F(s, f, phi):
        x, vx, y, vy, theta, omega = s

        return np.array([
            vx,
            fx(f, theta, phi) / M,
            vy,
            fy(f, theta, phi) / M - g,
            omega,
            -(l * f / (2 * J)) * np.sin(phi),
        ])

    return (F,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We define the state vector as

    $$
    s =
    (x, v_x, y, v_y, \theta, \omega)
    \in \mathbb{R}^6,
    $$

    where

    $$
    v_x = \dot{x},
    \qquad
    v_y = \dot{y},
    \qquad
    \omega = \dot{\theta}.
    $$

    Therefore, the dimension of the state space is

    $$
    n = 6.
    $$

    The system evolves according to

    $$
    \dot{s} = F(s, f, \phi).
    $$

    Using the equations of motion, we obtain

    $$
    \dot{s}
    =
    \begin{pmatrix}
    \dot{x} \\
    \dot{v}_x \\
    \dot{y} \\
    \dot{v}_y \\
    \dot{\theta} \\
    \dot{\omega}
    \end{pmatrix}
    =
    \begin{pmatrix}
    v_x \\
    -\frac{f}{M}\sin(\theta+\phi) \\
    v_y \\
    \frac{f}{M}\cos(\theta+\phi)-g \\
    \omega \\
    -\frac{\ell f}{2J}\sin(\phi)
    \end{pmatrix}.
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Simulation

    Define a function `redstart_solve` that, given the input parameters:

    - `t_span`: a pair of initial time `t_0` and final time `t_f`,
    - `y0`: the value of `[x, vx, y, vy, theta, omega]` at `t_0`,
    - `f_phi`: a function that given the current time `t` and current state value `y`
         returns the values of the inputs `f` and `phi` in an array.

    returns:

    - `sol`: a function that given a time `t` returns the value of `[x, vx, y, vy, theta, omega]` at time `t` (and that also accepts 1d-arrays of times for multiple state evaluations).

    A typical usage would be:

    ```python
    def free_fall_example():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0] # [x, vx, y, vy, theta, omega]
        def f_phi(t, y):
            return np.array([0.0, 0.0]) # [f, phi]
        sol = redstart_solve(t_span, y0, f_phi)
        t = np.linspace(t_span[0], t_span[1], 1000)
        y_t = sol(t)[2]
        plt.plot(t, y_t, label=r"$y(t)$ (height in meters)")
        plt.plot(t, l * np.ones_like(t), color="grey", ls="--", label=r"$y=\ell$")
        plt.title("Free Fall")
        plt.xlabel("time $t$")
        plt.grid(True)
        plt.legend()
        return plt.gcf()
    free_fall_example()
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The goal of this part is to define a function `redstart_solve` that numerically solves the differential equation governing the motion of the booster.

    The state of the booster is

    $$
    s =
    (x, v_x, y, v_y, \theta, \omega).
    $$

    The dynamics of the system are given by

    $$
    \dot{s} = F(s, f, \phi),
    $$

    where \(f\) is the thrust magnitude and \(\phi\) is the angle of the reactor force with respect to the booster axis.

    Since the controls \(f\) and \(\phi\) may depend on time and on the current state, they are given by a function

    $$
    f_\phi(t, s).
    $$

    This function returns

    $$
    (f, \phi).
    $$

    To simulate the system, we use the function `scipy.integrate.solve_ivp`, which solves ordinary differential equations of the form

    $$
    \dot{s}(t) = G(t, s(t)).
    $$

    Here, the function \(G\) is obtained by first computing the current control inputs \(f\) and \(\phi\), then evaluating the vector field \(F\):

    $$
    G(t, s) = F(s, f, \phi).
    $$

    Therefore, for each time \(t\) and state \(s\), we compute

    $$
    (f, \phi) = f_\phi(t, s),
    $$

    then

    $$
    \dot{s} = F(s, f, \phi).
    $$

    The function `redstart_solve` takes as input:

    - `t_span`, the time interval of the simulation;
    - `y0`, the initial state;
    - `f_phi`, the function defining the control inputs.

    It returns a function `sol` such that, for any time \(t\),

    $$
    sol(t)
    $$

    gives the state of the booster at that time.
    """)
    return


@app.cell
def _(F, sci):
    def redstart_solve(t_span, y0, f_phi):
        def rhs(t, y):
            f, phi = f_phi(t, y)
            return F(y, f, phi)

        result = sci.solve_ivp(
            rhs,
            t_span,
            y0,
            dense_output=True,
            rtol=1e-9,
            atol=1e-9,
        )

        if not result.success:
            raise RuntimeError(result.message)

        return result.sol

    return (redstart_solve,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Freefall test


    In the `free_fall` example scenario. scenario, at what moment should the center of mass of the booster theoretically cross the
    height of $y = \ell$?

    Check your `redstart_solve` function in this scenario and produce a graph that allows us to check the above answer numerically/visually.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In the freefall scenario, the reactor is turned off:

    $$
    f=0.
    $$

    Therefore, the only force acting on the booster is gravity. The vertical equation of motion is

    $$
    \ddot y = -g.
    $$

    Since in this notebook

    $$
    g=1,
    $$

    we get

    $$
    \ddot y = -1.
    $$

    The initial conditions are

    $$
    y(0)=10,
    \qquad
    \dot y(0)=0.
    $$

    By integrating once, we obtain

    $$
    \dot y(t)=-t.
    $$

    By integrating again, we obtain

    $$
    y(t)=10-\frac{1}{2}t^2.
    $$

    The question asks when the center of mass crosses the height

    $$
    y=\ell.
    $$

    Therefore, we solve

    $$
    10-\frac{1}{2}t^2=\ell.
    $$

    In this notebook,

    $$
    \ell=2.
    $$

    Thus,

    $$
    10-\frac{1}{2}t^2=2.
    $$

    This gives

    $$
    \frac{1}{2}t^2=8,
    $$

    so

    $$
    t^2=16.
    $$

    Hence,

    $$
    t=4.
    $$

    Therefore, the center of mass theoretically crosses the height \(y=\ell\) at

    $$
    t=4.
    $$
    """)
    return


@app.cell
def _(g, l, np, plt, redstart_solve):
    def free_fall_example():
        t_span = [0.0, 5.0]

        y0 = [
            0.0,   # x(0)
            0.0,   # vx(0)
            10.0,  # y(0), center of mass height
            0.0,   # vy(0)
            0.0,   # theta(0)
            0.0,   # omega(0)
        ]

        def f_phi(t, y):
            return np.array([0.0, 0.0])

        sol = redstart_solve(t_span, y0, f_phi)

        t = np.linspace(t_span[0], t_span[1], 1000)
        states = sol(t)

        y_cm = states[2]

        theoretical_crossing_time = np.sqrt(2 * (10.0 - l) / g)

        plt.figure(figsize=(8, 5))

        plt.plot(t, y_cm, label=r"center of mass $y(t)$")

        plt.axhline(
            l,
            color="grey",
            linestyle="--",
            label=r"$y=\ell$",
        )

        plt.axvline(
            theoretical_crossing_time,
            color="black",
            linestyle=":",
            label=rf"$t={theoretical_crossing_time:.3f}$",
        )

        plt.title("Free Fall")
        plt.xlabel("time $t$")
        plt.ylabel("height of the center of mass $y(t)$")
        plt.grid(True)
        plt.legend()

        return plt.gcf()


    free_fall_example()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controlled Landing

    Assume that $x$, $\dot{x}$, $\theta$ and $\dot{\theta}$ are null at $t=0$ and that $y(0)= 10$ and $\dot{y}(0) = - 2$.

    Find a time-varying force $f(t)$ which, when applied in the booster axis ($\theta=0$), yields $y(5)=\ell / 2 = 1$ (the booster is at ground level) and $\dot{y}(5)=0$ (the booster is at rest).

    Simulate the corresponding scenario, display graphically the results and check that your solution works as expected.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We assume that initially

    $$
    x(0)=0,
    \qquad
    \dot{x}(0)=0,
    \qquad
    \theta(0)=0,
    \qquad
    \dot{\theta}(0)=0,
    $$

    and

    $$
    y(0)=10,
    \qquad
    \dot{y}(0)=-2.
    $$

    The goal is to find a time-varying thrust \(f(t)\), applied along the booster axis, such that at final time \(t=5\),

    $$
    y(5)=\frac{\ell}{2}
    $$

    and

    $$
    \dot{y}(5)=0.
    $$

    Since the thrust is applied along the booster axis, we take

    $$
    \phi = 0.
    $$

    Moreover, if the booster remains vertical, then

    $$
    \theta = 0.
    $$

    Therefore, the vertical equation of motion becomes

    $$
    \ddot{y} = \frac{f(t)}{M} - g.
    $$

    We choose a cubic polynomial trajectory for the center of mass:

    $$
    y(t)=at^3+bt^2+ct+d.
    $$

    Using the initial conditions,

    $$
    y(0)=10
    $$

    and

    $$
    \dot{y}(0)=-2,
    $$

    we get

    $$
    d=10
    $$

    and

    $$
    c=-2.
    $$

    Therefore,

    $$
    y(t)=at^3+bt^2-2t+10.
    $$

    Its derivative is

    $$
    \dot{y}(t)=3at^2+2bt-2.
    $$

    The final conditions are

    $$
    y(5)=\frac{\ell}{2}
    $$

    and

    $$
    \dot{y}(5)=0.
    $$

    Since in this notebook

    $$
    \ell=2,
    $$

    we have

    $$
    \frac{\ell}{2}=1.
    $$

    Thus,

    $$
    y(5)=1.
    $$

    Using \(y(5)=1\), we obtain

    $$
    125a+25b-10+10=1.
    $$

    So,

    $$
    125a+25b=1.
    $$

    Using \(\dot{y}(5)=0\), we obtain

    $$
    75a+10b-2=0.
    $$

    So,

    $$
    75a+10b=2.
    $$

    We now solve the linear system

    $$
    \begin{cases}
    125a+25b=1, \\
    75a+10b=2.
    \end{cases}
    $$

    The solution is

    $$
    a=0.064
    $$

    and

    $$
    b=-0.28.
    $$

    Therefore, the desired trajectory is

    $$
    y(t)=0.064t^3-0.28t^2-2t+10.
    $$

    Its second derivative is

    $$
    \ddot{y}(t)=6at+2b.
    $$

    Substituting the values of \(a\) and \(b\), we get

    $$
    \ddot{y}(t)=0.384t-0.56.
    $$

    Since

    $$
    \ddot{y}(t)=\frac{f(t)}{M}-g,
    $$

    we obtain

    $$
    f(t)=M(\ddot{y}(t)+g).
    $$

    With

    $$
    M=1
    $$

    and

    $$
    g=1,
    $$

    this gives

    $$
    f(t)=0.384t-0.56+1.
    $$

    Hence,

    $$
    f(t)=0.384t+0.44.
    $$

    This force is positive on the whole interval \([0,5]\), since

    $$
    f(0)=0.44>0
    $$

    and

    $$
    f(5)=2.36>0.
    $$

    Therefore, the thrust function

    $$
    f(t)=0.384t+0.44
    $$

    satisfies the constraint \(f(t)\geq 0\) and achieves the desired controlled landing.
    """)
    return


@app.cell
def _(l, np, plt, redstart_solve):
    def controlled_landing_force(t):
        return 0.384 * t + 0.44


    def controlled_landing_example():
        t_span = [0.0, 5.0]

        y0 = [
            0.0,    # x(0)
            0.0,    # vx(0)
            10.0,   # y(0)
            -2.0,   # vy(0)
            0.0,    # theta(0)
            0.0,    # omega(0)
        ]

        def f_phi(t, y):
            f = controlled_landing_force(t)
            phi = 0.0
            return np.array([f, phi])

        sol = redstart_solve(t_span, y0, f_phi)

        t = np.linspace(t_span[0], t_span[1], 1000)
        states = sol(t)

        x_t = states[0]
        vx_t = states[1]
        y_t = states[2]
        vy_t = states[3]
        theta_t = states[4]
        omega_t = states[5]

        f_t = controlled_landing_force(t)

        plt.figure(figsize=(8, 5))
        plt.plot(t, y_t, label=r"$y(t)$")
        plt.plot(t, vy_t, label=r"$\dot{y}(t)$")
        plt.axhline(l / 2, color="grey", linestyle="--", label=r"$y=\ell/2$")
        plt.axhline(0, color="black", linewidth=0.8)
        plt.title("Controlled Landing: height and vertical velocity")
        plt.xlabel("time $t$")
        plt.grid(True)
        plt.legend()
        plt.show()

        plt.figure(figsize=(8, 5))
        plt.plot(t, f_t, label=r"$f(t)$")
        plt.title("Controlled Landing: reactor force")
        plt.xlabel("time $t$")
        plt.ylabel("force $f(t)$")
        plt.grid(True)
        plt.legend()
        plt.show()

        print("Final state at t=5:")
        print("x(5)      =", x_t[-1])
        print("vx(5)     =", vx_t[-1])
        print("y(5)      =", y_t[-1])
        print("vy(5)     =", vy_t[-1])
        print("theta(5)  =", theta_t[-1])
        print("omega(5)  =", omega_t[-1])

        return sol


    controlled_landing_sol = controlled_landing_example()
    return (controlled_landing_force,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Animations

    It's very handy to visualize the evolution of our booster "as a movie"!

    Have a look at the [animations tutorial] to understand the basics of animated SVG documents.

    [animations tutorial]: http://localhost:2718/?file=animations.py
    """)
    return


@app.cell
def _():
    from svg import svg, transform, animate_transform

    return (svg,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Environment

    Create a function `world` whose arguments are:

    - `view_box`: a view box in cartesian coordinates `[x_min, x_max, y_min, y_max]`,

    - `*objects`: (optional) list of extra svg elements (default : `[]`).

    and that returns a SVG string which

    - has the appropriate cartesian view box and frame ($y$-axis upwards),

    - depicts the sky and the ground,

    - depicts a 2 meter wide green ground target centered on $(0, 0)$,

    - displays the objects (if any) inserted on top of the world.

    Test your function with the following scenes:

    ```python
    mo.hstack(
        [
            # Display an empty world
            mo.Html(
                world([-3, 3, -2, 4])
            ),
            # Display a world with a black square on top of the landing pad
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    svg.rect(x=-1, y=0, width=2, height=2, fill="black"),
                )
            ),
            # Display a world with a red square in the top-left corner of the view box
            # and a blue square on the top-right corner of the view box.
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    svg.rect(x=-3, y=2, width=2, height=2, fill="red"),
                    svg.rect(x=1, y=2, width=2, height=2, fill="blue"),
                )
            )
        ],
        justify="space-around"
    )
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The goal of this part is to define a function `world` that creates the SVG environment in which the booster evolves.

    The function takes as input a Cartesian view box

    $$
    [x_{\min}, x_{\max}, y_{\min}, y_{\max}]
    $$

    and optional SVG objects.

    In SVG, the default coordinate system is not the usual mathematical coordinate system. In particular, the vertical axis points downwards. However, in this notebook, we want to use Cartesian coordinates, where the vertical axis \(y\) points upwards.

    To do this, we use two transformations.

    First, we translate the origin:

    $$
    \text{translate}(-x_{\min}, y_{\max}).
    $$

    Then, we flip the vertical axis using

    $$
    \text{scale}(1,-1).
    $$

    This allows us to draw all objects using standard Cartesian coordinates.

    The environment contains:

    - a blue sky for \(y \geq 0\);
    - a brown ground for \(y \leq 0\);
    - a green landing target centered at \(x=0\);
    - optional SVG objects such as the booster.

    The landing target has width \(2\), so it extends from

    $$
    x=-1
    $$

    to

    $$
    x=1.
    $$

    Since the target is on the ground, it is placed at

    $$
    y=0.
    $$
    """)
    return


@app.cell
def _(svg):
    def world(view_box, *objects):
        x_min, x_max, y_min, y_max = view_box

        width = x_max - x_min
        height = y_max - y_min

        return svg.svg(
            viewbox=f"0 0 {width} {height}",
            xmlns="http://www.w3.org/2000/svg",
            width=300,
            height=300,
        )(
            svg.g(
                transform=f"translate({-x_min}, {y_max})",
            )(
                svg.g(
                    transform="scale(1, -1)",
                )(
                    # Sky
                    svg.rect(
                        x=x_min,
                        y=0,
                        width=width,
                        height=y_max,
                        fill="#bde9ff",
                    ),

                    # Ground
                    svg.rect(
                        x=x_min,
                        y=y_min,
                        width=width,
                        height=-y_min,
                        fill="#8b5a2b",
                    ),

                    # Landing target
                    svg.rect(
                        x=-1,
                        y=0,
                        width=2,
                        height=0.12,
                        fill="#2ecc71",
                    ),

                    # Ground line
                    svg.line(
                        x1=x_min,
                        y1=0,
                        x2=x_max,
                        y2=0,
                        stroke="black",
                        stroke_width=0.02,
                    ),

                    # Extra objects
                    *objects,
                )
            )
        )

    return (world,)


@app.cell
def _(mo, svg, world):
    mo.hstack(
        [
            mo.Html(
                world([-3, 3, -2, 4])
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    svg.rect(x=-1, y=0, width=2, height=2, fill="black"),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    svg.rect(x=-3, y=2, width=2, height=2, fill="red"),
                    svg.rect(x=1, y=2, width=2, height=2, fill="blue"),
                )
            ),
        ],
        justify="space-around",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Booster Drawing

    Create a `booster` function that:

    - takes the numeric arguments `x`, `y`, `theta` (in radians), `f` and `phi` (in radians)

    and returns

    - a SVG fragment that represents the body of the booster and the flame of its reactor.
    (The booster drawing can be very simple, for example a rectangle for the body and another one of a different color for the flame will be fine.)

    **Constraint:** make sure that

    - the orientation of the flame is correct,
    - its length is proportional to the force $f$,
    - the flame length is equal to $\ell/2$ when $f=Mg$.


    Test you function in the following scenarios:

    ```python
    mo.hstack(
        [
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l/2, 0, 0, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l, 0, M * g, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(-l/2, l, np.pi / 4, 2 * M * g, np.pi / 2),
                )
            ),
        ],
        justify="space-around",
    )
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Booster Drawing

    The goal of this part is to define a function `booster` that draws the booster at a given position and orientation.

    The booster is modeled as a thin rigid body of total length \(\ell\). Its center of mass is located at

    $$
    (x,y).
    $$

    Since \(\ell\) is the total length, the distance from the center of mass to the top of the booster is

    $$
    \frac{\ell}{2},
    $$

    and the distance from the center of mass to the base of the booster is also

    $$
    \frac{\ell}{2}.
    $$

    The angle \(\theta\) gives the orientation of the booster with respect to the vertical axis. With the convention used in the dynamics, the unit vector pointing from the center of mass to the top of the booster is

    $$
    \vec{u}
    =
    \begin{pmatrix}
    -\sin(\theta) \\
    \cos(\theta)
    \end{pmatrix}.
    $$

    Therefore, the top point of the booster is

    $$
    P_{\text{top}}
    =
    \begin{pmatrix}
    x \\
    y
    \end{pmatrix}
    +
    \frac{\ell}{2}
    \begin{pmatrix}
    -\sin(\theta) \\
    \cos(\theta)
    \end{pmatrix}.
    $$

    The base point of the booster is

    $$
    P_{\text{base}}
    =
    \begin{pmatrix}
    x \\
    y
    \end{pmatrix}
    -
    \frac{\ell}{2}
    \begin{pmatrix}
    -\sin(\theta) \\
    \cos(\theta)
    \end{pmatrix}.
    $$

    Equivalently,

    $$
    P_{\text{base}}
    =
    \begin{pmatrix}
    x \\
    y
    \end{pmatrix}
    +
    \frac{\ell}{2}
    \begin{pmatrix}
    \sin(\theta) \\
    -\cos(\theta)
    \end{pmatrix}.
    $$

    To draw the booster as a rectangle, we also define a perpendicular unit vector

    $$
    \vec{v}
    =
    \begin{pmatrix}
    \cos(\theta) \\
    \sin(\theta)
    \end{pmatrix}.
    $$

    The width of the booster is chosen only for visualization. The body is drawn as a polygon using the top, base, and perpendicular directions.

    The flame is drawn from the base of the booster. Since the reactor force is

    $$
    \vec{F}
    =
    f
    \begin{pmatrix}
    -\sin(\theta+\phi) \\
    \cos(\theta+\phi)
    \end{pmatrix},
    $$

    the flame points in the opposite direction:

    $$
    -\vec{F}.
    $$

    Thus, the direction of the flame is

    $$
    \begin{pmatrix}
    \sin(\theta+\phi) \\
    -\cos(\theta+\phi)
    \end{pmatrix}.
    $$

    The length of the flame is chosen proportional to the thrust \(f\). In particular, when

    $$
    f = Mg,
    $$

    the flame length is chosen to be

    $$
    \frac{\ell}{2}.
    $$
    """)
    return


@app.cell
def _(M, g, l, np, svg):
    def polygon_points(points):
        return " ".join(f"{px},{py}" for px, py in points)


    def booster(x, y, theta, f, phi):
        body_width = 0.18

        center = np.array([x, y])

        # Unit vector from the center of mass to the top of the booster
        axis = np.array([
            -np.sin(theta),
            np.cos(theta),
        ])

        # Unit vector perpendicular to the booster axis
        perp = np.array([
            np.cos(theta),
            np.sin(theta),
        ])

        # Top and base of the booster
        top = center + (l / 2) * axis
        base = center - (l / 2) * axis

        # Four corners of the rectangular body
        p1 = top + (body_width / 2) * perp
        p2 = top - (body_width / 2) * perp
        p3 = base - (body_width / 2) * perp
        p4 = base + (body_width / 2) * perp

        body_points = polygon_points([p1, p2, p3, p4])

        # Direction of the reactor force
        force_direction = np.array([
            -np.sin(theta + phi),
            np.cos(theta + phi),
        ])

        # The flame points in the opposite direction of the force
        flame_direction = -force_direction

        # Flame length: equal to l/2 when f = M*g
        flame_length = (l / 2) * (f / (M * g))

        flame_width = 0.25

        flame_tip = base + flame_length * flame_direction
        flame_left = base + (flame_width / 2) * perp
        flame_right = base - (flame_width / 2) * perp

        flame_points = polygon_points([flame_left, flame_tip, flame_right])

        return svg.g()(
            # Reactor flame
            svg.polygon(
                points=flame_points,
                fill="orange",
                stroke="red",
                stroke_width=0.02,
                fill_opacity=0.8,
            ),

            # Booster body
            svg.polygon(
                points=body_points,
                fill="lightgrey",
                stroke="black",
                stroke_width=0.03,
            ),

            # Center of mass
            svg.circle(
                cx=x,
                cy=y,
                r=0.05,
                fill="black",
            ),
        )

    return booster, polygon_points


@app.cell
def _(M, booster, g, l, mo, np, world):
    mo.hstack(
        [
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l / 2, 0, 0, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l / 2, 0, M * g, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(-l / 2, l, np.pi / 4, 2 * M * g, np.pi / 2),
                )
            ),
        ],
        justify="space-around",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Booster Animation

    Create a `booster_anim` function whose arguments are:

    - `x`, `y`, `theta` (in radians), `f` and `phi` (in radians)
    **which are functions of a time `t`**.
    - an animation duration `T`,

    and returns

    - a SVG fragment that represents the animated body of the booster and the flame of its reactor during `T` seconds, then repeats.
    (The booster drawing can be very simple, for example a rectangle for the body and another one of a different color for the flame will be fine.)

    **Constraint:** make sure that

    - the orientation of the flame is correct,
    - its length is proportional to the force $f$,
    - the flame length is equal to $\ell/2$ when $f=Mg$.

    Test your function in the following scenario:

    ```python
    def booster_anim_0():
        T = 5.0
        def x(t):
            return -l/2 + l * (t / T)
        def y(t):
            return l/2 + l/2 * (t / T)
        def theta(t):
            return (t / T) * 2 * np.pi
        def f(t):
            return M * g * (t / T)
        def phi(t):
            return 2 * np.pi * (t / T)
        return booster_anim(x, y, theta, f, phi, T=T)

    mo.Html(
        world([-3, 3, -2, 4], booster_anim_0())
    ).center()
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The goal of this part is to define a function `booster_anim` that creates an animated SVG fragment for the booster.

    The inputs of the function are time-dependent functions:

    $$
    x(t), \quad y(t), \quad \theta(t), \quad f(t), \quad \phi(t).
    $$

    The function must return an SVG fragment representing the booster body and the reactor flame during a duration \(T\), then repeating periodically.

    The booster body is drawn in the same way as in the static drawing. At each time \(t\), the center of mass is

    $$
    (x(t), y(t)).
    $$

    Since the booster has total length \(\ell\), the distance from the center of mass to the top and to the base is

    $$
    \frac{\ell}{2}.
    $$

    The unit vector pointing from the center of mass to the top of the booster is

    $$
    \vec{u}(t)
    =
    \begin{pmatrix}
    -\sin(\theta(t)) \\
    \cos(\theta(t))
    \end{pmatrix}.
    $$

    Therefore, the top and base points are

    $$
    P_{\text{top}}(t)
    =
    \begin{pmatrix}
    x(t) \\
    y(t)
    \end{pmatrix}
    +
    \frac{\ell}{2}\vec{u}(t)
    $$

    and

    $$
    P_{\text{base}}(t)
    =
    \begin{pmatrix}
    x(t) \\
    y(t)
    \end{pmatrix}
    -
    \frac{\ell}{2}\vec{u}(t).
    $$

    To draw the body as a rectangle, we also use the perpendicular unit vector

    $$
    \vec{v}(t)
    =
    \begin{pmatrix}
    \cos(\theta(t)) \\
    \sin(\theta(t))
    \end{pmatrix}.
    $$

    The reactor force direction is

    $$
    \vec{d}_F(t)
    =
    \begin{pmatrix}
    -\sin(\theta(t)+\phi(t)) \\
    \cos(\theta(t)+\phi(t))
    \end{pmatrix}.
    $$

    The flame points in the opposite direction of the force, so its direction is

    $$
    -\vec{d}_F(t)
    =
    \begin{pmatrix}
    \sin(\theta(t)+\phi(t)) \\
    -\cos(\theta(t)+\phi(t))
    \end{pmatrix}.
    $$

    The length of the flame must be proportional to the force \(f(t)\). We choose

    $$
    L_{\text{flame}}(t)
    =
    \frac{\ell}{2}
    \frac{f(t)}{Mg}.
    $$

    Thus, when \(f(t)=Mg\), the flame length is

    $$
    L_{\text{flame}}(t)=\frac{\ell}{2}.
    $$

    To animate the booster, we sample several times between \(0\) and \(T\), compute the polygon points for the body and the flame at each time, and use SVG `<animate>` elements to interpolate the polygon points over time.
    """)
    return


@app.cell
def _(M, g, l, np, polygon_points, svg):
    def booster_geometry(x, y, theta, f, phi):
        body_width = 0.18
        flame_width = 0.25

        center = np.array([x, y])

        # Direction from the center of mass to the top of the booster
        axis = np.array([
            -np.sin(theta),
            np.cos(theta),
        ])

        # Direction perpendicular to the booster axis
        perp = np.array([
            np.cos(theta),
            np.sin(theta),
        ])

        # Top and base of the booster
        top = center + (l / 2) * axis
        base = center - (l / 2) * axis

        # Body corners
        p1 = top + (body_width / 2) * perp
        p2 = top - (body_width / 2) * perp
        p3 = base - (body_width / 2) * perp
        p4 = base + (body_width / 2) * perp

        body_points = polygon_points([p1, p2, p3, p4])

        # Direction of the reactor force
        force_direction = np.array([
            -np.sin(theta + phi),
            np.cos(theta + phi),
        ])

        # The flame points in the opposite direction
        flame_direction = -force_direction

        # Flame length: equal to l/2 when f = M*g
        flame_length = (l / 2) * (f / (M * g))

        flame_tip = base + flame_length * flame_direction
        flame_left = base + (flame_width / 2) * perp
        flame_right = base - (flame_width / 2) * perp

        flame_points = polygon_points([flame_left, flame_tip, flame_right])

        return body_points, flame_points


    def booster_anim(x, y, theta, f, phi, T=5.0, frames=100, show_flame=True):
        times = np.linspace(0.0, T, frames)

        key_times = "; ".join(str(t / T) for t in times)

        body_values = []
        flame_values = []

        for t in times:
            body_points, flame_points = booster_geometry(
                x(t),
                y(t),
                theta(t),
                f(t),
                phi(t),
            )

            body_values.append(body_points)
            flame_values.append(flame_points)

        body_values = "; ".join(body_values)
        flame_values = "; ".join(flame_values)

        first_body = body_values.split("; ")[0]

        body_svg = svg.polygon(
            points=first_body,
            fill="lightgrey",
            stroke="black",
            stroke_width=0.03,
        )(
            svg.animate(
                attributeName="points",
                values=body_values,
                keyTimes=key_times,
                dur=f"{T}s",
                repeatCount="indefinite",
            )
        )

        if not show_flame:
            return svg.g()(body_svg)

        first_flame = flame_values.split("; ")[0]

        flame_svg = svg.polygon(
            points=first_flame,
            fill="orange",
            stroke="red",
            stroke_width=0.02,
            fill_opacity=0.8,
        )(
            svg.animate(
                attributeName="points",
                values=flame_values,
                keyTimes=key_times,
                dur=f"{T}s",
                repeatCount="indefinite",
            )
        )

        return svg.g()(flame_svg, body_svg)

    return (booster_anim,)


@app.cell
def _(M, booster_anim, g, l, mo, np, world):
    def booster_anim_0():
        T = 5.0

        def x(t):
            return -l / 2 + l * (t / T)

        def y(t):
            return l / 2 + l / 2 * (t / T)

        def theta(t):
            return (t / T) * 2 * np.pi

        def f(t):
            return M * g * (t / T)

        def phi(t):
            return 2 * np.pi * (t / T)

        return booster_anim(x, y, theta, f, phi, T=T)


    mo.Html(
        world([-3, 3, -2, 4], booster_anim_0())
    ).center()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Animated Simulation Results

    Let's go back to a booster whose evolution is governed by its system of ordinary differentential equations. Produce a animation of the booster for 5 seconds for each of the following initial value problems:

    1. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=0$ and $\phi=0$

    2. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=Mg$ and $\phi=0$

    3. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=Mg$ and $\phi=\pi/8$

    4. The "controlled landing" scenario (see above).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We now use the numerical simulation of the booster dynamics to animate the motion of the booster.

    For each scenario, the system is solved using the function `redstart_solve`. The solution gives the state

    $$
    s(t)
    =
    (x(t), \dot{x}(t), y(t), \dot{y}(t), \theta(t), \dot{\theta}(t)).
    $$

    The animation then uses the functions

    $$
    x(t), \quad y(t), \quad \theta(t), \quad f(t), \quad \phi(t)
    $$

    to draw the booster at each time.

    The four scenarios are:

    1. free fall, with \(f=0\) and \(\phi=0\);
    2. hovering, with \(f=Mg\) and \(\phi=0\);
    3. tilted thrust, with \(f=Mg\) and \(\phi=\pi/8\);
    4. controlled landing, using the force \(f(t)=0.384t+0.44\).

    In all cases, the animation duration is \(5\) seconds.
    """)
    return


@app.cell
def _(booster_anim, redstart_solve, world):
    def animation_from_simulation(
        t_span,
        y0,
        f_phi,
        view_box=[-3, 3, -2, 11],
        T=5.0,
    ):
        sol = redstart_solve(t_span, y0, f_phi)

        def x_fun(t):
            return sol(t)[0]

        def y_fun(t):
            return sol(t)[2]

        def theta_fun(t):
            return sol(t)[4]

        def f_fun(t):
            state = sol(t)
            return f_phi(t, state)[0]

        def phi_fun(t):
            state = sol(t)
            return f_phi(t, state)[1]

        return world(
            view_box,
            booster_anim(
                x_fun,
                y_fun,
                theta_fun,
                f_fun,
                phi_fun,
                T=T,
            ),
        )

    return (animation_from_simulation,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Scenario 1: Free fall

    In this first scenario, the reactor is turned off:

    $$
    f = 0
    $$

    and

    $$
    \phi = 0.
    $$

    Therefore, the only force acting on the booster is gravity. The booster falls vertically while keeping the same orientation, since no torque is applied.
    """)
    return


@app.cell
def _(booster_anim, mo, np, redstart_solve, world):
    def scenario_free_fall_anim():
        t_span = [0.0, 5.0]

        y0 = [
            0.0,   # x(0)
            0.0,   # vx(0)
            10.0,  # y(0)
            0.0,   # vy(0)
            0.0,   # theta(0)
            0.0,   # omega(0)
        ]

        def f_phi(t, y):
            return np.array([0.0, 0.0])

        sol = redstart_solve(t_span, y0, f_phi)

        def x_fun(t):
            return sol(t)[0]

        def y_fun(t):
            return sol(t)[2]

        def theta_fun(t):
            return sol(t)[4]

        def f_fun(t):
            return 0.0

        def phi_fun(t):
            return 0.0

        return world(
            [-3, 3, -2, 11],
            booster_anim(
                x_fun,
                y_fun,
                theta_fun,
                f_fun,
                phi_fun,
                T=5.0,
                show_flame=False,
            ),
        )


    mo.Html(scenario_free_fall_anim()).center()
    return (scenario_free_fall_anim,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Scenario 2: Hovering

    In this scenario, the reactor force is equal to the weight:

    $$
    f = Mg.
    $$

    The thrust is applied along the booster axis:

    $$
    \phi = 0.
    $$

    Since the booster is initially vertical, we have

    $$
    \theta = 0.
    $$

    The vertical acceleration is therefore

    $$
    \ddot{y}
    =
    \frac{Mg}{M}-g
    =
    0.
    $$

    Since the initial vertical velocity is also zero, the booster remains at the same height.
    """)
    return


@app.cell
def _(M, animation_from_simulation, g, mo, np):
    def scenario_hover_anim():
        t_span = [0.0, 5.0]

        y0 = [
            0.0,   # x(0)
            0.0,   # vx(0)
            10.0,  # y(0)
            0.0,   # vy(0)
            0.0,   # theta(0)
            0.0,   # omega(0)
        ]

        def f_phi(t, y):
            return np.array([M * g, 0.0])

        return animation_from_simulation(
            t_span,
            y0,
            f_phi,
            view_box=[-3, 3, -2, 11],
            T=5.0,
        )


    mo.Html(scenario_hover_anim()).center()
    return (scenario_hover_anim,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Scenario 3: Tilted thrust

    In this scenario, the reactor force still has magnitude

    $$
    f = Mg,
    $$

    but it is no longer aligned with the booster axis:

    $$
    \phi = \frac{\pi}{8}.
    $$

    Since \(\phi \neq 0\), the reactor force creates a nonzero torque around the center of mass.

    The angular acceleration is

    $$
    \ddot{\theta}
    =
    -\frac{\ell f}{2J}\sin(\phi).
    $$

    Therefore, the booster starts rotating.

    Moreover, since the thrust is not perfectly vertical, the booster also has horizontal acceleration.
    """)
    return


@app.cell
def _(M, animation_from_simulation, g, mo, np):
    def scenario_tilted_force_anim():
        t_span = [0.0, 5.0]

        y0 = [
            0.0,   # x(0)
            0.0,   # vx(0)
            10.0,  # y(0)
            0.0,   # vy(0)
            0.0,   # theta(0)
            0.0,   # omega(0)
        ]

        def f_phi(t, y):
            return np.array([M * g, np.pi / 8])

        return animation_from_simulation(
            t_span,
            y0,
            f_phi,
            view_box=[-8, 3, -2, 11],
            T=5.0,
        )


    mo.Html(scenario_tilted_force_anim()).center()
    return (scenario_tilted_force_anim,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Scenario 4: Controlled landing

    In the controlled landing scenario, the initial state is

    $$
    (x, \dot{x}, y, \dot{y}, \theta, \dot{\theta})
    =
    (0,0,10,-2,0,0).
    $$

    The thrust is applied along the booster axis:

    $$
    \phi = 0.
    $$

    The force used for the controlled landing is

    $$
    f(t)=0.384t+0.44.
    $$

    This force was chosen so that the center of mass reaches

    $$
    y(5)=\frac{\ell}{2}
    $$

    with zero vertical velocity:

    $$
    \dot{y}(5)=0.
    $$

    Since \(\ell=2\), this means

    $$
    y(5)=1.
    $$

    Thus, the booster lands with its base at ground level and with zero vertical velocity.
    """)
    return


@app.cell
def _(animation_from_simulation, controlled_landing_force, mo, np):
    def scenario_controlled_landing_anim():
        t_span = [0.0, 5.0]

        y0 = [
            0.0,    # x(0)
            0.0,    # vx(0)
            10.0,   # y(0)
            -2.0,   # vy(0)
            0.0,    # theta(0)
            0.0,    # omega(0)
        ]

        def f_phi(t, y):
            return np.array([controlled_landing_force(t), 0.0])

        return animation_from_simulation(
            t_span,
            y0,
            f_phi,
            view_box=[-3, 3, -2, 11],
            T=5.0,
        )


    mo.Html(scenario_controlled_landing_anim()).center()
    return (scenario_controlled_landing_anim,)


@app.cell
def _(
    mo,
    scenario_controlled_landing_anim,
    scenario_free_fall_anim,
    scenario_hover_anim,
    scenario_tilted_force_anim,
):
    mo.vstack(
        [
            mo.md("### Scenario 1: Free fall"),
            mo.Html(scenario_free_fall_anim()).center(),

            mo.md("### Scenario 2: Hovering"),
            mo.Html(scenario_hover_anim()).center(),

            mo.md("### Scenario 3: Tilted thrust"),
            mo.Html(scenario_tilted_force_anim()).center(),

            mo.md("### Scenario 4: Controlled landing"),
            mo.Html(scenario_controlled_landing_anim()).center(),
        ]
    )
    return


if __name__ == "__main__":
    app.run()
