Stray Light Analysis and Control
================================

Reference: Eric C. Fest, *Stray Light Analysis and Control* (SPIE Press, 2013).

Use this reference to distinguish unwanted geometric paths, specular ghosts,
surface scatter, and calibrated radiometric quantities.

Define the quantity
-------------------

Record source radiance or power, angular and spectral distributions,
surface properties, apertures, detector response, and normalization.
A ray count is not generally a power fraction.

For detector irradiance, directional radiance contributes

.. math::

   E=\int_{\Omega} L(\boldsymbol{\omega})
   \cos\theta\,\mathrm{d}\Omega.

Include spectral integration when source, coatings, or detector response
vary materially with wavelength.

Separate the mechanisms
-----------------------

* **Direct paths:** an unintended opening or line of sight.
* **Ghosts:** unwanted paths formed by specular reflections.
* **Surface scatter:** angular redistribution described by a BRDF or BSDF.
* **Volume effects:** absorption or bulk scattering within a medium.

Check energy accounting, angular sampling, normalization, and convergence
of low-probability paths. Compare suppression measures using the same source
and detector definitions as the original prediction.

Related documentation
---------------------

* :doc:`/knowledge_base/coaxial_led_dark_edges`
* :doc:`/knowledge_base/pupil_sampling`
* :doc:`/knowledge_base/eol_imaging_qualification/lens`
