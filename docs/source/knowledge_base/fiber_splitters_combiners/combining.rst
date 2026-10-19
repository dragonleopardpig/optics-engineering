Combining Several Fibers into One Fiber
=======================================

The required output determines the architecture. Several wavelengths,
two polarization components, or many spatial modes can share one fiber.
Combining all power into one spatial mode, one polarization, and one
spectral channel is a more restrictive problem.

.. contents:: On this page
   :local:
   :depth: 2


Why reversing a splitter has a penalty
--------------------------------------

Reciprocity relates transmission between the same pair of optical modes
in opposite directions. It does not say that unrelated inputs all couple
with unity efficiency into one output mode.

For a symmetric splitter with forward common-port transmission
:math:`\eta/N` into each branch, the reverse transmission of each branch
into that common port is also :math:`\eta/N`. Here :math:`\eta` is the
power transmission after excess loss. For mutually incoherent inputs,
interference averages to zero, giving

.. math::

   \left\langle P_{\rm common}\right\rangle
       =\frac{\eta}{N}\sum_{j=1}^{N}P_j.

**Calculated example.** Four independent 100 mW inputs into an ideal
equal splitter used backward deliver 100 mW to the common port, rather
than 400 mW. The other power occupies other device channels, radiates,
or is dissipated, depending on the physical implementation.

This result is a scattering-model calculation for the specified optical
modes. It does not apply to a wavelength router, a polarization combiner,
or an output that accepts additional spatial modes. The general passive
single-output constraint is
:math:`\sum_j |S_{oj}|^2\leq 1`, with :math:`S_{oj}` the field transmission
from input :math:`j` to output mode :math:`o` at the frequency of interest.
It prevents every independent input from having unit transmission into
that same output mode.

There is also a practical packaging consequence: the unused arm of a
1-by-2 coupler can become an internally dumped output in reverse operation.
Thorlabs discusses this explicitly in its
`PM coupler tutorial and manufacturer response <https://www.thorlabs.com/newgrouppage9.cfm?objectgroup_id=10015>`_.
Use the manufacturer's approved topology and account for rejected power.


Different wavelengths: WDM and spectral combining
-------------------------------------------------

A WDM routes wavelength bands, allowing each input wavelength to have
high transmission to the common fiber. Implementations include fused
wavelength-selective couplers, thin-film dichroic filters, and AWGs.
For widely separated visible laser lines, a collimator/dichroic/fiber-launch
assembly is another implementation.

The output remains multiwavelength. It does not become a single optical
frequency. Passband separation, linewidth, temperature drift, leakage
between channels, and the common fiber's guidance and attenuation across
the entire spectrum determine suitability. An SM fiber at one wavelength
may be multimode at a shorter wavelength.

Primary background includes :ref:`fiber-original-smit` and the
:ref:`fiber-review-smit` review. A product example is Thorlabs'
`two-wavelength PM WDM family <https://www.thorlabs.us/newgrouppage9.cfm?objectgroup_id=6166>`_.

High-power spectral beam combining can instead use free-space gratings or
filters. A combined free-space beam still needs an adequately rated,
well-matched fiber launch to satisfy a fiber-output requirement. The
overall spectral/coherent distinction is developed in
:ref:`fiber-review-fan`.


Two polarizations: polarization beam combining
----------------------------------------------

A PBC combines two suitably aligned, orthogonally polarized inputs into
one spatial mode. Mutual phase locking is unnecessary for transferring
their powers into the two orthogonal output polarization states. The
result is not generally one fixed linear polarization.

There are only two independent polarization states per spatial mode.
Repeated PBC stages alone therefore cannot combine an arbitrary number of
independent same-wavelength sources into that same spatial mode without
another distinction between channels. If a downstream linear polarizer
selects one axis of two equal, mutually incoherent orthogonal components,
it transmits only half their combined power in the ideal case.

Verify input polarization extinction ratio, axis/key conventions,
insertion loss, and whether the common pigtail is SM or PM. Thorlabs'
`fused-fiber PBC documentation <https://www.thorlabs.com/fused-fiber-polarization-combinerssplitters-3-pm-ports>`_
describes bidirectional operation and the required axis alignment. PM
fiber itself is not a polarizer.


Independent same-wavelength sources: multimode power combining
--------------------------------------------------------------

A tapered fused bundle merges several input fibers into an output with
sufficient modal capacity. This can transfer a large fraction of the
total input power while allowing a larger output core, a larger angular
spread, or both. It does not promise the beam quality of a single
diffraction-limited input.

Two practical classes must be distinguished:

* **Pump combiner:** several pump fibers feed the inner cladding of a
  double-clad fiber. A pump/signal design adds a central signal path to
  the output core. Thus ``(6+1)x1`` usually means six pump inputs and one
  signal input; check the vendor's actual port definition.
* **Signal power combiner:** several laser outputs feed the guiding core
  of a common output fiber. Beam parameter product, mode content, and
  backward-power handling are central specifications.

The construction and difference between pump-only and pump/signal devices
are reviewed by :ref:`fiber-review-stachowiak`. An original tapered-bundle
disclosure is :ref:`fiber-patent-digiovanni`. For signal combining,
`Coherent's kilowatt signal-combiner datasheet <https://www.coherent.com/resources/datasheet/optics/kilowatt-signal-combiner-ksc-ds.pdf>`_
explicitly specifies output beam-quality parameters as well as power
transfer. High transfer efficiency and single-mode output are separate
requirements.

End-pump bundles interrupt and join the signal path. Taper-fused side-pump
designs inject pump light along a signal fiber while retaining an
uninterrupted signal core; see :ref:`fiber-review-lei`. Pump injection
followed by stimulated emission in a gain fiber is an active laser or
amplifier process. It is not passive conversion of arbitrary pump beams
into one coherent signal mode.

Lei's full-text review also identifies input-pump NA sensitivity and
fabrication-induced signal degradation. An uninterrupted core still
needs suitable heating, fusion geometry, and control of mechanical
deformation and dopant diffusion. Verify pump transfer, backward coupling,
and signal beam quality together.


An initial acceptance-capacity calculation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For highly multimode, fully filled step-index fibers in comparable media,
optical etendue scales as :math:`G\propto A\,NA^2`. A necessary capacity
condition for transferring all independent input phase space is

.. math::

   A_{\rm out}NA_{\rm out}^{2}
       \gtrsim \sum_j A_jNA_j^2.

Here :math:`A` is guiding core area, or guiding inner-cladding area for
a pump path. For :math:`N` identical circular input cores of diameter
:math:`d_{\rm in}`,

.. math::

   d_{\rm out}NA_{\rm out}
       \gtrsim \sqrt{N}\,d_{\rm in}NA_{\rm in}.

**Calculated example.** Seven fully filled 105 micrometre cores at
NA = 0.22 require about a 278 micrometre output core at the same NA by
this capacity estimate. A 200 micrometre output at NA = 0.22 has only

.. math::

   \frac{200^2}{7\times105^2}=0.518

of the input acceptance. For equally bright, uniformly filled inputs,
this implies at most about 52% throughput in that restricted model.
Underfilled inputs can behave differently. Meeting the capacity condition
is necessary, not sufficient: taper geometry, splices, bends, and leakage
still determine real performance. This is an engineering screening
calculation based on radiance conservation, not a component specification.


Photonic lanterns and spatial mode multiplexers
-----------------------------------------------

A photonic lantern adiabatically maps several SM cores into the modes
of one few-mode or MM core. A sufficiently large output modal space
allows independent inputs to remain independent optical degrees of
freedom inside one fiber. For low loss in both directions over all
supported modes, match the mode counts and maintain an adiabatic
transition. Count polarization consistently on both sides.

An ordinary lantern does not guarantee a particular input-to-output-mode
assignment. Mode-selective lanterns and other mode multiplexers address
that mapping. Multi-plane light conversion (MPLC) implements spatial
transformations with repeated phase manipulation and propagation;
:ref:`fiber-original-morizur` gives an experimental basis.

The early lantern demonstration is :ref:`fiber-original-leonsaval`;
:ref:`fiber-review-birks` explains the wider technology. The 2005
proof-of-concept filter used 19 SM paths with a much larger MM mode
count and measured only 3.4% off-notch transmission. Its principle and
its measured efficiency must therefore be distinguished when tracing
the development of low-loss lanterns.

A multicore-fiber fan-in is a further option if separate cores inside one
physical fiber are acceptable. It does not merge their powers into one
core.


Same output mode and wavelength: coherent combining
---------------------------------------------------

Mutually coherent inputs can interfere constructively at one port and
destructively at another. A useful ideal two-input model, with the
coupler's fixed phase included in the definition of :math:`\phi`, is

.. math::

   P_{\pm}=\frac{\eta}{2}
      \left[P_1+P_2
      \pm2\sqrt{P_1P_2}\,|\gamma|\cos\phi\right].

Here :math:`\gamma` is normalized mutual coherence and field overlap,
:math:`\phi` is the residual relative phase, and :math:`\eta` accounts
for common transmission loss in this model. With equal powers,
:math:`|\gamma|=1`, and :math:`\phi=0`, all transmitted power reaches
the plus port. Random phase averaging instead reproduces the equal
incoherent split between the two ports. For perfect overlap,
:math:`P_+/(\eta(P_1+P_2))=\cos^2(\phi/2)` when the powers are equal.

A practical system needs a shared coherent seed or another means of
establishing mutual coherence, controlled polarization, field matching,
and phase stabilization. Pulses also require temporal overlap and
compatible dispersion. A fixed 50:50 coupler additionally requires equal
input amplitudes to cancel the other output completely; a variable
combiner can accommodate imbalance.

An early all-fiber experiment is :ref:`fiber-original-kozlov`: its cleaved
active-fiber taper was a shared output mirror for two laser cavities,
with injection locking obtained by tuning a Bragg grating. This supplies
a concrete example of establishing coherence through coupled resonators.
A later integrated all-fiber architecture is disclosed in
:ref:`fiber-patent-rothenberg`. For broad context, use
:ref:`fiber-review-fan`.

At high power, the final fiber again concentrates power into a small
guided region. Coherent combining does not remove output-fiber limits
such as stimulated scattering, nonlinear phase, thermal effects, or
facet loading. A free-space coherent-combining demonstration is therefore
not automatically a demonstrated high-power single-fiber delivery system.


Time selection and switching
----------------------------

If only one source must use the output at any instant, a fiber switch can
avoid the fixed split penalty for the selected path. Time interleaving
can also place nonoverlapping pulse streams on a common output with a
suitable switching arrangement. These are routing solutions; they do not
sum simultaneous powers. Specify timing, extinction, switching speed,
and output-fiber peak-power limits.
