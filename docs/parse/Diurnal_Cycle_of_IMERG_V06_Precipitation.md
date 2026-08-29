Check for updates

AGU 100 ADVANCING EARTH AND SPACE SCIENCE logo

# Geophysical Research Letters

## RESEARCH LETTER

10.1029/2019GL085395

**Key Points:**

* The maturity of the Integrated Multi-satellitE Retrievals for Global Precipitation Measurement for diurnal cycle analysis is demonstrated

* Ground validation suggests that the diurnal cycle has a slight lag of generally no more than an hour

* The high resolution, global coverage, and long record allow an unprecedented view of diurnal cycle around the world

**Supporting Information:**

* Supporting Information S1

**Correspondence to:**

J. Tan,
jackson.tan@nasa.gov

**Citation:**

Tan, J., Huffman, G. J., Bolvin, D. T., & Nelkin, E. J. (2019). Diurnal cycle of IMERG V06 precipitation. *Geophysical Research Letters*, 46, 13,584–13,592. [https://doi.org/10.1029/2019GL085395](https://doi.org/10.1029/2019GL085395)

Received 12 SEP 2019
Accepted 5 NOV 2019
Accepted article online 9 NOV 2019
Published online 28 NOV 2019

# Diurnal Cycle of IMERG V06 Precipitation

Jackson Tan<sup>1,2</sup> ORCID icon, George J. Huffman<sup>2</sup> ORCID icon, David T. Bolvin<sup>2,3</sup> ORCID icon, and Eric J. Nelkin<sup>2,3</sup>

<sup>1</sup>Universities Space Research Association, Columbia, MD, USA, <sup>2</sup>NASA Goddard Space Flight Center, Greenbelt, MD, USA, <sup>3</sup>Science Systems and Applications, Inc., Lanham, MD, USA

**Abstract** This study demonstrates the maturing ability of the half-hourly precipitation estimates from the Integrated Multi-satellitE Retrievals for GPM (IMERG) for use in global analyses of the diurnal cycle. The refined intercalibration and interpolation between the sensors in V06 leads to greater consistency in the precipitation retrievals over different hours of the day. Evaluation against ground measurements suggests a slight lag in the diurnal phase of only +0.59 hr. We demonstrate the diurnal cycle over different regions around the globe, including the Maritime Continent, where accurate representation of precipitation variability in global models remains a challenge. Using examples over Singapore, Bangladesh, and Lake Victoria, we reveal the intricate interplay between diurnal and seasonal variability. This study demonstrates the unprecedented capability of IMERG in capturing the diurnal cycle of precipitation globally, potentially advancing our understanding in regions of sparse ground measurements and supporting improvements in its representation in global models.

**Plain Language Summary** Most people are familiar with afternoon thunderstorms in warm seasons or climates, which are a common feature of the diurnal cycle of rainfall. Over the central United States in summer, storms are more likely in the middle of the night, while over ocean, rainfall tends to be highest in the early morning. To study the diurnal cycle and the interplaying factors that drive them, many studies have relied on satellite observations. Here, we demonstrate how refinements in the latest NASA Global Precipitation Measurement gridded precipitation product, Integrated Multi-satellitE Retrievals for Global Precipitation Measurement (IMERG) V06, can lead to improved reliability for studying diurnal cycles. With only a slight delay in time—an improvement over its predecessor—the IMERG diurnal cycle reveals the time of day when rainfall is heaviest in the Maritime Continent, a region in Southeast Asia where intricate coastlines and complex topography pose challenges to global models. With a high resolution, long record, and global coverage, IMERG can quantify the diurnal cycle of rainfall globally, from the small island of Singapore to the monsoon-dominated Bangladesh and to the sparsely measured Lake Victoria region in Africa. The maturing ability of IMERG V06 in depicting the diurnal cycle of precipitation gives new confidence in using these data for scientific studies.

## 1. Introduction

The diurnal cycle is one of the most prominent features of precipitation variability, reflecting not just the local convective heating but also dynamical interactions between different surface types and orography. Due to the challenges in representing such processes that span across multiple spatiotemporal scales, global numerical models often struggle to represent the diurnal cycle of precipitation accurately (e.g., Covey et al., 2016; Dai et al., 1999; Dai & Trenberth, 2004), especially in regions such as the Maritime Continent where intricate coastlines and topography accentuate the importance of local circulations between the land and the ocean (Peatman et al., 2014; Qian, 2008; Worku et al., 2019). In many regions, sparse subdaily ground measurements limit our ability to characterize the local diurnal variability, especially over lakes and oceans.

To overcome the limitation of sparse ground observations, some studies have used satellite-based precipitation products to examine the diurnal variability (e.g., Dai et al., 2007; Kikuchi & Wang, 2008; Watters & Battaglia, 2019; Worku et al., 2019). These products may be based on active microwave retrievals (e.g., radar), which are generally more accurate but have limited sampling, or merged passive microwave (PMW) and infrared (IR) retrievals, which have wider coverage and higher time resolution but possess greater uncertainty, including possible lags in diurnal phase. These studies generally find an afternoon peak over land and a morning peak over ocean, a more pronounced cycle over land, and a greater reliability in the phase than amplitude.

©2019. American Geophysical Union. All Rights Reserved.

TAN ET AL.

13,584


---


19448007, 2019, 22, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2019GL085395 by Capes, Wiley Online Library on [17/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU 100 ADVANCING EARTH AND SPACE SCIENCE logo

# Geophysical Research Letters

10.1029/2019GL085395

This study uses the Integrated Multi-satellitE Retrievals for Global Precipitation Measurement (IMERG) V06 Final run product to examine the diurnal cycle of precipitation, with the goal of demonstrating this data set's maturing capability to advance our understanding of diurnal variability globally and provide a basis for improving the representation of the diurnal cycle in global models. Evaluation of earlier versions of IMERG suggested a lag in phase but greater uncertainty in amplitude, with the precipitation amount better represented than frequency and conditional precipitation rate (Li et al., 2018; Mayor et al., 2017; Oliveira et al., 2016; O & Kirstetter, 2018; Tang et al., 2016). Compared to previous V05, IMERG V06 possesses improved intercalibration and interpolation (Huffman, Bolvin, Nelkin, et al., 2019), leading to increased confidence in its representation of the diurnal cycle. We will illustrate the improvement over V05 and compare it with ground observations to quantify a residual lag in the diurnal cycle. We will apply IMERG to several regions to reveal the intricate dependence of diurnal cycle on the local conditions, possible even over small areas by virtue of the fine spatial resolution and robust due to the long record.

## 2. Data and Methods

IMERG is the U.S. merged satellite gridded precipitation product from the Global Precipitation Measurement (GPM) mission that unifies observations from a network of partner satellites in the GPM constellation (Huffman, Bolvin, Braithwaite, et al., 2019; Huffman, Bolvin, Nelkin, et al., 2019; Precipitation Processing System, 2019a). Precipitation estimates are provided at 0.1° grids every half hour, between 60° latitudes for V05 and globally for V06. The record for IMERG V05 begins in March 2014, while IMERG V06 extends this record back to June 2000 (eventually to January 1998). IMERG has three runs—Early, Late, and Final—to accommodate different user requirements for latency and accuracy. This study uses the gauge-adjusted estimates from the Final runs of IMERG V05B and V06B, the latest versions of V05 and V06 respectively.

IMERG uses precipitation estimates derived from PMW sensors. The PMW precipitation estimates are derived primarily from the Goddard Profiling algorithm (Kummerow et al., 2001, 2011, 2015; Precipitation Processing System, 2017), a fully parametric retrieval algorithm that estimates the surface precipitation rate from the PMW brightness temperature using a Bayesian approach conditioned upon surface classes, surface temperature, and total precipitable water. This retrieval algorithm is used for all PMW sensors except Sondeur Atmosphérique du Profil d'Humidité Intertropicale par Radiométrie, which uses the Precipitation Retrieval and Profiling Scheme (Kidd, 2019; Precipitation Processing System, 2019b). The PMW estimates are gridded to 0.1° every half hour, and quasi-Lagrangian interpolation (known as "morphing") is applied to the gridded estimates to fill in gaps in the field using motion vectors computed from total precipitable water vapor from numerical models in V06 and from geosynchronous IR brightness temperatures in V05. The morphed precipitation is further supplemented, via a Kalman filter approach following Joyce and Xie (2011), with microwave-calibrated IR precipitation estimates using the Precipitation Estimation from Remotely-Sensed Information from Artificial Neural Networks-Cloud Cluster System algorithm (Hong et al., 2004; Nguyen et al., 2018). IMERG masks PMW and morphed estimates over frozen surfaces as depicted in the National Oceanic and Atmospheric Administration AutoSnow product (Romanov et al., 2000), resulting in the use of IR precipitation within 60°N/S and missing values at high latitudes. The merged satellite estimates are then calibrated by and merged with the Full and Monitoring surface gauge analyses from the Global Precipitation Climatology Centre (Schneider et al., 2014, 2015) following the approach employed by Huffman et al. (2007) for the Tropical Rainfall Measuring Mission (TRMM) Multisatellite Precipitation Analysis (TMPA).

IMERG estimates are provided in UTC time. To obtain the mean precipitation rate as a function of local solar time (LST), we first compute the mean precipitation rate at each half hour over a period sufficiently long to average out other modes of variability. We then convert the UTC time to LST time based on its longitude (ranging from -180° to +180°): LST hour = UTC hour + longitude/15, where the factor 15 represents the degree-longitude distance in an hour and LST is rounded to the nearest half hour.

To filter out noise and other possible modes of subdaily variability in some of the analyses, we utilize a low-pass filter on the mean precipitation rates as a function of LST. This is especially useful if the precipitation rates are noisy, which is typical for fine-scale estimates. Each use of the low-pass filter will be explicitly mentioned. The low-pass filter is achieved by applying a fast Fourier transform, discarding components with

TAN ET AL.

13,585


---



19448007, 2019, 22, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2019GL085395 by Capes, Wiley Online Library on [17/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU 100 ADVANCING EARTH AND SPACE SCIENCE logo

Geophysical Research Letters

10.1029/2019GL085395

<table>
  <thead>
    <tr>
        <th>LST hour</th>
        <th>AMSR2 (obs)</th>
        <th>SSMIS (obs)</th>
        <th>MHS (obs)</th>
        <th>ATMS (obs)</th>
        <th>IMERG V05B (mm/h)</th>
        <th>IMERG V06B (mm/h)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0.120</td>
<td>0.120</td>
    </tr>
<tr>
        <td>1</td>
<td>1.8e7</td>
<td>0</td>
<td>1.2e7</td>
<td>1.2e7</td>
<td>0.158</td>
<td>0.130</td>
    </tr>
<tr>
        <td>2</td>
<td>1.8e7</td>
<td>1.2e7</td>
<td>0</td>
<td>0</td>
<td>0.142</td>
<td>0.122</td>
    </tr>
<tr>
        <td>3</td>
<td>0</td>
<td>1.8e7</td>
<td>0</td>
<td>0</td>
<td>0.125</td>
<td>0.125</td>
    </tr>
<tr>
        <td>4</td>
<td>0</td>
<td>2.5e7</td>
<td>0</td>
<td>0</td>
<td>0.120</td>
<td>0.122</td>
    </tr>
<tr>
        <td>5</td>
<td>0</td>
<td>3.2e7</td>
<td>0</td>
<td>0</td>
<td>0.135</td>
<td>0.130</td>
    </tr>
<tr>
        <td>6</td>
<td>0</td>
<td>3.8e7</td>
<td>0</td>
<td>0</td>
<td>0.125</td>
<td>0.128</td>
    </tr>
<tr>
        <td>7</td>
<td>0</td>
<td>2.5e7</td>
<td>0</td>
<td>0</td>
<td>0.120</td>
<td>0.120</td>
    </tr>
<tr>
        <td>8</td>
<td>0</td>
<td>0</td>
<td>3.8e7</td>
<td>0</td>
<td>0.158</td>
<td>0.128</td>
    </tr>
<tr>
        <td>9</td>
<td>0</td>
<td>0</td>
<td>3.8e7</td>
<td>0</td>
<td>0.125</td>
<td>0.115</td>
    </tr>
<tr>
        <td>10</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0.128</td>
<td>0.128</td>
    </tr>
<tr>
        <td>11</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0.118</td>
<td>0.108</td>
    </tr>
<tr>
        <td>12</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0.115</td>
<td>0.105</td>
    </tr>
<tr>
        <td>13</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0.125</td>
<td>0.110</td>
    </tr>
<tr>
        <td>14</td>
<td>1.2e7</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0.132</td>
<td>0.125</td>
    </tr>
<tr>
        <td>15</td>
<td>1.8e7</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0.128</td>
<td>0.122</td>
    </tr>
<tr>
        <td>16</td>
<td>1.8e7</td>
<td>1.2e7</td>
<td>0</td>
<td>0</td>
<td>0.138</td>
<td>0.125</td>
    </tr>
<tr>
        <td>17</td>
<td>0</td>
<td>1.8e7</td>
<td>0</td>
<td>0</td>
<td>0.125</td>
<td>0.120</td>
    </tr>
<tr>
        <td>18</td>
<td>0</td>
<td>2.5e7</td>
<td>0</td>
<td>0</td>
<td>0.135</td>
<td>0.125</td>
    </tr>
<tr>
        <td>19</td>
<td>0</td>
<td>3.2e7</td>
<td>0</td>
<td>0</td>
<td>0.138</td>
<td>0.122</td>
    </tr>
<tr>
        <td>20</td>
<td>0</td>
<td>3.8e7</td>
<td>0</td>
<td>0</td>
<td>0.125</td>
<td>0.122</td>
    </tr>
<tr>
        <td>21</td>
<td>0</td>
<td>2.5e7</td>
<td>0</td>
<td>0</td>
<td>0.120</td>
<td>0.125</td>
    </tr>
<tr>
        <td>22</td>
<td>0</td>
<td>0</td>
<td>3.8e7</td>
<td>0</td>
<td>0.175</td>
<td>0.138</td>
    </tr>
<tr>
        <td>23</td>
<td>0</td>
<td>0</td>
<td>3.8e7</td>
<td>0</td>
<td>0.135</td>
<td>0.115</td>
    </tr>
<tr>
        <td>24</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0.120</td>
<td>0.120</td>
    </tr>
  </tbody>
</table>

Figure 1. Number of observations for Sun‐synchronous PMW sensors (top) and mean precipitation rate for IMERG V05B and V06B (bottom) as a function of LST hour from December 2014 to February 2015 over the Southern Ocean latitudes (40–60°S), where actual diurnal variability should be minimal. The sun‐synchronous PMW sensors are: Advanced Microwave Scanning Radiometer‐2 (AMSR2), Special Sensor Microwave Imager/ Sounder (SSMIS), Microwave Humidity Sounder (MHS), and Advanced Technology Microwave Sounder (ATMS).

frequencies above two cycles per day, and inverting it back. This approach extracts the mean value, the diurnal cycle, and the semidiurnal cycle, a process equivalent to a least square fit to the first and second harmonics (Dai, 2001; O & Kirstetter, 2018).

## 3. Improved Intersensor Calibration

The PMW observations used in IMERG are provided by a host of different sensors on board various satellite platforms. Due to vastly differing sensor properties, such as scan strategies (conical versus cross track), frequency channels, and footprint sizes, two sensors viewing the same precipitation system may give different precipitation estimates even when the same retrieval scheme is applied. While resolving instantaneous (i.e., random) differences remains a major challenge, the intercalibration applied in IMERG is intended to remove the mean (i.e., systematic) differences. This is especially pertinent in this study because most of these satellite platforms fly in Sun‐synchronous orbits, so they observe precipitation at the same two local times each day, although these times may change over the years due to satellite drift. Therefore, when we analyze the diurnal cycle by averaging the precipitation rate at different half hours, any imperfections in the satellite intercalibrations will introduce artificial (i.e., instrument‐induced) diurnal variability.

IMERG uses the Ku‐band Combined Radar and Radiometer (CORRA) product as the reference standard for calibration, with seasonal climatological adjustments to the Global Precipitation Climatology Project V2.3 product (Adler et al., 2003, 2016) to control for known deficiencies at certain latitudes. Ideally, all sensors would be directly calibrated to CORRA, but coincident sampling is too sparse for partner sensors due to orbit characteristics and the narrow swath of the CORRA estimates. Instead, the

intercalibration is performed in two steps. First, mean values of gridded partner sensors are adjusted to the GPM Microwave Imager (GMI) or TRMM Microwave Imager (TMI) for the GPM and TRMM eras, respectively, using static seasonal calibrations based on 1 year of coincident estimates. Second, GMI/TMI is calibrated to CORRA using dynamic 45‐day calibrations updated every 5 days, and this calibration is also applied to the GMI/TMI‐calibrated partner sensors. In V05, assumptions were made regarding sensor characteristics, so only the Special Sensor Microwave Imager/Sounder sensors were calibrated to GMI in the first step. For more details, see Huffman, Bolvin, Braithwaite, et al. (2019).

To compare the magnitudes of artificial diurnal variability, we show the mean precipitation rate from IMERG V05B and V06B as a function of LST over the Southern Ocean latitudes (40–60°S) in Figure 1, limited to the period between December 2014 and February 2015 to minimize effects of satellite drift. Absent station‐keeping, the satellite would drift, gradually changing the LST hour of a Sun‐synchronous sensor overpass, which—while desirable for analysis of the diurnal cycle—would limit our ability to isolate the effects of intersensor differences and interpolation. In this region, actual diurnal variability is relatively muted, so any high‐frequency variation across the LST is likely attributable to deficiencies in intercalibration. Indeed, V05B and V06B display variations across the LST, but this variability is reduced in V06B. In particular, the spikes in the mean precipitation rate associated with the Microwave Humidity Sounder (MHS), which may be misinterpreted as semidiurnal signals, are reduced considerably. This improved instrumental consistency is also evident in other regions (supporting information Figure S1). Therefore, the improved intercalibration in V06B allows for a more consistent precipitation retrieval over different times of the day for diurnal cycle analysis.

In addition, IMERG V06 introduced a morphing scheme based on total precipitable water vapor from numerical models, which tests show to be an improvement over the previous IR‐based scheme, especially in these Southern Ocean latitudes (Huffman, Bolvin, Nelkin, et al., 2019). In terms of its impact on diurnal cycle, this will lead to less artificial variability during times that are only occasionally sampled by non‐Sun‐

TAN ET AL.

13,586


---



19448007, 2019, 22, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2019GL085395 by Capes, Wiley Online Library on [17/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU 100 ADVANCING EARTH AND SPACE SCIENCE logo

Geophysical Research Letters

10.1029/2019GL085395

<table>
  <thead>
    <tr>
        <th>difference in diurnal peak (h)</th>
        <th>no. of pixels</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>-12</td>
<td>0</td>
    </tr>
<tr>
        <td>-9</td>
<td>0</td>
    </tr>
<tr>
        <td>-6</td>
<td>0</td>
    </tr>
<tr>
        <td>-3</td>
<td>0</td>
    </tr>
<tr>
        <td>0</td>
<td>3000</td>
    </tr>
<tr>
        <td>3</td>
<td>500</td>
    </tr>
<tr>
        <td>6</td>
<td>0</td>
    </tr>
<tr>
        <td>9</td>
<td>0</td>
    </tr>
<tr>
        <td>12</td>
<td>0</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
        <th>LST hour</th>
        <th>IMERG unfiltered</th>
        <th>IMERG filtered</th>
        <th>MRMS unfiltered</th>
        <th>MRMS filtered</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>0</td>
<td>0.08</td>
<td>0.08</td>
<td>0.08</td>
<td>0.08</td>
    </tr>
<tr>
        <td>6</td>
<td>0.10</td>
<td>0.10</td>
<td>0.12</td>
<td>0.12</td>
    </tr>
<tr>
        <td>12</td>
<td>0.25</td>
<td>0.25</td>
<td>0.28</td>
<td>0.28</td>
    </tr>
<tr>
        <td>18</td>
<td>0.43</td>
<td>0.43</td>
<td>0.48</td>
<td>0.48</td>
    </tr>
<tr>
        <td>24</td>
<td>0.08</td>
<td>0.08</td>
<td>0.08</td>
<td>0.08</td>
    </tr>
  </tbody>
</table>

**Figure 2.** The LST hour of the peak in low-pass filtered mean precipitation rate at every 0.1° over the conterminous United States during June-July-August from 2014 to 2018 in (a) IMERG and (b) MRMS; (c) the histogram of the difference in the peak LST hour for grid boxes in the outlined southeastern U.S. states; and (d) unfiltered (black) and low-pass filtered (gray) mean precipitation rates of the outlined southeastern U.S. states in IMERG (solid line) and MRMS (dashed line) as a function of LST.

synchronous PMW satellites such as GMI. Indeed, from LST Hour 10 to 13 when there is a long gap between successive Sun-synchronous PMW overpasses, the mean precipitation rate in V06B is constant (Figure 1). In contrast, the mean precipitation rate in V05B has considerable variability, including a minimum at Hour 12. Hence, the new morphing scheme creates a more consistent precipitation rate between PMW observations through a smoother interpolation.

## 4. Evaluation of the IMERG V06 Diurnal Cycle

Ground validation of diurnal variability for satellite-based precipitation products often identifies a lag in phase. Here, we use a version of the Multi-Radar Multi-Sensor (MRMS)—a U.S. radar- and gauge-based product—processed for GPM ground validation (Kirstetter et al., 2012, 2014, 2015) to evaluate the diurnal cycle in IMERG. Figures 2a and 2b examine the diurnal phase by showing the LST time of the peak in the low-pass filtered mean precipitation rate between IMERG and MRMS, respectively, for June-July-August from 2014 to 2018. Broadly speaking, the times of the diurnal peak in precipitation are comparable. In particular, the eastward propagation of nocturnal mesoscale convective systems in the central United States—a distinctive feature of summertime precipitation in this region (e.g., Carbone & Tuttle, 2008)—is well captured by IMERG. Likewise, IMERG identifies the conspicuous afternoon peak in precipitation in the southeastern United States, a region with a prominent diurnal cycle of convection amidst a general absence of strong orography. In the Gulf of Mexico near the coast, IMERG is able to discern the late morning peak in precipitation due to near-surface wind convergence (Virts et al., 2015). In the southwestern United States, there is a distinct lag in the peak time of IMERG, though the aridity of this region may limit the robustness of this result due to weaker diurnal variability.

Focusing on the southeast United States due to its strong diurnal cycle and reliable radar coverage, Figure 2c shows the histogram of the difference in peak times between IMERG and MRMS of the grid boxes in the region outlined in Figures 2a and 2b. The majority of the pixels are distributed near 0 with a small offset toward the positive. The mean difference in peak time between IMERG and MRMS is +0.59 hr, with a median of +0.5 hr and an interquartile range of 0 hr to +1.0 hr. This indicates that IMERG peaks at a time close to MRMS but with a slight lag, though no more than an hour for at least half the points. A similar analysis for the central United States nocturnal convection showed a comparable lag (Figure S2). Such a lag can be attributed to the delay in the falling hydrometeors at the level of the ice-scattering signal aloft as observed

TAN ET AL.

13,587


---



19448007, 2019, 22, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2019GL085395 by Capes, Wiley Online Library on [17/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU 100 ADVANCING EARTH AND SPACE SCIENCE logo

Geophysical Research Letters

10.1029/2019GL085395

Map showing the LST hour of the peak in mean precipitation rate over the Maritime Continent

Figure 3. The LST hour of the peak in low-pass filtered mean precipitation rate of IMERG at every 0.1° over the Maritime Continent during March-April-May from 2001 to 2018.

by the PMW sensors to the surface (e.g., Tan et al., 2018; You et al., 2019). This result contrasts with IR-based precipitation, which has a higher mean lag of +1.48 hr (Figure S3), likely because IR observes the cloud tops that are at a higher altitude. In fact, the legacy TRMM multisatellite precipitation product, TMPA, typically possesses a larger diurnal lag (e.g., Kikuchi & Wang, 2008), which is partly due to its greater IR contribution and exacerbated by its coarser time resolution of 3 hr. While IMERG uses IR precipitation, the contribution is much lower than in TMPA due to the use of morphing for interpolating between PMW observations, so the lag largely reflects the lag of PMW retrievals.

The discussion in this section thus far focused on diurnal phase; Figure 2d includes an assessment of the diurnal amplitude by showing the mean precipitation rate of the same southeastern states as Figure 2c. Apart from the slight lag, IMERG also underestimates the amplitude of the mean precipitation rate in this region compared to MRMS, consistent with the results of O and Kirstetter (2018) and Figure S4, both of which conversely also observed overestimation in other regions. Given that the mean precipitation rate is lower in IMERG than in MRMS at most times of the day in Figure 2d, this suggests that the gauges used in the IMERG bias adjustment may be underestimating the amount of precipitation. Since the gauge adjustment technique is identical between V06B and previous versions, we refer readers to O and Kirstetter (2018) for a more comprehensive evaluation of diurnal amplitude. Figure 2d also includes both the unfiltered and low-pass filtered precipitation rates, which indicate that the low-pass filter may modify the diurnal amplitude but not the phase (Watters & Battaglia, 2019). The mean IMERG precipitation rates over different years vary in diurnal amplitude to some degree, but the diurnal phase is generally consistent (Figure S5).

## 5. Global Diurnal Cycle

The general consistency of the IMERG diurnal phase against ground observations, with a slight lag of generally no more than 1 hr, encourages us to examine IMERG in other regions of the world with strong diurnal cycles. One such region is the Maritime Continent, where the intense tropical heating and complex coastlines result in an intricate diurnal pattern that is often challenging for global weather and climate models to represent accurately (e.g., Gianotti et al., 2012; Neale & Slingo, 2003; Qian, 2008).

Figure 3 shows the time of the peak in the low-pass filtered mean IMERG precipitation rate over the Maritime Continent for March-April-May (MAM) of 2001–2018, a season selected for the lack of monsoon precipitation that would otherwise reduce the prominence of the diurnal variability. The diurnal cycle is distinct over land but noisier over oceanic areas far from land, a reflection of the weaker influence of convection over ocean compared to other factors, including artificial diurnal variability (Figure 1). Precipitation reaches

TAN ET AL.

13,588


---



19448007, 2019, 22, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2019GL085395 by Capes, Wiley Online Library on [17/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU 100 ADVANCING EARTH AND SPACE SCIENCE logo

Geophysical Research Letters

10.1029/2019GL085395

<table>
  <thead>
    <tr>
        <th colspan="13">Mean precipitation rate (mm / h)</th>
    </tr>
<tr>
        <th rowspan="2">LST hour</th>
        <th colspan="4">(a) Singapore</th>
        <th colspan="4">(b) Bangladesh</th>
        <th colspan="4">(c) Lake Victoria</th>
    </tr>
<tr>
        <th>DJF</th>
        <th>MAM</th>
        <th>JJA</th>
        <th>SON</th>
        <th>DJF</th>
        <th>MAM</th>
        <th>JJA</th>
        <th>SON</th>
        <th>DJF</th>
        <th>MAM</th>
        <th>JJA</th>
        <th>SON</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>0</td>
<td>0.15</td>
<td>0.15</td>
<td>0.15</td>
<td>0.20</td>
<td>0.15</td>
<td>0.25</td>
<td>0.60</td>
<td>0.25</td>
<td>0.10</td>
<td>0.10</td>
<td>0.05</td>
<td>0.10</td>
    </tr>
<tr>
        <td>6</td>
<td>0.25</td>
<td>0.20</td>
<td>0.20</td>
<td>0.30</td>
<td>0.15</td>
<td>0.20</td>
<td>0.75</td>
<td>0.30</td>
<td>0.65</td>
<td>0.85</td>
<td>0.10</td>
<td>0.30</td>
    </tr>
<tr>
        <td>12</td>
<td>0.25</td>
<td>0.25</td>
<td>0.25</td>
<td>0.30</td>
<td>0.15</td>
<td>0.15</td>
<td>0.60</td>
<td>0.25</td>
<td>0.10</td>
<td>0.15</td>
<td>0.05</td>
<td>0.10</td>
    </tr>
<tr>
        <td>18</td>
<td>0.35</td>
<td>0.85</td>
<td>0.65</td>
<td>0.75</td>
<td>0.15</td>
<td>0.25</td>
<td>0.70</td>
<td>0.30</td>
<td>0.05</td>
<td>0.05</td>
<td>0.05</td>
<td>0.05</td>
    </tr>
<tr>
        <td>24</td>
<td>0.15</td>
<td>0.15</td>
<td>0.15</td>
<td>0.20</td>
<td>0.15</td>
<td>0.25</td>
<td>0.60</td>
<td>0.25</td>
<td>0.10</td>
<td>0.10</td>
<td>0.05</td>
<td>0.10</td>
    </tr>
  </tbody>
</table>

Figure 4. Mean precipitation rate during different months of the year for (a) Singapore, (b) Bangladesh, and (c) Lake Victoria in Africa from 2001 to 2018.

a peak in the afternoon over land near the coast, and in the late afternoon or evening further inland. Over ocean, maximum precipitation occurs around midnight close to the shore, and in the morning further offshore. This is consistent with other studies using active retrievals and ground observations (e.g., Mori et al., 2004). The time of peak precipitation over different surface type varies as a function of the distance from the coast, indicating the importance of land-sea breezes and gravity waves in modulating precipitation in this region (e.g., Birch et al., 2016; Hassim et al., 2016; Sato et al., 2009; Yokoi et al., 2017). While previous studies have used products such as TMPA to probe the diurnal cycle in the Maritime Continent (e.g., Kikuchi & Wang, 2008; Rauniyar et al., 2017; Worku et al., 2019), the lower lag and higher time resolution of IMERG reveals a more intricate and refined picture of diurnal phase.

The high spatial resolution of IMERG allows us to study regions of limited area, and its long record enables us to construct a robust diurnal profile by increasing the number of observations. To illustrate this capability, we plot the mean precipitation rate over Singapore (Figure 4a), where only the centers of three grid boxes fall within its boundary (see Text S1 on method and Figure S6 on boundary). While there is still some noise in the mean precipitation rate, the diurnal variability is clear. The afternoon peak in convection is evident across all four seasons. Furthermore, for September-October-November (SON), there is a secondary peak in the morning, which is likely caused by the eastward propagating Sumatra Squalls (Lo & Orton, 2016). Seasonal variability over Singapore is weak, with only the precipitation rates of June-July-August (JJA) being appreciably lower due to the dry southwesterly monsoon.

As a contrast to this strong diurnal variability, Figure 4b shows the mean precipitation rate over Bangladesh (Figure S7), a subtropical Asian country but with a markedly different climatology. Here, diurnal variability is more subdued; instead, there is a very strong seasonal cycle associated with the monsoon. Unlike the southwesterly monsoon in Singapore, which is dry due to the mountains in Sumatra, the southwesterly monsoon arrives in Bangladesh unimpeded from the Indian Ocean in JJA, producing copious rainfall throughout all times of the day with two distinct peaks (Islam & Uyeda, 2006). In contrast, the northeasterly monsoon originating from the Asian continent is dry and suppresses precipitation in December-January-February (DJF).

One key advantage of satellite-based precipitation products such as IMERG is their ability to provide estimates over water, where surface observations are sparse and infrequent. Figure 4c shows the mean precipitation rate over Lake Victoria (Figure S8), the largest of the African Great Lakes, where there is both diurnal variability and seasonal variability. In JJA, the Intertropical Convergence Zone migrates northward away from the region, leading to less precipitation over the lake. Precipitation is greater in other seasons, with the heaviest rainfall occurring in MAM. In terms of diurnal variability, precipitation is greatest in the morning driven by land-lake breeze, evaporation, and katabatic winds originating from surrounding topography (Anyah et al., 2006; Thiery et al., 2015). However, in MAM, the timing of peak precipitation shifts several hours earlier in the morning, with substantial precipitation falling in the hours before midnight.

# 6. Conclusions

This study demonstrated the maturing ability of the improved IMERG in depicting the diurnal cycle of precipitation around the world. An analysis over the Southern Ocean showed that the improved intercalibration and interpolation in V06 reduced artificial diurnal variability compared to V05. Evaluation against U.S.

TAN ET AL.

13,589


---


19448007, 2019, 22, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2019GL085395 by Capes, Wiley Online Library on [17/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU 100 ADVANCING EARTH AND SPACE SCIENCE logo

# Geophysical Research Letters

10.1029/2019GL085395

ground observations shows broad agreements and suggests a slight lag in the diurnal phase—but generally no more than an hour—and regional differences in the diurnal amplitude. Applying IMERG to the Maritime Continent revealed an intricate pattern in the time of the day that the precipitation peaks and thus the importance of land-sea breezes in modulating diurnal variability. Analyses leveraging the fine resolution and long record of IMERG over Singapore, Bangladesh, and Lake Victoria illustrated the interplay between diurnal and seasonal cycles, exemplifying the unprecedented ability of IMERG in capturing the diurnal variability of precipitation globally.

In the comparison against ground observations, the 0 to +1 hr lag in diurnal phase of IMERG over land is an improvement over the longer lag in TMPA, primarily due to the increased contribution from PMW and use of morphing, though the former advantage diminishes in the earlier IMERG record. This improvement in lag is consistent with other studies (e.g., Dezfuli et al., 2017; O & Kirstetter, 2018), and its magnitude is similar to the +40 min offset in O et al. (2017) and the +30 min lag in You et al. (2019). On the other hand, over ocean, PMW retrievals rely on the emission signal of both the solid and liquid hydrometeors, with the latter being closer to the surface. Therefore, we expect any lag due to fall delay in the diurnal phase of IMERG over the ocean to be even lower than the average of +0.59 hr over the southeastern United States.

Accurate representations of diurnal cycles of precipitation by global weather and climate models generally remain an ongoing goal. At the same time, sparse subdaily ground observations limit our ability to understand the diurnal cycles in many regions around the world. The results in this study suggest that IMERG has the potential to advance our understanding in regions of sparse ground measurements and complement ongoing efforts to improve its representation in global models (Covey et al., 2016; Tapiador et al., 2017, 2019; Xie et al., 2018).

### Acknowledgments

The authors thank two anonymous reviewers and the Editor Kaicun Wang for their detailed comments that improved this study. The authors also benefited from discussions with Wim Theiry and Elise Monsieurs. IMERG was provided by the NASA Goddard Space Flight Center's IMERG and PPS teams, which develop and compute IMERG as a contribution to the GPM mission, and archived at the NASA GES DISC ([https://disc.gsfc.nasa.gov/datasets/GPM_3IMERGHH_V06/summary](https://disc.gsfc.nasa.gov/datasets/GPM_3IMERGHH_V06/summary)) and online (at [https://pmm.nasa.gov/data-access/download/gpm](https://pmm.nasa.gov/data-access/download/gpm)). All authors are supported by the NASA Precipitation Measurement Missions funding (NNH18ZDA001N-PMMST). Codes used to perform the analysis in this study can be obtained online (at [https://github.com/JacksonTanBS/2019_GRL_IMERGdiurnal](https://github.com/JacksonTanBS/2019_GRL_IMERGdiurnal)).

### References

Adler, R. F., Huffman, G. J., Chang, A., Ferraro, R., Xie, P.-P., Janowiak, J., et al. (2003). The version-2 global precipitation climatology project (GPCP) monthly precipitation analysis (1979-present). *Journal of Hydrometeorology*, 4(6), 1147–1167. https://doi.org/10.1175/1525-7541(2003)004<1147:TVGPCP>2.0.CO;2004<1147:TVGPCP>2.0.CO;2)

Adler, R. F., Wang, J.-J., Sapiano, M., Huffman, G., Chiu, L., Xie, P. P., et al. (2016). Global Precipitation Climatology Project (GPCP) Climate Data Record (CDR), version 2.3 (monthly) [data set]. NOAA National Centers for Environmental Information. [https://doi.org/10.7289/v56971m6](https://doi.org/10.7289/v56971m6)

Anyah, R. O., Semazzi, F. H. M., & Xie, L. (2006). Simulated physical mechanisms associated with climate variability over Lake Victoria basin in East Africa. *Monthly Weather Review*, 134(12), 3588–3609. [https://doi.org/10.1175/MWR3266.1](https://doi.org/10.1175/MWR3266.1)

Birch, C. E., Webster, S., Peatman, S. C., Parker, D. J., Matthews, A. J., Li, Y., & Hassim, M. E. E. (2016). Scale interactions between the MJO and the western Maritime Continent. *Journal of Climate*, 29(7), 2471–2492. [https://doi.org/10.1175/JCLI-D-15-0557.1](https://doi.org/10.1175/JCLI-D-15-0557.1)

Carbone, R. E., & Tuttle, J. D. (2008). Rainfall occurrence in the U.S. warm season: The diurnal cycle. *Journal of Climate*, 21(16), 4132–4146. [https://doi.org/10.1175/2008JCLI2275.1](https://doi.org/10.1175/2008JCLI2275.1)

Covey, C., Gleckler, P. J., Doutriaux, C., Williams, D. N., Dai, A., Fasullo, J., et al. (2016). Metrics for the diurnal cycle of precipitation: Toward routine benchmarks for climate models. *Journal of Climate*, 29(12), 4461–4471. [https://doi.org/10.1175/JCLI-D-15-0664.1](https://doi.org/10.1175/JCLI-D-15-0664.1)

Dai, A. (2001). Global precipitation and thunderstorm frequencies. Part II: Diurnal variations. *Journal of Climate*, 14(6), 1112–1128. https://doi.org/10.1175/1520-0442(2001)014<1112:GPATFP>2.0.CO;2014<1112:GPATFP>2.0.CO;2)

Dai, A., Giorgi, F., & Trenberth, K. E. (1999). Observed and model-simulated diurnal cycles of precipitation over the contiguous United States. *Journal of Geophysical Research*, 104(D6), 6377–6402. [https://doi.org/10.1029/98JD02720](https://doi.org/10.1029/98JD02720)

Dai, A., Lin, X., & Hsu, K.-L. (2007). The frequency, intensity, and diurnal cycle of precipitation in surface and satellite observations over low- and mid-latitudes. *Climate Dynamics*, 29(7–8), 727–744. [https://doi.org/10.1007/s00382-007-0260-y](https://doi.org/10.1007/s00382-007-0260-y)

Dai, A., & Trenberth, K. E. (2004). The diurnal cycle and its depiction in the Community Climate System Model. *Journal of Climate*, 17(5), 930–951. https://doi.org/10.1175/1520-0442(2004)017<0930:TDCAID>2.0.CO;2017<0930:TDCAID>2.0.CO;2)

Dezfuli, A. K., Ichoku, C. M., Huffman, G. J., Mohr, K. I., Selker, J. S., van de Giesen, N., et al. (2017). Validation of IMERG precipitation in Africa. *Journal of Hydrometeorology*, 18(10), 2817–2825. [https://doi.org/10.1175/JHM-D-17-0139.1](https://doi.org/10.1175/JHM-D-17-0139.1)

Gianotti, R. L., Zhang, D., & Eltahir, E. A. B. (2012). Assessment of the Regional Climate Model Version 3 over the Maritime Continent using different cumulus parameterization and land surface schemes. *Journal of Climate*, 25(2), 638–656. [https://doi.org/10.1175/JCLI-D-11-00025.1](https://doi.org/10.1175/JCLI-D-11-00025.1)

Hassim, M. E. E., Lane, T. P., & Grabowski, W. W. (2016). The diurnal cycle of rainfall over New Guinea in convection-permitting WRF simulations. *Atmospheric Chemistry and Physics*, 16(1), 161–175. [https://doi.org/10.5194/acp-16-161-2016](https://doi.org/10.5194/acp-16-161-2016)

Hong, Y., Hsu, K.-L., Sorooshian, S., & Gao, X. (2004). Precipitation estimation from remotely sensed imagery using an artificial neural network cloud classification system. *Journal of Applied Meteorology*, 43(12), 1834–1853. [https://doi.org/10.1175/JAM2173.1](https://doi.org/10.1175/JAM2173.1)

Huffman, G. J., Bolvin, D. T., Braithwaite, D., Hsu, K., Joyce, R., Kidd, C., et al. (2019). Algorithm Theoretical Basis Document (ATBD) version 06. NASA Global Precipitation Measurement (GPM) Integrated Multi-satellitE Retrievals for GPM (IMERG) (Algorithm Theoretical Basis Document) (p. 38). NASA. Retrieved from [https://pmm.nasa.gov/data-access/downloads/gpm](https://pmm.nasa.gov/data-access/downloads/gpm)

Huffman, G. J., Bolvin, D. T., & Nelkin, E. J. (2019). IMERG V06: Changes to the morphing algorithm. *Journal of Atmospheric and Oceanic Technology*. [https://doi.org/10.1175/JTECH-D-19-0114.1](https://doi.org/10.1175/JTECH-D-19-0114.1)

Huffman, G. J., Bolvin, D. T., Nelkin, E. J., & Tan, J. (2019). Integrated Multi-satellitE Retrievals for GPM (IMERG) technical documentation (technical documentation) (p. 71). NASA. Retrieved from [https://pmm.nasa.gov/data-access/downloads/gpm](https://pmm.nasa.gov/data-access/downloads/gpm)

TAN ET AL. 13,590


---



19448007, 2019, 22, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2019GL085395 by Capes, Wiley Online Library on [17/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU 100 ADVANCING EARTH AND SPACE SCIENCE logo

# 

 Geophysical Research Letters 

 10.1029/2019GL085395

Huffman, G. J., Bolvin, D. T., Nelkin, E. J., Wolff, D. B., Adler, R. F., Gu, G., et al. (2007). The TRMM Multisatellite Precipitation Analysis (TMPA): Quasi-global, multiyear, combined-sensor precipitation estimates at fine scales. *Journal of Hydrometeorology*, 8(1), 38–55. [https://doi.org/10.1175/JHM560.1](https://doi.org/10.1175/JHM560.1)

Islam, M., & Uyeda, H. (2006). TRMM observed vertical structure and diurnal variation of precipitation in South Asia. In *2006 IEEE International Symposium on Geoscience and Remote Sensing*, (pp. 1292–1295). Denver, CO, USA: IEEE. [https://doi.org/10.1109/IGARSS.2006.334](https://doi.org/10.1109/IGARSS.2006.334)

Joyce, R. J., & Xie, P. (2011). Kalman filter-based CMORPH. *Journal of Hydrometeorology*, 12(6), 1547–1563. [https://doi.org/10.1175/JHM-D-11-022.1](https://doi.org/10.1175/JHM-D-11-022.1)

Kidd, C. (2019). Algorithm Theoretical Basis Document (ATBD) version 01-02. NASA Global Precipitation Measurement (GPM) Precipitation Retrieval and Profiling Scheme (PRPS) (algorithm theoretical basis document). NASA. Retrieved from. [https://pmm.nasa.gov/data-access/downloads/gpm](https://pmm.nasa.gov/data-access/downloads/gpm)

Kikuchi, K., & Wang, B. (2008). Diurnal precipitation regimes in the global tropics. *Journal of Climate*, 21(11), 2680–2696. [https://doi.org/10.1175/2007JCLI2051.1](https://doi.org/10.1175/2007JCLI2051.1)

Kirstetter, P.-E., Gourley, J. J., Hong, Y., Zhang, J., Moazamigoodarzi, S., Langston, C., & Arthur, A. (2015). Probabilistic precipitation rate estimates with ground-based radar networks. *Water Resources Research*, 51, 1422–1442. [https://doi.org/10.1002/2014WR015672](https://doi.org/10.1002/2014WR015672)

Kirstetter, P.-E., Hong, Y., Gourley, J. J., Cao, Q., Schwaller, M., & Petersen, W. (2014). Research framework to bridge from the Global Precipitation Measurement Mission Core Satellite to the Constellation Sensors using ground-radar-based national mosaic QPE. In V. Lakshmi, D. Alsdorf, M. Anderson, S. Biancamaria, M. Cosh, J. Entin, et al. (Eds.), *Remote sensing of the terrestrial water cycle, geophysical monograph 206*, (pp. 61–79). Hoboken, NJ: John Wiley & Sons, Inc.

Kirstetter, P.-E., Hong, Y., Gourley, J. J., Chen, S., Flamig, Z., Zhang, J., et al. (2012). Toward a framework for systematic error modeling of spaceborne precipitation radar with NOAA/NSSL ground radar-based national mosaic QPE. *Journal of Hydrometeorology*, 13(4), 1285–1300. [https://doi.org/10.1175/JHM-D-11-0139.1](https://doi.org/10.1175/JHM-D-11-0139.1)

Kummerow, C. D., Hong, Y., Olson, W. S., Yang, S., Adler, R. F., McCollum, J., et al. (2001). The evolution of the Goddard Profiling Algorithm (GPROF) for rainfall estimation from passive microwave sensors. *Journal of Applied Meteorology*, 40(11), 1801–1820. https://doi.org/10.1175/1520-0450(2001)040<1801:TEOTGP>2.0.CO;2040%3C1801:TEOTGP%3E2.0.CO;2)

Kummerow, C. D., Randel, D. L., Kulie, M., Wang, N.-Y., Ferraro, R., Joseph Munchak, S., & Petkovic, V. (2015). The evolution of the Goddard Profiling Algorithm to a fully parametric scheme. *Journal of Atmospheric and Oceanic Technology*, 32(12), 2265–2280. [https://doi.org/10.1175/JTECH-D-15-0039.1](https://doi.org/10.1175/JTECH-D-15-0039.1)

Kummerow, C. D., Ringerud, S., Crook, J., Randel, D., & Berg, W. (2011). An observationally generated a priori database for microwave rainfall retrievals. *Journal of Atmospheric and Oceanic Technology*, 28(2), 113–130. [https://doi.org/10.1175/2010JTECHA1468.1](https://doi.org/10.1175/2010JTECHA1468.1)

Li, R., Wang, K., & Qi, D. (2018). Validating the Integrated Multisatellite Retrievals for Global Precipitation Measurement in terms of diurnal variability with hourly gauge observations collected at 50,000 stations in China. *Journal of Geophysical Research: Atmospheres*, 123, 10,423–10,442. [https://doi.org/10.1029/2018JD028991](https://doi.org/10.1029/2018JD028991)

Lo, J. C.-F., & Orton, T. (2016). The general features of tropical Sumatra Squalls. *Weather*, 71(7), 175–178. [https://doi.org/10.1002/wea.2748](https://doi.org/10.1002/wea.2748)

Mayor, Y., Tereshchenko, I., Fonseca-Hernández, M., Pantoja, D., & Montes, J. (2017). Evaluation of error in IMERG precipitation estimates under different topographic conditions and temporal scales over Mexico. *Remote Sensing*, 9(5), 503. [https://doi.org/10.3390/rs9050503](https://doi.org/10.3390/rs9050503)

Mori, S., Jun-Ichi, H., Tauhid, Y. I., Yamanaka, M. D., Okamoto, N., Murata, F., et al. (2004). Diurnal land–sea rainfall peak migration over Sumatra Island, Indonesian Maritime Continent, observed by TRMM satellite and intensive rawinsonde soundings. *Monthly Weather Review*, 132(8), 2021–2039. https://doi.org/10.1175/1520-0493(2004)132<2021:DLRPMO>2.0.CO;2132%3C2021:DLRPMO%3E2.0.CO;2)

Neale, R., & Slingo, J. (2003). The Maritime Continent and its role in the global climate: A GCM study. *Journal of Climate*, 16(5), 834–848. https://doi.org/10.1175/1520-0442(2003)016<0834:TMCAIR>2.0.CO;2016%3C0834:TMCAIR%3E2.0.CO;2)

Nguyen, P., Ombadi, M., Sorooshian, S., Hsu, K., AghaKouchak, A., Braithwaite, D., et al. (2018). The PERSIANN family of global satellite precipitation data: A review and evaluation of products. *Hydrology and Earth System Sciences*, 22(11), 5801–5816. [https://doi.org/10.5194/hess-22-5801-2018](https://doi.org/10.5194/hess-22-5801-2018)

Oliveira, R., Maggioni, V., Vila, D., & Morales, C. (2016). Characteristics and diurnal cycle of GPM rainfall estimates over the central Amazon Region. *Remote Sensing*, 8(7), 544. [https://doi.org/10.3390/rs8070544](https://doi.org/10.3390/rs8070544)

Peatman, S. C., Matthews, A. J., & Stevens, D. P. (2014). Propagation of the Madden-Julian Oscillation through the Maritime Continent and scale interaction with the diurnal cycle of precipitation: MJO propagation and scale interaction with the diurnal cycle. *Quarterly Journal of the Royal Meteorological Society*, 140(680), 814–825. [https://doi.org/10.1002/qj.2161](https://doi.org/10.1002/qj.2161)

Precipitation Processing System. (2017). GPM GMI (GPROF) Radiometer precipitation profiling L2A 1.5 hours 13 km V05 [Data set]. NASA Goddard Earth Sciences Data and Information Services Center. [https://doi.org/10.5067/gpm/gmi/gpm/gprof/2a/05](https://doi.org/10.5067/gpm/gmi/gpm/gprof/2a/05)

Precipitation Processing System. (2019a). GPM IMERG final precipitation L3 half hourly 0.1 degree × 0.1 degree V06 [Data set]. NASA Goddard Earth Sciences Data and Information Services Center. [https://doi.org/10.5067/gpm/imerg/3b-hh/06](https://doi.org/10.5067/gpm/imerg/3b-hh/06)

Precipitation Processing System. (2019b). GPM SAPHIR on MT1 (PRPS) Radiometer precipitation profiling L2 1.5 hours 10 km V06 [Data set]. NASA Goddard Earth Sciences Data and Information Services Center. [https://doi.org/10.5067/gpm/saphir/mt1/prps/2a/06](https://doi.org/10.5067/gpm/saphir/mt1/prps/2a/06)

Qian, J.-H. (2008). Why precipitation is mostly concentrated over islands in the Maritime Continent. *Journal of the Atmospheric Sciences*, 65(4), 1428–1441. [https://doi.org/10.1175/2007JAS2422.1](https://doi.org/10.1175/2007JAS2422.1)

Rauniyar, S. P., Protat, A., & Kanamori, H. (2017). Uncertainties in TRMM-Era multisatellite-based tropical rainfall estimates over the Maritime Continent: Uncertainties in SBR rainfall estimates. *Earth and Space Science*, 4, 275–302. [https://doi.org/10.1002/2017EA000279](https://doi.org/10.1002/2017EA000279)

Romanov, P., Gutman, G., & Csiszar, I. (2000). Automated monitoring of snow cover over North America with multispectral satellite data. *Journal of Applied Meteorology*, 39(11), 1866–1880. https://doi.org/10.1175/1520-0450(2000)039<1866:AMOSCO>2.0.CO;2039%3C1866:AMOSCO%3E2.0.CO%3B2)

Sato, T., Miura, H., Satoh, M., Takayabu, Y. N., & Wang, Y. (2009). Diurnal cycle of precipitation in the tropics simulated in a global cloud-resolving model. *Journal of Climate*, 22(18), 4809–4826. [https://doi.org/10.1175/2009JCLI2890.1](https://doi.org/10.1175/2009JCLI2890.1)

Schneider, U., Becker, A., Finger, P., Meyer-Christoffer, A., Rudolf, B., & Ziese, M. (2015). GPCC full data reanalysis version 7.0 at 1.0°: Monthly land-surface precipitation from rain-gauges built on GTS-based and historic data: Gridded monthly totals [data set]. Global Precipitation Climatology Centre (GPCC) at Deutscher Wetterdienst. [https://doi.org/10.5676/dwd_gpcc/fd_m_v7_100](https://doi.org/10.5676/dwd_gpcc/fd_m_v7_100)

Schneider, U., Becker, A., Finger, P., Meyer-Christoffer, A., Ziese, M., & Rudolf, B. (2014). GPCC's new land surface precipitation climatology based on quality-controlled in situ data and its role in quantifying the global water cycle. *Theoretical and Applied Climatology*, 115(1–2), 15–40. [https://doi.org/10.1007/s00704-013-0860-x](https://doi.org/10.1007/s00704-013-0860-x)

TAN ET AL.

13,591


---



19448007, 2019, 22, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2019GL085395 by Capes, Wiley Online Library on [17/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU 100 ADVANCING EARTH AND SPACE SCIENCE logo

# Geophysical Research Letters

10.1029/2019GL085395

O, S., Foelsche, U., Kirchengast, G., Fuchsberger, J., Tan, J., & Petersen, W. A. (2017). Evaluation of GPM IMERG early, late, and final rainfall estimates using WegenerNet gauge data in southeastern Austria. *Hydrology and Earth System Sciences*, 21(12), 6559–6572. [https://doi.org/10.5194/hess-21-6559-2017](https://doi.org/10.5194/hess-21-6559-2017)

O, S., & Kirstetter, P. (2018). Evaluation of diurnal variation of GPM IMERG-derived summer precipitation over the contiguous US using MRMS data. *Quarterly Journal of the Royal Meteorological Society*, 144(S1), 270–281. [https://doi.org/10.1002/qj.3218](https://doi.org/10.1002/qj.3218)

Tan, J., Petersen, W. A., Kirchengast, G., Goodrich, D. C., & Wolff, D. B. (2018). Evaluation of global precipitation measurement rainfall estimates against three dense gauge networks. *Journal of Hydrometeorology*, 19(3), 517–532. [https://doi.org/10.1175/JHM-D-17-0174.1](https://doi.org/10.1175/JHM-D-17-0174.1)

Tang, G., Ma, Y., Long, D., Zhong, L., & Hong, Y. (2016). Evaluation of GPM Day-1 IMERG and TMPA version-7 legacy products over Mainland China at multiple spatiotemporal scales. *Journal of Hydrology*, 533, 152–167. [https://doi.org/10.1016/j.jhydrol.2015.12.008](https://doi.org/10.1016/j.jhydrol.2015.12.008)

Tapiador, F. J., Navarro, A., Levizzani, V., García-Ortega, E., Huffman, G. J., Kidd, C., et al. (2017). Global precipitation measurements for validating climate models. *Atmospheric Research*, 197, 1–20. [https://doi.org/10.1016/j.atmosres.2017.06.021](https://doi.org/10.1016/j.atmosres.2017.06.021)

Tapiador, F. J., Roca, R., Del Genio, A., Dewitte, B., Petersen, W., & Zhang, F. (2019). Is precipitation a good metric for model performance? *Bulletin of the American Meteorological Society*, 100(2), 223–233. [https://doi.org/10.1175/BAMS-D-17-0218.1](https://doi.org/10.1175/BAMS-D-17-0218.1)

Thiery, W., Davin, E. L., Panitz, H.-J., Demuzere, M., Lhermitte, S., & van Lipzig, N. (2015). The impact of the African Great Lakes on the regional climate. *Journal of Climate*, 28(10), 4061–4085. [https://doi.org/10.1175/JCLI-D-14-00565.1](https://doi.org/10.1175/JCLI-D-14-00565.1)

Virts, K. S., Wallace, J. M., Hutchins, M. L., & Holzworth, R. H. (2015). Diurnal and seasonal lightning variability over the Gulf Stream and the Gulf of Mexico. *Journal of the Atmospheric Sciences*, 72(7), 2657–2665. [https://doi.org/10.1175/JAS-D-14-0233.1](https://doi.org/10.1175/JAS-D-14-0233.1)

Watters, D., & Battaglia, A. (2019). The summertime diurnal cycle of precipitation derived from IMERG. *Remote Sensing*, 11(15), 1781. [https://doi.org/10.3390/rs11151781](https://doi.org/10.3390/rs11151781)

Worku, L. Y., Mekonnen, A., & Schreck, C. J. (2019). Diurnal cycle of rainfall and convection over the Maritime Continent using TRMM and ISCCP. *International Journal of Climatology*, 39(13), 5191–5200. [https://doi.org/10.1002/joc.6121](https://doi.org/10.1002/joc.6121)

Xie, S., Neelin, D., Bechtold, P., & Ma, H.-Y. (2018, June 24). Improving the simulation of diurnal and sub-diurnal precipitation over different climate regimes. WCRP/GEWEX/GASS. Retrieved from [https://portal.nersc.gov/project/capt/diurnal/](https://portal.nersc.gov/project/capt/diurnal/)

Yokoi, S., Mori, S., Katsumata, M., Geng, B., Yasunaga, K., Syamsudin, F., et al. (2017). Diurnal cycle of precipitation observed in the western coastal area of Sumatra Island: Offshore preconditioning by gravity waves. *Monthly Weather Review*, 145(9), 3745–3761. [https://doi.org/10.1175/MWR-D-16-0468.1](https://doi.org/10.1175/MWR-D-16-0468.1)

You, Y., Meng, H., Dong, J., & Rudlosky, S. (2019). Time-lag correlation between passive microwave measurements and surface precipitation and its impact on precipitation retrieval evaluation. *Geophysical Research Letters*, 46, 8415–8423. [https://doi.org/10.1029/2019GL083426](https://doi.org/10.1029/2019GL083426)

TAN ET AL.

13,592
13,592
