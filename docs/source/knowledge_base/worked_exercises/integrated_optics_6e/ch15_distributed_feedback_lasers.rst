Chapter 15: Distributed-Feedback Lasers
=======================================

Source: Hunsperger, sixth edition (2009), Problems 15.1--15.8,
printed pages 321--322.

Problem 15.1 — First-order GaAs feedback period
-----------------------------------------------

**Working.** Backward guided-wave feedback requires
:math:`2\beta=2\pi/\Lambda`. At 0.895 micrometres the Table 4.2
GaAs index is approximately 3.57411. Approximating modal index by
that material value,

.. math::

   \Lambda=\frac{0.895}{2(3.57411)}=0.125206\,\mu{\rm m}.

**Answer.** Approximately 125.2 nm.

**Check.** The exact period uses the guided effective index and
therefore depends on the vertical structure. A bulk index is the
implicit approximation when no guide geometry is supplied.

Problem 15.2 — Feedback period in Al0.2Ga0.8As
----------------------------------------------

**Working.** Table 4.2 at the same wavelength gives
:math:`n(x=0.2)=3.43621`. Repeat the first-order condition:

.. math::

   \Lambda=\frac{0.895}{2(3.43621)}
   =0.130231\,\mu{\rm m}.

**Answer.** Approximately 130.2 nm in the material-index approximation.

**Check.** Reducing index increases the required geometric period
for a fixed vacuum Bragg wavelength.

Problem 15.3 — Two prism-assisted exposure geometries
-----------------------------------------------------

**Working.** For writing wavelength 325 nm, the period from 15.1
requires :math:`n_p\sin\alpha=\lambda_w/(2\Lambda)=1.29786`.
Two possible design pairs are

.. math::

   n_p=1.48:\quad\alpha=\sin^{-1}(1.29786/1.48)\simeq61.27^\circ,
   \qquad
   n_p=1.65:\quad\alpha\simeq51.87^\circ.

**Answer.** A UV-transparent fused-silica prism near index 1.48
and a quartz prism under the book's 1.65 index assumption give
these illustrative angle choices.

**Check.** Verify the actual writing-wavelength index and UV
transmission of the selected material. Index must exceed 1.29786;
an opaque high-index prism is not useful.

Problem 15.4 — Fourth-order feedback and scattering directions
--------------------------------------------------------------

**Working.** An order-4 backward condition satisfies
:math:`4K=2\beta`, with :math:`K=2\pi/\Lambda`.
Hence :math:`\Lambda=2\lambda_0/N`.
The intermediate grating orders have axial components
:math:`\beta_\ell=\beta-\ell K=\beta(1-\ell/2)`.

**Answer.** In the simple same-index wavevector construction,
:math:`\cos\theta_\ell=1-\ell/2` gives directions
0, 60, 90, 120, and 180 degrees for
:math:`\ell=0,1,2,3,4`.
The perpendicular order requires :math:`\ell=m/2`, an integer,
so it is absent for odd backward-feedback orders.

.. figure:: /_static/knowledge_base/worked_exercises/integrated_optics_6e/grating_orders.svg
   :alt: Fourth-order feedback allows intermediate directions at 60, 90, and 120 degrees between forward and backward waves.
   :width: 100%

   Same-index wavevector construction for the intermediate orders.

**Check.** Escaping radiation must additionally satisfy the
cladding dispersion and refraction conditions. The wavevector
construction does not guarantee equal power in all orders.

Problem 15.5 — Bragg wavelength and index tuning
------------------------------------------------

**Working.** For first-order feedback,

.. math::

   \lambda_B=2N\Lambda=2(3.8)(0.120)=0.912\,\mu{\rm m}.

At fixed period, :math:`\delta\lambda/\lambda=\delta N/N`.
A one-part-in-ten-million index increase gives
:math:`\delta\lambda=9.12\times10^{-5}` nm and
:math:`\delta\nu/\nu=-10^{-7}`.

**Answer.** Nominal wavelength 912 nm; frequency shifts downward
by approximately 32.872 MHz for a positive index change of that
fraction. A negative index change reverses both signs.

**Check.** Do not confuse a fractional change :math:`10^{-7}`
with an absolute index change of :math:`10^{-7}`.

Problem 15.6 — High-gain DFB frequency and spacing
--------------------------------------------------

**Working.** The Bragg angular frequency is
:math:`\omega_B=2\pi c/(2N\Lambda)=2.24378\times10^{15}\,{\rm rad/s}`.
The book's high-gain approximation gives

.. math::

   \omega_m\simeq\omega_B-(m+\tfrac12)\frac{\pi c}{n_gL}.

Taking :math:`n_g\simeq N=3.65` and :math:`L=300\,\mu{\rm m}`,
:math:`\pi c/(n_gL)=8.60115\times10^{11}\,{\rm rad/s}`.

**Answer.** The :math:`m=0` branch has
:math:`\omega_0\simeq2.24335\times10^{15}\,{\rm rad/s}`.
Adjacent orders on that branch are separated by
:math:`8.60115\times10^{11}\,{\rm rad/s}`.

**Check.** The lowest-order oscillation is shifted from the Bragg
frequency by half a spacing. A general DFB spectrum also depends
on coupling and boundary conditions; the supplied high-gain assumption
is what permits this simplified answer.

Problem 15.7 — Second-order gratings
------------------------------------

**Working.** A second-order feedback grating has
:math:`K=\beta`. Its first scattering order therefore has zero
longitudinal wavevector and can couple light out perpendicular
to the guide. That radiation drains power from an edge-emitting
laser instead of contributing only to backward guided feedback.

**Answer.** Avoid that extra radiation loss in a conventional
edge-emitting DFB; exploit it in a surface-emitting grating laser.

**Check.** Whether an order actually radiates depends on the
surrounding optical structure, but second-order designs make the
normal-outcoupling momentum available.

Problem 15.8 — Interpret the frequency-spacing units
----------------------------------------------------

**Working.** Converting the angular-frequency spacing to hertz,

.. math::

   \Delta\nu=\frac{c}{2n_gL}
   \simeq\frac{299792458}{2(3.62)(250\times10^{-6})}
   =1.65631\times10^{11}\,{\rm Hz}.

**Answer.** Approximately 165.63 GHz, or
:math:`1.65631\times10^{14}` mHz if the printed lowercase
unit is taken literally. It is 165631 MHz if MHz was intended.

**Check.** Lowercase m means milli, uppercase M means mega.
The physical spacing of this short cavity is not millihertz.
