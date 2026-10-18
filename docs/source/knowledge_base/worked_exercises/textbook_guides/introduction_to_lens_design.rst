Introduction to Lens Design
===========================

Reference: José Sasián, *Introduction to Lens Design* (Cambridge University
Press, 2019).

Use this reference as a route from surface geometry and ray tracing to
image evaluation, optimization, tolerancing, and ghost analysis.

Read the prescription
---------------------

Record curvature, separation, medium, clear aperture, decentre, and tilt
for each surface. State the object conjugate, stop, field, spectrum, and
detector plane separately. Distinguish an optical aperture from a blank,
barrel, bevel, or mount.

Choose a starting family by inspecting symmetry, stop position, element
powers, glass dispersion, and conjugate ratio.

Optimization and verification
-----------------------------

A weighted residual objective can be expressed as

.. math::

   \Phi(\boldsymbol{x})=\sum_i w_i
   \left[q_i(\boldsymbol{x})-q_{i,\mathrm{target}}\right]^2.

Choose residual scales and weights deliberately. Include field, wavelength,
and manufacturing constraints, and inspect physical metrics separately
from the aggregate objective.

Check marginal rays, clearances, sensitivity to focus, manufacturing and
alignment perturbations, and unwanted illumination paths.

Related documentation
---------------------

* :doc:`../../lens_design_intro`
* :doc:`../../pupil_sampling`
* :doc:`../../step_overlay_promotion`
* :doc:`optical_system_design`
