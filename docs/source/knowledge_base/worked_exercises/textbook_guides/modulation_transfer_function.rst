Modulation Transfer Function
============================

Reference: Glenn D. Boreman, *Modulation Transfer Function in Optical and
Electro-Optical Systems*, second edition (2021).

Use this reference to connect image formation, detector sampling, and
measured system contrast.

Define the transfer function
----------------------------

For linear, shift-invariant incoherent intensity imaging,

.. math::

   \mathrm{OTF}(\nu_x,\nu_y)=
   \frac{\mathcal{F}\{\mathrm{PSF}\}(\nu_x,\nu_y)}
        {\mathcal{F}\{\mathrm{PSF}\}(0,0)},
   \qquad \mathrm{MTF}=|\mathrm{OTF}|.

Record field, spectral weighting, focus, and object- or image-space units.

Optics, detector, and sampling
------------------------------

A rectangular sensitive pixel width :math:`a` contributes

.. math::

   \mathrm{MTF}_{\mathrm{pixel}}(\nu)=
   \left|\frac{\sin(\pi a\nu)}{\pi a\nu}\right|.

This differs from the sampling Nyquist frequency :math:`1/(2p)`, where
:math:`p` is pitch. Transfer functions multiply when the required linear,
shift-invariant assumptions hold. Aliasing needs separate consideration.

A pupil model predicts a PSF and MTF; a slanted edge estimates system SFR;
a USAF target measures square-wave contrast. State processing, noise, phase,
field, orientation, focus, and repeatability before comparing these methods.

Related documentation
---------------------

* :doc:`../../eol_imaging_qualification/lens`
* :doc:`../../eol_imaging_qualification/camera`
* :doc:`../../rules_of_thumb`
