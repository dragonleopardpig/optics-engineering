From CAD Geometry to an Optical Model
=====================================

A CAD drawing describes mechanical geometry. An optical model also needs
materials, refractive indices, coatings, clear apertures, and explicit
assumptions about how light interacts with each boundary.

Three useful representations
----------------------------

.. list-table::
   :header-rows: 1
   :widths: 25 40 35

   * - Representation
     - Useful for
     - Check before tracing
   * - Display mesh
     - Position, orientation, envelopes, and mechanical clearance
     - Whether the geometry participates in the optical calculation
   * - Triangulated optical boundary
     - General shapes and occlusion
     - Mesh resolution, topology, surface normals, and material assignment
   * - Analytic optical surfaces
     - Spheres, planes, conics, and fitted aspheres
     - Fit residuals, aperture boundaries, and the surface prescription

A visually smooth tessellation does not establish optical surface accuracy.
Check the error in sag and surface normal against the required ray or
wavefront precision.

Coordinate frames and normals
-----------------------------

Transform both the position and direction of a ray consistently between
local and global frames. For a rigid rotation :math:`R` and translation
:math:`\boldsymbol{t}`,

.. math::

   \boldsymbol{x}_{g}=R\boldsymbol{x}_{l}+\boldsymbol{t},
   \qquad
   \boldsymbol{d}_{g}=R\boldsymbol{d}_{l}.

Surface normals determine the incidence angle and the media on either side
of an interface. Keep the material sequence consistent with the chosen
normal convention.

Converting a lens
-----------------

#. Identify the optical faces and separate them from bevels, mounts, and
   mechanical decoration.
#. Determine the surface shapes and their clear apertures.
#. Assign glass or other media to the correct volume or interval.
#. Assign coatings or scattering properties where needed.
#. Check the coordinate frames and the physical order of the interfaces.
#. Trace axial, marginal, and field rays; inspect hits, normals, and clipping.
#. Compare the model with a known focal length or an independent prescription.

Reversing an optical assembly
-----------------------------

Rotate the physical geometry and rebuild the traversal order. Recalculate
curvature signs, coordinate transforms, material intervals, and surrounding
air gaps in the adopted convention. Reversing a list of surface records
alone does not establish the same physical assembly.

Validation
----------

Check dimensions, units, refractive-index data, intersections, and power
accounting. Compare a mesh representation with an analytic surface when a
known reference exists, and refine the mesh until the optical result
converges.

See :doc:`lens_design_intro` for interpreting a prescription and
:doc:`cardinal_points` for checking first-order image geometry.
