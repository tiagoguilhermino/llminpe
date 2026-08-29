Check for updates

AGU ADVANCING EARTH AND SPACE SCIENCES logo

# JGR Atmospheres

Open Access icon

## RESEARCH ARTICLE

10.1029/2024JD043111

# Improved High-Latitude Light Precipitation Estimation Using a Combined Radiometer-Cloud Radar Retrieval

**Key Points:**

* Precipitation over the high-latitude oceans is poorly understood due to lack of in situ observations and the high frequency of drizzle

* Drizzle is difficult to separate from cloud water with satellite observations

* A method has been developed to combine active and passive sensors to separate drizzle from cloud water with physical consistency

**Spencer R. Jones<sup>1</sup> ORCID icon and Christian D. Kummerow<sup>1</sup> ORCID icon**

<sup>1</sup>Department of Atmospheric Science, Colorado State University, Fort Collins, CO, USA

**Correspondence to:**

S. R. Jones, spencer.jones@colostate.edu

**Citation:**

Jones, S. R., & Kummerow, C. D. (2025). Improved high-latitude light precipitation estimation using a combined radiometer-cloud radar retrieval. *Journal of Geophysical Research: Atmospheres*, 130, e2024JD043111. [https://doi.org/10.1029/2024JD043111](https://doi.org/10.1029/2024JD043111)

Received 13 DEC 2024
Accepted 29 JAN 2025

**Abstract** The high-latitude oceans are problematic for satellite estimations of precipitation due to the high frequency of occurrence of light drizzle and snowfall. Microwave radiometric observations are sensitive to integrated cloud water path but lack skill in distinguishing precipitation onset from cloud water and cloud ice due to radiation scattering. Precipitation radars to date have lacked sensitivity to drizzle and cloud radars have suffered from both the uncertainties inherent in Z-R relations and poor sampling due to nadir-only scans. This study optimally combines coincident active and passive microwave observations from CloudSat's Cloud Profiling Radar (CPR) and the Advanced Scanning Microwave Radiometer (AMSR2) to resolve cloud and hydrometeor distribution parameters and to force consistency between the two independent sets of coincident observations. The result is an estimation of drizzle frequency and intensity that are consistent with both the CPR and AMSR2 observations for the high-latitude oceans. This study finds that zonal means of retrieved high-latitude drizzle below 0.25 mm hr<sup>−1</sup> from these combined observations (0.263 mm day<sup>−1</sup>) fall slightly above those of CloudSat estimates (0.244 mm day<sup>−1</sup>) provided by the 2C-RAIN-PROFILE and 2C-SNOW-PROFILE products (Lebsock, 2018; Wood & L’Ecuyer, 2018) and far below that of radiometer-only estimates (0.920 mm day<sup>−1</sup>) provided by GPROF (C. D. Kummerow et al., 2015).

**Plain Language Summary** Most of the precipitation in the world occurs over oceans. Oceanic precipitation, especially in the high latitudes, is hard to measure due to the lack of permanent rain gauges or other traditional precipitation measurement techniques. Satellite observations provide key insight and good sampling, but radars that measure rain usually are not sensitive to very light drizzle and snow, which are the dominant form of precipitation in these regions. Radars that are sensitive to very light drizzle, such as cloud radars, have a very narrow measurement width, so sampling is poor. Satellite measurements of naturally emitted radiation in the microwave spectrum are commonly used to measure cloud water but are not good at distinguishing cloud water from light drizzle. We use both cloud radar and passive measurements together to get drizzle estimates that are consistent with both observation types. These combined satellite observations of drizzle can provide key insight into the nature of precipitation in these hard-to-observe regions.

## 1. Introduction

Clouds and precipitation remain some of the most highly variable and uncertain parameters in global climate trend forecasting (Ban et al., 2014). The advancement of satellite atmospheric remote sensing techniques over the last half century have contributed much to the current understanding of changing precipitation trends and extremes on the global scale (Adler et al., 2017). However, much progress remains to be made to reduce uncertainties in order to form a consistent precipitation climate data record. Despite more global coverage than ever before and despite continual improvements in retrieval algorithms, uncertainties remain in satellite precipitation estimates on the order of tenths of millimeters per day (Petković et al., 2023).

One of the main contributors to these uncertainties is the problem of light precipitation in operational satellite precipitation climatology products (Schulte & Kummerow, 2022). This problem is particularly relevant in the high-latitude oceans, where light precipitation is meteorologically prevalent and where few sensors capable of detecting low precipitation rates have sampled (Behrangi et al., 2012). Precipitation in the high-latitude regions has recently become of much scientific interest due to both poor historical understanding from under observation (Behrangi et al., 2016) and because of its greater sensitivity to climate change (Lau et al., 2013). Historically, satellite observations have been key for these regions due to lack of in situ measurements traditionally used for ground truth, such as rain gauges. For the global scale, the best effort so far has been the Global Precipitation Measurement Mission constellation (GPM; Hou et al., 2014). The GPM Core Observatory has provided over a

© 2025. The Author(s). This is an open access article under the terms of the Creative Commons Attribution License, which permits use, distribution and reproduction in any medium, provided the original work is properly cited.

JONES AND KUMMEROW

1 of 21


---



21698996, 2025, 4, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024JD043111 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU ADVANCING EARTH AND SPACE SCIENCES logo

# Journal of Geophysical Research: Atmospheres

10.1029/2024JD043111

decade of continuous active and passive microwave (PMW) observations from its Dual-frequency Precipitation Radar (DPR) and GPM Microwave Imager (GMI). However, the high latitudes poleward of 65° remain unsampled by the DPR, and light drizzle and snowfall rates below 0.25 mm/hr remain unobserved due to the DPR's Ka-band minimum detection threshold of ~12 dBZ (Schulte et al., 2022; Skofronick-Jackson et al., 2013).

PMW instruments are skillful at detecting absorption and scattering signals associated with clouds and precipitation, and many efforts have been made to produce robust retrievals of precipitation intensity from multichannel passive measurements (Kummerow, 2020). At the low precipitation rates common in the high latitudes, however, separating cloud water and drizzle with PMW-based retrievals is difficult due to their sensitivity only to the path-integrated absorption and lack of scattering signal due to small drop sizes (Berg et al., 2006; Stephens & Kummerow, 2007). The scattering associated with larger precipitation-sized particles can be used as a signal to infer precipitation, but this suffers from nonunique solutions (Weng, 2007). The Microwave Integrated Retrieval System (MiRS; Boukabara et al., 2011), a variational PMW retrieval scheme, uses this instability signal in order to assign hydrometeor water and ice content to the profile, but this can be unreliable at low precipitation rates (discussed further in Section 3.2). Hilburn and Wentz (2008) use an empirically derived relationship to assign precipitation water and cloud water based on the total water path retrieved from the PMW measurements. Without further observational constraint, data-driven methods such as these are necessary to produce PMW precipitation estimates that agree statistically with global climatology.

The method of combining active and passive observations together for a more physically based precipitation estimate has been the basis of the GPM Level 2B Combined Algorithm (GPM-CMB; Grecu et al., 2016), which uses coincident observations from both the DPR and GMI. The retrieved hydrometeor profile and resulting surface precipitation rate are forced to be radiatively consistent with both the observed radar profile and GMI brightness temperatures (Tbs). These GPM-CMB retrieved profiles also form the a priori database for GPM's passive-only scheme, the Bayesian Goddard Profiling Algorithm (Kummerow et al., 2015) as well as the training data for the latest machine-learning based version of GPROF (Pfreundschuh et al., 2022). However, since the DPR misses precipitation rates below 0.25 mm/hr and since the GPM-CMB algorithm relies on DPR echo to distinguish rain from cloud water, GPROF also lacks the ability to retrieve drizzle directly. Instead, GPROF retrieves light precipitation rates below the DPR's ability to detect via three mechanisms: (a) spatial averaging of the much smaller GPM-CMB profiles at the 5-km DPR resolution into the ~13 × 18 km GMI footprint in the database, (b) the Bayesian averaging of precipitation rates from raining and nonraining profiles simultaneously, and lastly (c) the addition of precipitation from the aforementioned MiRS retrievals on GMI observations over ocean (Pfreundschuh et al., 2024).

Compared to the DPR, the much more sensitive CloudSat's 94-GHz Cloud Profiling Radar (CPR; Stephens, 2002), designed to be optimally sensitive to clouds (typically down to -26 dBZ), has been shown to be successful in observing light rain and snow over ocean (Haynes et al., 2009). CloudSat's first operational precipitation algorithm, 2C-PRECIP-COLUMN (Haynes, 2018) as well as its subsequent improved products, 2C-RAIN-PROFILE (Lebsock, 2018) and 2C-SNOW-PROFILE (Wood & L'Ecuyer, 2018), retrieve light precipitation rates well below the DPR's capability to detect. This has led several authors to leverage CloudSat's capabilities to build global precipitation statistics from complementary radar estimates. Berg et al. (2010) used CloudSat rainfall estimates to conclude that GPM's predecessor, the Tropical Rainfall Measurement Mission Precipitation Radar (TRMM-PR) missed around 10% of the total accumulation over the tropical and subtropical oceans with the amount missed in the high latitudes remaining unknown. Behrangi et al. (2014) merged CloudSat rainfall estimates from the 2C-RAIN-PROFILE algorithm with those from the TRMM-PR to fill out the zonal distribution of rain that would be below the TRMM-PR detection threshold and to extend the distribution into the high-latitude oceans. The work of Behrangi and Song (2020) expanded this study into the GPM era and merged precipitation estimates from TRMM, GPM, and CloudSat in order to build a global precipitation climatology up to 81°N/S.

CloudSat has several drawbacks, however, including poor sampling due to its narrow beam width (~1.4 × 1.7 km), frequent echo saturation in the case of high humidity and cloud water content (Behrangi et al., 2012), surface echo contamination of radar bins above the surface (Christensen et al., 2013), and assumed particle size distribution (PSD) parameters (Schulte et al., 2022). Finally, as is the case with any radar-only retrieval but even more so at the CPR's 94 GHz operating frequency, attenuation of the radar beam by cloud water and water vapor must be constrained by ancillary data in order to get an estimate of the effective backscatter

JONES AND KUMMEROW

2 of 21


---



21698996, 2025, 4, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024JD043111 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU ADVANCING EARTH AND SPACE SCIENCES logo

# Journal of Geophysical Research: Atmospheres

10.1029/2024JD043111

signal (Haynes et al., 2007), leading to this being a source of additional uncertainty in the retrieval. Furthermore, all of the aforementioned studies rely on a radar-only estimate of the atmosphere and hydrometeor profile, and retrieved atmospheric states from radar estimates have no guarantee of physical consistency with any radiometer observations of the same scene.

Figure 1 shows high-latitude zonal mean estimates from some operational precipitation products, highlighting the disagreement in all precipitation rates (top two panels) and in light precipitation (lower two panels), even among CloudSat's operational precipitation algorithms. This also hints at the fact that light drizzle and snowfall are important for both the frequency of occurrence as well as the overall accumulations for these regions. This is in agreement with the seminal findings of Petty (1995) regarding the frequency of occurrence of light rain and more recently by (Klepp et al., 2018), who constructed accumulation statistics using shipborne disdrometer measurements from the Ocean Rainfall And Ice-phase precipitation measurement Network (OceanRAIN) field campaign with unprecedented sampling in the high-latitude oceans.

In this study, we consider light precipitation to be at or below 0.25 mm/hr, which corresponds with the DPR detection threshold.

In contrast to the many studies that incorporate CloudSat radar-only estimates, few attempts have been made to directly combine CPR observations with passive measurements for a more radiatively consistent answer. Duncan et al. (2018) used principal component analysis of CPR profiles to retrieve light warm rain by obtaining a solution that was physically consistent with coincident PMW observations from the Advanced Scanning Microwave Radiometer 2 (AMSR2) and the first EOF of radar reflectivity. Another CPR/AMSR warm rain retrieval, that by Eastman et al. (2019), approached the problem of light drizzle by exploiting the relationship between observed 89 GHz Tbs and rain rate estimates from 2C-RAIN-PROFILE. Focusing instead on ice particles, Pfreundschuh et al. (2022) combined airborne submillimeter radiometer measurements with CPR observations to successfully retrieve two parameters of particle distributions within ice clouds among other atmospheric state variables. In this study, we estimate both light drizzle and snow for the high-latitude oceans by directly combining CPR and AMSR2 observations scene-by-scene in order to obtain both drizzle and light snow estimates that are physically consistent with both sensors. Building on the previous works mentioned here, the use of combined observations allows the constraint of environmental variables simultaneously along with two parameters of the cloud and hydrometeor PSD. Hereafter, the combined AMSR2-CloudSat retrieval algorithm created for this study will be referred to as the A2CS algorithm. Section 2 outlines the data and methodology used in the retrieval, Section 3 shows the retrieval results, highlighting the benefits to using combined observations, and the paper concludes with Section 4, which contains a brief summary and discussion.

## 2. Methods and Algorithm Description

### 2.1. Domain of Study and Coincidence

For this study, we are interested in constraining the high-latitude drizzle intensity estimates over oceans. We therefore limit the retrievals and uncertainty estimations in the algorithm to poleward of and including 40° latitude. We use the period of observations from 1 January through 31 December 2015, since throughout this period, AMSR2, flying aboard the Global Change Observation Mission-Water satellite (GCOM-W1), and CloudSat shared the same orbital path in the A-Train (Stephens, 2002). This provides a continuous year of coincident AMSR2 and CPR observations with good coverage of the high latitudes due to their ~98° orbital inclination.

A common problem in radar-radiometer combined retrievals is the large spatial differences between the relatively small radar beam widths and the large radiometer pixel footprints. This issue is especially problematic in dealing with CloudSat data due to the large discrepancy between the CPR's ~1.4 × 1.7 km ground footprint compared with the ~14 × 22 km AMSR2 pixel footprint from the 18.7 GHz channel. Further complicating this issue is the 2D Gaussian nature of the radiometer pixel, which results in a nonlinear falloff of contribution to the measured radiance farther away from the pixel centroid. This mismatch in sampling volumes causes a large disparity between the frequency distributions of precipitation between CloudSat and other products as a direct result of the resolution dependency of precipitation observations. It is possible, however, to homogenize these sampling volumes at the statistical level by averaging the CPR observations along the orbital track. Although no unique solution to this method is known, there is a similar probability of precipitation between CloudSat and other

JONES AND KUMMEROW

3 of 21
3 of 21


---



21698996, 2025, 4, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024JD043111 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU ADVANCING EARTH AND SPACE SCIENCES logo

Journal of Geophysical Research: Atmospheres

10.1029/2024JD043111

# Zonal Mean Oceanic Precipitation

<table>
  <thead>
    <tr>
        <th colspan="18">Zonal Mean Oceanic Precipitation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td colspan="8">Northern Hemisphere</td>
        <td colspan="7">Southern Hemisphere</td>
        <td colspan="3"></td>
    </tr>
<tr>
        <td>Latitude</td>
<td>Ocean Fraction</td>
<td>CSAT 2C-RAIN</td>
<td>CSAT 2C-SNOW</td>
<td>CSAT 2C-PRECIP</td>
<td>2C-RAIN + 2C-SNOW</td>
<td>GPM 2B-Combined</td>
<td>GPROF OMI</td>
<td>ERA5</td>
<td>Latitude</td>
<td>Ocean Fraction</td>
<td>CSAT 2C-RAIN</td>
<td>CSAT 2C-SNOW</td>
<td>CSAT 2C-PRECIP</td>
<td>2C-RAIN + 2C-SNOW</td>
<td>GPM 2B-Combined</td>
<td>GPROF OMI</td>
<td>ERA5</td>
    </tr>
<tr>
        <td>80</td>
<td>0.1</td>
<td>0.5</td>
<td>0.8</td>
<td>1.3</td>
<td>1.3</td>
<td>0.4</td>
<td>0.2</td>
<td>0.6</td>
<td>-30</td>
<td>0.8</td>
<td>3.2</td>
<td>0.0</td>
<td>3.2</td>
<td>3.2</td>
<td>3.5</td>
<td>3.0</td>
<td>3.8</td>
    </tr>
<tr>
        <td>70</td>
<td>0.3</td>
<td>1.2</td>
<td>1.5</td>
<td>2.7</td>
<td>2.7</td>
<td>1.0</td>
<td>0.8</td>
<td>1.4</td>
<td>-40</td>
<td>0.9</td>
<td>3.5</td>
<td>0.1</td>
<td>3.6</td>
<td>3.6</td>
<td>3.8</td>
<td>3.2</td>
<td>4.2</td>
    </tr>
<tr>
        <td>60</td>
<td>0.4</td>
<td>2.5</td>
<td>1.0</td>
<td>3.5</td>
<td>3.5</td>
<td>2.2</td>
<td>1.8</td>
<td>2.8</td>
<td>-50</td>
<td>1.0</td>
<td>3.0</td>
<td>0.5</td>
<td>3.5</td>
<td>3.5</td>
<td>3.2</td>
<td>2.8</td>
<td>3.6</td>
    </tr>
<tr>
        <td>50</td>
<td>0.6</td>
<td>3.0</td>
<td>0.2</td>
<td>3.2</td>
<td>3.2</td>
<td>2.8</td>
<td>2.5</td>
<td>3.5</td>
<td>-60</td>
<td>1.0</td>
<td>2.5</td>
<td>1.2</td>
<td>3.7</td>
<td>3.7</td>
<td>2.8</td>
<td>2.2</td>
<td>3.2</td>
    </tr>
<tr>
        <td>40</td>
<td>0.7</td>
<td>3.5</td>
<td>0.0</td>
<td>3.5</td>
<td>3.5</td>
<td>3.2</td>
<td>3.0</td>
<td>4.0</td>
<td>-70</td>
<td>0.8</td>
<td>1.5</td>
<td>1.8</td>
<td>3.3</td>
<td>3.3</td>
<td>1.8</td>
<td>1.2</td>
<td>2.2</td>
    </tr>
<tr>
        <td>30</td>
<td>0.8</td>
<td>3.2</td>
<td>0.0</td>
<td>3.2</td>
<td>3.2</td>
<td>3.0</td>
<td>2.8</td>
<td>3.8</td>
<td>-80</td>
<td>0.2</td>
<td>0.5</td>
<td>2.0</td>
<td>2.5</td>
<td>2.5</td>
<td>0.8</td>
<td>0.5</td>
<td>1.2</td>
    </tr>
  </tbody>
</table>

# Zonal Mean Oceanic Precipitation ≤ 0.25 mm/hr

<table>
  <thead>
    <tr>
        <th colspan="6">Zonal Mean Oceanic Precipitation ≤ 0.25 mm/hr</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td colspan="3">Northern Hemisphere</td>
        <td colspan="3">Southern Hemisphere</td>
    </tr>
<tr>
        <td>Latitude</td>
<td>Ocean Fraction</td>
<td>Precipitation (mm/day)</td>
<td>Latitude</td>
<td>Ocean Fraction</td>
<td>Precipitation (mm/day)</td>
    </tr>
<tr>
        <td>80</td>
<td>0.1</td>
<td>0.25</td>
<td>-30</td>
<td>0.8</td>
<td>0.75</td>
    </tr>
<tr>
        <td>70</td>
<td>0.3</td>
<td>0.35</td>
<td>-40</td>
<td>0.9</td>
<td>0.85</td>
    </tr>
<tr>
        <td>60</td>
<td>0.4</td>
<td>0.65</td>
<td>-50</td>
<td>1.0</td>
<td>0.95</td>
    </tr>
<tr>
        <td>50</td>
<td>0.6</td>
<td>0.75</td>
<td>-60</td>
<td>1.0</td>
<td>1.05</td>
    </tr>
<tr>
        <td>40</td>
<td>0.7</td>
<td>0.85</td>
<td>-70</td>
<td>0.8</td>
<td>0.80</td>
    </tr>
<tr>
        <td>30</td>
<td>0.8</td>
<td>0.80</td>
<td>-80</td>
<td>0.2</td>
<td>0.40</td>
    </tr>
  </tbody>
</table>

**Figure 1.** Top two panels: zonal mean precipitation for Northern Hemisphere (left) and Southern Hemisphere (right) oceans from ECMWF Reanalysis 5, GPM Level 2B Combined Algorithm (version 7), Goddard Profiling Algorithm (version 7), and three operational CloudSat retrieval algorithms: 2C-RAIN-PROFILE, 2C-SNOW-PROFILE, and 2C-PRECIP-COLUMN (all version 5). All products were accumulated into a 1° × 1° grid in order to reduce the resolution dependency of these estimates and to make them more comparable, with ERA5 1-hr accumulations being kept at native resolution (shown for comparison purposes only). Bottom two panels: zonal mean estimates of drizzle by accumulating only precipitation rates less than or equal to 0.25 mm hr<sup>−1</sup>. Gray shading indicates ocean fraction as a function of latitude (top axis).

observational products if the averaging length is chosen to be much longer than the horizontal length of the radiometer footprint (Behrangi et al., 2012). Stephens et al. (2010) used TRMM-PR observations and model data to test the sensitivity of the frequency of occurrence to the 1D averaging length of radar data and found that a factor of 3 times the length of the 2D model gridbox area was optimal for the 1D averaging length but acknowledged that this becomes problematic when dealing with the spatial correlation of the observations. Forced

JONES AND KUMMEROW

4 of 21
4 of 21


---



21698996, 2025, 4, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024JD043111 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU ADVANCING EARTH AND SPACE SCIENCES logo

# Journal of Geophysical Research: Atmospheres

10.1029/2024JD043111

**Table 1**
Columns: Variables Used in the Retrieval, the First Guess Value (or the Origin of the First Guess), a Priori Uncertainty in Variance Space, and the Observational Instrument Primarily Sensitive to the Radiation Signal

<table>
  <thead>
    <tr>
        <th>Variable</th>
        <th>First guess</th>
        <th>A priori uncertainty (σ²)</th>
        <th>Observational sensitivity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>Sea Surface Temperature</td>
<td>From Reynolds SST</td>
<td>0.75 K²</td>
<td>AMSR2</td>
    </tr>
<tr>
        <td>Surface Wind Speed</td>
<td>From ERA5</td>
<td>4.0 m² s⁻²</td>
<td>AMSR2</td>
    </tr>
<tr>
        <td>Water Vapor EOF1</td>
<td>From SST-dependent mean profile</td>
<td>1.34</td>
<td>AMSR2</td>
    </tr>
<tr>
        <td>Water Vapor EOF2</td>
<td>N/A (see Section 2.3)</td>
<td> </td>
<td>N/A</td>
    </tr>
<tr>
        <td>Water Vapor EOF3</td>
<td>N/A</td>
<td> </td>
<td>N/A</td>
    </tr>
<tr>
        <td>Residual Cloud Water Path</td>
<td>10 g m⁻²</td>
<td>log₁₀(2.0) g² m⁻⁴</td>
<td>AMSR2</td>
    </tr>
<tr>
        <td>Liquid Precipitation Water Content</td>
<td>0.01 g m⁻³</td>
<td>2.0 g² m⁻⁶</td>
<td>both</td>
    </tr>
<tr>
        <td>Ice Water Content</td>
<td>0.01 g m⁻³</td>
<td>2.0 g² m⁻⁶</td>
<td>both</td>
    </tr>
<tr>
        <td>Gamma PSD shape parameter μ</td>
<td>1.5</td>
<td>0.5</td>
<td>both</td>
    </tr>
<tr>
        <td>Ice particle density</td>
<td>1.0 g cm⁻³</td>
<td>0.04 g² cm⁻⁶</td>
<td>both</td>
    </tr>
  </tbody>
</table>

to make a compromise between statistical congruence and spatial correlation in this scene-by-scene retrieval, we choose an averaging length of 30 km centered at the location of the AMSR2 pixel centroid. The implications of this assumption are examined later in this study.

## 2.2. Algorithm Overview

The method of optimal estimation (OE) is a physically constrained mathematical technique utilized in many retrieval algorithms in satellite remote sensing (Boukabara et al., 2011; Duncan & Kummerow, 2016; Lebsock & L’Ecuyer, 2011; Pfreundschuh et al., 2020; Schulte & Kummerow, 2019). A full mathematical treatment of OE can be found in numerous other works, including Rodgers (2000), so the discussion of OE here is kept brief. For this combined retrieval, the Level 1C cross-calibrated AMSR2 observed Tbs (Berg et al., 2016) and the coincident Level 2B CPR reflectivity profiles (Marchand et al., 2008) comprise the observation vector.

The state vector consists of the vertical profile of liquid and ice hydrometeor contents, cloud water path, water vapor, the adjustable PSD parameters (defined in Table 1 and discussed further in Section 2.5), and the surface variables to be retrieved—namely, sea surface temperature (SST) and ocean surface wind speed. The remaining ancillary data are necessary for physical forward model simulations and are read in a priori, but they are not modifiable in the retrieval. These come from the ECMWF Reanalysis 5 (ERA5; Hersbach et al., 2020) and consist of the atmospheric temperature and pressure profile. The assumption of a fixed temperature profile from an ancillary source is necessary when using a radiometer that does not contain temperature sounding channels (Duncan & Kummerow, 2016), but these errors are considered to be minimal. Uncertainties that might arise from this assumption, however, are addressed in the nondiagonal **S<sub>y</sub>** matrix discussed further in Section 2.4. The sea surface salinity is also fixed at 35.0 psu, since the sensitivity to the simulated Tbs at AMSR2 frequencies to varying sea surface salinity between 33.0 and 36.0 psu was found to be less than 0.4 K for all channels. ERA5 also provides the first guess on several variables except for SST, which comes from Reynolds SST (Reynolds et al., 2007). A list of retrieved variables and their a priori uncertainties is given in Table 1.

An additional consideration in a combined retrieval is the asymmetric weighting of the fit of the radar profile and the fit of the Tbs between simulated and observed measurements. It is common for the radar profile to dominate OE convergence due to the imbalance between the large number of radar range gates and the much smaller number of radiometer channels. This issue is addressed in two ways. First, averaging the radar reflectivities from the CPR's native resolution of 240–500 m per range bin reduces the number of radar bins from 125 per profile to 30 extending from the surface to 15 km. This also helps to reduce the accumulation of noise in the forward model that could occur by tracing scattering and absorption through too many atmospheric layers given the information content of the sensors. The second way is by utilizing an observational error covariance matrix that includes the estimations of cross-correlated errors between each element of **y** (described in Section 2.4).

JONES AND KUMMEROW

5 of 21



---


21698996, 2025, 4, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024JD043111 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU ADVANCING EARTH AND SPACE SCIENCES logo

# Journal of Geophysical Research: Atmospheres

10.1029/2024JD043111

## 2.3. Forward Model

The forward radiative transfer model used to simulate both passive and active microwave observations in the A2CS algorithm is built on previous works (Duncan & Kummerow, 2016; Schulte et al., 2022, 2023; Schulte & Kummerow, 2019, 2022). Passive microwave radiances for each frequency and polarization measured by AMSR2 are simulated using the FAST microwave Emissivity Model version 6 (FASTEM6; Liu et al., 2011) and the Eddington two-stream approximation (Kummerow, 1993050<1377:OTSTOT>2.0.CO;2)). Both ice and liquid hydrometeor scattering are simulated using Mie scattering codes. Radar reflectivity factors are calculated directly from the PSDs to ensure consistency between the passive and active simulations, and they are adjusted for attenuation by hydrometeors and water vapor at each vertical level. Forward-model-derived CloudSat radar simulations were evaluated for accuracy by comparing to QuickBeam (Haynes et al., 2007) CPR simulations offline.

## 2.4. Uncertainty Estimation

The construction of the error covariance matrices, **S<sub>a</sub>** and **S<sub>y</sub>**, is not straightforward and no unique solution for estimating their values is known to exist. We use a method similar to DK16 for the estimation of **S<sub>y</sub>**, and we assume diagonality for **S<sub>a</sub>**. The diagonal elements of **S<sub>a</sub>** essentially describe the variance of the departure of the retrieved state elements from the first guess, and since the true state is unknown beforehand, the problem is not well-posed. We therefore choose reasonable values for the variances of **S<sub>a</sub>**, and we assume that the cross-covariances between the elements of **x** are sufficiently low that diagonality is a good approximation.

The construction of **S<sub>y</sub>**, however, is very important to the final fit of the retrieval to both sets of observations and therefore requires more careful attention. **S<sub>y</sub>** encompasses the uncertainty in the measurements and in the forward model together forming the total observational uncertainties. The measurement uncertainties are given in terms of the noise equivalent differential temperature of the radiometer and the calibration error of the radar and are relatively small. The overall magnitudes of the observational uncertainties are driven by assumptions necessary in the forward model computations. These errors are much larger and must be accurately estimated in order for the retrieval to converge on physically realistic states.

In order to estimate the uncertainties in both passive and active observations simultaneously, we simulate the departure from the true profile that a successful retrieval would produce. Atmospheric profiles from ERA5 of temperature, pressure, humidity, and cloud and hydrometeor content are averaged and interpolated from their native resolution of 27 pressure levels between 1,000 and 1100 hPa to 30 layers of 500 m each between the surface and 15 km to emulate the vertical resolution of the retrieval. The cloud water, cloud ice, and liquid and frozen hydrometeor contents are given in the ERA5 profiles, and PSD parameters are randomly assigned using the models described in Section 2.5. These profiles represent the "true" profiles, and they are forward modeled to simulate the "error-free" observations. To maintain the sensitivity of **S<sub>y</sub>** to the high-latitude ocean regime, only profiles over ocean and poleward of and including ±40° latitude are considered.

The same profiles are then reconstructed in the format as used by the retrieval. For water vapor, this means deconstructing the ERA5 water vapor profile and reconstructing it according its first three EOFs. In DK16, retrieving water vapor in EOF space was found to successfully constrain the vertical profile in the presence of clouds. In their study, the vertical resolution of water vapor from the number of well-retrieved EOF coefficients used to reconstruct the profile depended on the number of channels measured that were sensitive to water vapor emission. This technique was originally applied to GMI, and three EOFs were found to be well-retrieved due to its high-frequency sounding channels. However, since AMSR2's water vapor sensitivity lies primarily in the two 23 GHz channels, we find that the first EOF, directly related to the total precipitable water (TPW), is all that can be skillfully retrieved in the presence of clouds and precipitation.

Adding noise to the temperature profile attempts to account for the departure of ERA5 from the unknown "true" profile. The noise added to the temperature profile is drawn from a Gaussian distribution with an uncertainty taken to be the DK16 value of 2 K. ERA5 cloud water contents are integrated and redistributed evenly between the cloud base and the freezing level, which is the same process the algorithm uses for vertically distributing cloud water that does not contribute to the precipitation content (see Section 2.5 for more detail). We further assume that the forward-model uncertainties caused by liquid and ice hydrometeor scattering increases with the amount present. A scaled noise is added to the hydrometeor contents as $\rho_{hyd,retr} = \rho_{hyd,ERA}(1 + \epsilon)$, where $\epsilon$ is a random noise value drawn from a Gaussian distribution with a standard deviation taken to be 0.03 g m<sup>−3</sup>. Finally, PSDs

JONES AND KUMMEROW

6 of 21


---


21698996, 2025, 4, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024JD043111 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU ADVANCING EARTH AND SPACE SCIENCES logo

# Journal of Geophysical Research: Atmospheres

10.1029/2024JD043111

Observational error covariance matrices for clear, cloudy, and precipitating scenes

Figure 2. Observational error covariance matrices for clear (left), cloudy (center), and precipitating (right) scenes. Errors are plotted using the signed square root of the variances in K for the AMSR2 channels and in dB for the radar height bins.

are remodeled by randomly reassigning moveable parameters $\mu$ and $\rho_{ice}$ within their retrieval bounds and by randomly varying the fixed a priori parameters ($N_{0,liq}$ and $N_{0,ice}$) by one order of magnitude in either direction to attempt to approximate the effect of using any fixed PSD model and its variance from the "true" (natural) PSD. The resulting profiles are again forward modeled, and the difference between the two sets of simulated observations, $\mathbf{y}_{sim,ERA5} - \mathbf{y}_{sim,retr}$ is deemed the "error." To calculate the elements of $\mathbf{S_y}$, we simply calculate the covariance of $\mathbf{Y}_{sim,ERA5} - \mathbf{Y}_{sim,retr}$, where $\mathbf{Y}$ is a matrix of dimensions [m x n], with m being the sampling dimension and n being the number of elements in $\mathbf{y}$ (Figure 2).

As stated before, estimating $\mathbf{S_y}$ as accurately as possible is paramount to producing successful and accurate retrievals. A degradation in retrieval quality is found when $\mathbf{S_y}$ is ill-suited for describing the errors in a given scene—for example, including error contributions based on highly uncertain ice scattering in the scene when there are no clouds present. We therefore allow the algorithm to use a different version of $\mathbf{S_y}$ based on whether the scene is predetermined to be clear, cloudy, or precipitating. This predetermination is a unique feature of using passive and active observations together, since we could not make such a discrimination uniquely using only passive observations. The scene is determined to be clear when all CPR reflectivities are at or below $-26$ dBZ. Scenes are determined to be cloudy, but not precipitating, when the CloudSat along-track averaged surface precipitation rate (a combination of 2C-RAIN-PROFILE and 2C-SNOW-PROFILE for the best estimates) for the AMSR2 pixel is below $0.01\text{ mm hr}^{-1}$, and scenes are considered to be precipitating when it is above or equal to this threshold. The only function of this predetermination between precipitating and cloud-only scenes is to allow the algorithm to use the most appropriate version of $\mathbf{S_y}$, and no further constraint is made to produce an appreciable precipitation rate on any scene; this allows a smooth transition in the retrieval statistics between the cloudy and drizzling regimes.

The last form of uncertainty to consider exists in the form of the posterior, or retrieval, uncertainty. This uncertainty, a scalar value, is directly estimated at retrieval time for each retrieved state and expressed in terms of the square root of the variance, or standard deviation, of the final solution:

$$ \sigma = \left( \mathbf{S}_a^{-1} + \mathbf{K}^T \mathbf{S}_y^{-1} \mathbf{K} \right)^{-0.5} \tag{1} $$

This uncertainty metric is generally valid for physical parameters that are understood to be approximately Gaussian in nature, such as SST and wind speed, but fails to capture the true retrieval uncertainty in any meaningful way if the problem is non-Gaussian. Rain and snow water content as well as cloud water and ice are extremely non-Gaussian and vary widely in their natural distributions. Therefore, the posterior uncertainties for these quantities are not a good estimate of the true retrieval uncertainty, and these are considered instantaneous random errors that generally disappear in zonal accumulations. More important to climatology, however, are errors that arise from the retrieval methodology itself, but these are difficult to estimate (Petković et al., 2023).

JONES AND KUMMEROW

7 of 21


---



21698996, 2025, 4, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024JD043111 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU ADVANCING EARTH AND SPACE SCIENCES logo

# Journal of Geophysical Research: Atmospheres

10.1029/2024JD043111

## 2.5. Cloud and Hydrometeor PSD Models

### 2.5.1. Clear Retrievals

Scenes are determined to be clear whenever the CPR reflectivity profile shows all bins at or below the algorithm's assumed noise floor of −26 dBZ. Although the scene is nominally clear, there may be some cloud water that is undetectable by the radar due to small drop sizes but may be contributing emission signals to the passive measurements and to the attenuation of the radar beam. With no appreciable backscatter signal, this cloud water is modeled as monodisperse with all cloud droplet diameters taken to be a single value, D<sub>cld</sub>. We tested the sensitivity of the simulated Tbs to the choice of D<sub>cld</sub> by modeling liquid cloud water in varying amounts from 0.05 to 0.25 g m<sup>−3</sup> and with varying values of D<sub>cld</sub> from 10 to 100 μm. The larger drop sizes tested are well into the size regime that would be detectable by the CPR, but we found that there is no appreciable effect on the top-of-atmosphere microwave radiances from the choice of D<sub>cld</sub> between these bounds. Therefore, it is taken to be 10 μm. Due to a lack of any vertical sensitivity in the passive measurements, cloud water is then evenly distributed between the freezing level and the surface bin. Retrieved residual cloud water paths in clear scenes are low and are most often less than 0.02 mm.

### 2.5.2. Cloudy Retrievals

Scenes are determined to be cloudy and not precipitating whenever CPR reflectivities are above the noise floor, but the 30 km along-track averaged CloudSat precipitation rate is less than 0.01 mm hr<sup>−1</sup>. Since there is signal in this case for both the cloud water path from the radiometer and the particle sizes from the radar, the algorithm distributes cloud water or cloud ice according to a prescribed PSD. In this combined algorithm, we assume no fundamental difference in the PSD model (only that the parameters can change) before and after drizzle onset. The liquid PSD is modeled as a nonnormalized gamma distribution:

$$n(D) = N_{0,liq}D^{\mu} \exp(-\Lambda D)$$ (2)

where n(D) is the number concentration, in m<sup>−3</sup> mm<sup>−1</sup>, of drops at diameter D, N<sub>0,liq</sub> is the intercept parameter, μ is the shape parameter, which is allowed to vary between 0 and 2.5, and Λ is the slope parameter in mm<sup>−1</sup>. In the algorithm μ and the rain water content are retrievable, whereas N<sub>0,liq</sub> is fixed at $1.1 \times 10^{5} \text{ m}^{-3} \text{ mm}^{-\mu}$. This value for N<sub>0,liq</sub> was derived from an analysis of high-latitude drizzle in situ observations from OceanRAIN, and the combination of this value along with varying μ was determined to be flexible enough to capture the natural variability of drizzle PSDs. This is illustrated in Figure 3.

In cloudy and precipitating retrievals, there is often a small amount of residual cloud water that is needed to correctly simulate the absorption and emission throughout the atmospheric column that is either not captured by the liquid PSD or that does not contribute to the radar reflectivities. This cloud water is also modeled as monodisperse with the same value for D<sub>cld</sub> as in the clear case, and it is vertically evenly distributed between the freezing level and the cloud base. This monodisperse residual cloud water is used here to mimic CloudSat's 2C-RAIN-PROFILE algorithm that accounts for some attenuation of the radar beam and that is also not part of the hydrometeor PSD (Lebsock, 2018). In 2C-RAIN-PROFILE, the cloud water amount is constrained to be a function of the surface rain rate. In the A2CS algorithm, the residual cloud water path is retrievable and is always small. More than 96% of cloudy retrievals were found to have retrieved residual cloud water paths of less than 0.2 mm, which corresponds to ~15% probability of drizzle using along-track averaged CloudSat radar-only estimates.

Both precipitation and cloud ice particles are modeled as spherical for radiative transfer computations and are distributed according to a simple inverse exponential PSD:

$$n(D) = N_{0,ice} \exp(-\Lambda D)$$ (3)

where N<sub>0,ice</sub> is the intercept parameter, derived from in situ observations of high-latitude oceanic snow (again from OceanRAIN), and is fixed at 5,100 mm<sup>−1</sup> m<sup>−3</sup>. The inverse exponential PSD has been shown to be effective in capturing both cloud ice and snow particles to correctly simulate W-band radar observations (Liu, 2008), and it is additionally consistent with aircraft observations of snow clouds (Heymsfield et al., 2008). Unlike liquid drops,

JONES AND KUMMEROW

8 of 21


---



21698996, 2025, 4, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024JD043111 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU ADVANCING EARTH AND SPACE SCIENCES logo

Journal of Geophysical Research: Atmospheres

10.1029/2024JD043111

<table>
  <thead>
    <tr>
        <th colspan="3">Rain Rate PSD Observations and Model Fits</th>
    </tr>
<tr>
        <th>Rain Rate Bin [mm/h]</th>
        <th>Fit 1 (Red Line)</th>
        <th>Fit 2 (Yellow Line)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>0.0 - 0.05</td>
<td>N₀ = 110000, μ = 2.5, Λ = 12.0</td>
<td>N₀ = 110000, μ = 0.0, Λ = 6.3</td>
    </tr>
<tr>
        <td>0.05 - 0.1</td>
<td>N₀ = 110000, μ = 2.5, Λ = 12.0</td>
<td>N₀ = 110000, μ = 0.0, Λ = 6.3</td>
    </tr>
<tr>
        <td>0.1 - 0.15</td>
<td>N₀ = 110000, μ = 2.5, Λ = 12.0</td>
<td>N₀ = 110000, μ = 0.0, Λ = 6.3</td>
    </tr>
<tr>
        <td>0.15 - 0.2</td>
<td>N₀ = 110000, μ = 2.5, Λ = 12.0</td>
<td>N₀ = 110000, μ = 0.0, Λ = 6.3</td>
    </tr>
<tr>
        <td>0.2 - 0.25</td>
<td>N₀ = 110000, μ = 2.5, Λ = 12.0</td>
<td>N₀ = 110000, μ = 0.0, Λ = 6.3</td>
    </tr>
<tr>
        <td>0.25 - 0.3</td>
<td>N₀ = 110000, μ = 2.5, Λ = 12.0</td>
<td>N₀ = 110000, μ = 0.0, Λ = 6.3</td>
    </tr>
<tr>
        <th colspan="3">Snow Rate PSD Observations and Model Fits</th>
    </tr>
<tr>
        <th>Snow Rate Bin [mm/h]</th>
        <th>Fit 1 (Red Line)</th>
        <th>Fit 2 (Yellow Line)</th>
    </tr>
<tr>
        <td>0.0 - 0.05</td>
<td>N₀ = 5100, Λ = 4.0</td>
<td>N₀ = 5100, Λ = 1.2</td>
    </tr>
<tr>
        <td>0.05 - 0.1</td>
<td>N₀ = 5100, Λ = 4.0</td>
<td>N₀ = 5100, Λ = 1.2</td>
    </tr>
<tr>
        <td>0.1 - 0.15</td>
<td>N₀ = 5100, Λ = 4.0</td>
<td>N₀ = 5100, Λ = 1.2</td>
    </tr>
<tr>
        <td>0.15 - 0.2</td>
<td>N₀ = 5100, Λ = 4.0</td>
<td>N₀ = 5100, Λ = 1.2</td>
    </tr>
<tr>
        <td>0.2 - 0.25</td>
<td>N₀ = 5100, Λ = 4.0</td>
<td>N₀ = 5100, Λ = 1.2</td>
    </tr>
<tr>
        <td>0.25 - 0.3</td>
<td>N₀ = 5100, Λ = 4.0</td>
<td>N₀ = 5100, Λ = 1.2</td>
    </tr>
  </tbody>
</table>

**Figure 3.** 5‐min averaged PSD observations from OceanRAIN shipborne ODM disdrometers for high‐latitude oceans. Color from blue to green indicates increasing density of observations. Also plotted are two extreme fits of the PSD models used in the algorithm to show sufficient flexibility to capture these observed PSDs.

JONES AND KUMMEROW

9 of 21


---


21698996, 2025, 4, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024JD043111 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU ADVANCING EARTH AND SPACE SCIENCES logo

# Journal of Geophysical Research: Atmospheres

10.1029/2024JD043111

however, an additional factor that must be considered that is radiatively important in the microwave spectrum is the ice particle density. Ice particle density strongly affects microwave scattering and is a retrievable variable in this algorithm along with the ice water content. The slope parameter $\Lambda$ is then constrained by the ice water content and is calculated as

$$ \Lambda = \left( \frac{N_{0,ice} \rho_{ice}}{IWC} \pi \right)^{\frac{1}{4}} \tag{4} $$

## 2.5.3. Precipitating Retrievals

A precipitating retrieval is performed on scenes where the CloudSat along-track mean precipitation rate is greater than or equal to 0.01 mm hr<sup>−1</sup>. Liquid and solid precipitation particles are modeled according to the PSDs described above with the additional step of calculating a liquid and solid precipitation rate for each bin. The precipitation rate for liquid drops is:

$$ R_{liq} = \int_{D_{min}}^{D_{max}} n_{liq}(D) V(D) v(D) dD \tag{5} $$

where $n_{liq}(D)$ is the number concentration of drops at diameter $D$, given by the PSD, $V(D)$ is the volume, and $v(D)$ is the terminal velocity of individual rain drops, calculated according to Equation 1 of Villermaux and Eloi (Villermaux & Eloi, 2011). For snow, a similar scheme is implemented, but the liquid equivalent precipitation rate follows from the liquid equivalent volume of the snow particles, or

$$ R_{ice} = \int_{D_{min}}^{D_{max}} n_{ice}(D) \frac{m_{ice}(D)}{\rho_l} v(D) dD \tag{6} $$

where $m_{ice}$ is the mass of the ice particles at diameter $D$, and $\rho_l$ is the density of liquid water. The terminal velocity of snow particles is difficult to estimate directly and can be parameterized in many different ways (Matrosov, 1998). We use the parameterization $v(D) = 8.8 \sqrt{D(\rho_{ice} - \rho_{air})}$, valid in the DPR algorithm for snow particles with densities between 0.05 g cm<sup>−3</sup> and 0.3 g cm<sup>−3</sup> (Iguchi et al., 2021). Ice particle density values allowable in the retrieval range from aggregate-like (0.05 g cm<sup>−3</sup>) to graupel-like (0.4 g cm<sup>−3</sup>) and have a strong effect on the liquid equivalent precipitation rate. Thus, having combined-observational constraints on the retrieval of ice particle density produces precipitation rates that are consistent with both sets of observations.

In some situations, complete attenuation of the radar beam or surface clutter makes determining the cloud base height from the CPR profile difficult (Lamer et al., 2020). Therefore, ERA5 cloud base heights are assumed for the precipitating profiles, and the bin above the bin containing the cloud base is considered the lowest "good" precipitating radar bin. Residual cloud water, however, is allowed to extend into the bin that contains the cloud base but does not contribute to the precipitation rate. This process improves convergence in the radar profile and is very effective in reducing the number of profiles contaminated with unresolved surface clutter, which can be the source of inflated precipitation rates in CloudSat. The precipitation water content in this bin is copied into each bin below the cloud base to the surface so that it can contribute to the total water path necessary to properly simulate the passive observations, and the precipitation rate from this bin is considered the surface precipitation rate. The radar uncertainties are also adjusted to a nominally high value below the cloud base bin in order to keep the algorithm from penalizing precipitation in the blind zone. If ERA5 cloud base is not available—e.g., if ERA5 shows no cloud in the profile but the CPR reflectivity indicates the presence of a cloud, then the cloud base derived from the CPR, found by assessing when the reflectivity drops below −26 dBZ, is used.

The freezing level, taken from ERA5, determines the phase of precipitation at the surface. If the bin that contains the freezing level is the surface bin, or if the freezing level is below the surface, the precipitation is retrieved as snow or graupel. Similarly, if the freezing level bin is above the surface bin, the precipitation rate is calculated as rain. In the current version of the algorithm, all surface precipitation is either classified as rain or snow, and there is no mixed-phase precipitation, but an important finding of Klepp et al. (2018) was that mixed-phase precipitation contributed to as little as 0.5% of the total accumulation over oceans. The presence of supercooled cloud

JONES AND KUMMEROW

10 of 21


---



21698996, 2025, 4, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024JD043111 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU ADVANCING EARTH AND SPACE SCIENCES logo

Journal of Geophysical Research: Atmospheres

10.1029/2024JD043111

<table>
  <thead>
    <tr>
        <th>Path (mm)</th>
        <th>10V</th>
        <th>10H</th>
        <th>18V</th>
        <th>18H</th>
        <th>23V</th>
        <th>23H</th>
        <th>36V</th>
        <th>36H</th>
        <th>89V</th>
        <th>89H</th>
        <th>W band</th>
    </tr>
<tr>
        <th colspan="12">Left Panel: Liquid Water Path</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>0.0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>-8</td>
    </tr>
<tr>
        <td>0.1</td>
<td>2</td>
<td>3</td>
<td>5</td>
<td>8</td>
<td>10</td>
<td>15</td>
<td>18</td>
<td>25</td>
<td>45</td>
<td>55</td>
<td>12</td>
    </tr>
<tr>
        <td>0.2</td>
<td>4</td>
<td>6</td>
<td>10</td>
<td>15</td>
<td>18</td>
<td>28</td>
<td>32</td>
<td>45</td>
<td>58</td>
<td>75</td>
<td>20</td>
    </tr>
<tr>
        <td>0.3</td>
<td>6</td>
<td>9</td>
<td>15</td>
<td>22</td>
<td>25</td>
<td>40</td>
<td>45</td>
<td>62</td>
<td>60</td>
<td>85</td>
<td>24</td>
    </tr>
<tr>
        <td>0.4</td>
<td>8</td>
<td>12</td>
<td>20</td>
<td>28</td>
<td>32</td>
<td>50</td>
<td>55</td>
<td>75</td>
<td>58</td>
<td>92</td>
<td>26</td>
    </tr>
<tr>
        <td>0.5</td>
<td>10</td>
<td>15</td>
<td>25</td>
<td>35</td>
<td>38</td>
<td>60</td>
<td>65</td>
<td>85</td>
<td>55</td>
<td>98</td>
<td>28</td>
    </tr>
<tr>
        <td>0.6</td>
<td>12</td>
<td>18</td>
<td>30</td>
<td>42</td>
<td>45</td>
<td>70</td>
<td>75</td>
<td>95</td>
<td>52</td>
<td>100</td>
<td>30</td>
    </tr>
<tr>
        <th colspan="12">Right Panel: Ice Water Path</th>
    </tr>
<tr>
        <td>0.0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>-8</td>
    </tr>
<tr>
        <td>0.1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>-1</td>
<td>-1</td>
<td>0</td>
    </tr>
<tr>
        <td>0.2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>-2</td>
<td>-2</td>
<td>3</td>
    </tr>
<tr>
        <td>0.3</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>-3</td>
<td>-3</td>
<td>5</td>
    </tr>
<tr>
        <td>0.4</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>-4</td>
<td>-4</td>
<td>6</td>
    </tr>
<tr>
        <td>0.5</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>-5</td>
<td>-5</td>
<td>7</td>
    </tr>
<tr>
        <td>0.6</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>-6</td>
<td>-6</td>
<td>8</td>
    </tr>
  </tbody>
</table>

Figure 4. Change in Tb as a function of liquid water path (left panel) and ice water path (right panel) for AMSR2 channels calculated using example high‐latitude profiles from ERA5 and an assumed 1–2 km cloud. TPW is 6 and 13 mm for the ice and liquid cases, respectively. Also shown is cloud top reflectivity for the CPR operating frequency (right axis). Upper limit of 0.6 mm corresponds to an approximate 90% probability of precipitation using 30‐km CloudSat estimates.

water, however, is globally important (Hu et al., 2010; Listowski et al., 2019), and the algorithm's forward model is able to model absorption by supercooled liquid. It is assumed that supercooled liquid is more common than ice near the freezing level, therefore all cloud and hydrometeor particles are considered liquid within the layer containing the freezing level. In reality, however, supercooled liquid can exist well above the freezing level at very cold temperatures especially in the pristine conditions of the Southern Ocean (Wu et al., 2021). In these situations, some retrieval errors are possible due to the suppression of the scattering signal by supercooled liquid absorption, but it is assumed that this is not a common occurrence.

## 2.6. Sensitivity Testing

To assess the dependency of retrievals on the assumptions necessary in the algorithm, several sensitivity tests were performed. As mentioned before, the along‐track averaging of CPR reflectivities is necessary to create approximately equivalent sampling between the radiometer and the radar. In addition to the 30‐km averaging length assumed in the retrieval, we also tested a 15‐km and 45‐km averaging length to get a sense of the dependence of the precipitation accumulations on the averaging length. We found a 5.0% decrease in mean precipitation for a month of retrievals when using a 15‐km averaging length compared to the assumed 30‐km averaging length. Similarly, using a 45‐km averaging length showed an increase of 3.4%. This suggests that the bulk statistics are not overly sensitive to the averaging length to within a reasonable value based on the along‐track radiometer field of view (FOV) length.

Inhomogeneities in the FOV are an additional potential source of retrieved precipitation rate uncertainty. Nonuniform beamfilling (NUBF) is a well‐known source of underestimation in both radar and PMW retrievals at the climate scale (Kummerow, 1998037<0356:ABFCFT>2.0.CO;2); Schulte et al., 2023). Although a full characterization of and a correction for NUBF errors is beyond the scope of this study, a simple synthetic retrieval was performed to get a first‐order estimate of how sensitive these precipitation retrievals might be to an inhomogeneous cloud field. We hypothesized that the sensitivity of the retrieval to NUBF might not be as great for drizzle as it would be for higher rain rates and cloud water contents. Figure 4 shows the relatively linear behavior of the AMSR2 Tbs in this regime with the notable exception of 89H for liquid water. The CPR reflectivities show extremely nonlinear behavior in both liquid and ice, but the saturation effect due to the liquid water attenuation is not as prominent in ice clouds, which form the majority of cloud observations in this domain.

To test the retrieval sensitivity to NUBF, an inhomogeneous cloud field was created by filling a synthetic AMSR2 pixel with an assumed 1–2 km liquid cloud that increased in cloud water content horizontally across the FOV from 0.025 to 0.05–0.1 g m<sup>−3</sup>, each occupying one‐third of the scene. Radar observations were simulated at the 1‐km radar resolution and averaged along the orbital track through the scene to produce the 30‐km radar observation. The "observed" Tbs for this scene were created using a 2D Gaussian weighted average of the Tbs simulated at the

JONES AND KUMMEROW

11 of 21
11


---



21698996, 2025, 4, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024JD043111 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU ADVANCING EARTH AND SPACE SCIENCES logo

# Journal of Geophysical Research: Atmospheres

10.1029/2024JD043111

radar resolution across the AMSR2 FOV for this scene. The mean radar precipitation rate for the inhomogeneous cloud field was determined to be 0.22 mm hr<sup>−1</sup>. A combined retrieval was then performed on these simulated observations and produced a precipitation rate of 0.28 mm hr<sup>−1</sup>. We compared this answer to a retrieval using a homogeneous cloud field that completely filled the FOV with the effective cloud water content as "observed" by the radiometer—a 2D Gaussian weighted average cloud water content of 0.056 g m<sup>−3</sup>. Once again, both radar and radiometer observations were simulated for this scene and the subsequent retrieval resulted in a precipitation rate of 0.27 mm hr<sup>−1</sup>. This test is far from a full investigation into NUBF errors, but the results of this simple experiment seem to indicate that the radiometer is largely able to correct for the NUBF from the radar because of the linear relationships in this portion of the cloud and precipitation water Tb space.

The assumption of spherical ice particles is usually unphysical in reality, but it is common in many operational retrieval algorithms, including GPM-CMB (Iguchi et al., 2021). Fully parameterizing the radiative effects of different particle shapes is beyond the scope of this study, but it is likely that snowfall estimates are sensitive to them. The main sensitivity to these signals are at higher frequencies, such as the 89 GHz AMSR2 channels and the 94 GHz CPR operating frequency, for which particle orientation is also currently thought to modify scattering parameters (Brath et al., 2020). These effects, however, as well as multiple scattering for these frequencies only become important at large particle sizes and generally at heavier precipitation rates (Haynes et al., 2009) that are beyond the drizzle size regime focused on in this study.

# 3. Results

## 3.1. Retrieval Validation

As already mentioned, validation over oceans, especially in the high latitudes, is challenging due to the relatively small number of retrieval matchups with sparse in situ observations. This makes establishing a "truth" data set difficult if not impossible. We can, however, compare the AMSR2-CloudSat combined retrieval (A2CS) to other independent and well-validated retrievals. Here, we present comparisons with Remote Sensing Systems (RSS) (Wentz et al., 2014), since we can directly compare A2CS to RSS AMSR2 retrievals of SST, water vapor, and surface wind speed for clear and cloudy scenes. Additionally, a relatively small number of coincident CloudSat overpasses for the period of study shows that the algorithm validates well against buoy and ship observations.

Initial comparisons showed excellent correlation but relatively large biases in surface variables when compared with in situ observations and RSS. We attributed this to biases in the forward model simulations of AMSR2 Tbs causing the retrieval to converge on biased states. We initially suspected emissivity calculations, since the biases were present in both clear and cloudy scenes, but this would be difficult to separate from any other type of forward model or sensor bias. This was addressed using offsets applied to the observed Tb vector before its ingestion into the algorithm. This algorithm-specific calibration is sometimes used in operational PMW ocean surface retrievals, including RSS (Gentemann & Hilburn, 2015), to improve validation against in situ data. To get sufficient sampling, again a challenge in this domain, we estimated the Tb offsets using an independent sensor, GMI, and by comparing the retrieved surface variables from the A2CS algorithm in clear scenes to RSS GMI (Wentz et al., 2015). Using an independent, well-calibrated radiometer helps ensure that the forward model biases can be isolated from the sensor information content. Tuning the offsets to compare well against RSS ensures good comparisons with in situ observations with better sampling than using in situ data alone. The offsets are adjusted until the retrieved surface variables are unbiased with respect to RSS GMI, indicating that the forward model bias has been correctly accounted for. These same offsets calculated from RSS GMI are applied to the AMSR2 channels that correspond to GMI channels, and the offset for the 23.8 GHz horizontally polarized channel (23H) is adjusted until retrievals of integrated water vapor aligns well with RSS AMSR2. The implementation of these Tb offsets, relatively small for all channels except for 23H (for which there is no GMI analog), resulted in much better comparisons with in situ surface observations and with RSS water vapor both in clear and cloudy scenes.

As seen in Figure 5, some consistent biases in wind speed seem to remain. These are most likely due to differing surface emissivity models between A2CS, which again uses FASTEM6 (Liu et al., 2011) and RSS AMSR2. At higher wind speeds (greater than 7.5 m s<sup>−1</sup>), the increasing drift in correlation means that higher wind speeds than are observed are needed by the forward model to simulate the correct surface emissivity. This is likely due to the presence of ocean surface foam in the scene, which can cause more uncertainty in the absolute values. The result is that any retrieved wind speed above 7.5 m s<sup>−1</sup> must be treated as an effective wind speed that is nearly always

JONES AND KUMMEROW

12 of 21


---



AGU ADVANCING EARTH AND SPACE SCIENCES logo

Journal of Geophysical Research: Atmospheres

10.1029/2024JD043111

21698996, 2025, 4, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024JD043111 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

<table>
  <thead>
    <tr>
        <th colspan="5">A2CS Retrievals of Surface Parameters</th>
    </tr>
<tr>
        <th>Scene Type</th>
        <th>Comparison Source</th>
        <th>Parameter 1: SST [K]</th>
        <th>Parameter 2: Water Vapor [mm]</th>
        <th>Parameter 3: Wind Speed [m/s]</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>Clear Scene</td>
<td>RSS AMSR2</td>
<td>Scatter Plot (Panel 1)</td>
<td>Scatter Plot (Panel 2)</td>
<td>Scatter Plot (Panel 3)</td>
    </tr>
<tr>
        <td>Clear Scene</td>
<td>SeaFlux (Buoy/Ship)</td>
<td>Scatter Plot (Panel 4)</td>
<td> </td>
<td>Scatter Plot (Panel 5)</td>
    </tr>
<tr>
        <td>Cloudy Scene</td>
<td>RSS AMSR2</td>
<td>Scatter Plot (Panel 6)</td>
<td>Scatter Plot (Panel 7)</td>
<td>Scatter Plot (Panel 8)</td>
    </tr>
<tr>
        <td>Cloudy Scene</td>
<td>SeaFlux (Buoy/Ship)</td>
<td>Scatter Plot (Panel 9)</td>
<td> </td>
<td>Scatter Plot (Panel 10)</td>
    </tr>
  </tbody>
</table>

Figure 5. A2CS retrievals of surface parameters compared with RSS AMSR2 (left six panels) retrievals and with buoy and ship observations from SeaFlux (Curry et al., 2004) (right four panels). Top row shows clear scene retrievals and bottom row shows cloudy scene retrievals.

higher than the physical wind speed at the surface. Given the focus here on precipitation, however, the surface wind speed bias should not be overly problematic given that the Tbs converge appropriately.

## 3.2. Improved Constraints

The clear-air retrievals of SST, water vapor, and surface wind speed with PMW observations are known to be robust (Gentemann et al., 2010). The following are some selected cases of cloudy retrievals to show the effect of having radar observations to constrain the vertical distribution of cloud particles and hydrometeors. In radiometer-only retrievals, the vertical distribution of cloud water must be assumed, since the PMW observations are only sensitive to the integrated absorption and emission throughout the atmospheric column. PMW retrievals of total liquid and ice water path tend to converge well until the particle sizes become large enough to significantly scatter the microwave radiation, causing the solutions to become nonunique. Normally, this signal manifests itself in an inflation of chi-square, indicating the algorithm is unable to find convergence on the scene. Some operational PMW retrieval algorithms, such as NOAA's Microwave Integrated Retrieval System (MiRS) (Boukabara et al., 2011), use the signal in chi-square to flag the scene for possible precipitation. As an illustration of this problem, retrieved liquid water paths associated with relatively large probabilities of precipitation often occur with chi-square values below the convergence limit in Figure 6.

By constraining the solution with coincident radar observations, the scattering in the forward model can be prescribed to the correct vertical levels. Figure 7 shows the evolution of the simulated observations throughout the iterations from three examples of cloudy retrievals. The rows show three different observed cloud scenarios: a shallow ice cloud, a shallow liquid cloud, and a mixed phase cloud. The columns represent different types of retrieval: from left to right, these are the combined retrieval, a retrieval using only the AMSR2 Tbs, and a retrieval using only the CPR reflectivity profile.

The combined retrieval (left column) shows the best fit between the observed Tbs and radar profile and the simulated observations from the retrieved state in all three cases. Here, we emulate a typical radiometer-only retrieval (middle column) by making the necessary a priori assumptions, namely the vertical distribution of ice and liquid water and their PSD parameters. Ice cloud layers are assumed to exist between 6 and 7 km, and the particle density is fixed, allowing the ice water path only to be retrievable. Similarly, liquid cloud water is assumed monodisperse and distributed between the freezing level and the cloud base both taken a priori from ERA5. For the radar-only retrieval (right column), there is no signal in SST, wind speed, or water vapor (except for attenuation, which alone is poorly constrained in the presence of cloud water), and these are also taken as fixed ancillary data. The ice particle density is again assumed fixed as well as the gamma PSD shape parameter $\mu$ in order to avoid instabilities in the algorithm due to too many free parameters. For the radiometer-only retrieval, the

JONES AND KUMMEROW

13 of 21


---



AGU ADVANCING EARTH AND SPACE SCIENCES logo

Journal of Geophysical Research: Atmospheres

10.1029/2024JD043111

21698996, 2025, 4, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024JD043111 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

<table>
  <thead>
    <tr>
        <th>AMSR2 Retrieved LWP [g/m²]</th>
        <th>Prob &gt; 0.001 [mm/hr]</th>
        <th>Prob &gt; 0.01 [mm/hr]</th>
        <th>Prob &gt; 0.1 [mm/hr]</th>
        <th>Prob &gt; 0.2 [mm/hr]</th>
        <th>Prob &gt; 0.5 [mm/hr]</th>
        <th>Chi-Squared</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>2.2</td>
    </tr>
<tr>
        <td>200</td>
<td>0.3</td>
<td>0.25</td>
<td>0.15</td>
<td>0.1</td>
<td>0.05</td>
<td>2.3</td>
    </tr>
<tr>
        <td>400</td>
<td>0.75</td>
<td>0.7</td>
<td>0.5</td>
<td>0.4</td>
<td>0.2</td>
<td>2.4</td>
    </tr>
<tr>
        <td>600</td>
<td>0.9</td>
<td>0.85</td>
<td>0.75</td>
<td>0.65</td>
<td>0.45</td>
<td>2.5</td>
    </tr>
<tr>
        <td>800</td>
<td>0.95</td>
<td>0.92</td>
<td>0.85</td>
<td>0.8</td>
<td>0.65</td>
<td>3.5</td>
    </tr>
<tr>
        <td>1000</td>
<td>0.98</td>
<td>0.95</td>
<td>0.9</td>
<td>0.85</td>
<td>0.75</td>
<td>5.5</td>
    </tr>
<tr>
        <td>1200</td>
<td>1.0</td>
<td>0.98</td>
<td>0.95</td>
<td>0.92</td>
<td>0.85</td>
<td>7.5</td>
    </tr>
  </tbody>
</table>

Figure 6. CloudSat along-track averaged probability of precipitation using several precipitation thresholds and associated final chi-square values from AMSR2 passive-only retrievals. Convergence limit is taken to be the MiRS convergence threshold of 3.0 to show that precipitating scenes can often converge as nonprecipitating scenes in passive-only retrievals.

radar observational uncertainties in **S<sub>y</sub>** are set to be very large and uncorrelated, which allow the algorithm to ignore the radar observations and vice versa.

In all three cases, we see the best fit between the final iteration (green) and the observations (blue) from the combined retrieval. The relatively larger differences between the simulated and observed Tbs at 89 GHz are due to the higher uncertainties in these channels produced by ice scattering. For both the ice cloud and the mixed phase cloud cases, the PMW observations are sensitive to the presence of ice scattering but not to the vertical location of cloud ice. This is illustrated by the fact that the radiometer-only retrieved state produces nearly identical Tbs to those from the retrieved state in the combined retrieval, even though the ice cloud is in the wrong layers. In the liquid cloud case (second row), the PMW observations correctly show no ice scattering in the scene, as the first guess of ice cloud water content is removed by the algorithm to get convergence. In this case, sufficient absorption by the monodisperse cloud water was enough to lead to convergence, even though this cloud water had no appreciable backscatter signal to produce simulated radar reflectivities above −26 dBZ.

In all cases, the radar-only final retrieved state shows significant differences in the simulated Tbs that are well outside their uncertainty estimates. An extreme example is the nearly 25-K difference between the simulated and observed Tb for the 23H in the mixed phase cloud case. This large difference does not exist in either the combined or radiometer-only retrieval due to water vapor being better constrained by the passive observations. Indeed, an 8-mm difference in TPW was found for the mixed phase case between the a priori value taken from ERA5 (19.7 mm) for radar-only retrieval and that from the combined retrieval (27.7 mm) or the passive-only retrieval (26.5 mm). Apparent errors in ERA5 water vapor can be large because precipitation in ERA5 is not always colocated with observed precipitation.

Statistically, we see much better correlation between observed Tbs and final simulated Tbs from retrieved profiles when we apply the constraint of the

radiometer observations in Figure 8. The remaining biases, though consistent, are either within or very close to the observational and forward model uncertainty estimations for these channels. Additionally, 25% of cloudy scenes that had converged in the non-precipitating radiometer-only retrieval were found to be precipitating due to the constraint of the CPR profile on the PMW observations.

## 3.3. Revisiting Zonal Means of Drizzle

Accumulating retrieved precipitation estimates from the A2CS retrieval show general agreement with CloudSat precipitation estimates from the 2C-RAIN-PROFILE and 2C-SNOW-PROFILE algorithms despite forcing the CPR radar profile to also be consistent with passive observations from AMSR2. Figure 9, a reproduction of the lower two panels of Figure 1 with the added A2CS retrieved drizzle accumulations, shows latitudinal means of the three operational CloudSat precipitation algorithms along with ERA5 and GPROF-GMI throughout the period of study for low precipitation rates. We see a large gap between ERA5 and any CloudSat estimate with CloudSat being the only sensor shown that is reliably capable of directly observing drizzle. As a reminder, some of the drizzle in GPROF GMI is a mathematical artifact caused by the averaging of convective precipitation as observed by the DPR at the radar resolution into the much larger GMI footprint, and the rest of the drizzle over oceans is added by blending MiRS retrievals on GMI with DPR observations within the a priori GPROF database. This brings GPROF estimations of drizzle into good agreement with ERA5 but far from CloudSat.

As latitudes get higher, the increasing reliance on snow retrievals as the dominant form of precipitation estimation becomes apparent as the accumulations of liquid surface rain get smaller and A2CS begins to follow the CloudSat 2C-SNOW-PROFILE accumulations. This trend is apparent in both hemispheres. Where liquid precipitation becomes more important toward the midlatitudes, the zonal means of drizzle follow the approximate sum of the

JONES AND KUMMEROW

14 of 21

14 of 21


---



21698996, 2025, 4, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024JD043111 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

10.1029/2024JD043111

AGU ADVANCING EARTH AND SPACE SCIENCES logo

# Journal of Geophysical Research: Atmospheres

<table>
  <thead>
    <tr>
        <th colspan="4">Evolution of Simulated Observations (Tb Residuals)</th>
    </tr>
<tr>
        <th>Cloud Type</th>
        <th>Combined Retrieval</th>
        <th>Radiometer-Only Retrieval</th>
        <th>Radar-Only Retrieval</th>
    </tr>
<tr>
        <th>Ice Cloud</th>
        <th>[Data: Δ Tb residuals for 9 channels across iterations]</th>
        <th>[Data: Δ Tb residuals for 9 channels across iterations]</th>
        <th>[Data: Δ Tb residuals for 9 channels across iterations]</th>
    </tr>
<tr>
        <th>Liquid Cloud</th>
        <th>[Data: Δ Tb residuals for 9 channels across iterations]</th>
        <th>[Data: Δ Tb residuals for 9 channels across iterations]</th>
        <th>[Data: Δ Tb residuals for 9 channels across iterations]</th>
    </tr>
<tr>
        <th>Mixed Phase Cloud</th>
        <th>[Data: Δ Tb residuals for 9 channels across iterations]</th>
        <th>[Data: Δ Tb residuals for 9 channels across iterations]</th>
        <th>[Data: Δ Tb residuals for 9 channels across iterations]</th>
    </tr>
<tr>
        <th colspan="4">Evolution of Simulated Observations (Radar Profiles)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>Cloud Type</td>
<td>Combined Retrieval</td>
<td>Radiometer-Only Retrieval</td>
<td>Radar-Only Retrieval</td>
    </tr>
<tr>
        <td>Ice Cloud</td>
<td>[Data: Height vs Reflectivity profiles]</td>
<td>[Data: Height vs Reflectivity profiles]</td>
<td>[Data: Height vs Reflectivity profiles]</td>
    </tr>
<tr>
        <td>Liquid Cloud</td>
<td>[Data: Height vs Reflectivity profiles]</td>
<td>[Data: Height vs Reflectivity profiles]</td>
<td>[Data: Height vs Reflectivity profiles]</td>
    </tr>
<tr>
        <td>Mixed Phase Cloud</td>
<td>[Data: Height vs Reflectivity profiles]</td>
<td>[Data: Height vs Reflectivity profiles]</td>
<td>[Data: Height vs Reflectivity profiles]</td>
    </tr>
  </tbody>
</table>

Figure 7. Evolution of simulated observations through three cloudy retrieval cases (rows) with three different retrieval methods (columns). First nine panels show simulated passive observations in residual Tb space (simulated Tb minus observed Tb), and last nine panels show observed and simulated radar profile. Gray shading indicates plus and minus one standard deviation of observational uncertainty.

JONES AND KUMMEROW

15 of 21


---



21698996, 2025, 4, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024JD043111 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU ADVANCING EARTH AND SPACE SCIENCES logo

Journal of Geophysical Research: Atmospheres

10.1029/2024JD043111

2D histograms of simulated AMSR2 channel Tbs compared with observed Tbs

**Figure 8.** 2D histograms of simulated AMSR2 channel Tbs compared with observed Tbs using the radar-only retrieved CPR profile and ancillary data (top two rows) and the combined retrieved profile (bottom two rows) for 1 month of coincident cloudy observations. Color from dark to light indicates the number of profiles. Orange dotted lines indicate the observational uncertainty variances for each channel.

means of CloudSat 2C-RAIN-PROFILE and 2C-SNOW-PROFILE. The agreement between A2CS and CloudSat operational algorithms is a surprising find as there is no constraint on the algorithm to produce intensity estimates that align with CloudSat, and CloudSat estimates are used on a first-order basis for precipitation detection only in the A2CS algorithm. This agreement also increases confidence that the A2CS drizzle estimates are not spurious retrieval artifacts as in GPROF. However, it is important to point out the small but consistent overestimation with respect to CloudSat especially in the Southern Ocean at latitudes south of −55°. This small increase of 7.6% in zonal means could be a signal of the radiometer's tendency to correct the radar's intensity estimates by constraining the total water path. It is also likely that the tendency of these latitudes to be dominated by supercooled liquid contributes to this disagreement, since neither 2C-RAIN-PROFILE, 2C-SNOW-PROFILE, nor A2CS retrieve mixed precipitation. It is also important to note the stark departure of A2CS drizzle from 2C-PRECIP-COLUMN accumulations, which generally follow, but consistently overestimate, those of 2C-RAIN-PROFILE. An overall overestimation by A2CS of 19.3% was found compared to 2C-PRECIP-COLUMN.

JONES AND KUMMEROW

16 of 21
16 of 21


---



21698996, 2025, 4, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024JD043111 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU ADVANCING EARTH AND SPACE SCIENCES logo

Journal of Geophysical Research: Atmospheres

10.1029/2024JD043111

# Zonal Mean Oceanic Precipitation $\le$ 0.25 mm/hr

<table>
  <thead>
    <tr>
        <th colspan="7">Northern Hemisphere (Left Panel)</th>
    </tr>
<tr>
        <th>Latitude</th>
        <th>Ocean Fraction</th>
        <th>A2CS (mm/day)</th>
        <th>CSAT 2C-RAIN (mm/day)</th>
        <th>CSAT 2C-SNOW (mm/day)</th>
        <th>CSAT 2C-PRECIP (mm/day)</th>
        <th>2C-RAIN + 2C-SNOW (mm/day)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>80</td>
<td>0.1</td>
<td>0.22</td>
<td>0.02</td>
<td>0.18</td>
<td>0.20</td>
<td>0.20</td>
    </tr>
<tr>
        <td>70</td>
<td>0.3</td>
<td>0.25</td>
<td>0.05</td>
<td>0.15</td>
<td>0.20</td>
<td>0.20</td>
    </tr>
<tr>
        <td>60</td>
<td>0.7</td>
<td>0.35</td>
<td>0.10</td>
<td>0.20</td>
<td>0.30</td>
<td>0.30</td>
    </tr>
<tr>
        <td>50</td>
<td>0.9</td>
<td>0.30</td>
<td>0.08</td>
<td>0.18</td>
<td>0.26</td>
<td>0.26</td>
    </tr>
<tr>
        <td>40</td>
<td>0.95</td>
<td>0.25</td>
<td>0.05</td>
<td>0.15</td>
<td>0.20</td>
<td>0.20</td>
    </tr>
<tr>
        <td>30</td>
<td>0.98</td>
<td>0.20</td>
<td>0.04</td>
<td>0.10</td>
<td>0.14</td>
<td>0.14</td>
    </tr>
<tr>
        <th colspan="7">Southern Hemisphere (Right Panel)</th>
    </tr>
<tr>
        <th>Latitude</th>
        <th>Ocean Fraction</th>
        <th>A2CS (mm/day)</th>
        <th>CSAT 2C-RAIN (mm/day)</th>
        <th>CSAT 2C-SNOW (mm/day)</th>
        <th>CSAT 2C-PRECIP (mm/day)</th>
        <th>2C-RAIN + 2C-SNOW (mm/day)</th>
    </tr>
<tr>
        <td>-30</td>
<td>1.0</td>
<td>0.15</td>
<td>0.02</td>
<td>0.05</td>
<td>0.07</td>
<td>0.07</td>
    </tr>
<tr>
        <td>-40</td>
<td>1.0</td>
<td>0.25</td>
<td>0.05</td>
<td>0.15</td>
<td>0.20</td>
<td>0.20</td>
    </tr>
<tr>
        <td>-50</td>
<td>1.0</td>
<td>0.45</td>
<td>0.10</td>
<td>0.30</td>
<td>0.40</td>
<td>0.40</td>
    </tr>
<tr>
        <td>-60</td>
<td>1.0</td>
<td>0.60</td>
<td>0.15</td>
<td>0.45</td>
<td>0.60</td>
<td>0.60</td>
    </tr>
<tr>
        <td>-70</td>
<td>0.8</td>
<td>0.70</td>
<td>0.10</td>
<td>0.55</td>
<td>0.65</td>
<td>0.65</td>
    </tr>
<tr>
        <td>-80</td>
<td>0.2</td>
<td>0.50</td>
<td>0.05</td>
<td>0.40</td>
<td>0.45</td>
<td>0.45</td>
    </tr>
  </tbody>
</table>

Figure 9. A reproduction of the bottom two panels of Figure 1, with the A2CS drizzle estimates added (dashed navy blue). Figure legend contains total latitude-weighted mean precipitation, in mm day<sup>-1</sup>, within the domain of study.

# 4. Summary and Discussion

We used an optimal estimation scheme to constrain observations of light drizzle over the high-latitude oceans ($\pm$40° latitude and poleward) using a combination of radar and radiometer observations. The radiometer observations from AMSR2 and the radar observations from the CPR are difficult to define coincidence for since they exist on such different spatial scales. This problem was addressed statistically by decreasing the horizontal and vertical resolution of the CPR observations. The OE algorithm successfully forced the inverted state to be radiatively consistent with both the CPR reflectivity profile and the AMSR2 Tbs. This is important since precipitation onset cannot be determined case-by-case with PMW observations alone nor can a radar profile alone produce the observed Tbs. The inverted state from the combined retrieval included the distribution of cloud particles and hydrometeors, resulting in a retrieved precipitation rate that was consistent with both sets of observations. A two-parameter PSD was possible in both liquid and frozen cloud and hydrometeor retrievals due to the additional constraints provided by both the active and passive measurements. Furthermore, complementary information from the passive observations constrained the ocean surface emissivity for all scenes as well as integrated water vapor and total liquid water path for all cloud types, therefore providing constraint to the ill-posed problem of radar beam attenuation. Additionally, the radar reflectivity profile allowed the assignment of absorption and scattering in the forward model to the correct vertical layers, which helped to reduce nonunique solutions.

We also found that relying primarily on the observational uncertainties as the primary driver of the total algorithm uncertainties produced physically sound retrievals on their own for this regime and at these low precipitation rates. Failed convergence was most likely an indicator of heavy, and likely multiple, scattering and seemed to be associated with very high precipitation estimates from CloudSat that were well beyond the saturation threshold of the radar beam. These scenes, while not retrievable by the A2CS algorithm, theoretically could be retrievable by a radar with an operating wavelength that is less prone to total attenuation, but this is outside the scope of the current study. This fact does, however, make the case for future missions with multiple-frequency spaceborne coincident radars to correctly capture all possible precipitation intensities via additional constraint to radiometer observations.

The A2CS algorithm was able to successfully constrain the discrimination between drizzling and nonprecipitating clouds, producing zonal means of light precipitation rates that were not only fairly consistent with both observations but also within the bounds of estimates by current operational satellite products. Using CloudSat native

JONES AND KUMMEROW

17 of 21


---



21698996, 2025, 4, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024JD043111 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU ADVANCING EARTH AND SPACE SCIENCES logo

# Journal of Geophysical Research: Atmospheres

10.1029/2024JD043111

estimates for frequency of occurrence only, we see good agreement between the A2CS algorithm and CloudSat combined rain and snow estimates for light precipitation. A slight overestimation of 7.6% with respect to the combined means of 2C-RAIN-PROFILE and 2C-SNOW-PROFILE as well as the much larger 19.3% increase with respect to the mean of 2C-PRECIP-COLUMN, however, likely showed the correction that the radiometer observations applied to the radar's intensity estimates in the bulk statistics. This general agreement with CloudSat increased confidence in retrieval skill, although validation in this meteorological regime remains difficult.

These findings, however, are encouraging and open the door to future investigations of drizzle observation using combined techniques. Although this study focused on high-latitude light precipitation over oceans only, an expansion of this work to land and sea ice is possible but would require more constraints on surface emissivity as well as an estimate of surface echo. This could be accomplished either via an offline scheme or by simultaneously retrieving emissivity using the passive observations similar to the method used by MiRS. Although the current formulation of the algorithm uses the radar-only estimate of rain rate from 2C-RAIN-PROFILE, which is currently only available over ocean, for the precipitation threshold, it could be possible to expand this over other surface types using a reflectivity threshold instead.

In addition to expanding this work to over land and ice surfaces, there are clear implications of applicability of this technique to enhance the light precipitation detection of radiometer-only retrievals. An obvious application of this work could be to add cloud-radar/radiometer retrieved light precipitation profiles directly to the training data for GPROF or to use GPM-CloudSat coincidences to build a data set of profiles consistent with GPM-CMB and CloudSat. For this study, AMSR2's 89.0 GHz channel was the highest frequency measurement available, but radiometers with higher frequency channels would likely allow even better constraints to ice particle scattering. Although CloudSat is currently undergoing end-of-radar operations, we look toward the upcoming EarthCARE mission (Wehr et al., 2023) for reliance on observations of this sensitive precipitation mode. Here, more coincidences between EarthCARE and currently flying and future multichannel radiometers will be a natural application of combined methods such as the one presented. Additionally, more PSD constraints provided by the Doppler velocity information in tandem with W-band reflectivity will be an obvious step forward in understanding the nature of light precipitation.

## Data Availability Statement

CloudSat Level 2B and 2C algorithm products used for this study (Lebsock, 2018; Marchand & Mace, 2018; Wood & L’Ecuyer, 2018) are publicly accessible at https://www.cloudsat.cira.colostate.edu. Level 1 C AMSR2 Tbs (Berg, 2022) and GPROF algorithm outputs (C. Kummerow, 2022) are available at [https://disc.gsfc.nasa.gov/](https://disc.gsfc.nasa.gov/). ERA5 data (Hersbach et al., 2020) is available from the Copernicus Climate Change Service Climate Data Store (CDS) (Copernicus Climate Change Service, Climate Data Store, 2023). Reynolds SST (Huang et al., 2021) is available from the National Oceanic and Atmospheric Administration (NOAA) at [https://psl.noaa.gov/data/gridded/data.noaa.oisst.v2.highres.html](https://psl.noaa.gov/data/gridded/data.noaa.oisst.v2.highres.html). Shipborne and buoy observations used for validation are from SeaFlux in situ data (Roberts et al., 2020). AMSR data are produced by Remote Sensing Systems and were sponsored by the NASA AMSR-E Science Team and the NASA Earth Science MEaSUREs Program. GMI data are produced by Remote Sensing Systems and sponsored by NASA Earth Science funding. RSS Data are available at www.remss.com. OceanRAIN shipborne disdrometer observations (Klepp et al., 2018) are available at [https://www.wdc-climate.de/ui/q?hierarchy_steps_ss=OceanRAIN](https://www.wdc-climate.de/ui/q?hierarchy_steps_ss=OceanRAIN). Source code for AMSR2-CPR combined retrieval and code to reproduce figures are available from a public repository ([https://doi.org/10.5281/zenodo.14456308](https://doi.org/10.5281/zenodo.14456308)).

### Acknowledgments

This research was funded by the National Aeronautics and Space Administration (award number 80NSSC22K0604). We would also like to thank four anonymous reviewers for their feedback, which contributed to a much-improved article.

## References

Adler, R. F., Gu, G., Sapiano, M., Wang, J.-J., & Huffman, G. J. (2017). Global precipitation: Means, variations, and trends during the satellite era (1979-2014). *Surveys in Geophysics*, 38(4), 679–699. [https://doi.org/10.1007/s10712-017-9416-4](https://doi.org/10.1007/s10712-017-9416-4)

Ban, N., Schmidli, J., & Schär, C. (2014). Evaluation of the convection-resolving regional climate modeling approach in decade-long simulations. *Journal of Geophysical Research: Atmospheres*, 119(13), 7889–7907. [https://doi.org/10.1002/2014JD021478](https://doi.org/10.1002/2014JD021478)

Behrangi, A., Christensen, M., Richardson, M., Lebsock, M., Stephens, G., Huffman, G. J., et al. (2016). Status of High latitude precipitation estimates from observations and reanalyses. *Journal of Geophysical Research: Atmospheres*, 121(9), 4468–4486. [https://doi.org/10.1002/2015JD024546](https://doi.org/10.1002/2015JD024546)

Behrangi, A., Lebsock, M., Wong, S., & Lambrigtsen, B. (2012). On the quantification of oceanic rainfall using spaceborne sensors. *Journal of Geophysical Research*, 117(D20). [https://doi.org/10.1029/2012JD017979](https://doi.org/10.1029/2012JD017979)

Behrangi, A., & Song, Y. (2020). A new estimate for oceanic precipitation amount and distribution using complementary precipitation observations from space and comparison with GPCP. *Environmental Research Letters*, 15(12), 124042. [https://doi.org/10.1088/1748-9326/abc6d1](https://doi.org/10.1088/1748-9326/abc6d1)

JONES AND KUMMEROW

18 of 21


---



21698996, 2025, 4, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024JD043111 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU ADVANCING EARTH AND SPACE SCIENCES logo

# Journal of Geophysical Research: Atmospheres

10.1029/2024JD043111

Behrangi, A., Stephens, G., Adler, R. F., Huffman, G. J., Lambrigtsen, B., & Lebsock, M. (2014). An update on the oceanic precipitation rate and its zonal distribution in light of advanced observations from space. *Journal of Climate*, 27(11), 3957–3965. [https://doi.org/10.1175/JCLI-D-13-00679.1](https://doi.org/10.1175/JCLI-D-13-00679.1)

Berg, W. (2022). GPM AMSR-2 on GCOM-W1 common calibrated brightness temperature L1C 1.5 hours 10 km V07. [Dataset]. [https://doi.org/10.5067/GPM/AMSR2/GCOMW1/1C/07](https://doi.org/10.5067/GPM/AMSR2/GCOMW1/1C/07)

Berg, W., Bilanow, S., Datta, S., Draper, D., Ebrahimi, H., Chen, R., et al. (2016). Intercalibration of the GPM microwave radiometer constellation. *Journal of Atmospheric and Oceanic Technology*, 33(12), 2639–2654. [https://doi.org/10.1175/JTECH-D-16-0100.1](https://doi.org/10.1175/JTECH-D-16-0100.1)

Berg, W., L’Ecuyer, T., & Haynes, J. M. (2010). The distribution of rainfall over oceans from spaceborne radars. *Journal of Applied Meteorology and Climatology*, 49(3), 535–543. [https://doi.org/10.1175/2009jamc2330.1](https://doi.org/10.1175/2009jamc2330.1)

Berg, W., L’Ecuyer, T., & Kummerow, C. (2006). Rainfall climate regimes: The relationship of regional TRMM rainfall biases to the environment. *Journal of Applied Meteorology and Climatology*, 45(3), 434–454. [https://doi.org/10.1175/JAM2331.1](https://doi.org/10.1175/JAM2331.1)

Boukabara, S.-A., Garrett, K., Chen, W., Iturbide-Sanchez, F., Grassotti, C., Kongoli, C., et al. (2011). MiRS: An all-weather 1DVAR satellite data assimilation and retrieval system. *IEEE Transactions on Geoscience and Remote Sensing: A Publication of the IEEE Geoscience and Remote Sensing Society*, 49(9), 3249–3272. [https://doi.org/10.1109/TGRS.2011.2158438](https://doi.org/10.1109/TGRS.2011.2158438)

Brath, M., Ekelund, R., Eriksson, P., Lemke, O., & Buehler, S. A. (2020). Microwave and submillimeter wave scattering of oriented ice particles. *Atmospheric Measurement Techniques*, 13(5), 2309–2333. [https://doi.org/10.5194/amt-13-2309-2020](https://doi.org/10.5194/amt-13-2309-2020)

Christensen, M. W., Stephens, G. L., & Lebsock, M. D. (2013). Exposing biases in retrieved low cloud properties from CloudSat: A guide for evaluating observations and climate data. *Journal of Geophysical Research: Atmospheres*, 118(21). [https://doi.org/10.1002/2013jd020224](https://doi.org/10.1002/2013jd020224)

Copernicus Climate Change Service, & Climate Data Store. (2023). ERA5 hourly data on single levels from 1940 to present. Copernicus Climate Change Service (C3S) Climate Data Store (CDS). [Dataset]. [https://doi.org/10.24381/cds.adbb2d47](https://doi.org/10.24381/cds.adbb2d47)

Curry, J. A., Bentamy, A., Bourassa, M. A., Bourras, D., Bradley, E. F., Brunke, M., et al. (2004). Seaflux. *Bulletin of the American Meteorological Society*, 85(3), 409–424. [https://doi.org/10.1175/bams-85-3-409](https://doi.org/10.1175/bams-85-3-409)

Duncan, D. I., & Kummerow, C. D. (2016). A 1DVAR retrieval applied to GMI: Algorithm description, validation, and sensitivities. *Journal of Geophysical Research: Atmospheres*, 121(12), 7415–7429. [https://doi.org/10.1002/2016JD024808](https://doi.org/10.1002/2016JD024808)

Duncan, D. I., Kummerow, C. D., Dolan, B., & Petković, V. (2018). Towards variational retrieval of warm rain from passive microwave observations. *Atmospheric Measurement Techniques*, 11(7), 4389–4411. [https://doi.org/10.5194/amt-11-4389-2018](https://doi.org/10.5194/amt-11-4389-2018)

Eastman, R., Lebsock, M., & Wood, R. (2019). Warm rain rates from AMSR-E 89-GHz brightness temperatures trained using CloudSat rain-rate observations. *Journal of Atmospheric and Oceanic Technology*, 36(6), 1033–1051. [https://doi.org/10.1175/jtech-d-18-0185.1](https://doi.org/10.1175/jtech-d-18-0185.1)

Gentemann, C. L., & Hilburn, K. A. (2015). In situ validation of sea surface temperatures from the GCOM-W1 AMSR2 RSS calibrated brightness temperatures. *Journal of Geophysical Research: Oceans*, 120(5), 3567–3585. [https://doi.org/10.1002/2014JC010574](https://doi.org/10.1002/2014JC010574)

Gentemann, C. L., Wentz, F. J., Brewer, M., Hilburn, K., & Smith, D. (2010). Passive microwave remote sensing of the Ocean: An overview. In *Oceanography from space*. Springer. [https://doi.org/10.1007/978-90-481-8681-5_2](https://doi.org/10.1007/978-90-481-8681-5_2)

Grecu, M., Olson, W. S., Munchak, S. J., Ringerud, S., Liao, L., Haddad, Z., et al. (2016). The GPM combined algorithm. *Journal of Atmospheric and Oceanic Technology*, 33(10), 2225–2245. [https://doi.org/10.1175/JTECH-D-16-0019.1](https://doi.org/10.1175/JTECH-D-16-0019.1)

Haynes, J. M. (2018). CloudSat 2C-PRECIP-COLUMN data product process description and interface control document, product version: P1 R05. NASA JPL CloudSat project document revision 0, 22. Retrieved from [https://www.cloudsat.cira.colostate.edu/cloudsat-static/info/dl/2c-precip-column/2C-PRECIP-COLUMN_PDICD.P1_R05.rev1_.pdf](https://www.cloudsat.cira.colostate.edu/cloudsat-static/info/dl/2c-precip-column/2C-PRECIP-COLUMN_PDICD.P1_R05.rev1_.pdf)

Haynes, J. M., L’Ecuyer, T. S., Stephens, G. L., Miller, S. D., Mitrescu, C., Wood, N. B., & Tanelli, S. (2009). Rainfall retrieval over the ocean with spaceborne W-band radar. *Journal of Geophysical Research*, 114(D8), D00A22. [https://doi.org/10.1029/2008JD009973](https://doi.org/10.1029/2008JD009973)

Haynes, J. M., Marchand, R. T., Luo, Z., Bodas-Salcedo, A., & Stephens, G. L. (2007). A multipurpose radar simulation package: QuickBeam. *Bulletin of the American Meteorological Society*, 88(11), 1723–1728. [https://doi.org/10.1175/BAMS-88-11-1723](https://doi.org/10.1175/BAMS-88-11-1723)

Hersbach, H., Bell, B., Berrisford, P., Hirahara, S., Horányi, A., Muñoz-Sabater, J., et al. (2020). The ERA5 global reanalysis. *Quarterly Journal of the Royal Meteorological Society*, 146(730), 1999–2049. [https://doi.org/10.1002/qj.3803](https://doi.org/10.1002/qj.3803)

Heymsfield, A. J., Field, P., & Bansemer, A. (2008). Exponential size distributions for snow. *Journal of the Atmospheric Sciences*, 65(12), 4017–4031. [https://doi.org/10.1175/2008JAS2583.1](https://doi.org/10.1175/2008JAS2583.1)

Hilburn, K. A., & Wentz, F. J. (2008). Intercalibrated passive microwave rain products from the unified microwave ocean retrieval algorithm (UMORA). *Journal of Applied Meteorology and Climatology*, 47(3), 778–794. [https://doi.org/10.1175/2007jamc1635.1](https://doi.org/10.1175/2007jamc1635.1)

Hou, A. Y., Kakar, R. K., Neeck, S., Azarbarzin, A. A., Kummerow, C. D., Kojima, M., et al. (2014). The global precipitation measurement mission. *Bulletin of the American Meteorological Society*, 95(5), 701–722. [https://doi.org/10.1175/BAMS-D-13-00164.1](https://doi.org/10.1175/BAMS-D-13-00164.1)

Hu, Y., Rodier, S., Xu, K.-M., Sun, W., Huang, J., Lin, B., et al. (2010). Occurrence, liquid water content, and fraction of supercooled water clouds from combined CALIOP/IIR/MODIS measurements. *Journal of Geophysical Research*, 115(D4). [https://doi.org/10.1029/2009jd012384](https://doi.org/10.1029/2009jd012384)

Huang, B., Liu, C., Banzon, V., Freeman, E., Graham, G., Hankins, B., et al. (2021). Improvements of the daily optimum interpolation sea surface temperature (DOISST) version 2.1. *Journal of Climate*, 34(8), 2923–2939. [https://doi.org/10.1175/jcli-d-20-0166.1](https://doi.org/10.1175/jcli-d-20-0166.1)

Iguchi, T., Seto, S., Meneghini, R., Yoshida, N., Awaka, J., Le, M., et al. (2021). GPM/DPR level-2 algorithm theoretical basis document. Retrieved from [https://gpm.nasa.gov/sites/default/files/2022-06/ATBD_DPR_V07A.pdf](https://gpm.nasa.gov/sites/default/files/2022-06/ATBD_DPR_V07A.pdf)

Klepp, C., Michel, S., Protat, A., Burdanowitz, J., Albern, N., Kähnert, M., et al. (2018). OceanRAIN, a new in-situ shipboard global ocean surface-reference dataset of all water cycle components. *Scientific Data*, 5(180122), 180122. [https://doi.org/10.1038/sdata.2018.122](https://doi.org/10.1038/sdata.2018.122)

Kummerow, C. (1993). On the accuracy of the Eddington approximation for radiative transfer in the microwave frequencies. *Journal of Geophysical Research*, 98(D2), 2757–2765. [https://doi.org/10.1029/92jd02472](https://doi.org/10.1029/92jd02472)

Kummerow, C. (1998). Beamfilling errors in passive microwave rainfall retrievals. *Journal of Applied Meteorology and Climatology*, 37(4), 356–370. https://doi.org/10.1175/1520-0450(1998)037<0356:BEIPMR>2.0.CO;2037<0356:BEIPMR>2.0.CO;2)

Kummerow, C. (2022). GPM GMI (GPROF) radiometer precipitation profiling L2A 1.5 hours 13 km V07 (GPM_2AGPROFGPMGMI). [Dataset]. [https://doi.org/10.5067/GPM/GMI/GPM/GPROF/2A/07](https://doi.org/10.5067/GPM/GMI/GPM/GPROF/2A/07)

Kummerow, C. D. (2020). Introduction to passive microwave retrieval methods. In *Advances in global change Research* (pp. 123–140). Springer International Publishing. [https://doi.org/10.1007/978-3-030-24568-9_7](https://doi.org/10.1007/978-3-030-24568-9_7)

Kummerow, C. D., Randel, D. L., Kulie, M., Wang, N.-Y., Munchak, S. J., Ferraro, R., & Petković, V. (2015). The evolution of the goddard profiling algorithm to a fully parametric scheme. *Journal of Atmospheric and Oceanic Technology*, 32(12), 2265–2280. [https://doi.org/10.1175/JTECH-D-15-0039.1](https://doi.org/10.1175/JTECH-D-15-0039.1)

Lamer, K., Kollias, P., Battaglia, A., & Preval, S. (2020). Mind the gap – Part 1: Accurately locating warm marine boundary layer clouds and precipitation using spaceborne radars. *Atmospheric Measurement Techniques*, 13(5), 2363–2379. [https://doi.org/10.5194/amt-13-2363-2020](https://doi.org/10.5194/amt-13-2363-2020)

JONES AND KUMMEROW

19 of 21


---



21698996, 2025, 4, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024JD043111 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU ADVANCING EARTH AND SPACE SCIENCES logo

# Journal of Geophysical Research: Atmospheres

10.1029/2024JD043111

Lau, W. K.-M., Wu, H.-T., & Kim, K.-M. (2013). A canonical response of precipitation characteristics to global warming from CMIP5 models. *Geophysical Research Letters*, 40(12), 3163–3169. [https://doi.org/10.1002/grl.50420](https://doi.org/10.1002/grl.50420)

Lebsock, M. D. (2018). Level 2C RAIN-PROFILE product process description and interface control document. Retrieved from [https://www.cloudsat.cira.colostate.edu/cloudsat-static/info/dl/2c-rain-profile/2C-RAIN-PROFILE_PDICD.P1_R05.rev0_.pdf](https://www.cloudsat.cira.colostate.edu/cloudsat-static/info/dl/2c-rain-profile/2C-RAIN-PROFILE_PDICD.P1_R05.rev0_.pdf)

Lebsock, M. D., & L’Ecuyer, T. S. (2011). The retrieval of warm rain from CloudSat. *Journal of Geophysical Research*, 116(D20209), D20209. [https://doi.org/10.1029/2011JD016076](https://doi.org/10.1029/2011JD016076)

Listowski, C., Delanoë, J., Kirchgaessner, A., Lachlan-Cope, T., & King, J. (2019). Antarctic clouds, supercooled liquid water and mixed phase, investigated with DARDAR: Geographical and seasonal variations. *Atmospheric Chemistry and Physics*, 19(10), 6771–6808. [https://doi.org/10.5194/acp-19-6771-2019](https://doi.org/10.5194/acp-19-6771-2019)

Liu, G. (2008). Deriving snow cloud characteristics from CloudSat observations. *Journal of Geophysical Research*, 113(D8), D00A09. [https://doi.org/10.1029/2007JD009766](https://doi.org/10.1029/2007JD009766)

Liu, Q., Weng, F., & English, S. J. (2011). An improved fast microwave water emissivity model. *IEEE Transactions on Geoscience and Remote Sensing*, 49(4), 1238–1250. [https://doi.org/10.1109/TGRS.2010.2064779](https://doi.org/10.1109/TGRS.2010.2064779)

Marchand, R., & Mace, G. (2018). Level 2 GEOPROF product process description and interface control document, product version: P1 R05. NASA JPL CloudSat project document revision 0, 27. Retrieved from [https://www.cloudsat.cira.colostate.edu/cloudsat-static/info/dl/2b-geoprof/2B-GEOPROF_PDICD.P1_R05.rev0__0.pdf](https://www.cloudsat.cira.colostate.edu/cloudsat-static/info/dl/2b-geoprof/2B-GEOPROF_PDICD.P1_R05.rev0__0.pdf)

Marchand, R., Mace, G. G., Ackerman, T., & Stephens, G. (2008). Hydrometeor detection using cloudsat—An earth-orbiting 94-GHz cloud radar. *Journal of Atmospheric and Oceanic Technology*, 25(4), 519–533. [https://doi.org/10.1175/2007JTECHA1006.1](https://doi.org/10.1175/2007JTECHA1006.1)

Matrosov, S. Y. (1998). A dual-wavelength radar method to measure snowfall rate. *Journal of Applied Meteorology and Climatology*, 37(11), 1510–1521. https://doi.org/10.1175/1520-0450(1998)037<1510:ADWRMT>2.0.CO;2037<1510:ADWRMT>2.0.CO;2)

Petković, V., Brown, P., Berg, W., Randel, D. L., Jones, S. R., & Kummerow, C. D. (2023). Can we estimate the uncertainty level of satellite long-term precipitation records? *Journal of Applied Meteorology and Climatology*, 62(8), 1069–1082. [https://doi.org/10.1175/JAMC-D-22-0179.1](https://doi.org/10.1175/JAMC-D-22-0179.1)

Petty, G. W. (1995). Frequencies and characteristics of global oceanic precipitation from shipboard present-weather reports. *Bulletin of the American Meteorological Society*, 76(9), 1593–1616. https://doi.org/10.1175/1520-0477(1995)076<1593:FACOGO>2.0.CO;2076<1593:FACOGO>2.0.CO;2)

Pfreundschuh, S., Brown, P. J., Kummerow, C. D., Eriksson, P., & Norrestad, T. (2022a). GPROF-NN: A neural-network-based implementation of the goddard profiling algorithm. *Atmospheric Measurement Techniques*, 15(17), 5033–5060. [https://doi.org/10.5194/amt-15-5033-2022](https://doi.org/10.5194/amt-15-5033-2022)

Pfreundschuh, S., Eriksson, P., Buehler, S. A., Brath, M., Duncan, D., Larsson, R., & Ekelund, R. (2020). Synergistic radar and radiometer retrievals of ice hydrometeors. *Atmospheric Measurement Techniques*, 13(8), 4219–4245. [https://doi.org/10.5194/amt-13-4219-2020](https://doi.org/10.5194/amt-13-4219-2020)

Pfreundschuh, S., Fox, S., Eriksson, P., Duncan, D., Buehler, S. A., Brath, M., et al. (2022b). Synergistic radar and sub-millimeter radiometer retrievals of ice hydrometeors in mid-latitude frontal cloud systems. *Atmospheric Measurement Techniques*, 15(3), 677–699. [https://doi.org/10.5194/amt-15-677-2022](https://doi.org/10.5194/amt-15-677-2022)

Pfreundschuh, S., Guilloteau, C., Brown, P. J., Kummerow, C. D., & Eriksson, P. (2024). GPROF V7 and beyond: Assessment of current and potential future versions of the GPROF passive microwave precipitation retrievals against ground radar measurements over the continental US and the Pacific ocean. *Atmospheric Measurement Techniques*, 17(2), 515–538. [https://doi.org/10.5194/amt-17-515-2024](https://doi.org/10.5194/amt-17-515-2024)

Reynolds, R. W., Smith, T. M., Liu, C., Chelton, D. B., Casey, K. S., & Schlax, M. G. (2007). Daily high-resolution-blended analyses for sea surface temperature. *Journal of Climate*, 20(22), 5473–5496. [https://doi.org/10.1175/2007JCLI1824.1](https://doi.org/10.1175/2007JCLI1824.1)

Roberts, J. B., Clayson, C. A., & Robertson, F. R. (2020). SeaFlux data products in-situ data. NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. [Dataset]. [https://doi.org/10.5067/SEAFLUX/DATA101](https://doi.org/10.5067/SEAFLUX/DATA101)

Rodgers, C. D. (2000). *Inverse methods for atmospheric sounding* (Vol. 2). World Scientific Publishing Co. Pte. Ltd.

Schulte, R. M., & Kummerow, C. D. (2019). An optimal estimation retrieval algorithm for microwave humidity sounding channels with minimal scan position bias. *Journal of Atmospheric and Oceanic Technology*, 36(3), 409–425. [https://doi.org/10.1175/JTECH-D-18-0133.1](https://doi.org/10.1175/JTECH-D-18-0133.1)

Schulte, R. M., & Kummerow, C. D. (2022). Can DSD assumptions explain the differences in satellite estimates of warm rain? *Journal of Atmospheric and Oceanic Technology*, 39(12), 1889–1901. [https://doi.org/10.1175/JTECH-D-22-0036.1](https://doi.org/10.1175/JTECH-D-22-0036.1)

Schulte, R. M., Kummerow, C. D., Klepp, C., & Mace, G. G. (2022). How accurately can warm rain realistically Be retrieved with satellite sensors? Part I: DSD uncertainties. *Journal of Applied Meteorology and Climatology*, 61(9), 1087–1105. [https://doi.org/10.1175/JAMC-D-21-0158.1](https://doi.org/10.1175/JAMC-D-21-0158.1)

Schulte, R. M., Kummerow, C. D., Saleeby, S. M., & Mace, G. G. (2023). How accurately can warm rain realistically Be retrieved with satellite sensors? Part II: Horizontal and vertical heterogeneities. *Journal of Applied Meteorology and Climatology*, 62(2), 155–170. [https://doi.org/10.1175/JAMC-D-22-0051.1](https://doi.org/10.1175/JAMC-D-22-0051.1)

Skofronick-Jackson, G. M., Johnson, B. T., & Munchak, S. J. (2013). Detection thresholds of falling snow from satellite-borne active and passive sensors. *IEEE Transactions on Geoscience and Remote Sensing: A Publication of the IEEE Geoscience and Remote Sensing Society*, 51(7), 4177–4189. [https://doi.org/10.1109/tgrs.2012.2227763](https://doi.org/10.1109/tgrs.2012.2227763)

Stephens, G. L., & Kummerow, C. D. (2007). The remote sensing of clouds and precipitation from space: A review. *Journal of the Atmospheric Sciences*, 64(11), 3742–3765. [https://doi.org/10.1175/2006JAS2375.1](https://doi.org/10.1175/2006JAS2375.1)

Stephens, G. L., L’Ecuyer, T. S., Forbes, R., Gettlemen, A., Golaz, J.-C., Bodas-Salcedo, A., et al. (2010). Dreary state of precipitation in global models. *Journal of Geophysical Research*, 115(D24), D24211. [https://doi.org/10.1029/2010JD014532](https://doi.org/10.1029/2010JD014532)

Stephens, G. L., Vane, D. G., Boain, R. J., Mace, G. G., Sassen, K., Wang, Z., et al. (2002). The cloudsat mission and the a-train: A new dimension of space-based observations of clouds and precipitation. *Bulletin of the American Meteorological Society*, 83(12), 1771–1790. [https://doi.org/10.1175/BAMS-83-12-1771](https://doi.org/10.1175/BAMS-83-12-1771)

Villermaux, E., & Eloi, F. (2011). The distribution of raindrops speeds. *Geophysical Research Letters*, 38(L19805). [https://doi.org/10.1029/2011GL048863](https://doi.org/10.1029/2011GL048863)

Wehr, T., Kubota, T., Tzeremes, G., Wallace, K., Nakatsuka, H., Ohno, Y., et al. (2023). The EarthCARE mission – Science and system overview. *Atmospheric Measurement Techniques*, 16(15), 3581–3608. [https://doi.org/10.5194/amt-16-3581-2023](https://doi.org/10.5194/amt-16-3581-2023)

Weng, F. (2007). Advances in radiative transfer modeling in support of satellite data assimilation. *Journal of the Atmospheric Sciences*, 64(11), 3799–3807. [https://doi.org/10.1175/2007JAS2112.1](https://doi.org/10.1175/2007JAS2112.1)

Wentz, F. J., Meissner, T., Gentemann, C., Hilburn, K. A., & Scott, J. (2014). Remote sensing systems daily environmental suite on 0.25 deg grid, version 8.2. Retrieved from www.remss.com/missions/amsr

Wentz, F. J., Meissner, T., Scott, J., & Hilburn, K. A. (2015). Remote sensing systems GPM GMI daily environmental suite on 0.25 deg grid, version 8.2. Remote Sensing Systems, Santa Rosa, CA. Retrieved from www.remss.com/missions/gmi

JONES AND KUMMEROW 20 of 21


---


21698996, 2025, 4, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024JD043111 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU ADVANCING EARTH AND SPACE SCIENCES logo

# Journal of Geophysical Research: Atmospheres

### 10.1029/2024JD043111

Wood, N. B., & L’Ecuyer, T. S. (2018). Level 2C snow profile process description and interface control document, product version: P1 R05. *NASA JPL CloudSat project document revision 0*, 26. Retrieved from [https://www.cloudsat.cira.colostate.edu/cloudsat-static/info/dl/2c-snow-profile/2C-SNOW-PROFILE_PDICD.P1_R05.rev0_.pdf](https://www.cloudsat.cira.colostate.edu/cloudsat-static/info/dl/2c-snow-profile/2C-SNOW-PROFILE_PDICD.P1_R05.rev0_.pdf)

Wu, W., Yang, C. A., Diao, M., Gettelman, A., Zhang, K., Sun, J., & McFarquhar, G. (2021). Ice and supercooled liquid water distributions over the Southern Ocean based on in situ observations and climate model simulations. *Journal of Geophysical Research: Atmospheres*, 126(24), e2021JD036045. [https://doi.org/10.1029/2021JD036045](https://doi.org/10.1029/2021JD036045)

JONES AND KUMMEROW 21 of 21
