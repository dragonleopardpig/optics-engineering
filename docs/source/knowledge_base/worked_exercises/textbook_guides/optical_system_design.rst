Optical System Design
=====================

Reference: Robert E. Fischer, Biljana Tadic-Galeb, and Paul R. Yoder,
*Optical System Design*, second edition.

Use this reference to connect an optical prescription with instrument
requirements: imaging, illumination, detectors, packaging, and verification.

Start with measurable requirements
----------------------------------

Record object conjugate, field, spectrum, aperture, working distance,
detector sampling, and required signal or contrast. Express acceptance
criteria in quantities that can be calculated and measured.

Keep the optical resolution requirement separate from detector sampling:

.. math::

   \nu_{\mathrm{Nyquist}}=\frac{1}{2p},

where :math:`p` is pixel pitch. State whether frequency is specified in
object or image space.

Build an error budget
---------------------

For independent, small, approximately linear contributors,

.. math::

   \sigma_P^2 \simeq \sum_i
   \left(\frac{\partial P}{\partial x_i}\sigma_i\right)^2.

Correlated errors, clipping, nonlinear compensators, and asymmetric yield
limits require a fuller model or Monte Carlo analysis.

Review requirements, establish a first-order model, evaluate field and
wavelength dependence, identify compensators, then define acceptance tests.

Related documentation
---------------------

* :doc:`../../rules_of_thumb`
* :doc:`../../active_fiber_alignment`
* :doc:`../../eol_imaging_qualification/index`
