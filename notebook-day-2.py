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

    return la, np, plt, scipy


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
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _():
    g = 1.0
    M = 1.0
    l = 2
    return M, g, l


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Forces

    Compute the cartesian coordinates $f_x$ and $f_y$ of the force applied to the booster by the reactor, as functions of $f$, $\theta$ and $\phi$.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Given the geometric setting, the cartesian coordinates of the unit vector $\vec{u}=(u_x, u_y)$ aligned with the reactor (or flame) axis and pointing from the reactor towards the flame satisfy:

    \begin{align*}
    u_x & = +\sin (\theta + \phi) \\
    u_y & = -\cos(\theta +\phi)
    \end{align*}

    Assuming that $f \geq 0$, the force applied to the booster is in the opposite direction and has amplitude $f$:

    $$
    \vec{f} = -f \vec{u}
    $$

    Therefore,

    \begin{align*}
    f_x & = -f \sin (\theta + \phi) \\
    f_y & = +f \cos(\theta +\phi)
    \end{align*}
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Center of Mass

    Give the ordinary differential equation that governs the evolution of the position $(x, y)$ of the center of mass of the booster.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The force exerted by the gravity on the booster is

    $$
    \vec{f}_g =
    \begin{bmatrix}
    0 \\ - M g
    \end{bmatrix}
    $$

    By Newton's second law of motion, the acceleration $\vec{a} = (\ddot{x}, \ddot{y})$
    satisfies $M \vec{a} = \vec{f} + \vec{f}_g$ and thus

    \begin{align*}
    M \ddot{x} & = -f \sin (\theta + \phi) \\
    M \ddot{y} & = +f \cos(\theta +\phi) - Mg
    \end{align*}
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
    ### 🔓 Solution

    The moment of inertia of a thin rod with uniformly distributed mass about its center is of mass is

    $$
    J = \frac{1}{12} M \ell^2
    $$
    """)
    return


@app.cell
def _(M, l):
    J = M * l ** 2 / 12
    J
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
    ### 🔓 Solution

    Newton's Second Law for Rotation is $J \ddot{\theta} = \tau$ where $\tau$ is the torque applied to the booster. Here the torque applied by the gravity to the booster is $0$ by symmetry and only the booster reactor induces a torque. The torque can be
    first computed as a vector in 3D as the cross-product of the vector between the center of the booster and the reactor location and the force applied by the reactor.
    Afterwards, we can be project it on the 3rd axis to get $\tau$.

    Thus, we have

    $$
    \tau =
    \left(
    \ell / 2
    \begin{bmatrix}
    {} +\sin \theta \\ - \cos \theta \\ 0
    \end{bmatrix}
    \wedge \begin{bmatrix} -f \sin (\theta + \phi) \\ +f \cos (\theta + \phi) \\ 0
    \end{bmatrix}
    \right)
    \cdot \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}
    =
    \ell/2 (f\sin \theta \cos (\theta + \phi) - f\sin (\theta + \phi) \cos \theta).
    $$

    Since $\sin \alpha \cos \beta - \sin \beta \cos \alpha = \sin (\alpha - \beta)$,
    we obtain

    $$
    \tau = - f (\ell/2) \sin \phi,
    $$

    thus the angular acceleration is governed by

    $$
    J \ddot{\theta} = - f (\ell / 2)  \sin \phi.
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    Given that

    \begin{align*}
    M \ddot{x} & = -f \sin (\theta + \phi) \\
    M \ddot{y} & = +f \cos(\theta +\phi) - Mg \\
    J \ddot{\theta} & = - f (\ell/2) \sin \phi
    \end{align*}

    and $\dot{x} = v_x$, $\dot{y} = v_y$ and $\dot{\theta} = \omega$, we
    can use as a state vector $s = (x, v_x, y, v_y, \theta, \omega) \in \mathbb{R}^6$
    and the corresponding function $F$ is given by

    $$
    F(s, f, \phi) = \begin{bmatrix}
    v_x \\ -(f / M) \sin (\theta + \phi) \\
    v_y \\ +(f / M) \cos(\theta +\phi) - g \\
    \omega \\ - (f / J) (\ell/2) \sin \phi
    \end{bmatrix}
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
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(J, M, g, l, np, scipy):
    def redstart_solve(t_span, y0, f_phi):
        def fun(t, state):
            x, vx, y, vy, theta, omega = state
            f, phi = f_phi(t, state)
            d2x = (-f * np.sin(theta + phi)) / M
            d2y = (+ f * np.cos(theta + phi)) / M - g
            d2theta = - (f / J) * (l / 2) * np.sin(phi)
            return np.array([vx, d2x, vy, d2y, omega, d2theta])
        r = scipy.integrate.solve_ivp(fun, t_span, y0, dense_output=True)
        return r.sol

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
    ### 🔓 Solution

    In the free fall scenario, the solution satisfies $x(t)=0$, $y(t) = y(0) - g/2 t^2$ and $\theta(t) = 0$. Since numerically $y(0)=10.0$, $g=1$ and $\ell=2$, the threshold
    is crossed when $10 - 1/2 t^2 = 2$, that is $t=4$.
    """)
    return


@app.cell(hide_code=True)
def _(l, np, plt, redstart_solve):
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
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can search for a cubic polynomial

    $$
    y(t) = a_3 t^3 + a_2 t^2 + a_1 t + a_0
    $$

    that solves the four given constraints,
    then deduce $f(t)$ from the equation $M \ddot{y} = f + Mg$.

    The time derivative of $y$ satisfies
    $$
    \dot{y}(t) = 3 a_3 t^2 + 2 a_2 t + a_1,
    $$
    thus the constraints are:

    \begin{align*}
    y(0) = a_0 &= 10, \\
    \dot{y}(0) = a_1 &= -2,\\
    y(5) = 125 a_3 + 25 a_2 + 5 a_1 + a_0 &= 1, \\
    \dot{y}(5) = 75 a_3 + 10 a_2 + a_1 &= 0. \\
    \end{align*}

    The solution of this linear system provides:

    $$
    y(t)
    =\frac{8}{125}t^3 - \frac{7}{25} t^2 - 2t + 10,
    $$
    which yields
    $$
    \ddot{y}(t)
    =
    \frac{48}{125}t - \frac{14}{25}
    $$
    and therefore since $M=1$ and $g=1$,
    $$
    f(t) = \frac{\ddot{y}(t)}{M} + g = \frac{48}{125}t + \frac{11}{25}.
    $$
    """)
    return


@app.cell(hide_code=True)
def _(l, np, plt, redstart_solve):
    def controlled_landing_example():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, -2.0, 0.0, 0.0]
        def f_phi_smooth_landing(t, state):
            return np.array([48 / 125 * t + 11 / 25, 0])
        sol = redstart_solve(t_span, y0, f_phi=f_phi_smooth_landing)
        t = np.linspace(t_span[0], t_span[1], 1000)
        y_t = sol(t)[2]
        plt.plot(t, y_t, label=r"$y(t)$ (height in meters)")
        plt.plot(t, (l / 2) * np.ones_like(t), color="grey", ls="--", label=r"$y=\ell/2$")
        plt.title("Controlled Landing")
        plt.xlabel("time $t$")
        plt.grid(True)
        plt.legend()
        return plt.gcf()
    controlled_landing_example()
    return


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

    return animate_transform, svg, transform


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
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(svg, transform):
    def world(view_box, *objects):
        x_min, x_max, y_min, y_max = view_box    
        width, height = x_max - x_min, y_max - y_min

        return svg.svg(
          xmlns="http://www.w3.org/2000/svg",
          viewBox=f"0 0 {width} {height}",
          style="max-height:80vh")(
              transform.translate(x=-x_min, y=y_max)(
                  transform.scale(y=-1.0)(
                      # Sky
                      svg.rect(x=-1e3, y=0, width=2e3, height=1e3, fill="lightskyblue"),
                      # Ground
                      svg.rect(x=-1e3, y=-2e3, width=2e3, height=2e3, fill="sandybrown"),
                      # Target 
                      svg.rect(x=-1, y =-1, width=2, height=1, fill="lightgreen"),
                      *objects,
                )
            )
        )

    return (world,)


@app.cell
def _(mo, svg, world):
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
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(M, g, l, np, svg, transform):
    def booster(x, y, theta, f, phi):
        flame_length = (l / 2) * (f / M / g)
        return transform.translate(x, y)(
            transform.rotate(theta / np.pi * 180.0)(
                svg.rect(x=-l/20, y=-l/2, width=l/10, height=l, fill="black"),
                transform.translate(0, -l / 2)(
                    transform.rotate(phi / np.pi * 180)(
                        svg.rect(
                            x=-l/20,
                            y=-flame_length,
                            width=l/10,
                            height=flame_length,
                            fill="red",
                        )
                    )
                )
            )
        )

    return (booster,)


@app.cell(hide_code=True)
def _(M, booster, g, l, mo, np, world):
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
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(M, animate_transform, g, l, np, svg):
    def booster_anim(x, y, theta, f, phi, T):
        if not callable(theta):
            theta_cst = theta
            theta = lambda t: theta_cst
        if not callable(phi):
            phi_cst = phi
            phi = lambda t: phi_cst

        def theta_deg(t):
            return theta(t) / np.pi * 180.0

        def phi_deg(t):
            return phi(t) / np.pi * 180.0

        return animate_transform.translate(x, y, T=T)(
            animate_transform.rotate(theta_deg, T=T)(
                svg.rect(
                    x=-l / 20,
                    y=-l/2,
                    width=l / 10,
                    height=l,
                    fill="black",
                ),
                animate_transform.translate(y=-l/2, T=T)(
                    animate_transform.rotate(phi_deg, T=T)(
                        animate_transform.scale(y=f, T=T)(
                            svg.rect(
                                x=-l/20,
                                y=-1/M/g,
                                width=l / 10,
                                height=1/M/g,
                                fill="red",
                            )
                        )
                    )
                ),
            )
        )

    return (booster_anim,)


@app.cell
def _(M, booster_anim, g, l, np):
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

    return (booster_anim_0,)


@app.cell
def _(booster_anim_0, mo, world):
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
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(booster_anim, mo, np, redstart_solve, world):
    def anim_1():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0] 
        def f_phi(t, state):
            return np.array([0, 0])
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[0]
        return mo.Html(
            world(
                [-3, 3, -2, 12], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    anim_1()
    return


@app.cell
def _(M, booster_anim, g, mo, np, redstart_solve, world):
    def anim_2():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]
        def f_phi(t, state):
            return np.array([M * g, 0])
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[1]
        return mo.Html(
            world(
                [-3, 3, -2, 12], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    anim_2()
    return


@app.cell
def _(M, booster_anim, g, mo, np, redstart_solve, world):
    def anim_3():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]
        def f_phi(t, state):
            return np.array([M * g, np.pi / 8])
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[1]
        return mo.Html(
            world(
                [-3, 3, -2, 12], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    anim_3()
    return


@app.cell
def _(booster_anim, mo, np, redstart_solve, world):
    def anim_4():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, -2.0, 0.0, 0.0]
        def f_phi(t, state):
            return np.array([48 / 125 * t + 11 / 25, 0])
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[1]
        return mo.Html(
            world(
                [-3, 3, -2, 12], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    anim_4()
    return


@app.cell
def _(mo):
    mo.md(r"""
    # Linearized Dynamics
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Equilibria

    We assume that

    - $|\theta| < \pi/2$,
    - $|\phi| < \pi/2$, and
    - $f > 0$.

    What are the possible equilibria of the system for constant inputs $f$ and $\phi$ and what are the corresponding values of these inputs?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    An **equilibrium** is a constant state $\bar{s}$ with constant inputs $\bar{f}, \bar{\phi}$ such that $\dot{s} = F(\bar{s}, \bar{f}, \bar{\phi}) = 0$.

    Setting all time derivatives to zero in the vector field:

    $$
    F(s, f, \phi) =
    \begin{bmatrix}
    v_x \\
    -(f/M)\sin(\theta+\phi) \\
    v_y \\
    (f/M)\cos(\theta+\phi) - g \\
    \omega \\
    -(f/J)(\ell/2)\sin\phi
    \end{bmatrix} = 0
    $$

    **Condition 1 — Velocities must vanish:**
    $$v_x = v_y = \omega = 0$$

    **Condition 2 — Angular torque must vanish:**
    $$-(f/J)(\ell/2)\sin\phi = 0 \quad \xrightarrow{f>0,\, \ell>0} \quad \sin\phi = 0 \implies \boxed{\bar{\phi} = 0}$$
    (since $|\phi|<\pi/2$, the only solution is $\phi=0$)

    **Condition 3 — Horizontal acceleration must vanish:**
    $$-(f/M)\sin(\theta + 0) = 0 \implies \sin\theta = 0 \implies \boxed{\bar{\theta} = 0}$$
    (since $|\theta|<\pi/2$)

    **Condition 4 — Vertical acceleration must vanish:**
    $$(f/M)\cos(0) - g = 0 \implies \boxed{\bar{f} = Mg}$$

    The coordinates $(x, y)$ can be **arbitrary** — any lateral position $\bar{x}$ and any altitude $\bar{y}$ are valid.

     **Conclusion:** The equilibria are all points $(\bar{x},\, 0,\, \bar{y},\, 0,\, 0,\, 0)$ for any $\bar{x}, \bar{y} \in \mathbb{R}$,
     with equilibrium inputs $\bar{f} = Mg$ and $\bar{\phi} = 0$.

     Physically: the booster hovers vertically with thrust exactly balancing gravity.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Linearized Model

    Introduce the error variables $\Delta x$, $\Delta y$, $\Delta \theta$, and $\Delta f$ and $\Delta \phi$ of the state and input values with respect to the generic equilibrium configuration.
    What are the linear ordinary differential equations that govern (approximately) these variables in a neighbourhood of the equilibrium?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We set:
    $$x = \bar{x} + \Delta x, \quad y = \bar{y} + \Delta y, \quad \theta = 0 + \Delta\theta, \quad f = Mg + \Delta f, \quad \phi = 0 + \Delta\phi$$

    We expand each equation to **first order** around $(\Delta\theta, \Delta\phi, \Delta f) = (0,0,0)$,
    using the approximations $\sin(\varepsilon) \approx \varepsilon$ and $\cos(\varepsilon) \approx 1$
    for small $\varepsilon$.

    #### Horizontal acceleration

    $$M\ddot{x} = -f\sin(\theta+\phi) \approx -(Mg+\Delta f)(\Delta\theta + \Delta\phi) \approx -Mg(\Delta\theta + \Delta\phi)$$

    (We drop the second-order term $\Delta f \cdot (\Delta\theta + \Delta\phi)$.) This gives:

    $$\boxed{\Delta\ddot{x} = -g(\Delta\theta + \Delta\phi)}$$

    #### Vertical acceleration

    $$M\ddot{y} = f\cos(\theta+\phi) - Mg \approx (Mg+\Delta f)\cdot 1 - Mg = \Delta f$$

    $$\boxed{\Delta\ddot{y} = \frac{\Delta f}{M}}$$

    #### Angular acceleration

    $$J\ddot{\theta} = -f\frac{\ell}{2}\sin\phi \approx -Mg\frac{\ell}{2}\Delta\phi$$

    $$\boxed{\Delta\ddot{\theta} = -\frac{Mg\ell}{2J}\,\Delta\phi \;\triangleq\; -\alpha\,\Delta\phi}$$

    where we define $\alpha = \frac{Mg\ell}{2J}$.

    With our numerical constants ($g=M=1$, $\ell=2$, $J=1/3$):
    $$\alpha = \frac{1 \cdot 1 \cdot 2}{2 \cdot 1/3} = 3$$

     The three degrees of freedom **decouple** in the linearized model:
    - Vertical dynamics: governed by $\Delta f$ alone.
    - Lateral + angular dynamics: governed by $\Delta\phi$ alone.

     This decoupling makes the controller design much simpler.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Standard Form

    1. What are the matrices $A$ and $B$ associated to this linear model in standard form?
    2. Define the corresponding NumPy arrays `A` and `B`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We choose the error state vector:
    $$\Delta s = (\Delta x,\; \Delta\dot{x},\; \Delta y,\; \Delta\dot{y},\; \Delta\theta,\; \Delta\dot{\theta}) \in \mathbb{R}^6$$

    and the control input vector:
    $$u = (\Delta f,\; \Delta\phi) \in \mathbb{R}^2$$

    The linearized system $\Delta\dot{s} = A\,\Delta s + B\,u$ has the form:

    $$
    A =
    \begin{bmatrix}
    0 & 1 & 0 & 0 & 0  & 0 \\
    0 & 0 & 0 & 0 & -g & 0 \\
    0 & 0 & 0 & 1 & 0  & 0 \\
    0 & 0 & 0 & 0 & 0  & 0 \\
    0 & 0 & 0 & 0 & 0  & 1 \\
    0 & 0 & 0 & 0 & 0  & 0
    \end{bmatrix},
    \qquad
    B =
    \begin{bmatrix}
    0   & 0 \\
    0   & -g \\
    0   & 0 \\
    1/M & 0 \\
    0   & 0 \\
    0   & -\alpha
    \end{bmatrix}
    $$

    **Reading the structure of A:**
    - Rows 1,3,5: velocity relationships $\dot{x}=v_x$, $\dot{y}=v_y$, $\dot{\theta}=\omega$ (the `1` off-diagonals)
    - Row 2: $\Delta\ddot{x} = -g\Delta\theta$ (the $-g$ entry couples lateral and angular dynamics)
    - Rows 4,6: no internal dynamics (accelerations depend only on inputs, not on state)

    **Reading the structure of B:**
    - Column 1 ($\Delta f$): only affects $\Delta\ddot{y}$ via $1/M$
    - Column 2 ($\Delta\phi$): affects both $\Delta\ddot{x}$ (via $-g$) and $\Delta\ddot{\theta}$ (via $-\alpha$)
    """)
    return


@app.cell
def _(J, M, g, l, np):
    alpha = M * g * l / (2 * J)
    print(f"α = Mgℓ/(2J) = {alpha}")

    # State:   [Δx, Δẋ, Δy, Δẏ, Δθ, Δθ̇]
    # Control: [Δf, Δφ]

    A = np.array([
        [0, 1,   0, 0,  0,     0],   # Δẋ  = Δvx
        [0, 0,   0, 0, -g,     0],   # Δẍ  = -g·Δθ  (Δφ contribution is in B)
        [0, 0,   0, 1,  0,     0],   # Δẏ  = Δvy
        [0, 0,   0, 0,  0,     0],   # Δÿ  = Δf/M   (fully in B)
        [0, 0,   0, 0,  0,     1],   # Δθ̇  = Δω
        [0, 0,   0, 0,  0,     0],   # Δθ̈  = -α·Δφ  (fully in B)
    ], dtype=float)

    B = np.array([
        [0,      0    ],  # no effect on Δẋ
        [0,     -g    ],  # Δẍ  = -g·Δφ
        [0,      0    ],  # no effect on Δẏ
        [1/M,    0    ],  # Δÿ  = Δf/M
        [0,      0    ],  # no effect on Δθ̇
        [0,     -alpha],  # Δθ̈  = -α·Δφ
    ], dtype=float)

    print("\nA =\n", A)
    print("\nB =\n", B)
    return A, B, alpha


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Stability

    Is the generic equilibrium asymptotically stable?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A linear system $\dot{s} = As$ is **asymptotically stable** if and only if **all eigenvalues of $A$ have strictly negative real parts**.

    Let's compute the eigenvalues numerically:
    """)
    return


@app.cell
def _(A, la):
    eigenvalues = la.eigvals(A)
    print("Eigenvalues of A :", eigenvalues)
    print("Real parts       :", eigenvalues.real)

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ```python
    eigenvalues = la.eigvals(A)
    print("Eigenvalues of A :", eigenvalues)
    # → [0. 0. 0. 0. 0. 0.]
    ```

    All six eigenvalues are **zero** → the equilibrium is **not asymptotically stable**
    (only marginally stable).


    #### Nuance — linearization vs. reality

    This conclusion is drawn on the **linearized model**, which is only a local
    approximation. When all eigenvalues are zero, we have **no conclusion** about the true nonlinear system — one would need a
    deeper analysis to decide.

    Here, physical intuition confirms that the booster is indeed unstable in practice:
    an uncorrected tilt causes an ever-growing lateral drift.

     **An active controller is therefore necessary**, designed so that all
     eigenvalues of the closed-loop matrix $A - BK$ are strictly negative.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controllability

    Is the linearized model controllable?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Kalman's controllability criterion:** The system $(A, B)$ is controllable if and only if the **controllability matrix**

    $$\mathcal{C} = \begin{bmatrix} B & AB & A^2B & \cdots & A^{n-1}B \end{bmatrix} \in \mathbb{R}^{n \times nm}$$

    has **full row rank** (rank $= n = 6$).

    **Intuition:** This matrix captures all the directions in state space that the inputs can "reach" over time. If it has full rank, the inputs can steer the system to any desired state.
    """)
    return


@app.cell
def _(A, B, np):
    def controllability_matrix(A, B):
        n = A.shape[0]
        cols = [B]
        for _ in range(n - 1):
            cols.append(A @ cols[-1])
        return np.hstack(cols)

    n = A.shape[0]
    C_mat = controllability_matrix(A, B)
    rank_C = np.linalg.matrix_rank(C_mat)

    print(f"State dimension  n = {n}")
    print(f"Rank of controllability matrix : {rank_C}")
    print(f"Controllable : {rank_C == n}")
    return (controllability_matrix,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The full system $(A, B)$ is controllable (rank = 6 = $n$).

    This means we can theoretically place the closed-loop poles anywhere in the complex plane,
    and we can drive the system from any initial state to any target state in finite time.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Lateral Dynamics

    We limit our interest in the lateral position $x$, the tilt $\theta$ and their derivatives (we are for the moment fine with letting $y$ and $\dot{y}$ be uncontrolled). We also set $f = M g$ and control the system only with $\phi$.

    - What are the new (reduced) matrices $A$ and $B$ for this reduced system?

    - Check the controllability of this new system.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Reduced state:** $z = (\Delta x,\, \Delta\dot{x},\, \Delta\theta,\, \Delta\dot{\theta}) \in \mathbb{R}^4$

    **Scalar control:** $u = \Delta\phi \in \mathbb{R}$

    The relevant linearized equations are:

    $$
    \Delta\ddot{x} = -g(\Delta\theta + \Delta\phi), \qquad
    \Delta\ddot{\theta} = -\alpha\,\Delta\phi
    $$

    with $\alpha = Mg\ell/(2J) = 3$. This gives:

    $$
    A_\text{lat} =
    \begin{bmatrix}
    0 & 1 & 0 & 0 \\
    0 & 0 & -g & 0 \\
    0 & 0 & 0 & 1 \\
    0 & 0 & 0 & 0
    \end{bmatrix},
    \qquad
    B_\text{lat} =
    \begin{bmatrix}
    0 \\ -g \\ 0 \\ -\alpha
    \end{bmatrix}
    $$

    **Note:** $\Delta x$ is coupled to $\Delta\theta$ through $A_{\text{lat}}$ (the $-g$ entry in row 2),
    and both are driven by $\Delta\phi$ through $B_{\text{lat}}$.
    The tilt can be controlled directly by $\phi$, and through the tilt we indirectly control $x$.
    """)
    return


@app.cell
def _(alpha, controllability_matrix, g, np):
    A_lat = np.array([
        [0,  1,   0,  0],
        [0,  0,  -g,  0],
        [0,  0,   0,  1],
        [0,  0,   0,  0],
    ], dtype=float)

    B_lat = np.array([[0], [-g], [0], [-alpha]], dtype=float)

    print("A_lat =\n", A_lat)
    print("\nB_lat =\n", B_lat)

    C_lat = controllability_matrix(A_lat, B_lat)
    rank_lat = np.linalg.matrix_rank(C_lat)
    print(f"\nRank of lateral controllability matrix : {rank_lat} / {A_lat.shape[0]}")
    print(f"Controllable : {rank_lat == A_lat.shape[0]}")
    return A_lat, B_lat


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The reduced lateral system $(A_\text{lat}, B_\text{lat})$ is controllable (rank = 4).

    This is good news: with a single input $\Delta\phi$, we can simultaneously stabilize both
    the tilt angle $\theta$ and the lateral position $x$.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Linear Model in Free Fall

    Make graphs of $x(t)$ and $\theta(t)$ for the linearized model when
    - $x(0)=0$, $\dot{x}(0)=0$, $\theta(0) = \pi/4$, $\dot{\theta}(0) =0$, and
    - $\phi(t)=0$ at all times.

    What do you see? How do you explain it?
    """)
    return


@app.cell
def _(A_lat, B_lat, np, plt):
    from scipy.integrate import solve_ivp

    # Initial conditions for the lateral reduced system
    theta0  = np.pi / 4
    z0_lat  = np.array([0.0, 0.0, theta0, 0.0])  # [Δx, Δẋ, Δθ, Δθ̇]

    # Open-loop linear dynamics (φ = 0  →  u = 0)
    def linear_open_loop(t, z):
        return A_lat @ z + B_lat @[0] 

    t_span = [0.0, 5.0]
    t_eval = np.linspace(0, 5, 500)
    sol_ol = solve_ivp(linear_open_loop, t_span, z0_lat,
                       t_eval=t_eval, dense_output=True)

    x_lin     = sol_ol.y[0]
    theta_lin = sol_ol.y[2]

    fig, axes = plt.subplots(1, 2, figsize=(11, 4))

    axes[0].plot(t_eval, x_lin, color="steelblue", lw=2)
    axes[0].set_title(r"$\Delta x(t)$ — lateral drift  (m)")
    axes[0].set_xlabel("time  $t$  (s)")
    axes[0].grid(True)

    axes[1].plot(t_eval, theta_lin * 180 / np.pi, color="tomato", lw=2)
    axes[1].axhline(0, color="grey", ls="--")
    axes[1].set_title(r"$\Delta\theta(t)$ — tilt angle  (°)")
    axes[1].set_xlabel("time  $t$  (s)")
    axes[1].grid(True)

    fig.suptitle(r"Open-loop linearized model — $\phi=0$, $\theta(0)=\pi/4$")
    plt.tight_layout()
    plt.show()
    return (solve_ivp,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Observations and Explanation

    **What we see:**

    1. $\theta(t) = \pi/4 = \text{const}$ — the angle **stays fixed**.
       Without $\phi \neq 0$, there is no torque, so the angular equation $\Delta\ddot{\theta} = -\alpha\Delta\phi = 0$
       gives zero angular acceleration. The initial angle is "frozen".

    2. $x(t)$ **diverges quadratically** — the booster drifts laterally at an accelerating rate.

    **Mathematical explanation:**

    Since $\Delta\theta = \pi/4 = \text{const}$, the lateral acceleration equation gives:
    $$\Delta\ddot{x} = -g\,\Delta\theta = -g \cdot \frac{\pi}{4} \approx -0.785 \text{ m/s}^2 = \text{const}$$

    Integrating twice:
    $$\Delta x(t) \approx -\frac{g}{2}\cdot\frac{\pi}{4}\cdot t^2 = -\frac{\pi g}{8}\,t^2$$

    This is a classic **double integrator** response.

    **Physical interpretation:**

     A tilted booster with no angular correction produces a constant horizontal thrust component,
     which accelerates the booster sideways like a projectile. This is exactly why rockets use
     active TVC (Thrust Vector Control): any uncorrected tilt causes an ever-growing lateral drift.
     A state-feedback controller is essential.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Manually Tuned Controller

    Try to find the two missing coefficients of the matrix

    $$
    K =
    \begin{bmatrix}
    0 & 0 & ? & ?
    \end{bmatrix}
    \in \mathbb{R}^{4\times 1}
    $$

    such that the control law

    $$
    \Delta \phi(t) = - K \cdot
    \begin{bmatrix}
    \Delta x(t) \\
    \Delta \dot{x}(t) \\
    \Delta \theta(t) \\
    \Delta \dot{\theta}(t)
    \end{bmatrix} \in \mathbb{R}
    $$

    manages  when
    $\Delta x(0)=0$, $\Delta \dot{x}(0)=0$, $\Delta \theta(0) = 45 / 180  \times \pi$  and $\Delta \dot{\theta}(0) =0$ to:

    - make $\Delta \theta(t) \to 0$ in approximately $20$ sec (or less),
    - $|\Delta \theta(t)| < \pi/2$ and $|\Delta \phi(t)| < \pi/2$ at all times,
    - (but we don't care about a possible drift of $\Delta x(t)$).

    Explain your thought process, show your iterative guesses and simulations!

    Is your final closed-loop model asymptotically stable?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###  Theoretical Analysis

    Let the gain vector be defined as:

    $$
    K = [0,\;0,\;k_3,\;k_4]
    $$

    The control law is given by:

    $$
    \Delta \phi = -k_3 \Delta \theta - k_4 \Delta \dot{\theta}
    $$

    Substituting this expression into the system dynamics:

    $$
    \Delta \ddot{\theta} = -\alpha \Delta \phi
    $$

    we obtain:

    $$
    \Delta \ddot{\theta}
    = -\alpha(-k_3 \Delta \theta - k_4 \Delta \dot{\theta})
    $$

    $$
    = \alpha k_3 \Delta \theta + \alpha k_4 \Delta \dot{\theta}
    $$

    ###  Characteristic Polynomial

    The associated characteristic polynomial is:

    $$
    s^2 - \alpha k_4 s - \alpha k_3 = 0
    $$


    ###  Stability Condition

    For a second-order system of the form:

    $$
    s^2 + a_1 s + a_0
    $$

    stability requires:

    $$
    a_1 > 0 \quad \text{and} \quad a_0 > 0
    $$

    In our case, we identify:

    $$
    a_1 = -\alpha k_4, \quad a_0 = -\alpha k_3
    $$

    Therefore, assuming $\alpha > 0$, the stability conditions become:

    $$
    k_3 < 0, \quad k_4 < 0
    $$
    """)
    return


@app.cell
def _(A_lat, B_lat, np, plt, solve_ivp):
    # ── Simulation function ───────────────────────────────────────────────────
    def simulate_lateral_closed_loop(K, z0, t_span, t_eval):
        """Simulate the lateral system with state feedback Δφ = -K·z."""

        A_cl = A_lat - B_lat @ K   # closed-loop system matrix

        def dyn(t, z):
            return A_cl @ z

        sol = solve_ivp(dyn, t_span, z0, t_eval=t_eval, dense_output=True)

        phi_t = -(K @ sol.y)[0]   # control signal applied over time

        return sol, phi_t


    # ── Simulation setup (RENAMED VARIABLES) ──────────────────────────────────
    theta0_cl = np.pi / 4

    z0_cl = np.array([0.0, 0.0, theta0_cl, 0.0])

    t_span_cl = [0.0, 25.0]
    t_eval_cl = np.linspace(0, 25, 1000)


    # ── Iterative manual tuning ───────────────────────────────────────────────
    candidates = {
        "Trial 1 : k3=-1, k4=-1  (too slow)"  : np.array([[0, 0, -1.0, -1.0]]),
        "Trial 2 : k3=-2, k4=-3  (better)"    : np.array([[0, 0, -2.0, -3.0]]),
        "Trial 3 : k3=-3, k4=-4  ✓ (good)"    : np.array([[0, 0, -3.0, -4.0]]),
    }


    # ── Plot (RENAMED VARIABLES) ──────────────────────────────────────────────
    fig_cl, axes_cl = plt.subplots(1, 2, figsize=(12, 4))

    colors = ["#ff6b6b", "#ffd43b", "#69db7c"]

    for (label, K), color in zip(candidates.items(), colors):
        sol, phi_t = simulate_lateral_closed_loop(K, z0_cl, t_span_cl, t_eval_cl)

        axes_cl[0].plot(t_eval_cl, sol.y[2] * 180/np.pi,
                        label=label, color=color, lw=2)

        axes_cl[1].plot(t_eval_cl, phi_t * 180/np.pi,
                        label=label, color=color, lw=2)


    for ax in axes_cl:
        ax.axhline( 90, color="white", ls="--", alpha=0.4, label="±π/2 limit")
        ax.axhline(-90, color="white", ls="--", alpha=0.4)
        ax.grid(True)
        ax.legend(fontsize=8)


    axes_cl[0].set_title(r"$\Delta\theta(t)$  (degrees)")
    axes_cl[1].set_title(r"$\Delta\phi(t)$   (degrees)")

    fig_cl.suptitle("Manual controller tuning — iterative design")

    plt.tight_layout()
    plt.show()
    return (simulate_lateral_closed_loop,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Analysis of the manual controller

    All the K selected respect the conditions above!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controller Tuned with Pole Assignment

    Using pole assignement, find a matrix

    $$
    K_{pp} =
    \begin{bmatrix}
    ? & ? & ? & ?
    \end{bmatrix}
    \in \mathbb{R}^{4\times 1}
    $$

    such that the control law

    $$
    \Delta \phi(t)
    = - K_{pp} \cdot
    \begin{bmatrix}
    \Delta x(t) \\
    \Delta \dot{x}(t) \\
    \Delta \theta(t) \\
    \Delta \dot{\theta}(t)
    \end{bmatrix} \in \mathbb{R}
    $$

    satisfies the conditions defined for the manually tuned controller and additionally:

    - result in an asymptotically stable closed-loop dynamics,

    - make $\Delta x(t) \to 0$ in approximately $20$ sec (or less).

    Explain how you find the proper design parameters!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Pole placement** is a systematic method: given a controllable system $(A, B)$,
    we choose desired poles $\{p_1, p_2, p_3, p_4\}$ with $\text{Re}(p_i) < 0$,
    then compute $K$ such that the characteristic polynomial of $(A - BK)$ equals $\prod_i (s - p_i)$.

    **Choosing the poles:**
    - For convergence in ~10–15 s, we want $|\text{Re}(p)| \approx 0.3$ to $0.5$
      (time constant $\tau = 1/|\text{Re}(p)|$, converge in $\approx 4\tau$).
    - Complex conjugate pairs give oscillatory but damped convergence.
    - All four poles must be at strictly negative real parts for full asymptotic stability.

    **Selected poles:**
    $$\{-0.3,\; -0.4,\; -0.5 + 0.3j,\; -0.5 - 0.3j\}$$

    These give:
    - Slowest time constant: $\tau = 1/0.3 \approx 3.3$ s → converges in $\approx 4 \times 3.3 \approx 13$ s
    - Gentle oscillation from the complex pair (damping ratio $\approx 0.86$)
    """)
    return


@app.cell
def _(A_lat, B_lat, la, np, plt, simulate_lateral_closed_loop):

    from scipy.signal import place_poles

    # ─────────────────────────────────────────────────────────────────────────────
    # CONDITIONS INITIALES + TEMPS
    # ─────────────────────────────────────────────────────────────────────────────
    z0 = np.array([
        0.1,               # Δx (m)
        0.0,               # vitesse
        5*np.pi/180,      # Δθ (rad)
        0.0                # vitesse angulaire
    ])

    t_span = (0, 10)
    t_eval = np.linspace(0, 10, 300)

    # ─────────────────────────────────────────────────────────────────────────────
    # POLES DESIRES
    # ─────────────────────────────────────────────────────────────────────────────
    desired_poles_pp = np.array([
        -0.3,
        -0.4,
        -0.5 + 0.3j,
        -0.5 - 0.3j
    ])

    # ─────────────────────────────────────────────────────────────────────────────
    # CALCUL DU GAIN K (Pole Placement)
    # ─────────────────────────────────────────────────────────────────────────────
    result_pp = place_poles(A_lat, B_lat, desired_poles_pp)
    K_pp = result_pp.gain_matrix

    print("K_pp (pole placement) =", np.round(K_pp, 4))

    # ─────────────────────────────────────────────────────────────────────────────
    # VERIFICATION DES POLES
    # ─────────────────────────────────────────────────────────────────────────────
    A_cl_pp = A_lat - B_lat @ K_pp
    eigs_pp = la.eigvals(A_cl_pp)

    print("\nActual  closed-loop poles :", np.round(eigs_pp, 4))
    print("Desired closed-loop poles :", desired_poles_pp)

    # ─────────────────────────────────────────────────────────────────────────────
    # SIMULATION
    # ─────────────────────────────────────────────────────────────────────────────
    sol_pp, phi_pp = simulate_lateral_closed_loop(
        K_pp,
        z0,
        t_span,
        t_eval
    )

    # ─────────────────────────────────────────────────────────────────────────────
    # AFFICHAGE (plots)
    # ─────────────────────────────────────────────────────────────────────────────
    fig_pp, axes_pp = plt.subplots(1, 3, figsize=(14, 4))

    # Δx(t)
    axes_pp[0].plot(t_eval, sol_pp.y[0], lw=2)
    axes_pp[0].axhline(0, linestyle="--")
    axes_pp[0].set_title(r"$\Delta x(t)$ (m)")
    axes_pp[0].set_xlabel("time (s)")
    axes_pp[0].grid(True)

    # Δθ(t)
    axes_pp[1].plot(t_eval, sol_pp.y[2] * 180/np.pi, lw=2)
    axes_pp[1].axhline(0, linestyle="--")
    axes_pp[1].set_title(r"$\Delta\theta(t)$ (°)")
    axes_pp[1].set_xlabel("time (s)")
    axes_pp[1].grid(True)

    # Δφ(t)
    axes_pp[2].plot(t_eval, phi_pp * 180/np.pi, lw=2)
    axes_pp[2].axhline(0, linestyle="--")
    axes_pp[2].set_title(r"$\Delta\phi(t)$ (°)")
    axes_pp[2].set_xlabel("time (s)")
    axes_pp[2].grid(True)

    fig_pp.suptitle(f"Pole Placement Controller — K_pp = {np.round(K_pp, 3)}")

    plt.tight_layout()
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controller Tuned with Optimal Control

    Using optimal control, find a gain matrix $K_{oc}$ that satisfies the same set of requirements that the one defined using pole placement.

    Explain how you find the proper design parameters!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Validation

    Test the two control strategies (pole placement and optimal control) on the "true" (nonlinear) model with an animation. Check that both controllers achieve their goal; otherwise, go back to the drawing board and tweak the design parameters until they do!
    """)
    return


if __name__ == "__main__":
    app.run()
