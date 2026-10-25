Photonics Formula Guide
=======================

This guide connects the principal ray, wave, and detector models used in
the worked exercises. Use :doc:`mathematical_formula_reference` for the
mathematical identities behind the detailed derivations.

Conventions
-----------

Use one consistent length unit within each equation. State the optical
axis, radius and angle signs, ray-vector order, and complex-phase
convention. Distinguish field amplitude, intensity, irradiance, and power.

Geometrical optics
------------------

Optical path length and refraction are described by

.. math::

   \mathrm{OPL}=\int n\,\mathrm{d}s,
   \qquad n_1\sin\theta_1=n_2\sin\theta_2.

Angles in Snell's law are measured from the interface normal. In a
homogeneous medium, rays travel along straight segments between surfaces.

Paraxial systems
----------------

For the ray vector :math:`(y,\theta)^T` in air,

.. math::

   \begin{pmatrix}y_2\\\theta_2\end{pmatrix}
   =
   \begin{pmatrix}A&B\\C&D\end{pmatrix}
   \begin{pmatrix}y_1\\\theta_1\end{pmatrix},
   \qquad
   T(d)=\begin{pmatrix}1&d\\0&1\end{pmatrix},
   \qquad
   L(f)=\begin{pmatrix}1&0\\-1/f&1\end{pmatrix}.

Apply matrices in physical traversal order, with the first encountered
element on the right. Paraxial models assume small angles.

Gaussian beams
--------------

For an ideal fundamental Gaussian beam in free space,

.. math::

   z_R=\frac{\pi w_0^2}{\lambda},
   \qquad w(z)=w_0\sqrt{1+(z/z_R)^2},
   \qquad
   \frac{1}{q}=\frac{1}{R}-i\frac{\lambda}{\pi w^2}.

Here :math:`w` is the intensity :math:`1/e^2` radius. Under the stated phase
convention and an appropriate paraxial matrix,

.. math::

   q_2=\frac{Aq_1+B}{Cq_1+D}.

Diffraction and image formation
-------------------------------

For scalar Fraunhofer propagation, the far-field amplitude is related to
the Fourier transform of the aperture field. For incoherent imaging,

.. math::

   \mathrm{PSF}\propto
   \left|\mathcal{F}\{P(x,y)\}\right|^2,
   \qquad
   P(x,y)=a(x,y)\exp\!\left(i\frac{2\pi W(x,y)}{\lambda}\right).

Here :math:`W` is optical-path error in length units. State sampling,
normalization, and frequency-coordinate scaling when calculating a PSF.

Absorption and detection
------------------------

For a uniform absorbing medium and a simple quantum-efficiency model,

.. math::

   I(d)=I(0)e^{-\alpha d},
   \qquad
   R_\lambda=\eta\frac{q_e\lambda}{hc}.

Absorption coefficient and thickness must use reciprocal units.
Responsivity is in A/W when SI units are used. This relation does not
supply bandwidth, saturation, dark current, or noise specifications.

The browser lab includes a standalone photodiode module and worked
transport examples in :doc:`../photonics_essentials/ch03_interactive_lab`.

Choose the appropriate model
----------------------------

* Use rays for geometric paths, apertures, and paraxial sanity checks.
* Use Gaussian beams for ideal paraxial mode size and curvature.
* Use wave propagation for diffraction and coherent interference.
* Use calibrated radiometry and detector models for absolute signals.
* Verify convergence and compare with independent measurements or limits.
