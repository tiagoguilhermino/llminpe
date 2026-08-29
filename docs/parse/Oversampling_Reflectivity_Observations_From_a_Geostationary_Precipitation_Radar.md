Check for updates

AGU ADVANCING EARTH AND SPACE SCIENCE logo

# JAMES Journal of Advances in Modeling Earth Systems

Open Access icon

# RESEARCH ARTICLE

10.1029/2020MS002332

# Oversampling Reflectivity Observations From a Geostationary Precipitation Radar Satellite: Impact on Typhoon Forecasts Within a Perfect Model OSSE Framework

**Key Points:**

* Reflectivity observations from a geostationary precipitation radar improved representation of convective features for a tropical cyclone

* Oversampling with finer beam sampling span improved tropical cyclone intensity errors in analyses and forecasts

* Oversampling improved precipitation and maximum surface wind intensity in forecasts

James Taylor<sup>1,2</sup>, Atsushi Okazaki<sup>1,3</sup>, Takumi Honda<sup>1,2</sup>, Shunji Kotsuki<sup>1,4</sup>, Moeka Yamaji<sup>5</sup>, Takuji Kubota<sup>5</sup>, Riko Oki<sup>5</sup>, Toshio Iguchi<sup>6</sup>, and Takemasa Miyoshi<sup>1,2,7,8,9</sup>

<sup>1</sup>RIKEN Center for Computational Science, Kobe, Japan, <sup>2</sup>Prediction Science Laboratory, RIKEN Cluster for Pioneering Research, Kobe, Japan, <sup>3</sup>Department of Global Environment and Disaster Prevention Sciences, Hirosaki University, Aomori, Japan, <sup>4</sup>Center for Environmental Remote Sensing, Chiba University, Chiba, Japan, <sup>5</sup>Earth Observation Research Center, Japan Aerospace Exploration Agency, Tsukuba, Japan, <sup>6</sup>Earth System Science Interdisciplinary Center, University of Maryland, MD, USA, <sup>7</sup>RIKEN Interdisciplinary Theoretical and Mathematical Sciences Program, Kobe, Japan, <sup>8</sup>Department of Atmospheric and Oceanic Science, University of Maryland, College Park, MD, USA, <sup>9</sup>Japan Agency for Marine Earth Science and Technology, Yokohama, Japan

**Correspondence to:**

J. Taylor and T. Miyoshi, james.taylor@riken.jp; takemasa.miyoshi@riken.jp

**Citation:**

Taylor, J., Okazaki, A., Honda, T., Kotsuki, S., Yamaji, M., Kubota, T., et al. (2021). Oversampling reflectivity observations from a geostationary precipitation radar satellite: Impact on typhoon forecasts within a perfect model OSSE framework. *Journal of Advances in Modeling Earth Systems*, 13, e2020MS002332. [https://doi.org/10.1029/2020MS002332](https://doi.org/10.1029/2020MS002332)

Received 11 SEP 2020
Accepted 5 MAY 2021

**Abstract** For the past two decades, precipitation radars (PR) onboard low-orbiting satellites such as Tropical Rainfall Measuring Mission (TRMM) have provided invaluable insight into global precipitation variability and led to advancements in numerical weather prediction through data assimilation. Building upon this success, planning has begun on the next generation of satellite-based PR instruments, with the consideration for a future geostationary-based PR (GPR), bringing the advantage of higher observation frequency over previous and current PR satellites. Following the successful demonstration by a recent study to test the feasibility of a GPR to obtain three-dimensional precipitation data, this study takes the first step to investigate the potential usefulness of GPR observations for numerical weather prediction by performing a perfect model observing system simulation experiment (OSSE) for a West Pacific tropical cyclone (TC). Data assimilation experiments are performed assimilating reflectivity observations obtained for a range of beam sampling spans, following a previous finding that oversampling improves observation quality. Results showed observations obtained with finer sampling spans of 5 km and 10 km were able to better capture key tropical cyclone features in analyses, including the eye, heavy rainfall associated with the eyewall, and outer convective rainbands. Results also showed that through increased moistening and upward velocity within the inner storm environment, assimilation of observations drove an intensification of the secondary circulation and deepening of the storm, leading to an improvement in TC intensity error. Intensity forecasts were found improved for assimilation of observations obtained with increasingly finer beam sampling span, suggesting an important benefit of oversampling.

**Author Contributions:**

**Conceptualization:** James Taylor, Atsushi Okazaki, Takumi Honda, Shunji Kotsuki, Moeka Yamaji, Takuji Kubota, Riko Oki, Toshio Iguchi, Takemasa Miyoshi

**Data curation:** James Taylor, Takumi Honda

**Formal analysis:** James Taylor, Takumi Honda

**Funding acquisition:** Atsushi Okazaki

**Plain Language Summary** In a recent study, the feasibility of a future precipitation radar based onboard a geostationary satellite (GPR) that could obtain three-dimensional precipitation measurements was successfully tested. In this study, we take the first step to investigate whether reflectivity observations can be used to improve analyses and forecasts of global weather systems. We perform data assimilation experiments that use simulated GPR observations for a West Pacific tropical cyclone, with observations obtained with varying radar beam sampling spans to generate observation oversampling, following a previous finding that this improves observation quality. Results found that key convective features of the tropical cyclone (TC), including the eye, eyewall structure, and outer rainbands, were all better captured in simulations assimilating observations obtained with finer beam sampling spans, with 5 km sampling providing best results. Observations were also found to have a positive impact on TC intensity in both model analyses and forecasts, with forecast errors for minimum sea level pressure improved at all lead times up to 18 h. TC intensity forecasts were also improved with increasingly finer beam span, suggesting an important potential benefit of oversampling for TC prediction.

© 2021. The Authors. Journal of Advances in Modeling Earth Systems published by Wiley Periodicals LLC on behalf of American Geophysical Union. This is an open access article under the terms of the Creative Commons Attribution-NonCommercial-NoDerivs License, which permits use and distribution in any medium, provided the original work is properly cited, the use is non-commercial and no modifications or adaptations are made.

TAYLOR ET AL. 1 of 19


---



AGU ADVANCING EARTH AND SPACE SCIENCE logo **Journal of Advances in Modeling Earth Systems** 10.1029/2020MS002332

19422466, 2021, 7, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2020MS002332 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

**Investigation:** James Taylor, Takumi Honda
**Methodology:** James Taylor, Takumi Honda
**Project Administration:** Atsushi Okazaki
**Supervision:** Atsushi Okazaki
**Validation:** James Taylor, Takumi Honda
**Writing – original draft:** James Taylor, Takumi Honda
**Writing – review & editing:** James Taylor, Takumi Honda

# 1. Introduction

Monitoring the global distribution and variability of precipitation is essential for understanding the Earth's water and energy cycle. Over the past two decades, satellite observations of precipitation have provided valuable insight into the three-dimensional structure of precipitation. The first spaceborne precipitation radar (PR) was the Tropical Rainfall Measuring Mission (TRMM, Kozu et al., 2001; Kummerow et al., 1998079%3C0809:TTRMM%3E2.0.CO;2)), which launched in 1997 and provided measurements of tropical rainfall for 17 years until its deactivation in 2015. This was succeeded by the Global Precipitation Measurement Core Observatory (GPM), launched in 2014 (Hou et al., 2014; Skofronick-Jackson et al., 2017), consisting of a network of satellites to observe rain and snow globally. Both TRMM and GPM have played critical roles in advancing our understanding of global precipitation variability (e.g., Adler et al. 2000013%3C2457:TTRMMG%3E2.0.CO;2), 2009; Ikai & Nakamura, 2003042%3C1354:SOTRMM%3E2.0.CO;2)), as well as contributing to improvements in numerical weather prediction (NWP) through data assimilation (DA) (e.g., Benedetti et al., 2005; Chambon et al., 2014; Lien et al., 2016; Okamoto & Aonashi, 2016).

Following the success of these missions, planning has now begun on the next generation of precipitation observing satellites, with the aim to build upon the achievements of previous PR satellites and develop a more advanced observation platform for global precipitation monitoring. This has led to the concept of a PR stationed in a geostationary orbit (GPR), with the prospect of obtaining observations at much higher frequency compared to TRMM and GPM, both low-earth orbiting satellites. For instance, the GPM satellite is stationed in a circular, nonsynchronous orbit at 65° inclination, with the onboard dual-frequency PR (DPR) having a cross-track scanning with swath width of 245 km. This means the same location on Earth is observed eight times a day and so will often miss weather systems with shorter lifespans, such as isolated convective cells. The relatively narrow cross-track also means larger-scale precipitation systems, such as tropical cyclones and mesoscale convective systems, are often not observed in their entirety from one passing. Offering quasicontinuous global coverage, a GPR would greatly reduce these limitations and provide new insights into the 3-D structure and variability of global precipitating systems. The feasibility for a GPR to obtain three-dimensional global precipitation data was successfully demonstrated by Okazaki et al. (2019, hereafter "O19"). The study considered a GPR equipped with a dual-frequency 13.6 GHz Ku-band antenna, similar to the one onboard the GPM but with a larger size of antenna, owing to that fact the GPR would be stationed at much greater attitude, and therefore would require a larger antenna to increase horizontal resolution. Based on previous research studies, for example, Joudoi et al. (2018), an antenna size measuring 30 m by 30 m with a half-power beam width (−3 dB) of 0.032° was considered, giving horizontal resolution of 20 km at the nadir point. This size of antenna is more than an order of magnitude larger than for GPM or TRMM (~2 m by 2 m), while the 20-km horizontal resolution is several times larger than current PR satellites, for example, GPM's footprint size is ~5 km at the nadir. However, despite the coarse resolution, the GPR observations were able to capture key features of a tropical cyclone (TC), including the eye, eyewall, and convective rainbands, though representation of finer convective structures were not well defined. Observations were found to be heavily contaminated by surface clutter, particularly at low altitudes, resulting in weaker rainfall from shallow convective cloud to be considered unobservable. This limitation of the observations was a consequence of the GPR measuring precipitation at off-nadir angles, meaning the beam's sampling volume was tilted with respect to the Earth's surface. To mitigate the contamination issue, as well as improve definition of the TC's finer convective features, radar oversampling was proposed, a process in which the beam's sampling span is reduced, thereby increasing the number of observations over the domain covered by the GPR. Oversampling led to an improvement in observation quality, that included better representation of finer precipitation features, such as the eyewall and outer convective rainbands.

With the feasibility for a GPR tested, the next step is to investigate whether such observations would be useful for NWP. In addition, given the finding that oversampling can improve observation quality for the GPR, it is of added interest to investigate whether radar oversampling could enhance the usefulness of the observations. Presented with these lines of inquiry, this study performs an observing system simulation experiment (OSSE) for a TC case study to evaluate the impact of GPR observations obtained for a range of beam sampling spans, that is, degrees of oversampling, on TC analyses and forecasts. TC's represent global-scale, high-impact weather systems that pose considerable risk to life and property from strong winds, storm surge, and flooding from heavy rainfall. A GPR would be expected to be of enormous benefit for TC research and monitoring given its high observation frequency and global coverage. Several studies have demonstrated the value of observations

TAYLOR ET AL. 2 of 19


---


19422466, 2021, 7, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2020MS002332 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU ADVANCING EARTH AND SPACE SCIENCE logo

# Journal of Advances in Modeling Earth Systems 10.1029/2020MS002332

from geostationary satellites for TC forecasting, for example, Minamide and Zhang (2018), Zhang et al. (2016), Honda, Kotsuki, et al. (2018), Honda, Miyoshi, et al. (2018), and Honda et al. (2019), while PR observations from the GPM have shown to be beneficial for TC monitoring, for example, Battaglia et al. (2015). For the case study, we choose Typhoon Soudelor, the strongest West Pacific tropical cyclone in 2015. Soudelor formed as a tropical depression on July 29 and slowly gathered strength before undergoing a period of rapid intensification on August 2. Our experiments will focus on the period leading up to rapid intensification to understand the impact of observations on intensity prediction. In addition, we investigate whether observations positively impact the accumulated rainfall and maximum surface wind speed forecasts.

As this study represents the first investigation into the usefulness of a potential future radar data set, we assume a perfect prediction model and perfect forward observational operators. These assumptions are overly optimistic but are suitable for the initial assessment of a new data set that might warrant further investigation and considerations. For example, the perfect-model assumption is a common approach used in early OSSE radar studies, for example, Xue et al. (2006), Tong and Xue (2005), and Koch et al. (2012). Errors relating to microphysical schemes in the representation of precipitation species have been extensively studied (e.g., Chang & Wu, 2017; Di Michele et al., 2012; Geer & Baordo, 2014; Li & Pu 2008; Sieron et al., 2018), and will unequivocally be a major factor in determining the usefulness of observations. Both errors relating to model error and microphysical scheme will need to be examined thoroughly in future studies. Surface clutter contamination will also play a major role in usefulness of observations (Li et al., 2017). O19 found contamination was heavily dependent on many factors, including the positioning of the target precipitation system, precipitation intensity, and distance from the nadir. The complex nature of contamination shown by O19 means that, again for simplicity in this first study, we do not consider contamination by surface clutter. Exclusion of this and other major sources of error mean results will represent an overly optimistic understanding of their impact and we urge caution in their interpretation.

The study is structured as follows. Section 2 describes the nature run (NR) of Typhoon Soudelor performed by O19, the methodology for simulating radar reflectivity observations for a GPR using JAXA's Joint Simulator software (Hashino et al., 2013) and the GPR observations of Typhoon Soudelor at varying beam sampling spans, and a description of the DA experiments to evaluate their usefulness for TC forecasts. Section 3 presents the results, including the impact to track and intensity error, as well as predicted rainfall totals and maximum wind intensity. Section 4 provides conclusions and discussion of future work.

# 2. Methodology

## 2.1. Typhoon Soudelor Nature Run

The NR of Typhoon Soudelor was generated by O19 using the regional cloud-resolving SCALE-RM model version 5.0.0 (Scalable Computing for Advanced Library and Environment-Regional Model, Nishizawa et al., 2015; Sato et al., 2015). The source code for the SCALE library, including the SCALE-RM, is publicly available at [https://scale.riken.jp/](https://scale.riken.jp/)(last access: July 24, 2020). The moist physical processes were parameterized by a six-class single-moment bulk microphysics scheme (Tomita, 2008). The level 2.5 closure of the Mellor-Yamada-Nakanishi-Niino turbulence scheme was used for representing subgrid-scale turbulence activity (Nakanishi & Niino, 2004) and the Model Simulation Radiation Transfer code (MSTRN, Sekiguchi & Nakajima, 2008) was used for calculating shortwave and longwave radiation processes.

The NR was performed in an offline nesting simulation, consisting of two computational domains: an outer domain (hereafter D1NR), consisting of a 15-km mesh and 36 vertical levels and an inner domain (hereafter D2NR), consisting of a 3-km mesh and 56 vertical levels (Figure 1). The initial and lateral boundary conditions for D1NR were taken from the National Centers for Environmental Prediction (NCEP) Global Forecasting System (GFS) operational analyses at 0.5° resolution every 6 h. The simulation period for D1NR covers the period from 0000 UTC on July 28, 2015 to 0000 UTC on August 9, 2015. The simulation period for D2NR covers from 0000 UTC July 29, 2015 to 0000 UTC on August 7. Initial and lateral boundary conditions for D2NR are taken from D1NR. Figure 1 shows the domains for D1NR and D2NR, with the NR track of Typhoon Soudelor based on the location of minimum sea-level pressure (MSLP) of the simulated TC in D2NR. Also shown is the Typhoon Soudelor best track from Japan Meteorological Agency (JMA) from 0000 UTC August 1 to 0000 UTC August 12.

TAYLOR ET AL. 3 of 19


---



19422466, 2021, 7, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2020MS002332 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU ADVANCING EARTH AND SPACE SCIENCE logo

# Journal of Advances in Modeling Earth Systems

10.1029/2020MS002332

Map showing model domains D1NR/D1DA, D2NR, and D2DA with the track of Typhoon Soudelor (2015).

**Figure 1.** Model domains D1NR (outermost black rectangle) and D2NR (inner red rectangle) for the nature run (NR) using SCALE-RM version 5.0.0. D1DA covers the domain as D1NR (outermost black rectangle), while D2DA (inner green rectangle) is the model domain used to perform the data assimilation experiments with the SCALE-local ensemble transform Kalman filter (LETKF) version 5.1.1. The gray line represents the JMA best track of Typhoon Soudelor (2015) from 0000 UTC August 1 to 0000 UTC August 12. The blue line represents the NR track of Typhoon Soudelor in D2NR, with blue dots showing the location of the TC center (based on MSLP) at 12-h intervals.

## 2.2. Simulating Radar Reflectivity for a GPR

In this section, we describe the method for calculating radar reflectivity measured by the GPR using the Joint Simulator for Satellite Sensors (Joint Simulator; Hashino et al., 2013), a software package that simulates satellite observations based on atmospheric states simulated by cloud-resolving models. First, the Joint Simulator is used to covert model hydrometeor (cloud water, cloud ice, rainwater, snow and graupel) from the NR to total backscattering ($\overline{\sigma}_b$) and extinction coefficients ($\overline{k}_{ext}$) at every grid point based on the following formulas:

$$ \overline{\sigma}_b = \sum_{i=1}^{n_{spec}} \int_0^\infty \sigma_{b,i}^S(D) N_i(D) dD $$ (1)

$$ \overline{k}_{ext} = \sum_{i=1}^{n_{spec}} \int_0^\infty k_{ext,i}^S(D) N_i(D) dD $$ (2)

In Equations 1 and 2, total backscattering and extinction coefficients are obtained by summing single particle backscattering and extinction coefficients for the $i$th hydrometeor species following its drop size ($D$) distribution ($N_i(D)$). Here $n_{spec}$ is the number of hydrometeor species, which in this study uses five species (cloud water, cloud ice, rain, snow, and graupel). The Mie approximation is used to calculate $\sigma_{b,i}^S$ and $k_{ext,i}^S$ for all the species (Masunga & Kummerow, 2005) at all model grid points. After calculating $\overline{\sigma}_b$ and $\overline{k}_{ext}$ at every model grid point, the values are integrated over a scattering volume, following an antenna pattern, which in this case is assumed to be Gaussian and approximated by the following fifth-order polynomial (Gaspari & Cohn, 19991097-0088(199907)125:548%3C723::AID-QJ3%3E3.0.CO;2-9)), given by

$$ f^2(\psi) = \begin{cases} -\frac{1}{4}\psi^5 + \frac{1}{2}\psi^4 + \frac{5}{8}\psi^3 - \frac{5}{3}\psi^2 + 1 \\ \frac{1}{12}\psi^5 - \frac{1}{2}\psi^4 + \frac{5}{8}\psi^3 + \frac{5}{3}\psi^2 - 5\psi + 4 - \frac{2}{3}\psi^{-1} \\ 0 \end{cases} $$ (3)

TAYLOR ET AL.

4 of 19
4 of 19


---



19422466, 2021, 7, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2020MS002332 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU ADVANCING EARTH AND SPACE SCIENCE logo

# Journal of Advances in Modeling Earth Systems

10.1029/2020MS002332

where $\psi = \sqrt{(\theta - \theta_0)^2 + (\phi - \phi_0)^2} / \Psi$ and is obtained by solving the equation $f^2 \left( \frac{\theta_B}{2} / \Psi \right) = 0.5$ where $\theta_B$ is the half-power beam width (−3 dB). The radar-received power from precipitation ($P_r$) of the beam pointing range $r_0$ and scan angle $\theta_0$ and $\phi_0$ can be equated by,

$$ P_r = \frac{P_t \lambda^2}{(4\pi)^3} \int_{r_0 - c\tau/4}^{r_0 + c\tau/4} \int_{\theta_0 - \pi}^{\theta_0 + \pi} \int_{\phi_0 - \pi/2}^{\phi_0 + \pi/2} f^4(\theta, \phi) \bar{\sigma}_b(r, \theta, \phi) A_p(r, \theta, \phi) r^{-2} \cos \theta \, d\phi \, d\theta \, dr \tag{4} $$

where $P_t$ is the transmitted power, $c$ is the speed of light, $\tau$ is the pulse duration, and $f^4$ the two-way effective beam weighting function. $A_p$ is the attenuation factor from the radar to range $r$ in the direction of $(\theta, \phi)$ and is calculated by

$$ A_p(r, \theta, \phi) = \exp \left[ -0.2 \ln(10) \int_0^r \bar{k}_{ext}(r', \theta, \phi) \, dr' \right] \tag{5} $$

Finally, radar reflectivity (dBZ) measured by the GPR ($Z_G$) is calculated by:

$$ Z_G = \frac{\lambda^4}{\pi^5 \mid K \mid^2} \frac{\int_{r_0 - c\tau/4}^{r_0 + c\tau/4} \int_{\theta_0 - \pi}^{\theta_0 + \pi} \int_{\phi_0 - \pi/2}^{\phi_0 + \pi/2} f^4(\theta, \phi) \bar{\sigma}_b(r, \theta, \phi) r^{-2} A_p(r, \theta, \phi) \cos \theta \, d\phi \, d\theta \, dr}{\int_{r_0 - c\tau/4}^{r_0 + c\tau/4} \int_{\theta_0 - \pi}^{\theta_0 + \pi} \int_{\phi_0 - \pi/2}^{\phi_0 + \pi/2} f^4(\theta, \phi) r^{-2} \cos \theta \, d\phi \, d\theta \, dr} \tag{6} $$

where $\lambda$ is the wavelength and $K$ the function of a complex refractivity index of scattering particles. Following Masunga and Kummerow (2005), $\mid K \mid^2$ is assumed to be a constant, whose value is 0.925.

## 2.3. Radar Oversampling

An important aspect of this study is to examine the impact of observations obtained considering different degrees of oversampling. Radar oversampling comprises of a ensuite of processing techniques designed to improve estimation of meteorological variables, such as reflectivity (Aubry et al., 2015; Borowska et al., 2015; Torres & Zrnic, 2003a020%3C1435:WROFDP%3E2.0.CO;2), 2003b020%3C1452:WROFDP%3E2.0.CO;2); Yu et al., 2005) without increasing sampling volume acquisition times. As defined in Equation 6, returning radar signals represent the combined contributions of all hydrometeors over a sampling volume determined by the antenna pattern. Ordinarily, sampling of radar signals occurs at a rate $\tau^{-1}$ (pulse width), where $\tau$ is the duration of the transmitted pulse. Oversampling entails acquiring data at rates higher than $\tau^{-1}$, thereby increasing the number of range gates with the same pulse width. This means that sampling volumes from oversampled signals will be overlapped and correlated. The degree to which they are correlated is determined by the factor increase in number of range gates. This process is termed radar oversampling. Multiple approaches are available for combining oversampled signals to improve resolution of reflectivity (Torres and Zrnić 2003a020%3C1435:WROFDP%3E2.0.CO;2), 2003b020%3C1452:WROFDP%3E2.0.CO;2)), of which numerous studies have since successfully demonstrated, for example, Ivić, Zahrai, et al. (2003020%3C1435:WROFDP%3E2.0.CO;2)); Ivić, Zrnić, et al. (2003020%3C1452:WROFDP%3E2.0.CO;2)); Torres and Zrnić (2003a020%3C1435:WROFDP%3E2.0.CO;2)), (2003b020%3C1452:WROFDP%3E2.0.CO;2)); Yu et al. (2005). In this study, we simulate this process of radar oversampling for returning signals for the GPR in order to improve resolution of observations. This was previously performed in O19 by reducing the beam sampling span, thereby generating an increasing number of observations over the coverage region. We follow the same methodology for obtaining oversampled observations, with beam sampling spans set 20 (representing no oversampling), 15, 10, and 5 km that is, observations every 15, 10, and 5 km respectively.

## 2.4. Data Assimilation Experiments

Data assimilation experiments are performed with the SCALE-local ensemble transform Kalman filter (LETKF) version 5.1.1 (Lien et al., 2017), which couples the SCALE-RM (Nishizawa et al., 2015; Sato et al., 2015) with the LETKF (Hunt et al., 2007). The SCALE library used here consists of only minor differences to that used to generate the NR and so follows a "perfect model" setup, with considerations relating same model error not explored by this study. Though not optimal, it is a common approach for radar

TAYLOR ET AL.

5 of 19



---



19422466, 2021, 7, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2020MS002332 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU ADVANCING EARTH AND SPACE SCIENCE logo

# Journal of Advances in Modeling Earth Systems

10.1029/2020MS002332

**Table 1**

*Geostationary-Based Precipitation Radars (GPR) Settings for Data Assimilation Experiments*

<table>
  <thead>
    <tr>
        <th>Experiment Name</th>
        <th>Beam width/ Resolution (km)</th>
        <th>Beam sampling span (km)</th>
        <th>Assimilate conventional observations and TC vitals?</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>BS20</td>
<td>20</td>
<td>20</td>
<td>Yes</td>
    </tr>
<tr>
        <td>BS15</td>
<td>20</td>
<td>15</td>
<td>Yes</td>
    </tr>
<tr>
        <td>BS10</td>
<td>20</td>
<td>10</td>
<td>Yes</td>
    </tr>
<tr>
        <td>BS05</td>
<td>20</td>
<td>5</td>
<td>Yes</td>
    </tr>
<tr>
        <td>NO-GPR</td>
<td>-</td>
<td>-</td>
<td>Yes</td>
    </tr>
<tr>
        <td>NO-DA</td>
<td>-</td>
<td>-</td>
<td>No</td>
    </tr>
  </tbody>
</table>

Abbreviations: DA, data assimilation; GPR, geostationary-based precipitation radars.

OSSE studies taking the first step in exploring the potential usefulness of newly available radar datasets, for example, Xue et al. (2006), Sobash and Stensrud (2013), and Liu et al. (2019). However, because this approach makes major assumptions about the model and observation operator, we reaffirm clearly that they will represent an overly optimistic evaluation of the observations impact and urge caution when interpretating the results.

The model set up consists of two computational domains; an outer domain (hereafter D1DA) with 15-km mesh and an inner domain with 3-km mesh (hereafter D2DA), where the experiments are performed. Note that, while D1NR and D1DA are different, D1DA covers the same region as D1NR (see Figure 1). Ensemble size is fixed at 50 members. First, we perform 6-h update cycling for D1DA from 0000 UTC July 23, 2015 through to 0000 UTC August 7, 2015, assimilating real NCEP conventional observations (PREPBUFR) and TC-vital data from 0000 UTC July 23 to 1800 UTC July 28 and PREPBUFR-type observations created from D1NR from 0000 UTC July 29 to 0000 UTC August 7. Initial conditions for D1DA are provided by the NCEP GFS 0.5° operational analyses

at a range of arbitrary chosen times, while lateral boundary conditions are from NCEP GFS 0.5° operational analyses, where the same data are used for all members, that is, no boundary perturbations. This approach follows a similar set up of other TC data assimilation studies performed with the SCALE-LETKF, for example, Lien et al. (2017), Honda, Kotsuki, et al. (2018), and Honda, Miyoshi, et al. (2018). At 1800 UTC July 31 the 50-member ensembles are downscaled from D1DA to become the initial and boundary conditions for D2DA. Next, a 12-h warm-up period of cycling is performed in D2DA, in which PREPBUFR and TC-vital data-type observations created from D2NR are assimilated every hour until 1200 UTC August 1. At this time, the ensemble members form the initial conditions for each DA experiment. Each experiment consists of 18-h cycling until 0600 UTC August 2, with radar reflectivity observations from the GPR ($Z_G$) assimilated every 1 h. This is based on the assumption that the GPR can perform a full disk scan within 1-h and all observations are available at the time of assimilation. Table 1 presents the DA experiments performed in this study. They include four experiments where PREPBUFR and TC-vitals and $Z_G$ are assimilated, with GPR observations obtained assuming varying beam sampling spans, one experiment where only PREPBUFR and TC-vitals are assimilated (NO-GPR) and one experiment where no data assimilation is performed (NO-DA). NO-GPR and NO-DA are included to aid assessment into the impact of assimilating $Z_G$.

The SCALE-LETKF has been well tested for the assimilation of radar reflectivity observations, for example, Lien et al. (2017), Maejima et al. (2017). The forward operator calculates radar reflectivity from mass density W (g/m) of each hydrometeor in the model. The cloud microphysics scheme used is a single moment six-category scheme, with three categories for precipitation particle; rain, snow, and graupel (Tomita, 2008). The $Z_e$-$W$ relationship is the product of radiative scattering processes by the mixture of precipitation particles with different size distribution, given by

$$ Z_e = (2.53 \times 10^4)(\rho q_r)^{1.84} + (3.48 \times 10^4)(\rho q_s)^{1.66} + (5.54 \times 10^4)(\rho q_g)^{1.50} $$ (7)

$$ \text{dBZ} = 10 \times \log_{10}(Z) $$ (8)

where $\rho$, $q_r$, $q_s$, and $q_g$ are air density (kg m<sup>−2</sup>), mixing ratios of rain, snow and graupel (g kg<sup>−1</sup>), respectively. The coefficients in Equation 7 for each precipitation species are updated versions of those from Xue et al. (2009) by Amemiya et al. (2019), who calculated new coefficients by a linear fitting of $\log Z_e$-$\log W$ relation using the Joint Simulator software. Thus, the forward operator used to assimilate reflectivity observations into the SCALE-LEKTF is based upon the same microphysics used by the radar simulator to obtain synthetic GPR observations from the NR. This means that errors relating to the microphysics scheme employed in the calculation of reflectivity are not considered. As several recent studies have shown, large uncertainties in cloud microphysical parameterization schemes will affect precipitation species estimations (Di Michele et al., 2012; Galligani et al., 2017; Geer & Baordo, 2014; Li & Pu, 2008; Sierson et al., 2018), so

TAYLOR ET AL.

6 of 19


---



19422466, 2021, 7, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2020MS002332 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU ADVANCING EARTH AND SPACE SCIENCE logo

# Journal of Advances in Modeling Earth Systems

10.1029/2020MS002332

the assumption of perfect forward operator is overly optimistic and a major limitation of this study. However, for simplicity we assume perfect operator, with the aim to perform a comprehensive study into the sensitivity of the cloud microphysical scheme for the GPR in a future study.

For experiments where GPR observations are assimilated (collectively hereafter referred to as "GPR experiments"), we assume a GPR equipped with a 13.6 GHz KuPR antenna positioned at 0°N, 135°E with a scan angle of ±6°, which would cover a region extending from Sumatra to New Caledonia in the east-west direction and from Australia to Japan in the north-south direction. The antenna is assumed to be a square phased array antenna measuring 30 × 30 m with a half-power beam width of 0.032°, giving a horizontal resolution of 20 km at nadir point on the Earth's surface. For the control case, the beam sampling span is equal to horizontal resolution, that is, 20 km (hereafter, "BS20") and therefore represents no oversampling. Next, we consider three oversampling cases, where the beam sampling spans are less than the beam widths. These have beam sampling span set to 5, 10 km, and 15 km (hereafter, referred to as "BS05," "BS10," and "BS15," respectively). Observation error for radar reflectivity is set to 5 dBZ in each experiment, similar to previous studies assimilating satellite PR derived reflectivity observations, for example, Okamoto and Aonashi (2016). Observation correlated errors are not considered. We also do not consider the impact of attenuation ($A_p = 1.0$ in Equation 6) or effects of surface clutter contamination. Both attenuation and surface clutter contamination are important issues in radar data assimilation and are expected to be severe for GPR reflectivity observations. For instance, O19 estimated observations most affected by surface clutter contamination were in areas further away from nadir and up to 7-km height, to the point at which they were deemed unobservable. However, this varied extensively over the sampling domain, with areas of higher reflectivity and those closer to nadir less affected by surface clutter contamination. The complex nature as to the severity of contamination suggested that to adequately consider contaminated observations for NWP, a proper method was needed that would either distinguish between contaminated and noncontaminated observations within the data assimilation scheme or that would adequately remove contaminated observations prior to assimilation. Both approaches are nontrivial and beyond the scope of this study. Instead we choose, for reasons of simplicity, to not consider the affects of surface contamination and assume all observations are observable. We expect methods for reducing clutter for GPR observations will eventually become available in the future, as has been the case for other Ku-band PR satellites (Kubota et al., 2016) and believe they are necessary as part of understanding the potential usefulness of observations. Equally, we expect new methods for considering the effects of attenuation for a GPR to become available in the future, simular to those developed for TRMM PR (Iguchi et al., 2000) and for GPM (Iguchi et al., 2017).

A variable localization is used for radar reflectivity, in which only vertical velocity ($w$), temperature ($T$) and hydrometeors, for example, mass concentrations of cloud water ($q_c$), rain ($q_r$), cloud ice ($q_i$), water vapor ($q_v$), snow ($q_s$), and graupel ($q_g$), are updated. In early sensitivity experiments, it was found that updating some state variables, including zonal and meridional wind components $u$ and $v$, with assimilation of reflectivity, led to large imbalances in the analysis that had a large detrimental impact to intensity and track forecasts. This was similarly found in Dong and Xue (2013), who found using reflectivity observations to update wind, potential temperature, and $q_v$ had negative impact on hurricane intensity, resulting in them to update only pressure and certain microphysical variables with reflectivity assimilation. We take a equally cautious approach, deciding not to update $u$ and $v$ with $Z_G$ assimilation. Localization scale is uniformly applied to all variables via a Gaussian function with standard deviations of 200 km in the horizontal and 0.3 ln(p) in the vertical. Covariance inflation is applied via a relaxation to prior perturbation scheme (RTPP, Zhang et al., 2004) with coefficient of 0.8. Finally, to utilize the observation information that "it is not raining," all reflectivities below 20 dBZ are replaced with 15 dBZ. In such cases, innovations during each assimilation will be zero as both observed and simulated reflectivity are set to the same value. This ensures there is not added moistening that occurs in areas where there is no precipitation.

## 2.5. GPR Observations

Figures 2 and 3 present radar reflectivity observations of Typhoon Soudelor during its mature stage for each of the configurations set out in Table 1. Each set of observations shows the main features of the TC are adequately captured for each configuration of the GPR. In the control case BS20, the symmetrical structure, eye, eyewall, and spiral convective outer rainbands are all present, though finer details of the TC structure

TAYLOR ET AL. 7 of 19


---



19422466, 2021, 7, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2020MS002332 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU ADVANCING EARTH AND SPACE SCIENCE logo

# Journal of Advances in Modeling Earth Systems

10.1029/2020MS002332

Radar reflectivity maps for Nature Run, BS20, BS15, BS10, and BS05 experiments

Figure 2. Radar reflectivity (dBZ) near the surface at 0000 UTC on August 5, for the NR, BS20, BS15, BS10, and BS05.

are not well defined, with weaker outer rainfall shown distributed over a larger area compared to the NR. This particular feature is a consequence of the beam being tilted with a relatively large scattering volume, causing the radar to observe reflectivity signal at levels higher than what is represented. The region of high intensity precipitation observed to the south of the eye in the NR is also not well represented in BS20. This is due to the echo being averaged out over a large scattering volume. There is a noticable improvement when oversampling is applied. Features of the TC are noticeably better represented in observations, with BS05 displaying most clarity. For example, the strong precipitation to the south of the eye and associated with outer spiral rainbands are more clearly defined with the finer beam span. This attribute of the oversampling is attributed to the fact that when the beam sampling span is reduced, the probability of the beam center hitting an area of strong precipitation increases, making it more likely that higher rates of precipitation will be captured in observations.

Improved capturing of precipitating areas is further shown in the latitude-height cross sections shown in Figure 3. BS20 is able to represent the general vertical structure of precipitation but struggles to represent smaller scale features. Furthermore, the observations appear very jagged due to the tilted beam and large scattering volume. With oversampling, much of the jagged, distorting effect is reduced, giving a smoother representation of the vertical precipitation structure that is closer to the NR.

# 3. Results

## 3.1. Impact on Track and Intensity Error

Presented in Figure 4 are analyzed MSLP and maximum 10-m wind speed (VMAX10) over the 18-h period of cycling for each experiment. The initial conditions at 1200 UTC August 1 show an ~6 hPa error built up through the previous 12-h period of warm up cycling. Following an initial increase in MSLP, each of the experiments assimilating $Z_G$ show a steady deepening of the TC in the GPR experiments, though noticeably none are unable to capture the TC's rapid intensification. Nevertheless, compared to NO-GPR, MSLP error is smaller at most times during cycling for the GPR experiments, suggesting $Z_G$ has a positive impact on TC intensity. This is most evident from BS05, which consistently has smallest MSLP error through cycling,

TAYLOR ET AL.

8 of 19


---



AGU Journal of Advances in Modeling Earth Systems logo

Journal of Advances in Modeling Earth Systems

10.1029/2020MS002332

19422466, 2021, 7, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2020MS002332 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

<table>
    <tr>
        <th>Panel</th>
        <th>Description</th>
    </tr>
<tr>
        <td>Nature Run</td>
<td>Vertical cross-section of radar reflectivity showing TC structure.</td>
    </tr>
<tr>
        <td>BS05</td>
<td>Vertical cross-section of radar reflectivity for 5-km beam sampling.</td>
    </tr>
<tr>
        <td>BS10</td>
<td>Vertical cross-section of radar reflectivity for 10-km beam sampling.</td>
    </tr>
<tr>
        <td>BS15</td>
<td>Vertical cross-section of radar reflectivity for 15-km beam sampling.</td>
    </tr>
<tr>
        <td>BS20</td>
<td>Vertical cross-section of radar reflectivity for 20-km beam sampling.</td>
    </tr>
</table>

**Figure 3.** Radar reflectivity (dBZ) along 136.4°E longitude passing through the tropical cyclone (TC) center at 0000 UTC on August 5 for the NR, BS20, BS15, BS10, and BS05.

suggesting that oversampling with 5-km beam sampling span is an important factor in reducing intensity error. By the end of cycling at 0600 UTC August 2, the difference in error between BS05 and NO-GPR is 7 hPa, which represents a 50% reduction in MSLP error for case assimilating Z<sub>G</sub>. It is noticable also that BS05 has strongest maximum surface winds at most analysis times, which supports BS05 as having generated the strongest TC through cycling.

Next, Figures 5 and 6 present the mean track, MSLP and VMAX10 forecast errors from forecasts initialized from the ensemble mean every hour between 1800 UTC August 1 and 0600 UTC August 2 (13 in total).

TAYLOR ET AL.

9 of 19
9 of 19


---



19422466, 2021, 7, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2020MS002332 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU ADVANCING EARTH AND SPACE SCIENCE logo

# Journal of Advances in Modeling Earth Systems

10.1029/2020MS002332

<table>
  <thead>
    <tr>
        <th colspan="8">MSLP Analysis (hPa)</th>
    </tr>
<tr>
        <th>Time (UTC)</th>
        <th>BS05</th>
        <th>BS10</th>
        <th>BS15</th>
        <th>BS20</th>
        <th>NO-GPR</th>
        <th>NO-DA</th>
        <th>Nature Run</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>12 (1 Aug)</td>
<td>1000</td>
<td>1000</td>
<td>1000</td>
<td>1000</td>
<td>1000</td>
<td>1000</td>
<td>998</td>
    </tr>
<tr>
        <td>15</td>
<td>998</td>
<td>998</td>
<td>998</td>
<td>998</td>
<td>998</td>
<td>998</td>
<td>994</td>
    </tr>
<tr>
        <td>18</td>
<td>996</td>
<td>996</td>
<td>996</td>
<td>996</td>
<td>996</td>
<td>996</td>
<td>992</td>
    </tr>
<tr>
        <td>21</td>
<td>994</td>
<td>994</td>
<td>994</td>
<td>994</td>
<td>994</td>
<td>994</td>
<td>988</td>
    </tr>
<tr>
        <td>00 (2 Aug)</td>
<td>992</td>
<td>992</td>
<td>992</td>
<td>992</td>
<td>992</td>
<td>992</td>
<td>982</td>
    </tr>
<tr>
        <td>03</td>
<td>988</td>
<td>986</td>
<td>984</td>
<td>984</td>
<td>984</td>
<td>984</td>
<td>974</td>
    </tr>
<tr>
        <td>06</td>
<td>978</td>
<td>974</td>
<td>972</td>
<td>970</td>
<td>970</td>
<td>970</td>
<td>958</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
        <th colspan="7">VMAX10 Analysis (m s⁻¹)</th>
    </tr>
<tr>
        <th>Time (UTC)</th>
        <th>BS05</th>
        <th>BS10</th>
        <th>BS15</th>
        <th>BS20</th>
        <th>NO-GPR</th>
        <th>NO-DA</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>12 (1 Aug)</td>
<td>21</td>
<td>21</td>
<td>21</td>
<td>21</td>
<td>21</td>
<td>21</td>
    </tr>
<tr>
        <td>15</td>
<td>20</td>
<td>20</td>
<td>20</td>
<td>20</td>
<td>20</td>
<td>20</td>
    </tr>
<tr>
        <td>18</td>
<td>22</td>
<td>22</td>
<td>22</td>
<td>22</td>
<td>22</td>
<td>22</td>
    </tr>
<tr>
        <td>21</td>
<td>25</td>
<td>25</td>
<td>25</td>
<td>25</td>
<td>25</td>
<td>25</td>
    </tr>
<tr>
        <td>00 (2 Aug)</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
    </tr>
<tr>
        <td>03</td>
<td>28</td>
<td>27</td>
<td>26</td>
<td>25</td>
<td>25</td>
<td>25</td>
    </tr>
<tr>
        <td>06</td>
<td>46</td>
<td>42</td>
<td>38</td>
<td>36</td>
<td>34</td>
<td>34</td>
    </tr>
  </tbody>
</table>

Figure 4. Ensemble mean analyses of minimum sea-level pressure (MSLP, hPa) and maximum 10-m wind speed (VMAX10, m s<sup>−1</sup>), through 18 h period of cycling for BS20, BS15, BS10, BS05, NO-geostationary-based precipitation radar (GPR), and NO-data assimilation (DA).

Track forecast errors show no clear impact from the assimilation of $Z_G$, including when oversampling is applied. This is unsurprising given that $u$ and $v$ are not updated for assimilation of reflectivity, preventing any large changes to the large-scale atmospheric circulation that might impact the track of the TC in forecasts. MSLP forecast errors do signal a positive impact from the observations, with smaller errors when $Z_G$ are assimilated at all lead times. Furthermore, errors are smaller for observations with the finer beam sampling span at all lead times, with BS05 showing smallest errors. While not statistically significant, the results provide a clear indication that oversampling positively impacts TC intensity forecasts. Averaging MSLP error at all lead times, BS05 has ~20% and 17% smaller error compared to NO-GPR and BS20 respectively. Results of the VMAX10 forecast error are more mixed, though BS05 displays smallest errors at most lead times, sup-

<table>
  <thead>
    <tr>
        <th>Forecast Lead Time (hr)</th>
        <th>BS05</th>
        <th>BS10</th>
        <th>BS15</th>
        <th>BS20</th>
        <th>NO-GPR</th>
        <th>NO-DA</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
    </tr>
<tr>
        <td>2</td>
<td>25</td>
<td>25</td>
<td>25</td>
<td>25</td>
<td>25</td>
<td>25</td>
    </tr>
<tr>
        <td>4</td>
<td>45</td>
<td>45</td>
<td>45</td>
<td>45</td>
<td>45</td>
<td>45</td>
    </tr>
<tr>
        <td>6</td>
<td>65</td>
<td>65</td>
<td>65</td>
<td>65</td>
<td>65</td>
<td>65</td>
    </tr>
<tr>
        <td>8</td>
<td>80</td>
<td>80</td>
<td>80</td>
<td>80</td>
<td>80</td>
<td>80</td>
    </tr>
<tr>
        <td>10</td>
<td>95</td>
<td>95</td>
<td>95</td>
<td>95</td>
<td>95</td>
<td>95</td>
    </tr>
<tr>
        <td>12</td>
<td>110</td>
<td>110</td>
<td>110</td>
<td>110</td>
<td>110</td>
<td>110</td>
    </tr>
<tr>
        <td>14</td>
<td>130</td>
<td>135</td>
<td>140</td>
<td>145</td>
<td>145</td>
<td>150</td>
    </tr>
<tr>
        <td>16</td>
<td>150</td>
<td>160</td>
<td>170</td>
<td>180</td>
<td>185</td>
<td>210</td>
    </tr>
<tr>
        <td>18</td>
<td>160</td>
<td>175</td>
<td>185</td>
<td>195</td>
<td>200</td>
<td>220</td>
    </tr>
  </tbody>
</table>

Figure 5. Absolute forecast errors at each lead time for track position (km) for NO-ata assimilation (DA) (black), NO-geostationary-based precipitation radar (GPR) (red), BS20 (yellow), BS15 (cyan), BS10 (purple) and BS05 (blue, see legend). Errors represent the mean error from 13 forecasts initialized between 1800 UTC August 1 and 0600 UTC August 2.

porting the view that BS05 predicts a stronger TC in forecasts. Averaging the VMAX10 error at all lead times, BS05 has ~19% and 16% smaller error compared to NO-GPR and BS20, respectively, similar to the difference in MSLP error between these two experiments.

These results signify that the assimilation of $Z_G$ impacts the TC intensity positively in both the analysis and forecasts and is improved when observations are assimilated with finer beam sampling span. This is somewhat at odds with previous hurricane radar assimilation studies, which found little or no impact of radar reflectivity observations on intensity forecasts, for example, Pu et al. (2009), Zhao and Jin (2008), Dong and Xue (2013). However, Pu et al. (2009) attributed the weak impact on intensity to the use of a microphysics scheme that used a simple warm rain process and did not consider other precipitation species, such as ice and graupel, unlike the microphysical scheme used in this study (see Equation 7). In addition, assimilation was performed with the WRF 3DVAR that uses the National Meteorological Center (NMC) scheme to estimate background error covariance, which they stated was not appropriate for estimating background error statistics for rainwater mixing ratio and was the likely cause for a smaller impact to intensity and track forecasts. Ensemble Kalman filter schemes, such as the LETKF employed by this study, have proven to be highly suitable for radar assimilation studies (e.g., Bick et al., 2016; Gastaldo et al., 2018; Miyoshi et al., 2016; Snyder & Zhang, 2003131<1863:AORDAW>2.0.CO;2); Wu et al., 2020), with the advantage of flow dependency in

TAYLOR ET AL.

10 of 19


---



19422466, 2021, 7, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2020MS002332 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU ADVANCING EARTH AND SPACE SCIENCE logo

# 

 Journal of Advances in Modeling Earth Systems

10.1029/2020MS002332

<table>
  <thead>
    <tr>
        <th rowspan="2">Lead Time (hr)</th>
        <th colspan="6">MSLP Forecast Error (hPa)</th>
        <th colspan="6">VMAX10 Forecast Error (m s⁻¹)</th>
    </tr>
<tr>
        <th>B505</th>
        <th>ASIR</th>
        <th>BSL5</th>
        <th>BSL20</th>
        <th>NO-GPR</th>
        <th>NO-DA</th>
        <th>B505</th>
        <th>ASIR</th>
        <th>BSL5</th>
        <th>BSL20</th>
        <th>NO-GPR</th>
        <th>NO-DA</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>0</td>
<td>14</td>
<td>14</td>
<td>14</td>
<td>14</td>
<td>14</td>
<td>14</td>
<td>16</td>
<td>16</td>
<td>16</td>
<td>16</td>
<td>16</td>
<td>16</td>
    </tr>
<tr>
        <td>2</td>
<td>26</td>
<td>21</td>
<td>19</td>
<td>18</td>
<td>17</td>
<td>16</td>
<td>19</td>
<td>15</td>
<td>14</td>
<td>13</td>
<td>12</td>
<td>11</td>
    </tr>
<tr>
        <td>4</td>
<td>25</td>
<td>20</td>
<td>18</td>
<td>17</td>
<td>16</td>
<td>15</td>
<td>18</td>
<td>14</td>
<td>13</td>
<td>12</td>
<td>11</td>
<td>10</td>
    </tr>
<tr>
        <td>6</td>
<td>26</td>
<td>21</td>
<td>19</td>
<td>18</td>
<td>17</td>
<td>16</td>
<td>17</td>
<td>13</td>
<td>12</td>
<td>11</td>
<td>10</td>
<td>9</td>
    </tr>
<tr>
        <td>8</td>
<td>27</td>
<td>22</td>
<td>20</td>
<td>19</td>
<td>18</td>
<td>17</td>
<td>20</td>
<td>16</td>
<td>15</td>
<td>14</td>
<td>13</td>
<td>12</td>
    </tr>
<tr>
        <td>10</td>
<td>28</td>
<td>23</td>
<td>21</td>
<td>20</td>
<td>19</td>
<td>18</td>
<td>25</td>
<td>21</td>
<td>20</td>
<td>19</td>
<td>18</td>
<td>17</td>
    </tr>
<tr>
        <td>12</td>
<td>29</td>
<td>24</td>
<td>22</td>
<td>21</td>
<td>20</td>
<td>19</td>
<td>24</td>
<td>20</td>
<td>19</td>
<td>18</td>
<td>17</td>
<td>16</td>
    </tr>
<tr>
        <td>14</td>
<td>30</td>
<td>25</td>
<td>23</td>
<td>22</td>
<td>21</td>
<td>20</td>
<td>28</td>
<td>24</td>
<td>23</td>
<td>22</td>
<td>21</td>
<td>20</td>
    </tr>
<tr>
        <td>16</td>
<td>32</td>
<td>27</td>
<td>25</td>
<td>24</td>
<td>23</td>
<td>22</td>
<td>26</td>
<td>22</td>
<td>21</td>
<td>20</td>
<td>19</td>
<td>18</td>
    </tr>
<tr>
        <td>18</td>
<td>34</td>
<td>29</td>
<td>27</td>
<td>26</td>
<td>25</td>
<td>24</td>
<td>27</td>
<td>23</td>
<td>22</td>
<td>21</td>
<td>20</td>
<td>19</td>
    </tr>
  </tbody>
</table>

**Figure 6.** Same as Figure 5 except for minimum sea-level pressure (MSLP) (hPa) and maximum 10-m wind speed (VMAX10, m s<sup>−1</sup>).

background error covariance estimation and therefore more appropriate for convection modeling. Zhao and Jin (2008) did observe positive impact to hurricane intensity and forecasts of hurricane intensity, however this was only achieved with the additional assimilation of Doppler radial velocity. They stated the assimilation of radial velocities was important for modifying the dynamical structures and reorganization of rainbands, which led to the improvement in intensity forecasts. Given these discrepancies in reflectivity impact and in order to better understand why reflectivity data may be positively impacting TC intensity from this study, we investigated the increments for updated model prognostic variables from observations with 5-km beam sampling span. Figure 7 presents the azimuthally averaged increments of vertical velocity ($w$), temperature ($T$) and mixing ratio of water vapor ($q_v$) at all heights averaged between 1500 UTC August 1 and 0000 UTC August 2 (10 update cycles). Temperature increments show stronger warming of up to 3–4 K through the depth of the core, while $q_v$ increments show increases of up to 1.8–2.0 g kg<sup>−1</sup> within the storm environment, with largest increases within the eyewall structure and above the boundary layer. Finally, vertical velocity shows stronger upward velocity within the eyewall and subsidence in the eye. The increments suggests that increased moistening and stronger updrafts within the inner environment is driving an intensification of the secondary circulation through increased convective activity. This can be explained by the principle theory governing TC intensification, which states that, assuming frictionless flow, angular momentum is approximately conserved and the tangential momentum equation reduces to

$$Vt = \frac{M}{r} - \frac{1}{2}fr$$ (9)

Here, $Vt$ is the tangential wind component, $M$ is the absolute angular momentum per unit mass of an air parcel about the rotate axis, $r$ is the radius, and $f$ is the Coriolis parameter. Upon strengthening of the secondary circulation, the boundary inflow of air increases and $Vt$ increases. Assuming gradient wind balance over the TC environment, the equation relating radial pressure gradient and centrifugal and Coriolis forces is given by

$$\frac{1}{\rho} \frac{\partial p}{\partial r} = \frac{Vt^2}{r} + fv$$ (10)

where $\rho$ is density and $p$ is pressure. Equation 10 states that if $Vt$ increases, the central pressure will decrease. Combining Equations 9 and 10, we attribute the intensification of the TC with the assimilation of $Z_G$ is being driven by increases in vertical velocity in the inner storm environment, causing stronger boundary inflow through mass continuity and the advection of higher angular momentum air toward the TC center.

TAYLOR ET AL.

11 of 19


---



AGU ADVANCING EARTH AND SPACE SCIENCE logo

Journal of Advances in Modeling Earth Systems

10.1029/2020MS002332

19422466, 2021, 7, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2020MS002332 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

<table>
  <thead>
    <tr>
        <th colspan="2">Temp (K)</th>
        <th colspan="2">qv (g kg⁻¹)</th>
        <th colspan="2">w (m s⁻¹)</th>
    </tr>
<tr>
        <th>Radius (km)</th>
        <th>Height (km)</th>
        <th>Radius (km)</th>
        <th>Height (km)</th>
        <th>Radius (km)</th>
        <th>Height (km)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
    </tr>
<tr>
        <td>50</td>
<td>2</td>
<td>50</td>
<td>2</td>
<td>50</td>
<td>2</td>
    </tr>
<tr>
        <td>100</td>
<td>4</td>
<td>100</td>
<td>4</td>
<td>100</td>
<td>4</td>
    </tr>
<tr>
        <td>150</td>
<td>6</td>
<td>150</td>
<td>6</td>
<td>150</td>
<td>6</td>
    </tr>
<tr>
        <td>200</td>
<td>8</td>
<td>200</td>
<td>8</td>
<td>200</td>
<td>8</td>
    </tr>
<tr>
        <td>250</td>
<td>10</td>
<td>250</td>
<td>10</td>
<td>250</td>
<td>10</td>
    </tr>
<tr>
        <td> </td>
<td>12</td>
<td> </td>
<td>12</td>
<td> </td>
<td>12</td>
    </tr>
<tr>
        <td> </td>
<td>14</td>
<td> </td>
<td>14</td>
<td> </td>
<td>14</td>
    </tr>
  </tbody>
</table>

Figure 7. Azimuthally averaged increments (shading) of temperature (T), mixing ratio of water vapor ($q_v$) and vertical velocity ($w$) between 1500 UTC August 1 and 0000 UTC August 2 assimilating observations with 5-km beam sampling span. Contours show anomalies from outer storm environment defined to be between 250 and 500 km from TC center.

By conservation of angular momentum $V_t$ increases, leading to an increase in $\frac{\partial p}{\partial r}$ through gradient wind balance.

## 3.2. Moisture Analyses and Rain Prediction

Presented in Figure 8 are ensemble mean analyses of all mixing ratio of hydrometeors ($q_{all}$) at 2-km elevation at 0000 UTC August 2 (after 12 cycles) for the GPR experiments, NO-GPR and NR. Compared to NO-GPR, each of the GPR experiments show a moisture field more consistent to the NR, with many of key TC features presented, including a high intensity precipitation region surrounding the TC center and outer convective rainbands that are clearly visible in the surrounding outer storm environment. From the GPR experiments, the intensity and distribution of precipitation appears better represented in the experiments with a finer beam span. For example, the NR shows the TC with symmetrical structure and a clearly defined eye, identifiable by a region of dryer air (low $q_{all}$) at ~148.1°E, 14.4°N. In the analyses from experiments assimilating observations with coarser beam spans, that is, BS20 and BS15, this region of dryer air is not readily seen. In contrast, the experiments with finer beam span, that is, BS10 and BS05, display an analysis with a region of dryer air at this location, indicating the formation of an eye. Another prominent feature in the NR is a region of very high $q_{all}$ (>2 g kg<sup>-1</sup>) to the south of the eye, indicating very intense precipitation within the eyewall during this period of rapid intensification. While each of the GPR analyses successfully display higher $q_{all}$ within this region, BS05 displays notably more intense rainfall of >2 g kg<sup>-1</sup> at this location, in better agreement with the NR. The improved representation of stronger precipitation from BS05 is likely associated with the finer beam span providing improved capturing of higher intensity rainfall in observations. As stated in Section 2.3, as the beam sampling span is reduced and increase the number of observations across the coverage region, the probability of the beam center hitting an area of strong precipitation within the large scattering volume increases, allowing for regions of higher precipitation to be captured.

Next, to understand how oversampling impact precipitation forecasts we investigate accumulated rainfall forecasts initialized from the ensemble mean for BS20 and BS05 over 1-h and 18-h forecasts (Figures 9 and 10 respectively). In the 1-h forecasts, initialized at 0000 UTC August 2 (after 12 cycles), both forecasts correctly predict the highest intensity rainfall within the eyewall to the southwest of the center in agreement with the NR. However, BS05 shows many more regions of weaker rainfall (<10 mm) across the storm environment compared to BS20, including associated with outer convective rainbands. For example, larger

TAYLOR ET AL.

12 of 19


---



19422466, 2021, 7, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2020MS002332 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

10.1029/2020MS002332

AGU ADVANCING EARTH AND SPACE SCIENCE logo

# Journal of Advances in Modeling Earth Systems

Figure 8: Longitude-latitude mixing ratio of all hydrometeors (qall, g kg⁻¹), which includes rain, cloud water, cloud ice, snow, and graupel, at 2-km height at 0000 UTC August 2 for the NR, NO-GPR, BS20, BS15, BS10, and BS05.

Figure 8. Longitude-latitude mixing ratio of all hydrometeors ($q_{all}$, g kg<sup>−1</sup>), which includes rain, cloud water, cloud ice, snow, and graupel, at 2-km height at 0000 UTC August 2 for the NR, NO-GPR, BS20, BS15, BS10, and BS05.

regions of weaker rainfall are seen associated with the convective rainband located to the south of the TC in BS05, in better agreement with the NR. In the 18-h forecasts initialized at 2000and 2200 UTC on 1 August and 0000 UTC August 2 (Figure 10), considerable differences are shown between each set of forecasts. In general, BS05 predicts higher accumulations across more northern and western regions, in the direction of the forecast track, while BS20 on the other hand shows rainfall concentrated more heavily to the south, less in agreement with the NR. This is particularly apparent in the forecast initialized at 2000 UTC, where the rainfall is heavily accumulated south of 14°N for BS20, while BS05 shows considerably less rainfall in this region and with heavier concentrations to the north and west following the path of the forecast track.

To objectively evaluate the skill of the 18-h rainfall totals, we calculated the threat scores (TSs), defined as

$$ TS = \frac{FO}{FO + FX + XO} (0 \le TS \le 1) $$ (11)

Figure 9: Rainfall totals (mm) from 1-h forecasts initialized from the ensemble mean at 2000 UTC August 1 for BS20 (middle) and BS05 (right) and from the nature run (NR) (left). Contours show pressure levels (hPa).

Figure 9. Rainfall totals (mm) from 1-h forecasts initialized from the ensemble mean at 2000 UTC August 1 for BS20 (middle) and BS05 (right) and from the nature run (NR) (left). Contours show pressure levels (hPa).

TAYLOR ET AL.

13 of 19
13 of 19


---



AGU ADVANCING EARTH AND SPACE SCIENCE logo

Journal of Advances in Modeling Earth Systems

10.1029/2020MS002332

19422466, 2021, 7, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2020MS002332 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

Rainfall totals (mm) from 18-h forecasts for BS20, BS05, and Nature Run initialized at different times.

**Figure 10.** Rainfall totals (mm) from 18-h forecasts initialized from the ensemble mean at 2000, 2200 UTC 1 August and 0000 UTC August 2 for BS20 (left column) and BS05 (middle column). Also shown are the accumulated rainfall totals from the nature run (NR) over the same forecast periods (right column). Black lines in each figure denote tropical cyclone (TC) track position over the 18-h period based on minimum sea-level pressure (MSLP). The red rectangle shows the region where the threat scores of accumulated rainfall for each forecast are calculated.

where $FO$ is the number of forecast events that were observed (hits), $FX$ is number of forecasted events not observed (false alarms) and $XO$ is the observed events not forecast (misses). The TS ranges between 0 and 1 with the accuracy of the forecast with higher scores meaning better forecasts. TSs were calculated on the 3-km SCALE model grid within the region shown by the red rectangle in Figure 10 for a threshold of 150 millimeters (mm). The threat scores in Figure 11 are for each of the 13 18-h forecasts for BS20 and BS05 initialized between 1800 UTC August 1 and 0600 UTC August 2. The average TS from all 13 forecasts are shown in each figure. For both BS20 and BS05, the average TS is below 0.3, reflecting the large errors in track forecasts, which were shown to rapidly increase from initialization (Figure 5). Nevertheless, BS05 outperforms BS20 in each of the 13 forecasts, with average scores of 0.295 and 0.253, respectively, signaling an improvement in rainfall prediction with oversampling.

## 3.3. Maximum Wind Speed Forecasts

Information regarding the maximum intensity of surface winds in the following hours is of considerable value for communities and disasters agencies seeking to mitigate the risk from an approaching TC. Figure 12 shows VMAX10 for three 18-h forecasts initialized at 2000, 2200 UTC August 1 and 0000 UTC August 2 for BS20 and BS05 and for the NR. The spatial distribution of winds in both sets of forecasts are very similar, with the strongest winds located to the right of the storm center following the TC's propagation northwestwards. The near identical wind fields for BS20 and BS05 is attributed to similar track forecasts, which is attributed to horizontal wind components not being updated with $Z_G$ assimilation, meaning there will be little impact from oversampling to the large-scale circulation. Maximum wind intensity in each set

TAYLOR ET AL.

14 of 19
14 of 19


---



19422466, 2021, 7, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2020MS002332 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU ADVANCING EARTH AND SPACE SCIENCE logo

# Journal of Advances in Modeling Earth Systems

10.1029/2020MS002332

<table>
  <thead>
    <tr>
        <th>Time (UTC)</th>
        <th>BS05</th>
        <th>BS20</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>18</td>
<td>0.32</td>
<td>0.31</td>
    </tr>
<tr>
        <td>19</td>
<td>0.26</td>
<td>0.26</td>
    </tr>
<tr>
        <td>20</td>
<td>0.23</td>
<td>0.25</td>
    </tr>
<tr>
        <td>21</td>
<td>0.29</td>
<td>0.29</td>
    </tr>
<tr>
        <td>22</td>
<td>0.24</td>
<td>0.24</td>
    </tr>
<tr>
        <td>23</td>
<td>0.31</td>
<td>0.19</td>
    </tr>
<tr>
        <td>00</td>
<td>0.26</td>
<td>0.27</td>
    </tr>
<tr>
        <td>01</td>
<td>0.35</td>
<td>0.22</td>
    </tr>
<tr>
        <td>02</td>
<td>0.33</td>
<td>0.27</td>
    </tr>
<tr>
        <td>03</td>
<td>0.30</td>
<td>0.22</td>
    </tr>
<tr>
        <td>04</td>
<td>0.27</td>
<td>0.27</td>
    </tr>
<tr>
        <td>05</td>
<td>0.22</td>
<td>0.22</td>
    </tr>
<tr>
        <td>06</td>
<td>0.28</td>
<td>0.28</td>
    </tr>
  </tbody>
</table>

Figure 11. Threat scores calculated at 18-h lead times for forecasts initialized between 1800 UTC 1 August and 0600 UTC August 2 for BS20 and BS05. Threat scores are verified against the nature run (NR) using an accumulated rainfall threshold of 150 mm.

of forecasts though shows notable differences between the experiments, with BS05 predicting stronger maximum winds compared to BS20, in better agreement with the NR. The increase in wind intensity shown by BS05 is made more significant given how it changes the status of wind intensity on the JMA's typhoon intensity scale. For example, maximum wind speeds reach over 54 m s<sup>-1</sup> in the NR, indicative of violent typhoon force winds at this time according to the JMA typhoon classification ([https://www.jma.go.jp/en/typh/](https://www.jma.go.jp/en/typh/)). Each of the BS05 forecasts show that these violent strength winds are well predicted but hardly predicted in the BS20 forecasts. We found stronger maximum winds were predicted in all 13 forecasts initialized between 1800 UTC August 1 and 0600 UTC August 2 for BS05 compared to BS20 and were all in better agreement with the NR, providing another positive impact of oversampling in understanding how impactful a TC will likely be in the following hours.

## 4. Conclusion

This study represents the first attempt to evaluate the usefulness of reflectivity observations from a potential future precipitation radar onboard a geostationary satellite for NWP. We performed a perfect model OSSE for a strong West Pacific tropical cyclone with data assimilation experiments examining the impact of observations obtained for a range of beam sampling spans on TC analyses and forecasts. Results showed assimilation of observations obtained with finer beam sampling spans led to an improvement in moisture field analyses, with observations obtained with 5-km

sampling span providing markedly improved representation of key convective features, including the eye, eyewall, and outer convective rainbands. In both 1 and 18-h accumulated rain forecasts, improvement observed for the 5-km oversampling case was compared to the 20-km case representing no oversampling. This was evident from better representation of weaker rainfall associated with the outer rainbands and heavier rainfall totals following the path of the forecast track in 18-h forecasts. While threat scores for accumulated rainfall were low for both the no-oversampling and 5-km oversampling cases, they were improved for the oversampling case in all forecasts. The positive impact shown in precipitation analyses and forecasts was attributed to the finer beam sampling span, enabling better capturing of higher intensity rain in observations.

The impact to track forecasts was found to be minimal, though this was expected given winds were not updated for reflectivity assimilation due to the generation of imbalances, which should be addressed in future studies. TC intensity was improved in both analyses and forecasts, with the 5-km oversampling case generating the strongest TC through cycling, in closer agreement to the nature run. Intensity forecasts were also improved with observations, with MSLP errors increasingly reduced with finer beam span at each lead time, suggesting an important benefit of oversampling to TC forecasts.

While the results of this study show positive impact of observations and use of oversampling to TC analyses and forecasts, we made several major assumptions that can be expected to strongly determine the impact of real observations. First, by assuming a perfect prediction model, we did not consider model error, a major source of uncertainty in NWP. Second, observations were calculated from the nature run using the Joint Simulator software that was equally used to calculate reflectivity coefficients for the forward operator used by the LETKF. Large uncertainties can be expected in the estimation of precipitation species from the forward operator that will be a major determining factor on observation impact. Both model error and imperfect forward operator in estimations of precipitation species should be thoroughly investigated in future studies to provide a more complete understanding of potential usefulness of observations for NWP. In addition, we will need to investigate the impact of surface clutter contamination on observations, which is expected to be severe at low levels. For this, we recommend the formation of a new methodology to treat contaminated observations within the data assimilation scheme.

TAYLOR ET AL.

15 of 19
15 of 19


---



19422466, 2021, 7, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2020MS002332 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU ADVANCING EARTH AND SPACE SCIENCE logo

**Journal of Advances in Modeling Earth Systems**

10.1029/2020MS002332

Geographical maps showing ensemble-mean 18-h forecasts of maximum 10-m wind speed for BS20, BS05, and Nature Run initialized at different times.

**Figure 12.** Ensemble-mean 18-h forecasts of maximum 10-m wind speed (shading) initialized at 2000 and 2200 UTC on August 1 and 0000 UTC on August 2 for BS20 (left column) and BS05 (middle column). Right column shows maximum 10-m wind speeds from the nature run (NR) over the same periods. Black lines in each figure denote TC track position over the 18 h period based on minimum sea-level pressure (MSLP).

Satellite observations can be expected to play an increasing important role in data assimilation for NWP. Several recent studies have demonstrated a positive impact on TC analyses and forecasts from assimilation of satellite observations, including all-sky IR radiances from Himawari-8 (Honda, Kotsuki, et al., 2018; Honda, Miyoshi, et al., 2018; Honda et al., 2019; Minamide & Zhang, 2018). Honda, Kotsuki, et al. (2018) and Honda, Miyoshi, et al. (2018) demonstrated that all-sky IR radiances improves TC intensity and precipitation forecasts, while Honda et al. (2019) found all-sky IR radiances from Himawari-8 improves the representativeness in TC structure. Given a similarity between the results of those studies to this study, it would be of interest to compare the usefulness of IR radiances and reflectivity observations on TC prediction. It would also be of interest to explore whether the combined use of the two different datasets from geostationary-based satellites might provide further improvement to forecasts, particularly with regards to TC intensity.

TAYLOR ET AL.

16 of 19
16 of 19


---



19422466, 2021, 7, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2020MS002332 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU Advancing Earth and Space Science logo

# Journal of Advances in Modeling Earth Systems

10.1029/2020MS002332

## Data Availability Statement

The SCALE-RM is available at [http://r-ccs-climate.riken.jp/scale/](http://r-ccs-climate.riken.jp/scale/). The Joint Simulator is available at [http://www.eorc.jaxa.jp/theme/Joint-Simulator/userform/js_userform.html](http://www.eorc.jaxa.jp/theme/Joint-Simulator/userform/js_userform.html) (last accessed July 11, 2019).

**Acknowledgments**

The authors would like to thank the members of the Data Assimilation Research Team, RIKEN R-CCS and Japan Aerospace Exploration Agency (JAXA) for helpful insights and discussions. This study was supported by Japan Aerospace Exploration Agency, FLAGSHIP2020 Project of the Ministry of Education, Culture, Sports, Science and Technology of Japan, JST AIP (Grant Number JPMJCR19U2), MEXT as "Program for Promoting Researches on the Supercomputer Fugaku" (Large Ensemble Atmospheric and Environmental Prediction for Disaster Prevention and Mitigation), the COE research grant in computational science from Hyogo Prefecture and Kobe City through Foundation for Computational Science, JST SICORP (Grant Number JPMJSC1804), JSPS KAKENHI (Grant Number JP19H05605), JST CREST (Grant Number JPMJCR20F2) and JST Moonshot R&D - MILLENNIA Program (Grant Number JPMJMS20MK). This work used computational resources of the K computer provided by RIKEN through the HPCI System Research Project (Project ID: hp180062, hp190051, hp200026, ra000015, hp160229, hp170246, hp180194). The authors would like to thank the two anonymous reviewers for their constructive comments and suggestions.

## References

Adler, R. F., Huffman, G. J., Bolvin, D. T., Curtis, S., and Nelkin, E. J. (2000). Tropical rainfall distributions determined using TRMM combined with other satellite and rain gauge information. *Journal of Applied Meteorology and Climatology*, 39, 2007–2023. [https://doi.org/10.1175/1520-0450(2001)0402.0.CO;2](https://doi.org/10.1175/1520-0450(2001)0402.0.CO;2)0402.0.CO;2)

Adler, R. F., Wang, J.-J., Gu, G., Huffman, G. J. (2009). A ten-year tropical rainfall climatology based on a composite of TRMM products, *Journal of the Meteorological Society of Japan*, 87A, 281–293. [https://doi.org/10.2151/jmsj.87a.281](https://doi.org/10.2151/jmsj.87a.281)

Amemiya, A., Honda, T., Miyoshi, T. (2019). Improving the observation operator for the Phased Array Weather Radar in the SCALE-LETKF system. *Scientific online letters on the atmosphere: SOLA*, 16. [https://doi.org/10.2151/sola.2020-002](https://doi.org/10.2151/sola.2020-002)

Aubry, A., Maio, A. D., Foglia, G., Hao, C., Orlando, D., (2015). Radar detection and range estimation using oversampled data. *IEEE Transactions on Aerospace and Electronic Systems*, 51, 1039–1052. [https://doi.org/10.1109/TAES.2014.130364](https://doi.org/10.1109/TAES.2014.130364)

Battaglia, A., Tanalli, S., Mroz, K., Tridon, F. (2015). Multiple scattering in observations of the GPM dual-frequency precipitation radar: Evidence and impact on retrievals. *Journal of Geophysical Research - D: Atmospheres*, 120, 4090–4101. [https://doi.org/10.1002/2014JD022866](https://doi.org/10.1002/2014JD022866)

Bennedetti, A., Lopez, P., Bauer, P., Moreau, E. (2005). Experimental use of TRMM precipitation radar observations in 1D+4D−Var assimilation. *Quarterly Journal of the Royal Meteorological Society*, 131, 2473–2495. [https://doi.org/10.1256/qj.04.89](https://doi.org/10.1256/qj.04.89)

Bick, T., Simmer, C., Trömel, S., Wapler, K., Franssen, H. J. H., Stephan, K., Blahak, U., et al. (2016). Assimilation of 3D radar reflectivities with an ensemble Kalman filter on the convective scale. *Quarterly Journal of the Royal Meteorological Society*, 142, 1490–1504. [https://doi.org/10.1002/qj.2751](https://doi.org/10.1002/qj.2751)

Borowska, L., Zhang, G., Zrnic, D. S. (2015). Considerations for oversampling in azimuth in the phased array weather radar. *Journal of Atmospheric and Oceanic Technology*, 32, 1614–1629. [https://doi.org/10.1175/JTECH-D-15-0018.1](https://doi.org/10.1175/JTECH-D-15-0018.1)

Chambon, P., Zhang, S. Q., Hou, A. Y., Zupanski, M., Cheung, S. (2014), Assessing the impact of pre-GPM microwave precipitation observations in the Goddard WRF ensemble data assimilation system. *Quarterly Journal of the Royal Meteorological Society*, 140, 1219–1235. [https://doi.org/10.1002/qj.2215](https://doi.org/10.1002/qj.2215)

Chang, C. C., Wu, C. C. (2017). On the processes leading to the rapid intensification of Typhoon Megi (2010). *Journal of the Atmospheric Sciences*, 74, 1169–1200. [https://doi.org/10.1175/JAS-D-16-0075.1](https://doi.org/10.1175/JAS-D-16-0075.1)

Di Michele, S., Ahlgrimm, M., Forbes, R., Kulie, M., Bennartz, R., Janisková, M., Bauer, P. (2012). Interpreting an evaluation of the ECMWF global model with CloudSat observations: Ambiguities due to radar reflectivity forward operator uncertainties. *Quarterly Journal of the Royal Meteorological Society*, 138, 2047–2065. [https://doi.org/10.1002/qj.1936](https://doi.org/10.1002/qj.1936)

Dong, J., Xue, M. (2013). Assimilation of radial velocity and reflectivity data from coastal WSR-88D radars using an ensemble Kalman filter for the analysis and forecast of landfalling hurricane Ike (2008). *Quarterly Journal of the Royal Meteorological Society*, 139, 467–487. [https://doi.org/10.1002/qj.1970](https://doi.org/10.1002/qj.1970)

Galligani, V., Wang, D., Imaz, M. I., Salio, P., Prigent, C. (2017). Analysis and evaluation of WRF microphysics schemes for deep moist convection over south-eastern South America (SESA) using microwave satellite observation and radiative transfer simulations. *Atmospheric Measurement Techniques*, 10, 3627–3649. [https://doi.org/10.5194/amt-10-3627-2017](https://doi.org/10.5194/amt-10-3627-2017)

Gaspari, G., S. E. Cohn, (1999). Construction of correlation functions in two and three dimensions. *Quarterly Journal of the Royal Meteorological Society*, 12, 723–757.

Gastaldo, T., Poli, V., Marsigli, C., Paolo Alberoni, P., Paccagnella, T. (2018). Data assimilation of radar reflectivity volumes in a LETKF scheme. *Nonlinear Processes in Geophysics*. 25, 747–764. [https://doi.org/10.5194/npg-25-747-2018](https://doi.org/10.5194/npg-25-747-2018)

Geer, A. J., Baordo, F. (2014). Improved scattering radiative transfer for frozen hydrometeors at microwave frequencies, *Atmospheric Measurement Techniques*, 7, 1839–1860, [https://doi.org/10.5194/amt-7-1839-2014](https://doi.org/10.5194/amt-7-1839-2014)

Hashino, T., Satoh, M., Hagibara, Y., Kubota, T., Matsui, T., Nasuno, T., Okamoto, H. (2013). Evaluating cloud microphysics from NICAM against CloudSat and CALIPSO, *Journal of Geophysical Research - D: Atmospheres*, 118, 7273–7292. [https://doi.org/10.1002/jgrd.50564](https://doi.org/10.1002/jgrd.50564)

Honda, T., Kotsuki, S., Lien, G. Y., Maejima, Y., Okamoto, K., Miyoshi, T. (2018a). Assimilation of Himawari-8 all-sky radiances every 10 minutes: Impact on precipitation and flood risk prediction. *Journal of Geophysical Research: Atmospheres* 123, 965–976. [https://doi.org/10.1002/2017JD027096](https://doi.org/10.1002/2017JD027096)

Honda, T., Miyoshi, T., Lien, G. Y., Nishizawa, S., Yoshida, R., Adachi, S. A. (2018b). Assimilating all-sky Himawari-8 satellite infrared radiances: A case of Typhoon Soudelor (2015), *Monthly Weather Review* 146, 213–229. [https://doi.org/10.1175/MWR-D-16-0357.1](https://doi.org/10.1175/MWR-D-16-0357.1)

Honda, T., Takino, S., Miyoshi, T. (2019). Improving a precipitation forecast by assimilating all-sky Himawari-8 satellite infrared radiances: A case of typhoon Malakas (2016), *Scientific online letters on the atmosphere: SOLA*, 15, 7–11. [https://doi.org/10.2151/sola.2019-002](https://doi.org/10.2151/sola.2019-002)

Hou, A. Y., Kakar, R. K., Neeck, S. S., Azarbarzin, A. A., Kummerow, C. D., Kojima, M., et al. (2014). The global precipitation measurement mission, *Bulletin of the American Meteorological Society*, 95, 701–722. [https://doi.org/10.1175/BAMS-D-13-00164.1](https://doi.org/10.1175/BAMS-D-13-00164.1)

Hunt, B., Kostelich, E., Szunyogh, I. (2007). Efficient data assimilation for spatiotemporal chaos: A local ensemble transform Kalman filter. *Physica D Nonlinear Phenomena*, 230, 112‒126. [https://doi.org/10.1016/j.physd.2006.11.008](https://doi.org/10.1016/j.physd.2006.11.008)

Iguchi, T., Kozu, T., Meneghini, R., Awaka, J., Okamoto, K. (2000). Rain-profiling algorithm for the TRMM precipitation radar. *Journal of Applied Meteorology*, 39, 2038–2052.

Iguchi, T., Seto, S., Meneghini, R., Yoshida, N., Awaka, J., Le, M., et al. (2017). *GPM/DPR Level-2 algorithm theoretical basis document* (pp. 79). NASA Goddard Space Flight Center.

Ikai, J., Nakamura, K. (2003). Comparison of rain rates over the ocean derived from TRMM microwave imager and precipitation radar. *Journal of Atmospheric and Oceanic Technology*, 20(12), 1709–1726. https://doi.org/10.1175/1520-0426(2003)020<1709:CORROT>2.0.CO;2020<1709:CORROT>2.0.CO;2)

Ivić, I., Zahrai, A., & Zrnić, D. (2003a). Digital IF receiver: Capabilities, tests, and evaluation. *Preprints 31th conf. on radar meteorology*, Seattle, WA, American Meteorological Society, 732–734.

Ivić, I., Zrnić, D., & Torres, S. (2003b). Whitening in range to improve weather radar spectral moment estimates. Part II: Experimental evaluation. *Journal of Atmospheric and Oceanic Technology*, 20(11), 1449–1459. https://doi.org/10.1175/1520-0426(2003)020<1449:WIRTIW>2.0.CO;2020<1449:WIRTIW>2.0.CO;2)

TAYLOR ET AL.

17 of 19
17 of 19


---



19422466, 2021, 7, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2020MS002332 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU logo

# Journal of Advances in Modeling Earth Systems

10.1029/2020MS002332

Joudoi, D., Kuratomi, T., & Watanabe, K. (2018). The construction method of a 30-m-class large planar antenna for space solar power systems, 69th international astronautical congress. Bremen, Germany, 1–5. [https://doi.org/10.1299/transjsme.18-00248](https://doi.org/10.1299/transjsme.18-00248)

Koch, S. E., Stensrud, D. J., Xue, M., Wicker, L. J., Yussouf, N., Sobash, R. A., Potvin, C. K. (2012). An overview of observing system simulation experiment (OSSE) research on storm-scale analysis and prediction at the national weather center (Invited). American geophysical union, fall meeting 2012. American Geophysical Union.

Kozu, T., Kawanishi, T., Kuroiwa, H., Kojima, M., Oikawa, K., Kumagai, H., et al. (2001). Development of precipitation radar onboard the Tropical Rainfall Measuring Mission (TRMM) satellite, *IEEE Transactions on Geoscience and Remote Sensing*, 39, 102–116. [https://doi.org/10.1109/36.898669](https://doi.org/10.1109/36.898669)

Kubota, T., Iguchi, T., Kojima, M., Liao, L., Masaki, T., Hanado, H., et al. (2016). A statistical method for reducing sidelobe clutter for the Ku-band precipitation radar onboard the tropical rainfall measuring mission (TRMM) satellite, *IEEE Transactions on Geoscience and Remote Sensing*, 39, 102–116. [https://doi.org/10.1175/JTECH-D-15-0202.1](https://doi.org/10.1175/JTECH-D-15-0202.1)

Kummerow, C. D., W. Barnes, T. Kozu, J. Shiue, J. Simpson, (1998). The tropical rainfall measuring mission (TRMM) sensor package, *Journal of Atmospheric and Oceanic Technology*, 15, 808–816. https://doi.org/10.1175/1520-0426(1998)015<0809:TTRMMT>2.0.CO;2015<0809:TTRMMT>2.0.CO;2)

Li, X., He, J., Wang, C., Tang, S., Hou, X. (2017). Evaluation of surface clutter for future geostationary space borne weather radar, *Atmosphere*, 8, 14. [https://doi.org/10.3390/atmos8010014](https://doi.org/10.3390/atmos8010014)

Li, X., Pu, Z. (2008). Sensitivity of numerical simulation of early rapid intensification of Hurricane Emily (2005) to cloud microphysical and planetary boundary layer parameterizations. *Monthly Weather Review* 136, 4819–4838. [https://doi.org/10.1175/2008MWR2366.1](https://doi.org/10.1175/2008MWR2366.1)

Lien, G. Y., Miyoshi, T., Kalnay, E. (2016). Assimilation of TRMM multi-satellite precipitation analysis with a low-resolution NCEP global forecast system. *Monthly Weather Review*, 144, 643–661. [https://doi.org/10.1175/MWR-D-15-0149.1](https://doi.org/10.1175/MWR-D-15-0149.1)

Lien, G. Y., Miyoshi, T., Nishizawa, S., Yoshida, R., Yashiro, H., Adachi, S. A., et al. (2017). The near-realtime SCALE-LETKF system: A case of the September 2015 Kanto-Tohoku heavy rainfall. *Scientific online letters on the atmosphere: SOLA*, 13, 1–6. [https://doi.org/10.2151/sola.2017-001](https://doi.org/10.2151/sola.2017-001)

Liu, C., Xue, M., Kong, R. (2019). Direct assimilation of radar reflectivity data using 3DVAR: Treatment of hydrometeor background errors and OSSE tests. *Monthly Weather Review*, 147, 17–29. [https://doi.org/10.1175/MWR-D-18-0033.1](https://doi.org/10.1175/MWR-D-18-0033.1)

Maejima, Y., Kunii, M., Miyoshi, T. (2017). 30-second-uptae 100-m mesh data assimilation experiments: A sudden local rain case in Kobe on 11 September 2014. *Scientific online letters on the atmosphere: SOLA*, 13, 174–180.

Masunaga, H., C. D. Kummerow, (2005). Combined radar and radiometer analysis of precipitation profiles for a parametric retrieval algorithm, *Journal of Atmospheric and Oceanic Technology*, 22, 909–929. [https://doi.org/10.1175/JTECH1751.1](https://doi.org/10.1175/JTECH1751.1)

Minamide, M., Zhang, F. (2018). Assimilation of all-sky infrared radiances from Himawari-8 and impacts of moisture and hydrometer initialization on convection-permitting tropical cyclone prediction. *Monthly Weather Review*, 146, 3241–3258. [https://doi.org/10.1175/MWR-D-17-0367.1](https://doi.org/10.1175/MWR-D-17-0367.1)

Miyoshi, T., Kunii, M., Ruiz, J., Lien, G.-Y., Satoh, S., Ushio, T., et al. (2016). “Big data assimilation” revolutionizing severe weather prediction. *Bulletin of the American Meteorological Society*, 97, 1347–1354. [https://doi.org/10.1175/BAMS-D-15-00144.1](https://doi.org/10.1175/BAMS-D-15-00144.1)

Nakanishi, M., Niino, H. (2004). An improved Mellor–Yamada level 3 model with condensation physics: Its design and verification. *Boundary-Layer Meteorology*, 112, 1–31. [https://doi.org/10.1023/B:BOUN.0000020164.04146.98](https://doi.org/10.1023/B:BOUN.0000020164.04146.98)

Nishizawa, S., Yashiro, H., Sato, Y., Miyamoto, Y., & Tomita, H. (2015). Influence of grid aspect ratio on planetary boundary layer turbulence in large-eddy simulations. *Geoscientific Model Development*, 8, 3393−3419, [https://doi.org/10.5194/gmd-8-3393-2015](https://doi.org/10.5194/gmd-8-3393-2015)

Okamoto, K., Aonashi, K. (2016). Experimental assimilation of the GPR core observatory DPR reflectivity profiles for Typhoon Halong (2014), *Monthly Weather Review*, 144. [https://doi.org/10.1175/MWR-D-15-0399.1](https://doi.org/10.1175/MWR-D-15-0399.1)

Okazaki, A., Honda, T., Kotsuki, S., Yamaji, M., Kubuta, T., Oki, R., et al. (2019). Simulating precipitating radar observations from a geostationary satellite, *Atmospheric Measurement Techniques*, 12, 3985–3996. [https://doi.org/10.5194/amt-2018-278](https://doi.org/10.5194/amt-2018-278)

Pu, Z., Li, X., Sun, J. (2009). Impact of airborne Doppler radar data assimilation on the numerical simulation of intensity changes of hurricane Dennis near a landfall. *Journal of the Atmospheric Sciences*, 66, 3351–3365. [https://doi.org/10.1175/2009JAS3121.1](https://doi.org/10.1175/2009JAS3121.1)

Sato, Y., Nishizawa, S., Yashiro, H., Miyamoto, Y., Kajikawa, Y., Tomita, H. (2015). Impacts of cloud microphysics on trade wind cumulus: Which cloud microphysics processes contribute to the diversity in a large eddy simulation? *Progress in Earth and Planetary Science*, 2, 23. [https://doi.org/10.1186/s40645-015-0053-6](https://doi.org/10.1186/s40645-015-0053-6)

Sekiguchi, M., Nakajima, T. (2008). A k-distribution-based radiation code and its computational optimization for an atmospheric general circulation model, *Journal of Quantitative Spectroscopy & Radiative Transfer*, 109, 2779–2793. [https://doi.org/10.1016/j.jqsrt.2008.07.013](https://doi.org/10.1016/j.jqsrt.2008.07.013)
Sieron, S., Zhang, F., Clothiaux, E., Zhang, E., Lu, L. N. (2018). Representing precipitation ice species with both spherical and nonspherical particles for radiative transfer modeling of microphysics: Consistent cloud microwave scattering properties. *Journal of Advances in Modelling Earth Systems*, 10, 1011–1028. [https://doi.org/10.1002/2017MS001226](https://doi.org/10.1002/2017MS001226)

Skofronick-Jackson, G., Petersen, W. A., Berg, W., Kidd, C., Stocker, E. F., Kirschbaum, D. B., et al. (2017). The global precipitation measurement (GPM) mission for science and society, *Bulletin of the American Meteorological Society*, 98, 1679–1695. [https://doi.org/10.1175/BAMS-D-15-00306.1](https://doi.org/10.1175/BAMS-D-15-00306.1)

Snyder, C., Zhang, F. (2003). Assimilation of simulated Doppler radar observations with an ensemble Kalman filter. *Monthly Weather Review*, 131, 1663–1677. [https://doi.org/10.1175//2555.1](https://doi.org/10.1175//2555.1)

Sobash, R., Stensrud, D. (2013). The impact of covariance localization for radar data on EnKF analyses of a developing MCS: Observing system simulation experiments. *Monthly Weather Review*, 141, 3691–3709. [https://doi.org/10.1175/MWR-D-12-00203.1](https://doi.org/10.1175/MWR-D-12-00203.1)

Tomita, H. (2008). New microphysical schemes with five and six categories by diagnostic generation of cloud ice. *Journal of the Meteorological Society of Japan*, 86A, 121–142. [https://doi.org/10.2151/jmsj.86A.121](https://doi.org/10.2151/jmsj.86A.121)

Tong, M., Xue, M. (2005). Ensemble Kalman filter assimilation of Doppler radar data with a compressible nonhydrostatic model: OSS experiments. *Monthly Weather Review*, 133, 1789–1807. [https://doi.org/10.1175/MWR2898.1](https://doi.org/10.1175/MWR2898.1)

Torres, S., Zrnić, D. (2003a). Whitening in range to improve weather radar spectral moment estimates. Part I: Formulation and simulation. *Journal of Atmospheric and Oceanic Technology*, 20, 1433–1448. https://doi.org/10.1175/1520-0426(2003)020<1433:WIRTIW>2.0.CO;2020<1433:WIRTIW>2.0.CO;2)

Torres, S., Zrnić, D. (2003b). Whitening of signals in range to improve estimates of polarimetric variables. *Journal of Atmospheric and Oceanic Technology*, 20, 1776–1789. https://doi.org/10.1175/1520-0426(2003)020<1776:WOSIRT>2.0.CO;2020<1776:WOSIRT>2.0.CO;2)

Wu, P.-Y., Yang, S.-C., Tsai, C. C., Cheng, H. W. (2020). Convective-scale sampling error and its impact on the ensemble radar data assimilation system: A case study of a heavy rainfall event on 16 June 2008 in Taiwan, *Monthly Weather Review*, 148, 3631–3652. [https://doi.org/10.1175/MWR-D-19-0319.1](https://doi.org/10.1175/MWR-D-19-0319.1)

Xue, M., Tong, M., Droegemeier, K. (2006). An OSSE framework based on the ensemble square-root Kalman filter for evaluating impact of data from radar networks on thunderstorm analysis and forecast. *Journal of Atmospheric and Oceanic Technology*. 23, 46–66. [https://doi.org/10.1175/JTECH1835.1](https://doi.org/10.1175/JTECH1835.1)

TAYLOR ET AL. 18 of 19


---



19422466, 2021, 7, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2020MS002332 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU ADVANCING EARTH AND SPACE SCIENCE logo

# Journal of Advances in Modeling Earth Systems

10.1029/2020MS002332

Xue, M., Tong, M., Zhang, G. (2009). Simultaneous state estimation and attenuation correction for thunderstorms with radar data using an ensemble Kalman filter. Tests with simulated data. *Quarterly Journal of the Royal Meteorological Society*, 135, 1409–1423. [https://doi.org/10.1002/qj.453](https://doi.org/10.1002/qj.453)

Yu, T.-Y., Zhang, G., Chalamalasetti, A. B., Doviak, R. J., Zrnic, D. (2005). Resolution enhancement technique using range oversampling. *Journal of Atmospheric and Oceanic Technology*, 23, 228–240. [https://doi.org/10.1175/JTECH1841.1](https://doi.org/10.1175/JTECH1841.1)

Zhang, F., Minamide, M., Clothiaux, E. E., (2016). Potential impacts of assimilating all-sky satellite radiances from GOES-R on convection-permitting analysis and prediction of tropical cyclones. *Geophysical Research Letters*, 43. [https://doi.org/10.1002/2016GL068468](https://doi.org/10.1002/2016GL068468)

Zhang, F., Snyder, C., Sun, J. (2004). Impacts of initial estimate and observation availability on convective-scale data assimilation with an ensemble Kalman filter. *Monthly Weather Review*, 132, 1238–1253. https://doi.org/10.1175/1520-0493(2004)132<1238:IOIEAO>2.0.CO;2132<1238:IOIEAO>2.0.CO;2)

Zhao, Q., Jin, Y. (2008). High-resolution radar data assimilation for hurricane isabel (2003), at landfall. *Bulletin of the American Meteorological Society*, 89, 1355–1372. [https://doi.org/10.1175/2008BAMS2562.1](https://doi.org/10.1175/2008BAMS2562.1)

TAYLOR ET AL.

19 of 19
