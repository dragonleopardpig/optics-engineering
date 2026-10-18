Chapter 21: Optoelectronic Devices in Wireless Systems
======================================================

Source: Hunsperger, sixth edition (2009), Problems 21.1--21.8,
printed pages 464--465.

Problem 21.1 — Overall microwave-link power gain
------------------------------------------------

**Working.** Multiply the two conversion slopes and optical
transmission :math:`T=1/2.5`:

.. math::

   G_I=(10\,{\rm mW/mA})(3\,{\rm mA/mW})/2.5=12.

With the specified equal resistances,
:math:`G_P=G_I^2R_{\rm out}/R_{\rm in}=144`.

**Answer.** Power gain is 144, or
:math:`10\log_{10}(144)=21.5836` dB.

**Check.** Current gain is 12, not the power gain. The units of
the two electro-optic slopes cancel only after optical transmission
is included.

Problem 21.2 — Bandwidth under increased laser power
----------------------------------------------------

**Working.** If the quoted bandwidth is limited by the laser's
relaxation frequency, use the usual approximation
:math:`f_R\propto\sqrt P` at a fixed device/operating regime:

.. math::

   f_2=40\,{\rm GHz}\sqrt{200/100}=56.5685\,{\rm GHz}.

**Answer.** Approximately 56.6 GHz under that specific
relaxation-limited assumption.

**Check.** Optical power alone does not determine whole-link
bandwidth. An RC-, receiver-, package-, or transit-limited
40 GHz link could remain near 40 GHz after increasing power.

Problem 21.3 — Materials for an OMMIC
-------------------------------------

**Working.** III–V direct-gap alloys support optical emission
and detection, while high carrier mobility permits microwave
electronic devices. AlGaAs layers are compatible with GaAs;
appropriate InGaAsP compositions can be lattice matched to InP.

**Answer.** GaAs is the natural substrate for GaAs/AlGaAs
devices, and InP for lattice-matched InGaAsP devices.
Material composition sets optical wavelength and confinement.

**Check.** The acronym describes integrating microwave and
optoelectronic functions; substrate choice still requires
compatible lattice constants, bandgaps, and processing.

Problem 21.4 — Unequal-resistance link gain
-------------------------------------------

**Working.** For sinusoidal currents, the same peak/RMS
conversion appears at each port and cancels:

.. math::

   G_P=\left(\frac{I_{\rm out}}{I_{\rm in}}\right)^2
       \frac{R_{\rm out}}{R_{\rm in}}
   =30^2(1/2)=450.

**Answer.** :math:`G_{\rm dB}=10\log_{10}(450)=26.5321` dB.

**Check.** Using :math:`20\log_{10}(30)` alone neglects the
resistance ratio and overestimates power gain by 3.0103 dB.

Problem 21.5 — Four enabling improvements
-----------------------------------------

**Working.** In the book's historical interval, low-loss fiber
extended reach; stable narrow-linewidth semiconductor lasers
enabled dense channel allocation; high-speed modulators/detectors
raised per-channel rate; and optical amplifiers restored many
channels together without electronic regeneration at every repeater.

**Answer.** Those four developments form a consistent explanation
for modern lightwave telecom in the edition's context.

**Check.** Explain the role of each improvement rather than
listing four kinds of components with no connection to
capacity, reach, or practical deployment.

Problem 21.6 — GaAs and InP substrate advantages
------------------------------------------------

**Working.** The substrate supports compatible epitaxial optical
and microwave device layers. High electron mobility enables
fast electronic devices; direct-gap active layers provide gain
and detection; semi-insulating substrates can reduce parasitic
coupling between microwave structures.

**Answer.** The platform can combine lasers, detectors,
waveguides, and microwave electronics with reduced interconnect
and packaging length.

**Check.** The bare substrate need not perform every optical
function. Alloy layers and doping provide the required
bandgap, index, and carrier profiles.

Problem 21.7 — Gain from the two peak currents
----------------------------------------------

**Working.** With 10 mA input, 15 mA output, and equal
50 ohm resistances,

.. math::

   G_P=(15/10)^2=2.25,\qquad
   G_{\rm dB}=10\log_{10}(2.25)=3.52183\,{\rm dB}.

**Answer.** Approximately 3.522 dB.

**Check.** Use either peak currents at both ports or RMS at
both ports. Mixing them creates a factor of two in power.

Problem 21.8 — Double the receiver resistance
---------------------------------------------

**Working.** Keeping the stated current amplitudes unchanged,
increase :math:`R_{\rm out}/R_{\rm in}` from one to two:

.. math::

   G_P=(15/10)^2(100/50)=4.5,\qquad
   G_{\rm dB}=6.53213\,{\rm dB}.

**Answer.** Approximately 6.532 dB under the unchanged-current
assumption, a 3.0103 dB increase.

**Check.** A real receiver load change may also change current
and bandwidth. The arithmetic result uses the idealized
fixed-current comparison requested by the question.
