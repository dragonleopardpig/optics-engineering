Chapter 2: Optical Waveguide Modes
==================================

Source: Hunsperger, sixth edition (2009), Chapter 2, Problems 2.1--2.11,
printed pages 30--31. Use the conventions in :doc:`notation`.

Problem 2.1 — Index interval for one guided order
-------------------------------------------------

**Model.** Use the requested strongly asymmetric approximation with
:math:`n_2=3.4`, :math:`t=3\,\mu{\rm m}`, and
:math:`\lambda_0=1.10\,\mu{\rm m}`.

**Working.** The zeroth order must be above cutoff and the first order
below cutoff. Equation :eq:`integrated-asymmetric-approximation` gives

.. math::

   \frac{1.10^2}{32(3.4)(3^2)}
   <\Delta n<
   \frac{9(1.10^2)}{32(3.4)(3^2)}.

**Answer.** :math:`0.00123570<\Delta n<0.0111213`.
The strict upper bound supplies margin below the next-order cutoff.

**Check.** The cutoff ratio is 9 and both contrasts are small compared
with 3.4. This is a spatial-order condition, not proof of one polarization.

Problem 2.2 — Change the wavelength to 1.06 micrometres
-------------------------------------------------------

**Working.** Keep the geometry of 2.1 and substitute
:math:`\lambda_0=1.06\,\mu{\rm m}`:

.. math::

   \Delta n_{c,0}=\frac{1.06^2}{32(3.4)(3^2)}
   =0.00114747,\qquad
   \Delta n_{c,1}=9\Delta n_{c,0}=0.0103272.

**Answer.** :math:`0.00114747<\Delta n<0.0103272`.

**Check.** Multiplying both endpoints of 2.1 by
:math:`(1.06/1.10)^2=0.92860` recovers this interval. Shorter
wavelength requires less contrast at a fixed mode cutoff.

Problem 2.3 — Double the guiding-layer thickness
------------------------------------------------

**Working.** For :math:`t=6\,\mu{\rm m}`, divide both earlier cutoff
contrasts by four because :math:`\Delta n_c\propto t^{-2}`.

.. list-table:: Single-order contrast intervals
   :header-rows: 1

   * - Vacuum wavelength
     - Lower bound
     - Upper bound
   * - :math:`1.10\,\mu{\rm m}`
     - 0.000308926
     - 0.00278033
   * - :math:`1.06\,\mu{\rm m}`
     - 0.000286867
     - 0.00258180

**Answer.** Choose a contrast strictly between the appropriate bounds.

**Check.** This leaves :math:`t\sqrt{\Delta n}/\lambda_0` unchanged.
Doubling thickness without reducing contrast would permit more orders.

Problem 2.4 — Bounce angle at substrate cutoff
----------------------------------------------

**Working.** The larger cladding index is :math:`n_3=1.6`. At cutoff
:math:`\beta=k_0n_3`. Measure the book's bounce angle from the guide plane:

.. math::

   \cos\theta_c=\frac{\beta}{k_0n_2}=\frac{1.6}{2.0}=0.8,
   \qquad \theta_c=36.8699^\circ.

**Answer.** :math:`36.87^\circ`, the maximum bounce angle compatible
with substrate total internal reflection; bound modes have smaller angles.

**Check.** The complementary incidence angle is
:math:`53.1301^\circ=\sin^{-1}(1.6/2)`. It is measured from the normal.

Problem 2.5 — The three lowest symmetric-slab fields
----------------------------------------------------

**Working.** Reflection symmetry makes the fundamental TE field even,
with no internal zero. The next field is odd and has one zero at the
midplane. The third is even with two internal zeros. Every field decays
exponentially in the claddings.

.. figure:: /_static/knowledge_base/worked_exercises/integrated_optics_6e/slab_modes.svg
   :alt: Symmetric slab fields with zero, one, and two internal nodes and evanescent tails.
   :width: 100%

   Signed fields. Dashed lines mark core boundaries.

**Answer.** TE0 has one lobe, TE1 two opposite-sign lobes, and TE2
three alternating-sign lobes.

**Check.** Interior node count equals order. Squared intensity removes
the signs and is not a substitute for the requested field.

Problem 2.6 — Count reflections at one interface
------------------------------------------------

**Data.** The source diagram supplies :math:`t=3\,\mu{\rm m}`.
:math:`\beta/(k_0n_2)=0.8` gives :math:`\tan\theta=0.6/0.8=0.75`.

**Working.** One crossing advances the ray by :math:`t/\tan\theta`
along the guide. Consecutive reflections at the same interface are
separated by a round trip:

.. math::

   \Delta z=\frac{2t}{\tan\theta}=8\,\mu{\rm m},\qquad
   N_{\rm refl}\simeq\frac{10^4}{8}=1250.

**Answer.** Approximately 1250 cover-interface reflections per centimetre;
the precise endpoint count depends on initial ray position.

**Check.** Counting both interfaces would give 2500. The question names
only one interface.

Problem 2.7 — Reflection phase at critical incidence
----------------------------------------------------

**Working.** For TE reflection into cladding :math:`n_j`, set
:math:`\gamma_j=k_0\sqrt{N^2-n_j^2}`. Then

.. math::

   r_j=\frac{h-i\gamma_j}{h+i\gamma_j}
   =\exp[-2i\tan^{-1}(\gamma_j/h)].

At that interface's critical angle, :math:`N\to n_j^+` and
:math:`\gamma_j\to0`, so the reflection phase tends to zero.

**Answer.** Both :math:`\arg r_j` and the book's positive
half-phase :math:`\varphi_{2j}` tend to zero.

**Check.** At asymmetric-guide cutoff, only the higher-index cladding
reaches critical incidence. The other boundary can retain a phase.
The lateral Goos–Hänchen displacement is a phase derivative and need
not approach zero.

Problem 2.8 — Reflection phases at both boundaries
--------------------------------------------------

**Working.** With :math:`N=1.85`, :math:`n_2=2`, :math:`n_1=1`,
and :math:`n_3=1.7`, cancel the common vacuum wavevector:

.. math::

   h/k_0=\sqrt{4-1.85^2},\quad
   q/k_0=\sqrt{1.85^2-1},\quad
   p/k_0=\sqrt{1.85^2-1.7^2}.

Thus :math:`\varphi_{21}=\tan^{-1}(q/h)=1.11659` rad and
:math:`\varphi_{23}=\tan^{-1}(p/h)=0.765122` rad.

**Answer.** Half-phases: 1.11659 and 0.765122 rad. Full reflection
phases for the stated time convention: :math:`-2.23318` and
:math:`-1.53024` rad.

**Check.** Both decay constants are real because :math:`N>1.7`.
A displacement in metres would also require the wavelength; these
dimensionless phases do not.

Problem 2.9 — Wavevector triangle and increasing mode order
-----------------------------------------------------------

**Working.** Resolve the core wavevector into axial and transverse parts:

.. math::

   (k_0n_2)^2=\beta^2+h^2,\qquad \theta=\tan^{-1}(h/\beta).

At fixed frequency and composition, the hypotenuse is fixed. More
transverse oscillations in higher orders require larger :math:`h`,
smaller :math:`\beta`, and a larger bounce angle.

.. figure:: /_static/knowledge_base/worked_exercises/integrated_optics_6e/wavevectors.svg
   :alt: Higher order increases transverse wavevector and decreases axial wavevector at fixed total magnitude.
   :width: 100%

   Bounce angle is measured from the axial direction.

**Answer.** Draw right triangles with a common hypotenuse and progressively
taller transverse sides and shorter axial sides.

**Check.** The last guided order still satisfies
:math:`\beta>k_0n_3`. Below that bound the substrate supports radiation.

Problem 2.10 — Count modes with a quartz overlayer
--------------------------------------------------

**Data audit.** This exercise prints :math:`n_3=1.05` for quartz,
whereas the similar Problem 4.6 uses 1.5. Keep the printed value here.

**Working.** Substitute :math:`n_2=2.09`, :math:`t=2\,\mu{\rm m}`,
and :math:`\lambda_0=0.6328\,\mu{\rm m}` into the exact TE cutoff.
Part (a) has air cover; part (b) has a thick overlayer with
:math:`n_1=n_3=1.05`. Count orders with :math:`t>t_{c,m}`.

**Answer.** Both cases support 12 TE modes, :math:`m=0,\ldots,11`.
The overlayer changes effective indices without changing this integer count.
Each also supports 12 TM modes, giving 24 bound vector modes if both
polarizations are counted.
If 1.5 was intended, the air-covered guide supports 9 TE modes and
the symmetric guide supports 10.

**Check.** In the symmetric case, count nonnegative integers below
:math:`2t\sqrt{2.09^2-1.05^2}/0.6328\simeq11.42`.
The conditional 1.5-index totals are 18 and 20 vector modes, respectively.

Problem 2.11 — Fundamental cutoff and doubled thickness
-------------------------------------------------------

**Working.** For :math:`n_2=3.5`, :math:`n_3=3.38`, :math:`n_1=1`,
and :math:`\lambda_0=0.88\,\mu{\rm m}`, the exact cutoff gives

.. math::

   t_{c,0}=\frac{0.88}{2\pi\sqrt{3.5^2-3.38^2}}
   \tan^{-1}\sqrt{\frac{3.38^2-1}{3.5^2-3.38^2}}
   =0.199839\,\mu{\rm m}.

The next cutoff is
:math:`t_{c,1}=t_{c,0}+0.88/[2\sqrt{3.5^2-3.38^2}]`.
Doubling the fundamental limiting thickness stays below this next cutoff.

**Answer.** (a) A bound TE0 requires thickness just above 0.19984
micrometres. (b) A thickness of 0.39968 micrometres supports one TE mode.

**Check.** The numerical dispersion root at the doubled thickness is
:math:`N=3.42701`, between the substrate and core indices.
