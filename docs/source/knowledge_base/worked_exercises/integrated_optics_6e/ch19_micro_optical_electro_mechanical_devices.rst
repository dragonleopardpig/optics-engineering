Chapter 19: Micro-Optical-Electro-Mechanical Devices
====================================================

Source: Hunsperger, sixth edition (2009), Problems 19.1--19.9,
printed pages 419--420.

Units and boundary conditions
-----------------------------

Use Table 19.2 values :math:`E=190` GPa, :math:`G=73` GPa,
:math:`\nu=0.28`, and :math:`\rho=2300\,{\rm kg/m^3}`.
The pressures printed in kg/m2 are interpreted as kilogram-force per
square metre, so multiply by :math:`g=9.80665\,{\rm m/s^2}`.
Plate results assume clamped boundaries, small deflection, no residual
tension, and an isotropic approximation for crystalline silicon.

Problem 19.1 — Stress and strain of a loaded silicon rod
--------------------------------------------------------

**Working.** A 3 g mass exerts :math:`F=0.003g=0.02941995` N.
For diameter 1 mm,

.. math::

   A=\pi(0.0005)^2,\qquad
   |\sigma|=F/A=37458.6\,{\rm Pa},\qquad
   |\epsilon_a|=|\sigma|/E=1.97151\times10^{-7}.

**Answer.** Axial stress magnitude is 37.46 kPa and extension
strain magnitude is :math:`1.972\times10^{-7}`.
“Longitudinal” in part (c) describes the same axial direction.
If lateral strain was intended, its magnitude is
:math:`\nu|\epsilon_a|=5.5202\times10^{-8}`, with opposite sign.

**Check.** Under the usual extension-positive convention the axial
strain is positive and lateral strain negative. The book's
tension-negative stress convention changes signed labels, not magnitudes.

Problem 19.2 — Clamped square silicon plate
-------------------------------------------

**Working.** Convert pressure to :math:`P=98066.5` Pa.
For side :math:`a=0.007` m and thickness :math:`t=150\,\mu{\rm m}`,
form flexural rigidity :math:`D_p=Et^3/[12(1-\nu^2)]`.
The chapter's plate relations give

.. math::

   w_0=0.001265\,Pa^4/D_p,\quad
   \sigma_l=0.3081P(a/t)^2,\quad \sigma_t=\nu\sigma_l,
   \quad
   f_0=\frac{1.654t}{a^2}\sqrt{\frac{E}{\rho(1-\nu^2)}}.

**Answer.** Centre deflection 5.137 micrometres; maximum
longitudinal stress 65.80 MPa; transverse stress 18.42 MPa;
fundamental frequency approximately 47.94 kHz.

**Check.** Deflection is about 3.4 percent of thickness, consistent
with the small-deflection plate approximation.

Problem 19.3 — Uniformly pressure-loaded cantilever
---------------------------------------------------

**Working.** The observation point is
:math:`x=L-0.5\,{\rm mm}=1.0\,{\rm mm}` from the clamp.
For width :math:`b=0.5` mm and thickness 0.25 mm,
:math:`I_b=bt^3/12`. Convert surface pressure to line load:
:math:`q=(100g)b=0.4903325\,{\rm N/m}`.

.. math::

   w(x)=\frac{qx^2}{24EI_b}(6L^2-4Lx+x^2),\qquad
   \sigma_{\max}=\frac{qL^2t}{4I_b},\qquad
   f_0\simeq0.161\frac{t}{L^2}\sqrt{\frac E\rho}.

**Answer.** Deflection 1.404 nm; maximum bending stress
0.1059 MPa; unloaded-beam fundamental approximately 162.6 kHz.

**Check.** A pressure in N/m2 cannot be inserted directly where
the beam formula requires N/m. The beam model also neglects
fluid loading and shear corrections.

Problem 19.4 — A ten-gram point load at the free end
----------------------------------------------------

**Working.** Use :math:`F=0.01g=0.0980665` N at :math:`x=L`:

.. math::

   w(x)=\frac{Fx^2}{6EI_b}(3L-x),\qquad
   \sigma_{\max}=\frac{FLt}{2I_b}.

At the same observation point, these give 0.46246 micrometres
and maximum stress 28.243 MPa.
If the 10 g load is an attached mass, the first-mode estimate is

.. math::

   f\simeq\frac1{2\pi}\sqrt{
   \frac{3EI_b/L^3}{m_{\rm tip}+0.24m_{\rm beam}}}
   \simeq527.74\,{\rm Hz}.

**Answer.** Static deflection 0.4625 micrometres and stress
28.24 MPa; approximately 528 Hz for an attached 10 g mass.

**Check.** Reusing the unloaded 162.6 kHz frequency is appropriate
only if the force is applied without added moving mass. A physical
10 g weight dominates this tiny beam's effective mass.

Problem 19.5 — Formal torsion restoring torque
----------------------------------------------

**Working.** Apply the two-beam relation with
:math:`\ell=200\,\mu{\rm m},w=t=100\,\mu{\rm m}`:

.. math::

   T_r=\frac{2Gwt^3\theta}{3\ell}
   \left[1-\frac{192t}{\pi^5w}
   \tanh\left(\frac{\pi w}{2t}\right)\right].

For :math:`\theta=\pi/4`, the magnitude is
:math:`8.1141\times10^{-3}\,{\rm N\,m}`.

**Answer.** The linear model predicts about 8.11 mN m opposing
the rotation.

**Check.** This very large twist over a short, thick support
implies large shear strain. The formal calculation is not evidence
that crystalline silicon can sustain the specified elastic rotation
without fracture; the linear torsion assumptions need checking.

Problem 19.6 — Circular-plate centre deflection
-----------------------------------------------

**Working.** The clamped isotropic plate solution follows from
:math:`D_p\nabla^4w=P` and :math:`w(a)=w'(a)=0`:

.. math::

   w(r)=\frac{P(a^2-r^2)^2}{64D_p},\qquad
   w(0)=\frac{3P d^4(1-\nu^2)}{256Et^3}.

For diameter 8 mm, thickness 200 micrometres, and the stated pressure,
this gives :math:`w(0)=2.85404\,\mu{\rm m}`.

**Answer.** Approximately 2.854 micrometres from the clamped-plate
equation. The book prints 265 instead of 256 in Eq. (19.18);
using that printed denominator gives 2.75712 micrometres.

**Check.** The denominator 256 follows directly by substituting
radius :math:`a=d/2` into the plate solution. The discrepancy
is not an alternative pressure-unit conversion.

Problem 19.7 — Length relaxation after release
----------------------------------------------

**Working.** Strain magnitude is
:math:`|\epsilon|=20\,{\rm MPa}/280\,{\rm GPa}
=7.14286\times10^{-5}`.
For a 1000 micrometre beam, relaxation of that tensile strain changes
length by :math:`|\Delta L|=L|\epsilon|=0.0714286\,\mu{\rm m}`.

**Answer.** About 71.43 nm shortening when the initial tensile
stress is released. In the book's tension-negative convention,
the signed relaxation result is :math:`\Delta L=-71.43` nm.

**Check.** A beam subjected to a newly applied tensile force
would instead lengthen. Distinguish release of prestress from
application of a load.

Problem 19.8 — Three MOEM mechanical categories
-----------------------------------------------

**Working.** The chapter groups devices by their compliant structure:
membranes, cantilevers, and torsion plates. A membrane deflects
under pressure, a cantilever bends about its clamp, and torsion
supports rotate a plate about an axis.

**Answer.** Examples are an optically read pressure diaphragm,
a cantilever-supported tunable cavity mirror, and a torsional
scanning mirror or optical switch.

**Check.** “Sensor, actuator, and switch” classify device functions,
not the three structural categories emphasized by this chapter.

Problem 19.9 — Circular-plate deflection away from the centre
-------------------------------------------------------------

**Working.** For diameter 12 mm, thickness 250 micrometres,
and :math:`r=4` mm,

.. math::

   \frac{w(r)}{w(0)}=
   \left[1-\left(\frac{2r}{d}\right)^2\right]^2
   =\left(1-\frac49\right)^2=\frac{25}{81}.

Evaluate the centre deflection with the same pressure and elastic
constants as 19.6, then multiply by this factor.

**Answer.** :math:`w(4\,{\rm mm})=2.28324\,\mu{\rm m}`
using denominator 256. The printed denominator 265 gives
2.20569 micrometres.

**Check.** Deflection approaches zero with zero slope at the
clamped edge and is maximal at the centre.
