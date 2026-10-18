Chapter 7: Waveguide Input and Output Couplers
==============================================

Source: Hunsperger, sixth edition (2009), Problems 7.1--7.12,
printed pages 149--151.

Angle convention for prism calculations
---------------------------------------

Let :math:`\gamma` be the exit face angle to the guide plane and
:math:`\psi` the outgoing beam's angle above that plane. The face
normal lies at :math:`\nu=90^\circ-\gamma`. On the geometry branch
used below, Snell's law and phase matching give

.. math::
   :label: integrated-prism-angles

   \delta=\sin^{-1}\!\left[\frac{\sin(\psi-\nu)}{n_p}\right],
   \qquad N=n_p\cos(\nu+\delta),\qquad \beta=k_0N.

Reverse the rays for input coupling. Angles from a face normal are signed;
their sign identifies which side of the normal contains the ray.

Problem 7.1 — Effective indices from three prism lines
------------------------------------------------------

**Working.** Use :math:`\gamma=60^\circ`, so :math:`\nu=30^\circ`,
with :math:`n_p=2.32` and :math:`\lambda_0=0.905\,\mu{\rm m}`.
For each measured beam angle apply :eq:`integrated-prism-angles`.

.. list-table:: Prism-line results
   :header-rows: 1

   * - :math:`\psi`
     - :math:`N`
     - :math:`\beta\ [{\rm cm}^{-1}]`
   * - 36.5 degrees
     - 1.95018
     - 135396
   * - 30.2 degrees
     - 2.00743
     - 139371
   * - 24.6 degrees
     - 2.05458
     - 142644

**Answer.** The smallest listed exit angle belongs to the lowest
order because it gives the largest effective index.

**Check.** All effective indices remain below the core index 2.09.
The external surface angle is not the internal incidence angle.

Problem 7.2 — Excite the same fundamental through rutile
--------------------------------------------------------

**Working.** Keep :math:`N_0=2.05458` from 7.1 and replace the
prism index by 2.50. The internal ray angle from the guide plane is
:math:`\chi=\cos^{-1}(N_0/2.50)`. Subtract the face-normal
angle 30 degrees, refract to air, and restore that normal angle:

.. math::

   \psi=30^\circ+\sin^{-1}[2.50\sin(\chi-30^\circ)]
   =41.9005^\circ.

**Answer.** Use the reciprocal input ray making about 41.90 degrees
with the guide surface.

**Check.** The 11.90 degree result inside the last arcsine is the
angle relative to the entrance-face normal, not the requested surface angle.

Problem 7.3 — Derive longitudinal phase matching
------------------------------------------------

**Working.** A plane wave inside the prism has magnitude
:math:`k_0n_p`. If its incidence angle from the guide normal is
:math:`\theta_p`, its tangential component is
:math:`k_0n_p\sin\theta_p`. Coupling contributions at different
points along the guide accumulate constructively only when this
component equals the guided propagation constant.

.. math::

   \beta=k_0n_p\sin\theta_p
   =\frac{2\pi n_p}{\lambda_0}\sin\theta_p.

**Answer.** This is the required prism phase-matching condition.

**Check.** Phase matching alone is insufficient: the evanescent fields
must overlap across a sufficiently thin gap and the interaction length
must supply appreciable transfer.

Problem 7.4 — Input angle for the right-angle prism
---------------------------------------------------

**Working.** Convert :math:`\beta=1.40\times10^5\,{\rm cm}^{-1}`
to :math:`N=\beta(0.905\times10^{-4})/(2\pi)=2.01654`.
For :math:`n_p=2.32`, the internal ray makes
:math:`\chi=\cos^{-1}(N/n_p)` with the guide. With a 45 degree
face, its internal signed incidence is :math:`\chi-45^\circ`.
Snell refraction gives

.. math::

   \psi=45^\circ+\sin^{-1}[2.32\sin(\chi-45^\circ)]
   =7.0731^\circ.

**Answer.** The input beam makes about 7.07 degrees with the surface
on this reciprocal-ray branch.

.. figure:: /_static/knowledge_base/worked_exercises/integrated_optics_6e/prism_angles.svg
   :alt: The prism face, face normal, internal ray, and outgoing air ray are labelled separately.
   :width: 100%

   Reverse the arrows for reciprocal input coupling.

**Check.** Label :math:`\chi`, the face normal, and :math:`\psi`
separately. A 45 degree face does not imply 45 degree beam incidence.

Problem 7.5 — Smallest period for backward reflection
-----------------------------------------------------

**Working.** Reversing a guided wave changes its axial momentum
from :math:`+\beta` to :math:`-\beta`. A first-order grating supplies
:math:`K=2\pi/\Lambda=2\beta`. Therefore

.. math::

   \Lambda_{\min}=\frac{\lambda_0}{2N}
   =\frac{0.6328}{2(1.582)}=0.2000\,\mu{\rm m}.

**Answer.** A first-order 200 nm grating.

**Check.** Higher diffraction orders have larger periods for the same
backward-scattering momentum, so they do not give a smaller spacing.

Problem 7.6 — Choose a prism face for direct entrance
-----------------------------------------------------

**Working.** The given propagation constant implies
:math:`N=(1.44\times10^5)(0.905\times10^{-4})/(2\pi)`.
Phase matching in the :math:`n_p=2.5` prism gives an internal
ray angle :math:`\phi=33.9379^\circ` from the guide plane.
Choose normal incidence on the entrance face, making its normal
parallel to the ray.

**Answer.** A convenient face angle is
:math:`\gamma=90^\circ-\phi=56.0621^\circ`; the internal ray
makes 33.9379 degrees with the guide.

**Check.** This is the natural normal-entrance geometry, not a complete
optimization of coupling efficiency. Gap, beam width, polarization,
Fresnel transmission, and interaction length also matter.

Problem 7.7 — First-order grating input angle
---------------------------------------------

**Working.** For incidence from air at angle :math:`\psi` from the
surface, tangential momentum conservation is
:math:`N=\cos\psi+\lambda_0/\Lambda`. Hence

.. math::

   \cos\psi=3.6-\frac{1.15}{0.4}=0.725,
   \qquad \psi=\cos^{-1}(0.725)\simeq43.53^\circ.

**Answer.** Approximately 43.53 degrees from the surface.

**Check.** The required cosine lies between minus one and one.
Without grating momentum, an air beam cannot supply an effective
index of 3.6.

Problem 7.8 — Exit beam from a 45-degree prism
----------------------------------------------

**Working.** From :math:`N=1.481` and :math:`n_p=2.25`,
the internal ray angle is :math:`\chi=\cos^{-1}(1.481/2.25)`.
Refract its signed angle :math:`\chi-45^\circ` at the exit:

.. math::

   \psi=45^\circ+\sin^{-1}[2.25\sin(\chi-45^\circ)]
   =53.6565^\circ.

**Answer.** The emerging beam makes about 53.66 degrees with
the waveguide surface on the illustrated exit branch.

**Check.** The air-side angle relative to the prism normal is only
8.6565 degrees; it is not the surface angle.

Problem 7.9 — Use the face angle in the supplied drawing
--------------------------------------------------------

**Data.** The drawing shows a 30 degree face, index 2.2, and an
outgoing ray 26.43 degrees clockwise from the face normal.

**Working.** The normal is 60 degrees above the guide. The internal
ray angle above the guide is
:math:`\chi=60^\circ-\sin^{-1}[\sin(26.43^\circ)/2.2]`.
Then

.. math::

   \beta=\frac{2\pi}{0.6328\times10^{-4}}(2.2\cos\chi)
   =1.45236\times10^5\,{\rm cm}^{-1}.

**Answer.** Approximately :math:`1.4524\times10^5\,{\rm cm}^{-1}`.

**Check.** The effective index is about 1.4627, within the
1.4-to-1.5 guiding interval shown in the source figure.

Problem 7.10 — Prism incidence and core bounce angles
-----------------------------------------------------

**Working.** These are different media and different reference axes:

.. math::

   \theta_p=\sin^{-1}(1.481/2.25)=41.1644^\circ,\qquad
   \theta_{\rm bounce}=\cos^{-1}(1.481/1.5)=9.12911^\circ.

**Answer.** (a) 41.16 degrees inside the prism, measured from the
guide normal. (b) 9.129 degrees in the core, measured from the plane.

**Check.** Both share the same axial momentum :math:`k_0N`,
although their wavevector magnitudes and angles differ.

Problem 7.11 — Reuse a grating at a second wavelength
-----------------------------------------------------

**Working.** For a fixed grating period and order,

.. math::

   n_{\rm inc}\cos\psi(\lambda_0)
   =N(\lambda_0)-m\lambda_0/\Lambda.

Changing wavelength changes both the grating momentum normalized to
:math:`k_0` and the guided effective index. Adjust the beam angle
to restore equality.

**Answer.** Reuse is possible if the 1.06 micrometre guide mode
exists and the required right-hand side lies in
:math:`[-n_{\rm inc},n_{\rm inc}]`. Otherwise that order cannot couple.

**Check.** A grating that works at 0.85 micrometres does not guarantee
an accessible angle at every wavelength; the existence condition is essential.

Problem 7.12 — Holographic grating exposure periods
---------------------------------------------------

**Working.** Two coherent writing beams in the prism have opposite
tangential wavevectors. Their difference is
:math:`2(2\pi n_p/\lambda_w)\sin\alpha`, so

.. math::

   \Lambda=\frac{\lambda_w}{2n_p\sin\alpha}.

With :math:`n_p=1.65` and :math:`\alpha=5^\circ`,
the periods are about 1130 nm for the 325 nm laser and
671 nm for the 193 nm laser.

**Answer.** Approximately 1.130 and 0.671 micrometres.

**Check.** Their ratio equals :math:`325/193`. The angle is the
internal half-angle measured from the normal in Fig. 7.10.
