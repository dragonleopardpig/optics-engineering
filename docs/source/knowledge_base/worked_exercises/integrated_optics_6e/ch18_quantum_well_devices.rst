Chapter 18: Quantum-Well Devices
================================

Source: Hunsperger, sixth edition (2009), Problems 18.1--18.9,
printed pages 398--399.

Infinite-well convention
------------------------

For well width :math:`L_z`, a subband edge is
:math:`E_n=\hbar^2\pi^2n^2/(2m^*L_z^2)`.
Including spin degeneracy, each occupied 2D subband adds
:math:`m^*/(\pi\hbar^2)` to density of states per area per energy.
The number of states integrated up to energy has linear segments;
the density of states itself has steps.

Problem 18.1 — MQW versus superlattice
--------------------------------------

**Working.** Multiple wells with thick barriers have nearly independent
confined states: tunnelling between neighboring wells is weak.
With thin barriers, adjacent wavefunctions overlap and the repeated
potential forms coupled minibands along the growth direction.

**Answer.** MQW normally denotes substantially isolated wells;
superlattice emphasizes coherent coupling and miniband formation.

**Check.** Merely counting the number of layers cannot distinguish
them. Barrier thickness and electronic coupling are decisive.

Problem 18.2 — GaAs subband steps
---------------------------------

**Working.** State the material assumption
:math:`m_e^*=0.067m_0`. With :math:`L_z=7` nm,

.. math::

   (E_1,E_2,E_3)=(0.114539,0.458154,1.03085)\ {\rm eV}.

The step magnitude is

.. math::

   \Delta D_{2D}=\frac{0.067m_0}{\pi\hbar^2}
   =2.79880\times10^{13}\ {\rm eV^{-1}cm^{-2}}.

**Answer.** Equal DOS jumps occur at those three energies. For
the :math:`100\,\mu{\rm m}\times100\,\mu{\rm m}` area, each
whole-well DOS step is :math:`2.79880\times10^9\,{\rm eV}^{-1}`.

.. figure:: /_static/knowledge_base/worked_exercises/integrated_optics_6e/quantum_well_dos.svg
   :alt: Infinite-well subband energies scale as squared order while the two-dimensional density of states gains equal-height steps.
   :width: 100%

   The idealized first three GaAs conduction subbands.

**Check.** Energies scale as :math:`n^2`, whereas each DOS
step has the same height. The infinite-barrier assumption becomes
poor for high subbands above a real barrier.

Problem 18.3 — Fundamental interband quantum-well emission
----------------------------------------------------------

**Working.** Electron and hole confinement both increase transition
energy. With stated approximations
:math:`E_g=1.43` eV, :math:`m_e^*=0.067m_0`,
and heavy-hole mass :math:`m_h^*=0.5m_0`,

.. math::

   E_\gamma=E_g+E_{1e}+E_{1h}
   =1.43+0.114539+0.0153482=1.55989\,{\rm eV}.

**Answer.** :math:`\lambda_0=1.239841984/E_\gamma
\simeq0.79483\,\mu{\rm m}`.

**Check.** The hole term adds despite being plotted downward in
an electron band diagram. Finite barriers, excitons, and the selected
valence band shift the actual wavelength.

Problem 18.4 — SEED optical feedback and logic
----------------------------------------------

**Working.** Absorbed light changes the current in an MQW p-i-n
diode. In an appropriate electrical load circuit, that current
changes diode voltage. The quantum-confined Stark effect makes
absorption depend on that voltage, closing a feedback loop.
Suitable load lines can yield two stable optical/electrical states.

**Answer.** This self-consistent absorption-voltage feedback enables
bistability and therefore potential binary switching or logic.

**Check.** A bare passive MQW layer is not automatically bistable.
The bias circuit, optical operating point, and feedback sign matter.

Problem 18.5 — Six-nanometre well and twenty-well gain
------------------------------------------------------

**Working.** With :math:`E_g=1.52` eV and the same GaAs
electron/heavy-hole masses as 18.3, the 6 nm infinite well gives
:math:`E_{1e}+E_{1h}\simeq0.17679` eV.
Thus :math:`\lambda_0\simeq1.239841984/1.69679=0.73070\,\mu{\rm m}`.

For independent equally pumped wells, modal gain sums:
:math:`g_{\rm modal}=\sum_j\Gamma_jg_{{\rm mat},j}`.

**Answer.** (a) Approximately 730.7 nm within the infinite-well
model. (b) If 80 inverse centimetres is each well's **modal
contribution** and all overlaps remain equal, twenty contribute
1600 inverse centimetres.

**Check.** If 80 is material gain, it does not automatically
multiply by twenty. Optical confinement, carrier distribution, and
total layer thickness must be specified. A high infinite-well level
may not be bound in a finite AlGaAs barrier.

Problem 18.6 — QCSE extinction for two propagation geometries
-------------------------------------------------------------

**Working.** The absorption change is
:math:`\Delta\alpha=2000-10=1990\,{\rm cm}^{-1}`.
For perpendicular passage through 10 micrometres,

.. math::

   \frac{T_{\rm on}}{T_{\rm off}}=e^{\Delta\alpha(0.001)}
   =7.31553.

For parallel passage over 50 micrometres with confinement 0.8,
the exponent is :math:`1990(0.8)(0.005)=7.96`.

**Answer.** Ratios are 7.316 (8.642 dB) and
2864.07 (34.57 dB), respectively.

**Check.** Compare ratios of transmitted states, not absorbed
fractions. The confinement factor multiplies the absorption-length product.

Problem 18.7 — InGaAs subband density of states
-----------------------------------------------

**Working.** Substitute the supplied electron mass
:math:`0.045m_0` and 7 nm width:

.. math::

   (E_1,E_2,E_3)=(0.170535,0.682141,1.53482)\ {\rm eV},
   \qquad
   \Delta D_{2D}=1.87979\times10^{13}\ {\rm eV^{-1}cm^{-2}}.

**Answer.** Equal steps occur at those energies. Multiplying
by the stated area gives :math:`1.87979\times10^9\,{\rm eV}^{-1}`
per whole-well step.

**Check.** The hole mass does not enter the requested conduction-band
DOS. The lighter electron mass raises confinement energy and reduces
DOS step height compared with GaAs.

Problem 18.8 — Temperature-dependent threshold
----------------------------------------------

**Working.** Use the empirical characteristic-temperature law
:math:`I_{\rm th}(T_2)/I_{\rm th}(T_1)=e^{(T_2-T_1)/T_0}`.
Temperature differences have the same numerical value in kelvin
and degrees Celsius:

.. math::

   I_{\rm th}(45^\circ{\rm C})=10\,{\rm mA}\,e^{24/425}
   =10.58095\,{\rm mA}.

**Answer.** Approximately 10.58 mA.

**Check.** :math:`T_0` is a fitted temperature scale, not a
temperature to which 273.15 must be added in this ratio.

Problem 18.9 — Why quantum wells can narrow laser linewidth
-----------------------------------------------------------

**Working.** A step-like electronic DOS and strong differential gain
can reduce the carrier-number change needed to alter stimulated
emission. The associated amplitude-phase coupling and spontaneous-emission
contribution to the lasing mode can be reduced in a well-designed QW laser.

**Answer.** Quantum confinement can improve differential gain and
noise/phase dynamics, producing a narrower line at comparable
operating conditions.

**Check.** Linewidth also depends on cavity loss, output power,
linewidth-enhancement factor, temperature, and technical noise.
Adding wells alone does not guarantee a narrower spectrum.
