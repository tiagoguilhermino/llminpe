Check for updates

AGU ADVANCING EARTH AND SPACE SCIENCE logo

# Earth and Space Science

**RESEARCH ARTICLE**

10.1029/2022EA002595

Open access icon

# Long-Term High-Resolution Gauge Adjusted Satellite Rainfall Product Over India

**Key Points:**

* Generate a long-term high spatiotemporal resolution satellite rainfall product adjusted by rain gauge measurements over Indian mainland

* The new satellite rainfall product adjusted by gauges had a smaller error and higher correlation against independent sources

* These improvements were significant in orographic regions with high rainfall amounts, mainly the western Ghats and northeastern India

Prashant Kumar<sup>1</sup> ORCID icon, Atul K. Varma<sup>1</sup> ORCID icon, Takuji Kubota<sup>2</sup> ORCID icon, Moeka Yamaji<sup>2</sup>, Tomoko Tashima<sup>2</sup>, Tomoaki Mega<sup>3</sup>, and Tomoo Ushio<sup>3</sup>

<sup>1</sup>Atmospheric and Oceanic Sciences Group, EPSA, Space Applications Centre, ISRO, Ahmedabad, India, <sup>2</sup>Earth Observation Research Center, Japan Aerospace Exploration Agency, Tsukuba, Japan, <sup>3</sup>Graduate School of Engineering, Osaka University, Suita, Japan

**Correspondence to:**

P. Kumar,
kam3545@gmail.com

**Citation:**

Kumar, P., Varma, A. K., Kubota, T., Yamaji, M., Tashima, T., Mega, T., & Ushio, T. (2022). Long-term high-resolution gauge adjusted satellite rainfall product over India. *Earth and Space Science*, 9, e2022EA002595. [https://doi.org/10.1029/2022EA002595](https://doi.org/10.1029/2022EA002595)

Received 31 AUG 2022
Accepted 3 DEC 2022

**Abstract** This study aims to create a 21-year, high spatiotemporal resolution Global Satellite Mapping of Precipitation (GSMaP) rainfall product adjusted by rain gauge measurements over the Indian mainland and highlighted the importance of the Indian Meteorological Department (IMD) daily gridded rainfall to generate gauge adjusted GSMaP rainfall products over Indian landmass. The targeted resolutions of the GSMaP are hourly and 0.1° × 0.1°. The National Oceanic and Atmospheric Administration Climate Prediction Center daily gauge analysis (0.5° × 0.5°) and IMD daily gridded rainfall (0.25° × 0.25°) were utilized to generate long-term rainfall products, GSMaP_CPC and GSMaP_IMD rainfall, respectively. After preliminary verification of the GSMaP_CPC and GSMaP_IMD rainfalls with IMD gauges, these rainfall products are evaluated for the Indian Summer Monsoon periods of 2000–2020 with comparisons of other gauge adjusted rainfall products such as the Integrated Multi-satellitE Retrievals for Global Precipitation Measurement final-run. The results suggest GSMaP_IMD has a smaller root-mean-square difference (RMSD) and higher correlation than GSMaP_CPC, evaluated against independent rainfall products. In the 3-hour mean analysis with spaceborne precipitation radar data, it is found that the value of RMSD decreases in GSMaP_IMD with respect to GSMaP_CPC throughout the day. The statistics against the hourly dense gauge network suggests that the GSMaP_IMD is more effective in capturing large spatiotemporal rainfall variation. Thus, validation results with the independent sources suggest that GSMaP_IMD rainfall generally improved over GSMaP_CPC rainfall. These improvements are significant in orographic regions with high rainfall amounts, mainly the western Ghats and northeastern parts of India.

**Author Contributions:**

**Conceptualization:** Prashant Kumar, Takuji Kubota
**Formal analysis:** Moeka Yamaji
**Methodology:** Prashant Kumar, Tomoko Tashima, Tomoaki Mega, Tomoo Ushio
**Software:** Takuji Kubota, Moeka Yamaji, Tomoko Tashima, Tomoaki Mega
**Supervision:** Atul K. Varma, Takuji Kubota, Tomoo Ushio
**Validation:** Prashant Kumar, Takuji Kubota, Moeka Yamaji, Tomoko Tashima, Tomoaki Mega
**Writing – original draft:** Prashant Kumar, Atul K. Varma, Takuji Kubota, Moeka Yamaji

## 1. Introduction

Precipitation is the primary source of fresh water globally and a key component of the global water budget (Kidd et al., 2021). The physical processes of precipitation occur on diverse spatiotemporal scales and drive its highly variable intermittency, intensity, areal extent, and duration. This large variability poses challenges to observations, specifically by spaceborne sensors (Adler et al., 2001; Ebert et al., 2007; Kirstetter et al., 2020; Varma & Liu, 2006, 2010; Varma et al., 2004). Further, converting satellite measurements into precipitation poses challenges due to large spatial heterogeneity, rain, no-rain, and rain type (e.g., convective, stratiform, warm, and orographic) classification, the indirect nature of measurements from thermal infrared and high-frequency microwave (e.g., >85 GHz) passive instruments, the sensor resolution and sensitivity, and the retrieval algorithm (Kubota et al., 2007, 2009; Maggioni et al., 2016, 2022; Piyush et al., 2012; Varma, 2018; You et al., 2020). Hence, satellite precipitation retrievals often suffer from poorly characterized and quantified sources of uncertainty, which currently limit their applications (Beck et al., 2017; Kumar & Varma, 2017; Sun et al., 2018; Yamaji et al., 2021).

© 2022 The Authors. Earth and Space Science published by Wiley Periodicals LLC on behalf of American Geophysical Union.

This is an open access article under the terms of the Creative Commons Attribution-NonCommercial-NoDerivs License, which permits use and distribution in any medium, provided the original work is properly cited, the use is non-commercial and no modifications or adaptations are made.

To overcome these issues partially, precipitation retrievals from active and passive microwave (PMW) sensors onboard Low Earth Orbiting satellites (having higher accuracy but limited spatial and temporal resolution) are combined with infrared (IR) precipitation estimates from Geosynchronous Earth Orbiting satellites. The merging takes advantage of their higher spatiotemporal resolution and lower latency (Huffman et al., 2020; Joyce et al., 2004; Kubota et al., 2020; Ushio et al., 2009). Further rain gauge observed rainfall is crucial to calibrate IR-MW retrieved precipitation products (Mega et al., 2019; Tashima et al., 2020). Although satellite precipitation estimates, adjusted by rain gauge data, were improved, but the spatial variability of precipitation is inadequate to characterize because of the sparse distribution of gauges (Sun et al., 2018). Earlier studies also showed that

KUMAR ET AL.

1 of 18


---


23335084, 2022, 12, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2022EA002595 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU ADVANCING EARTH AND SPACE SCIENCE logo

# Earth and Space Science

10.1029/2022EA002595

high-resolution precipitation products calibrated with daily gauge measurements are more accurate than those calibrated with monthly gauge measurements (Beck et al., 2019; Sharifi & Brocca, 2022; Sharifi et al., 2019 and references therein).

The large spatiotemporal rainfall variations over India's mainland during the Indian Summer Monsoon (ISM) period make this region a unique testbed to access the quality of various global rainfall products (e.g., Brown, 2006). Further, a large part of India's population depends on ISM rainfall data, which plays a vital role in its economy and agriculture. The localized heavy rainfall events in strong wind shear associated with monsoonal systems are often tilted (Sharma et al., 2022; Shige & Kummerow, 2016) and also play a vital role that complicates rainfall estimation further. The study of ISM variability is also of interest to weather and climate modeling researchers who need precise long-term rainfall estimates.

A number of studies have been performed earlier on the evaluation of existing rainfall products (e.g., satellite only, gauge-adjusted, etc.) over India and presented their limitations. Sun et al. (2018) presented the review of 30 global rainfall data sets (reanalysis, satellite only, gauge-based, and gauge-adjusted), and noticed large uncertainties over the mountainous regions mainly over Indian mainland. Authors also mentioned the issues of sparse distribution of gauges, uncertainties in the satellite retrieval algorithm, limitations to develop merge rainfall, etc. Several studies (Bushair et al., 2019; Kumar & Varma, 2017; Kumar et al., 2021; Prakash et al., 2018; Singh et al., 2019 and references therein) have been performed earlier to evaluate the quality of satellite retrieved rainfall against rain gauge networks over India. Prakash et al. (2018) noticed smaller error in gauge adjusted Global Satellite Mapping of Precipitation (GSMaP) rainfall as compared to Integrated Multi-satellitE Retrievals for Global Precipitation Measurement (IMERG) final-run rainfall when compared with gauge measurements.

The synergy of gauge and satellite retrieved rainfall in the form of gauge-adjusted rainfall product are attempted in several previous studies over India (Gairola et al., 2015; Kumar et al., 2021 and references therein). Gairola et al. (2015) used an objective analysis method to merge rainfall products using gauges and INSAT-series satellite retrieved rainfall. Mitra et al. (2009) also used a similar approach for adjusting TRMM multisatellite precipitation analysis (TMPA) rainfall with Indian Meteorological Department (IMD) gauges over India. Recently, Kumar et al. (2021) mentioned the limitations of the objective analysis method in which uncertainties in the satellite retrievals and gauge are not considered. The large uncertainties are reported for various merged rainfall products, largely over western Ghats and the northeastern parts of India (Brown, 2006; Kumar et al., 2021; Prakash et al., 2018; Shige et al., 2014). Kumar et al. (2021) suggested that the gauge-adjusted rainfall better represents the intrinsic variability of rainfall with larger reliability. Authors also showed the importance of gauge-adjustment technique using direct, variational and hybrid methods over a region with dense gauge network in India.

This study examined a long-term (21-year) high spatiotemporal resolution GSMaP rainfall product developed for the Indian landmass using the rain gauges of the IMD. Pai et al. (2014) suggested that the IMD gridded daily rainfall product is able to reproduce large rainfall variations over Indian landmass. The aim of the study is to present benefits of GSMaP gauge adjustment by IMD gridded rainfall as compared to National Oceanic and Atmospheric Administration (NOAA) Climate Prediction Center (CPC) rainfall analysis over Indian landmass. The details of various rainfall data used in this study for developing and verifying new GSMaP rainfall products and the methodology to generate new GSMaP rainfall products are given in Section 2. The results are summarized in Section 3 and concluded in the last Section.

## 2. Data and Method

### 2.1. IMD Gauge Rainfall

This study used the data set for IMD daily gridded rainfall over the Indian mainland (0.25° × 0.25°, Table 1) for 2000–2020. IMD gridded rainfall is a standard gauge based rainfall product provided by IMD after carrying out all necessary corrections and removing the spurious observations (Pai et al., 2014, 2015). To develop this rainfall product, Pai et al. (2014) utilized 6,955 gauges in India with varying observing intervals, available from the National Data Centre, IMD, India. First station rainfall data are quality checked for the location information, code checking and typographic errors, etc. Further, standard quality control tests such as tests for typing and coding errors, missing data, duplicate station check, extreme value check, etc. are implemented on the daily station point rainfall data. The inverse distance weighted interpolation (IDW) method developed by Shepard (1968) has been performed to generate gridded product from IMD gauge stations. The IMD data for the last 24 hr (ending

KUMAR ET AL. 2 of 18


---


23335084, 2022, 12, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2022EA002595 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU ADVANCING EARTH AND SPACE SCIENCE logo

# Earth and Space Science

10.1029/2022EA002595

**Table 1**
*Details of Selected Rainfall Products*

<table>
  <thead>
    <tr>
        <th>Product name</th>
        <th>Spatial resolution</th>
        <th>Temporal resolution (in hour)</th>
        <th>Coverage</th>
        <th>Raw data</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>KSNDMC Dense Gauge Network</td>
<td>–</td>
<td>Hourly during JJAS 2018 and daily during JJAS 2016–2020</td>
<td>Over Karnataka only</td>
<td>Rain gauges</td>
    </tr>
<tr>
        <td>Estimated surface precipitation from TRMM/PR and GPM/DPR</td>
<td>~5 km</td>
<td>Depending on satellite orbits, TRMM/PR for 2000–2013, and GPM/DPR for 2014–2020</td>
<td>Global domain with satellite inclination of 65°</td>
<td>Spaceborne precipitation radar</td>
    </tr>
<tr>
        <td>IMD Gridded Gauge Rainfall</td>
<td>0.25° × 0.25°</td>
<td>Daily during 2000–2020</td>
<td>Indian landmass</td>
<td>Rain gauges</td>
    </tr>
<tr>
        <td>IMERG final-run Rainfall</td>
<td>0.1° × 0.1°</td>
<td>Half-hourly during 2000–2020</td>
<td>Global domain of 60°S to 60°N</td>
<td>IR, MW, and GPCC monthly gauge analysis</td>
    </tr>
<tr>
        <td>NCMRWF Merged Satellite Gauge Rainfall</td>
<td>0.25° × 0.25°</td>
<td>Daily during 2017–2020</td>
<td>50°E−110°E<br/>30°S–40°N</td>
<td>GPM rainfall + IMD gauges</td>
    </tr>
<tr>
        <td>GSMaP_MVK</td>
<td>0.1° × 0.1°</td>
<td>Hourly during 2000–2020</td>
<td>Global domain of 60°S to 60°N</td>
<td>IR and MW</td>
    </tr>
<tr>
        <td>GSMaP_CPC</td>
<td>0.1° × 0.1°</td>
<td>Hourly during 2000–2020</td>
<td>Global domain of 60°S to 60°N</td>
<td>IR, MW, and NOAA CPC daily Gauge analysis</td>
    </tr>
<tr>
        <td>GSMaP_IMD</td>
<td>0.1° × 0.1°</td>
<td>Hourly during 2000–2020</td>
<td>Global domain of 60°S to 60°N</td>
<td>IR, MW, NOAA CPC daily Gauge analysis and IMD gauges over India</td>
    </tr>
  </tbody>
</table>

at 08:30 Indian Standard Time (IST) [03:00 UTC {Universal Time Coordinate}]) are used for multi-stage quality control of rain gauge observations before releasing the daily gridded rainfall data set (Pai et al., 2014). Jena et al. (2020) conducted performance analysis of IMD Gridded rainfall for detecting cloudburst events over the northwest Himalayas. Pai et al. (2014) mentioned that the low and heavy rainfall areas were more realistic and better presented in the IMD gridded rainfall products. More details of the development of IMD gridded rainfall is available in Pai et al. (2014, 2015). In addition to the daily gridded rainfall data set, station-measured rainfall was also utilized in this study for verification (Table 1).

## 2.2. JAXA GSMaP Rainfall

GSMaP is a precipitation product that uses combined data from the PMW sensors in low Earth orbit and IR radiometers in geostationary Earth orbit (Kubota et al., 2020; Table 1). The GSMaP_MVK product was also created, based on a Kalman filter model that refines the precipitation rate propagated and based on the cloud-moving vector derived from two successive IR images (Ushio et al., 2009). GSMaP was developed by the Japan Aerospace Exploration Agency (JAXA) for the Global Precipitation Measurement (GPM) mission as the standard Japanese GPM product. The product Version 03 (algorithm Version 6) data were used in this study. The horizontal resolution is 0.1° × 0.1° on a lat/long grid, and the temporal resolution is 1 hour. Shige et al. (2014) studied the PWR retrievals over India. Over land, PMW algorithms relate the rainfall rate to scattering signatures from ice crystals over the spectrum of higher-frequency channels, implicitly assuming that the deeper clouds with more precipitation-sized ice are more likely to produce heavy rainfall. However, heavy rainfall can be caused by shallow orographic convection, especially in moist Asian monsoon regions including the India. Therefore, the GSMaP has made improvements to the orographic/non-orographic rainfall classification scheme and to precipitation-related variable models in a radiative transfer model calculations, as described in Shige et al. (2013, 2014), Taniguchi et al. (2013), Yamamoto and Shige (2015), and Yamamoto et al. (2017).

The operating system of the JAXA GPM mission adjusts the GSMaP product with a 3-day latency based on the NOAA/CPC unified gauge-based analysis of global daily precipitation (Kubota et al., 2020). The algorithm used an optimal estimation scheme, in which the solution is calculated by maximizing the probability density function defined in the system model (Mega et al., 2019). Kumar et al. (2021) compared GSMaP_MVK and GSMaP_Gauge (defined as GSMaP_CPC in this study) version 7 rainfall products against the dense rain gauge network of Karnataka, a southwestern state of India. Authors showed better skill of GSMaP_CPC as compared to GSMaP_MVK rainfall with larger error over the high elevation regions. In this paper, the GSMaP product

KUMAR ET AL. 3 of 18


---



23335084, 2022, 12, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2022EA002595 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU ADVANCING EARTH AND SPACE SCIENCE logo

Earth and Space Science

10.1029/2022EA002595

adjusted by the CPC rain gauges is referred to as “GSMaP_CPC” to distinguish it from the GSMaP product adjusted by the IMD rain gauges (Table 1).

## 2.3. Integrated Multi-SatellitE Retrievals for GPM (IMERG) Final-Run Rainfall

The IMERG rainfall product was developed as the standard US GPM product (Huffman et al., 2020) and is one of the products used for corrected rainfall data over the globe (Table 1). This rainfall product uses microwave sensor data and IR-based observations from all constellations of geosynchronous satellites. The monthly gauge precipitation data from Global Precipitation Climatology Centre rain gauges (Schneider et al., 2014) are utilized in the IMERG final-run product to correct the bias of satellite retrievals over the land (Huffman et al., 2020). This gauge-adjusted rainfall product provides post-real-time rainfall estimates after ~3.5 months of data retrieval. This rainfall product is available at the 0.1° spatial and half-hourly temporal resolutions. Earlier Prakash et al. (2018) noticed smaller error in gauge adjusted GSMaP rainfall as compared to IMERG final-run rainfall when compared with gauge measurements. Bushair et al. (2019) found a root-mean-square error of ~15.4 mm day<sup>-1</sup> in IMERG final-run rainfall against IMD gridded rainfall for ISM 2015 and presented larger error over high elevation regions.

## 2.4. TRMM/PR and GPM/DPR Rainfall

The independent reference data for validation was from spaceborne precipitation radar products derived from precipitation radar aboard the Tropical Rainfall Measuring Mission (TRMM/PR, Kummerow et al., 1998079%3C0809:TTRMM%3E2.0.CO;2); Kozu et al., 2006) and Dual-frequency precipitation radar onboard the GPM Core Observatory (GPM/DPR, Hou et al., 2014; Skofronick-Jackson et al., 2017). We used precipitation rate data at the estimated surface level from the TRMM/PR and GPM/DPR (Ku-band precipitation radar algorithm) Version 06A product (Seto et al., 2021) for June, July, August and September months (hereafter JJAS) of 2000–2020. In Version 06A, better continuity of the TRMM/PR and GPM/DPR data was realized by reconsidering calibration coefficients and applying common precipitation estimation algorithms. The orbit-basis rainfall data from level-2 products are gridded for 0.1° spatial resolution, the same as the GSMaP resolution used for comparisons. It should be noted that the TRMM/PR and GPM/DPR rainfall data are not directly input to the GSMaP algorithm. However, physical precipitation models based on the TRMM/PR and GPM/DPR observations are incorporated into the radiative transfer model calculation for generating look-up tables (Kubota et al., 2020).

## 2.5. NCMRWF Merged Satellite Gauge Rainfall

The National Centre for Medium-Range Weather Forecasting (NCMRWF) Merged Satellite Gauge (NMSG, Table 1) rainfall product developed by Mitra et al. (2013) is a merged daily rainfall product with 0.25° spatial resolution using background rainfall from real-time GPM (earlier TMPA) and IMD gridded rainfall over India. The authors used successive correction methods to produce the analysis on a uniform latitude-longitude grid. The authors found that the NMSG daily rainfall has additional information due to the inclusion of IMD gauge observations. In the absence of TMPA, Reddy et al. (2019) used the GPM-based GSMaP-NRT rainfall as a background for generating merged rainfall data.

## 2.6. KSNDMC Dense Gauge Network

The Indian state of Karnataka is located between 11°50′N and 18°50′N and 74°E and 78°50′E and is enclosed by a dense rain gauge network that is a unique testbed for verifying rainfall products (Kumar et al., 2021). This state has a tableland region, coastal plains, and mountain slopes in the western part of the Deccan Peninsula of India. The Karnataka State Natural Disaster Monitoring Centre (KSNDMC) deployed gauges whose data were utilized in this study to validate daily and hourly rainfall products. This study used data from the dense rain gauge network of the KSNDMC (6,502 stations in 2018 with an average rain gauge density of ~5,800 stations during JJAS of 2016–2020) during ISM 2016–2020. Around 160 stations from the KSNDMC dense gauge network (~6,100; Kumar et al., 2021) are utilized to prepare the IMD gridded rainfall product. The rain gauge sensor in this network is a tipping bucket with low tolerance made of polycarbonate or industrial standard metal (Kumar et al., 2021). The instrument's precision is 1% rainfall intensity up to 50 mm day<sup>-1</sup> and 2% rainfall intensity of 50–100 mm day<sup>-1</sup>. The original time resolution of the observations was every 15 min using a tipping count

KUMAR ET AL.

4 of 18


---



23335084, 2022, 12, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2022EA002595 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU ADVANCING EARTH AND SPACE SCIENCE logo

# Earth and Space Science

10.1029/2022EA002595

method (0.2/0.5 mm per tip) with an operating range up to 600 mm hr<sup>−1</sup>, but in this study, hourly and daily (defined as rainfall observed from the last day 08:30 IST to the current day 08:30 IST) were used for verification purposes.

## 2.7. Methodology

Recently, Kumar et al. (2021) demonstrated the importance of the gauge density and adjustment (or merging) technique for generating more trustworthy merged rainfall products for wider applications. This study was prompted by the need to improve the current gauge-adjusted daily rainfall prepared by an objective analysis (e.g., Cressman) over India. The authors showed that the maximum likelihood estimation (MLE) method based merged rainfall provide the optimal solution over an objective analysis method. Moreover, the current merged rainfall products over India are at coarser spatial (0.25° × 0.25°) and temporal (24-hr) resolution (e.g., NMSG rain). These concerns have encouraged the improvement of the merged rainfall products over India using an IMD gridded gauge-based rainfall product.

To achieve these objectives, identical experiments were conducted to adjust GSMaP_MVK rainfall using NOAA CPC rainfall analysis and IMD gridded rainfall for 2000–2020 based upon the method of Mega et al. (2019). The NOAA CPC and IMD gridded rainfall adjusted GSMaP rainfall products are GSMaP_CPC and GSMaP_IMD, respectively. The GSMaP_CPC rainfall product was recalculated in this study using the latest version of the GSMaP_Gauge software. In the previous Version 03 (algorithm Version 6), the GSMaP_Gauge software didn't consider the number of the rain gauge station within the grid box. On the other hand, the latest version can consider the number of the rain gauge station within the grid box. Re-calculation of GSMaP_CPC in this study avoided any changes due to variation in the software version. This way, we could take advantage of the IMD gridded rainfall data generated by many gauges than the GSMaP_CPC rainfall product calibrated by NOAA CPC gauge analysis. The following steps were implemented to calibrate GSMaP_MVK rainfall using IMD gridded rain data: (a) First, due to a mismatch in spatial resolution, the IMD gridded rainfall was linearly interpolated at NOAA CPC spatial resolution (0.5° × 0.5°) from its original resolution (0.25° × 0.25°) over India. (b) In the next step, the MLE method was executed to update hourly GSMaP rainfall at a finer spatial resolution (0.1° × 0.1°) using daily gridded gauge analysis at a coarser 0.5° resolution from 1 March 2000 to 31 December 2020. Thus, the GSMaP hourly data with the 0.1° × 0.1° resolution are adjusted using the data of daily rain gauges with 0.5° × 0.5° resolution.

In brief, the output from IMD interpolated rainfall data at 0.5° × 0.5° resolution is expressed as $R$ and must equal the sum of the precipitation rate for 24 hr (Equation 3 in Mega et al., 2019). According to the system model (Equations 1–5 in Mega et al., 2019), the optimal estimation of the rain rate in GSMaP_IMD at a given pixel can be derived by maximizing the probability density function of the GSMaP_IMD estimation, multiplied by the $\exp[0.5\lambda (\sum_{n=1}^{24} a_n - R)]$ term, derived by calculating the derivative of the cost function of $L(a)$ in system Equation 5. The term $\lambda$ indicates the weight of $R$. We can change the value of $\lambda$ from 0 to 1 to reflect the reliability of the gauge data. Because all cells contain observation stations in the IMD gridded rainfall, the reliability of the IMD gridded rainfall is constant here ($\lambda = 0.5$) that can tune further in future with high resolution IMD gridded rainfall. In this way, GSMaP_IMD can reduce the effect of grids having no gauge observations on the rain rate. Furthermore, we consider a 7 × 7 grid around the original cell. We assume that gauge data are reliable, when two or more stations are near a cell (i.e., within the expanded 7 × 7 grid area, comprising 49 cells). In this case, the $\lambda$ value for the central cell is set to 1. The $\lambda$ value of the central cell is set at 0.5 when the 7 × 7 grid includes only one station and is set at 0 when there are no stations. In this last case with no gauge stations, the gauge data do not affect the GSMaP rain rate within this cell. In this way, Mega et al. (2019) algorithm calculates the optimal weight for each grid based on gauge information in the grid and surrounding grids. The details of the adjustment of GSMaP rainfall using NOAA CPC analysis are given in Mega et al. (2019).

The various statistical methods (Wilks, 2006) were computed to validate the gauge-adjusted GSMaP rain against observations (e.g., gauges, satellite). The mean error (bias), the root-mean-square difference (RMSD), and the correlation coefficient were estimated for different rainfall products. Bias is an error that is used to find how gauge-adjusted rain deviated from observations and is defined as

KUMAR ET AL.

5 of 18


---



23335084, 2022, 12, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2022EA002595 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU ADVANCING EARTH AND SPACE SCIENCE logo

Earth and Space Science

10.1029/2022EA002595

$$ \text{Bias} = \frac{1}{N} \sum_{i=1}^{N} (G_i - O_i) $$

where $N$ is the number of samples; $O$ and $G$ are observed and gauge-adjusted GSMaP rainfall, respectively. Positive (negative) bias values indicate that estimates are overestimated (underestimated). RMSD measures the average error magnitude and gives greater weight to the larger errors.

$$ \text{RMSD} = \sqrt{\left(\frac{1}{N}\right) \sum_{i=1}^{N} (G_i - O_i)^2} $$

The correlation coefficient shows the relationship between observation and gauge-adjusted rain products and measures the degree of linear association between the gauge-adjusted rainfall and observations.

$$ \text{Correlation Coefficient}(r) = \frac{\left[\sum_{i=1}^{N} (O_i - \bar{O}_i) (G_i - \bar{G}_i)\right]}{\sqrt{\sum_{i=1}^{N} (O_i - \bar{O}_i)^2} \sqrt{\sum_{i=1}^{N} (G_i - \bar{G}_i)^2}}, \text{ Range : } -1 \text{ to } +1 $$

here, $\bar{O}_i$ is the average of actual values, and $\bar{G}_i$ is the average of gauge-adjusted rainfall. Furthermore, various forecast accuracy scores were also computed using a contingency table (Bhomia et al., 2019). The Probability of Detection (POD), False Alarm Ratio (FAR), and Critical Success Index (CSI) present the ability of the gauge-adjusted rain products for different rainfall thresholds.

# 3. Results and Discussions

## 3.1. Verification of GSMaP Rainfall Against IMD Gauges

Figure 1 shows the spatial distribution of the mean JJAS daily rainfall from IMD gridded rainfall, IMERG final-run, GSMaP_CPC, and GSMaP_IMD for 2000–2020. The figure shows that the IMERG final-run (Figure 1b), GSMaP_CPC (Figure 1c), and GSMaP_IMD (Figure 1d) rainfall can capture low rainfall values over northwestern India, the rain-shadow region of the southern peninsula, and northern India when verified against IMD gridded rainfall (Figure 1a). The IMERG final-run and GSMaP_CPC rainfall capture high rainfall over western Ghats to some extent, but miss the spatial distribution of high rainfall over northeast India and foothills of the Himalaya. GSMaP_IMD rainfall (Figure 1d) most closely replicates the high rainfall over these regions, showing the successful adjustment of the GSMaP rainfall with IMD gauges. Figures 1e, 1f, and 1g show spatial plot of mean difference of IMERG final-run, GSMaP_CPC and GSMaP_IMD rainfall against IMD gridded rainfall data. It shows larger error over the high elevation regions in IMERG final-run and GSMaP_CPC rainfall, mainly over the western Ghats and northeast India. These difference are reduced in the GSMaP_IMD rainfall. A few pockets of marginal differences (in Figure 1g) are observed that are mainly due to large spatial heterogeneity in orographic region. It shows the need of dense gauge rainfall product over high elevation regions. These results show that both gauge measurements and adjustment techniques are very critical to truly represent large variations of rainfall in the northeast India. Kumar et al. (2021) also recommended advance assimilation method to improve gauge adjusted rainfall.

India is famous for its diverse climatic features ranging from tropical in the south to temperate and alpine in the Himalayan north. Moreover, large spatio-temporal variations are observed in different monsoon seasons that are very important to assess the robustness of new IMD gauge adjusted GSMaP rainfall. Indian landmass has been divided into 36 sub-divisions by IMD on the basis of meteorological characteristics (Figure 1 in Kelkar & Sreejith, 2020). In which, large states with varying climatic conditions are divided into smaller divisions, and small states and union territories with similar meteorological climate were combined together. The spatial distribution of the mean JJAS 2000–2020 daily rainfall from IMD gauges (gridded data), IMERG final-run, GSMaP_CPC, and GSMaP_IMD products are shown in Figure 2 for the 36 meteorological sub-divisions of India. The IMERG final-run (Figure 2b) underestimated rainfall in the western Ghats regions. The distribution of rainfall is closer to IMD gauges (Figure 2a) in GSMaP_IMD rain (Figure 2d) than in GSMaP_CPC rainfall (Figure 2c). These results reconfirm that the adjustment of IR-MW rain data using daily gauges is more accurate than data

KUMAR ET AL.

6 of 18


---



23335084, 2022, 12, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2022EA002595 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU ADVANCING EARTH AND SPACE SCIENCE logo

Earth and Space Science

10.1029/2022EA002595

Spatial distribution maps of mean daily rainfall and mean difference plots over India

**Figure 1.** Spatial distribution of mean daily rainfall from (a) IMD gridded rain, (b) IMERG final-run rain, (c) GSMaP_CPC rain, and (d) GSMaP_IMD rain, and spatial plot of mean difference of (e) IMERG final-run rain, (f) GSMaP_CPC rain, and (g) GSMaP_IMD rain against IMD gridded rain during the Indian summer monsoons (JJAS; June to September months) 2000–2020.

calibrated using monthly gauges. Overestimates were noted over northern India in a few rain regions. The figure shows larger uncertainties over northeast India when compared with IMD gridded gauge rainfall (Figure 2a). The high rainfall over Sikkim, West Bengal, Assam, and Arunachal Pradesh was missing from IMERG final-run and GSMaP_CPC data. Overestimates were noted over the Meghalaya, Tripura, and Assam states in IMERG final-run rain (Figure 2b). The precise values of satellite rainfall retrieval over the northeast part of India are still problematical, and gauge-based adjustments are required for further application. The GSMaP_IMD rain can capture these large variations over this region after adjusting with IMD gauges (Figure 2d) that demonstrate the importance of gauge observations over regions with large heterogeneity in rainfall. Overall, average rainfall values in different meteorological zones suggested adjustments to GSMaP_IMD data produce more accurate data.

Further, IMERG final-run, GSMaP_CPC, and GSMaP_IMD daily rainfall are also compared with IMD gridded rainfall (0.25° × 0.25°) and IMD stations rainfall for JJAS 2000–2020. The statistics in Figures 3d–3f are based on the average of 2475 IMD stations per day during JJAS 2000–2020. The RMSD (bias) is around 14.7 (0.2) mm day<sup>−1</sup> and 16.6 (0.3) mm day<sup>−1</sup> when IMERG final-run rainfall is compared with IMD gridded (Figure 3a) and stations rainfall (Figure 3d), respectively. The correlations are 0.61 and 0.59, contrasting with IMD gridded and IMD stations' rainfall, respectively. Similar to IMERG final-run rainfall, GSMaP_CPC rainfall is closer to IMD gridded rainfall and presented a larger error when compared with IMD rainfall. The RMSD (bias) is 13.5 (−0.8) mm day<sup>−1</sup> and 16.3 (−0.7) mm day<sup>−1</sup> when compared with IMD gridded (Figure 3b) and stations rainfall (Figure 3e). The value of correlation changes from 0.60 (against IMD gridded rain) to 0.56 (against IMD stations rain). Results show that GSMaP_IMD has fewer errors in RMSD (bias) of 6.7 (−0.3) mm day<sup>−1</sup> against IMD gridded rain (Figure 3c) than IMD stations' rain (Figure 3f). The smaller error in IMD gridded rain data at 0.25° × 0.25° suggests that the GSMaP_IMD is closer to observations that are utilized to adjust the GSMaP_MVK rain at coarser resolution (0.5° × 0.5°). RMSD (13.4 mm day<sup>−1</sup>) and bias (−0.4 mm day<sup>−1</sup>) are

KUMAR ET AL.

7 of 18


---



23335084, 2022, 12, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2022EA002595 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU ADVANCING EARTH AND SPACE SCIENCE logo

# Earth and Space Science

10.1029/2022EA002595

Spatial distribution maps of mean daily rainfall in India for (a) IMD gridded rain, (b) IMERG final-run rain, (c) GSMaP_CPC rain, and (d) GSMaP_IMD rain, with a color scale from 0 to 25 mm day⁻¹

Figure 2. Spatial distribution of mean daily rainfall from (a) IMD gridded rain, (b) IMERG final-run rain, (c) GSMaP_CPC rain, and (d) GSMaP_IMD rain for different meteorological sub-divisions of India (Figure 1 in Kelkar & Sreejith, 2020).

seen in GSMaP_IMD and are slightly larger when compared with IMD stations rain (Figure 3f). This presents the large heterogeneity of rainfall within a grid. It suggests the need for a rainfall product with high spatial resolution. RMSD (bias) decreased from 16.3 (−0.7) mm day<sup>−1</sup> in GSMaP_CPC rain (Figure 3e) to 13.4 (−0.4) mm day<sup>−1</sup> in GSMaP_IMD rain (Figure 3f) compared to IMD stations rainfall. The correlation improved from 0.56 for GSMaP_CPC rain to 0.73 for GSMaP_IMD rain. The aim of comparing selected rainfall products with both IMD gridded rainfall and IMD stations is presenting scope for further improvements in gauge adjusted rainfall product (Mega et al., 2019). Results show that the GSMaP_IMD rainfall is closer to IMD gridded rainfall product that is obvious also because IMD gridded rainfall is utilized to adjust GSMaP_IMD rainfall product at coarser spatial resolution (0.5° × 0.5°). As IMD gridded rainfall data are available at finer spatial resolution (0.25° × 0.25°), this gridded rainfall product can be utilized in native spatial resolution in future. Further, comparison with IMD station measurements presents the scope of further refinement in the generation of IMD gridded rainfall product with dense gauge network with lesser radius of influence (Pai et al., 2014).

Figure 4 (similar to Figure 5 in Kubota et al., 2007) shows the cumulative rainfall using daily rainfall during JJAS 2000–2020, comparing the IMERG final-run, GSMaP_CPC, and GSMaP_IMD to IMD gridded rain. The figure shows that the GSMaP_IMD rain is closer to IMD gridded rainfall (0.25° × 0.25°) than IMERG final-run and GSMaP_CPC rain products. The largest deviation can be seen in GSMaP_CPC rain. The probability distribution analysis (figure not shown) suggests that the IMERG final-run, GSMaP_CPC, and GSMaP_IMD rain overestimate weak rainfall intensities. This overestimation is the maximum for IMERG final-run rain. All rainfall products underestimate rainfall intensity, with the largest underestimation for IMERG final-run product for middle to larger rainfall intensities. The GSMaP_IMD rain is slightly closer to IMD rain for all ranges than IMERG final-run and GSMaP_CPC rain.

Figure 5 shows the spatial distribution of POD, FAR, and CSI for IMERG final-run, GSMaP_CPC, and GSMaP_IMD rainfall for a 0.5 mm day<sup>−1</sup> rainfall threshold with IMD gridded rainfall as reference. The values of POD are higher than 0.7 in IMERG final-run and GSMaP_CPC rain in most regions, except rain-shadow

KUMAR ET AL.

8 of 18


---



AGU ADVANCING EARTH AND SPACE SCIENCE logo

Earth and Space Science

10.1029/2022EA002595

23335084, 2022, 12, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2022EA002595 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

<table>
  <thead>
    <tr>
        <th>Panel</th>
        <th>Satellite Product</th>
        <th>Reference Data</th>
        <th>BIAS (mm day⁻¹)</th>
        <th>RMSD (mm day⁻¹)</th>
        <th>CORR</th>
        <th>NOB</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>(a)</td>
<td>IMERG</td>
<td>IMD Gridded Rain</td>
<td>0.2</td>
<td>14.7</td>
<td>0.61</td>
<td>12717768</td>
    </tr>
<tr>
        <td>(b)</td>
<td>GSMaP_CPC</td>
<td>IMD Gridded Rain</td>
<td>-0.8</td>
<td>13.5</td>
<td>0.60</td>
<td>12717768</td>
    </tr>
<tr>
        <td>(c)</td>
<td>GSMaP_IMD</td>
<td>IMD Gridded Rain</td>
<td>-0.3</td>
<td>6.7</td>
<td>0.91</td>
<td>12717768</td>
    </tr>
<tr>
        <td>(d)</td>
<td>IMERG</td>
<td>IMD Station Rain</td>
<td>0.3</td>
<td>16.6</td>
<td>0.59</td>
<td>6854435</td>
    </tr>
<tr>
        <td>(e)</td>
<td>GSMaP_CPC</td>
<td>IMD Station Rain</td>
<td>-0.7</td>
<td>16.3</td>
<td>0.56</td>
<td>6854435</td>
    </tr>
<tr>
        <td>(f)</td>
<td>GSMaP_IMD</td>
<td>IMD Station Rain</td>
<td>-0.4</td>
<td>13.4</td>
<td>0.73</td>
<td>6854435</td>
    </tr>
  </tbody>
</table>

**Figure 3.** Comparison of IMERG final-run, GSMaP_CPC, and GSMaP_IMD rainfall versus IMD gridded and stations rainfall during JJAS 2000–2020. Scatter plots (a) IMERG, (b) GSMaP_CPC, (c) GSMaP_IMD daily rainfall versus IMD gridded rainfall (at 0.25° × 0.25°), and (d) IMERG, (e) GSMaP_CPC, (f) GSMaP_IMD daily rainfall versus IMD station daily rainfall. The number of observations is abbreviated as “NOB.”

regions in the southern Indian peninsula and north and northwest India. Slightly larger values of POD are noted in GSMaP_CPC rain (Figure 5b) over the western Ghats and northeastern and central India than in IMERG final-run rain (Figure 5a). However, IMERG final-run shows larger POD over the rain-shadow region in the summer monsoon period. The value of POD is a maximum for GSMaP_IMD rain (Figure 5c), which shows the importance of adjustment using IMD gauges. The smaller values of POD over Ladakh (situated in eastern J&K, India) are largely due to the sparse distribution of IMD gauges. The spatial distributions of FAR for IMERG final-run, GSMaP_CPC, and GSMaP_IMD are shown in Figures 5d–5f. It shows larger FAR values over north and northwestern India, northeast India, and rain-shadow regions of southern peninsula India in IMERG final-run (Figure 5d) and GSMaP_CPC (Figure 5e) rain. Generally, the value of FAR is the minimum for GSMaP_IMD rain (Figure 5f). Similar to POD and FAR, CSI values show similar spatial distributions. The maximum values of CSI are achieved over central India. GSMaP_CPC (Figure 5h) shows larger CSI over orographic regions, largely western Ghats and northeast India. Only GSMaP_IMD can capture IMD gauge observed rainfall over northern India satisfactorily. The spatial distributions of POD, FAR, and CSI are considerably less at high rainfall thresholds (15.5 mm day<sup>-1</sup>), suggesting that there are large mismatches in precisely estimating the magnitude of larger rainfall in GSMaP_CPC and IMERG final-run rain (figure not shown). These results suggest that the

KUMAR ET AL.

9 of 18


---



23335084, 2022, 12, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2022EA002595 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU ADVANCING EARTH AND SPACE SCIENCE logo

Earth and Space Science

10.1029/2022EA002595

<table>
  <thead>
    <tr>
        <th>Rainfall Intensity (mm day⁻¹)</th>
        <th>Gauge</th>
        <th>IMERG</th>
        <th>GSMaP_CPC</th>
        <th>GSMaP_IMD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
    </tr>
<tr>
        <td>20</td>
<td>8.5</td>
<td>8.5</td>
<td>8.5</td>
<td>8.5</td>
    </tr>
<tr>
        <td>40</td>
<td>13.5</td>
<td>13.5</td>
<td>13.5</td>
<td>13.5</td>
    </tr>
<tr>
        <td>60</td>
<td>17.0</td>
<td>17.0</td>
<td>17.0</td>
<td>17.0</td>
    </tr>
<tr>
        <td>80</td>
<td>19.0</td>
<td>19.5</td>
<td>20.0</td>
<td>20.5</td>
    </tr>
<tr>
        <td>100</td>
<td>20.0</td>
<td>21.0</td>
<td>21.5</td>
<td>22.0</td>
    </tr>
<tr>
        <td>120</td>
<td>20.5</td>
<td>21.5</td>
<td>22.0</td>
<td>22.5</td>
    </tr>
<tr>
        <td>140</td>
<td>21.0</td>
<td>22.0</td>
<td>22.5</td>
<td>23.0</td>
    </tr>
<tr>
        <td>160</td>
<td>21.2</td>
<td>22.2</td>
<td>22.8</td>
<td>23.5</td>
    </tr>
<tr>
        <td>180</td>
<td>21.5</td>
<td>22.5</td>
<td>23.0</td>
<td>23.8</td>
    </tr>
<tr>
        <td>200</td>
<td>21.5</td>
<td>22.5</td>
<td>23.2</td>
<td>24.0</td>
    </tr>
  </tbody>
</table>

**Figure 4.** Cumulative rainfall over Indian landmass during ISM 2000–2020. The width of the bin is 1 mm day<sup>−1</sup>. This analysis is done for IMD gridded rainfall (at 0.25° × 0.25°).

Geographical maps of India showing statistical scores (a-i) for IMERG, GSMaP_CPC, and GSMaP_IMD

**Figure 5.** Statistical scores of IMERG (left), GSMaP_CPC (middle), and GSMaP_IMD (right) with IMD gridded rainfall with 0.5 mm/day threshold during JJAS 2000–2020.

KUMAR ET AL.

10 of 18


---



23335084, 2022, 12, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2022EA002595 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU ADVANCING EARTH AND SPACE SCIENCE logo

Earth and Space Science

10.1029/2022EA002595

<table>
  <thead>
    <tr>
        <th colspan="4">(a)</th>
        <th colspan="2">(b)</th>
    </tr>
<tr>
        <th>Time (Local Time)</th>
        <th>RMSD (CPC)</th>
        <th>RMSD (IMD)</th>
        <th>TRMM/GPM Mean Rain</th>
        <th>Spatial Corr (CPC)</th>
        <th>Spatial Corr (IMD)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>00</td>
<td>1.02</td>
<td>0.98</td>
<td>0.18</td>
<td>0.242</td>
<td>0.238</td>
    </tr>
<tr>
        <td>03</td>
<td>1.08</td>
<td>1.03</td>
<td>0.22</td>
<td>0.256</td>
<td>0.246</td>
    </tr>
<tr>
        <td>06</td>
<td>0.98</td>
<td>0.94</td>
<td>0.19</td>
<td>0.228</td>
<td>0.228</td>
    </tr>
<tr>
        <td>09</td>
<td>0.96</td>
<td>0.92</td>
<td>0.21</td>
<td>0.226</td>
<td>0.226</td>
    </tr>
<tr>
        <td>12</td>
<td>1.08</td>
<td>1.02</td>
<td>0.23</td>
<td>0.240</td>
<td>0.240</td>
    </tr>
<tr>
        <td>15</td>
<td>1.14</td>
<td>1.11</td>
<td>0.26</td>
<td>0.250</td>
<td>0.249</td>
    </tr>
<tr>
        <td>18</td>
<td>1.00</td>
<td>0.98</td>
<td>0.19</td>
<td>0.236</td>
<td>0.236</td>
    </tr>
<tr>
        <td>21</td>
<td>0.95</td>
<td>0.92</td>
<td>0.18</td>
<td>0.224</td>
<td>0.225</td>
    </tr>
<tr>
        <td>24</td>
<td>1.01</td>
<td>0.98</td>
<td>0.21</td>
<td>0.242</td>
<td>0.238</td>
    </tr>
  </tbody>
</table>

Figure 6. Three-hour mean values of (a) RMSD for GSMaP_CPC (solid red line) and GSMaP_IMD (dashed blue line) with mean rainfall from TRMM/GPM (gray boxes with right vertical axis), and (b) spatial correlation coefficient for GSMaP_CPC (dashed black line) and GSMaP_IMD (solid gray line).

gauge adjustments are crucial for IMERG final-run and GSMaP_CPC rain to estimate large spatial variations over India. Overall, these results suggest that the GSMaP_IMD is closer to gauge measurements over India and able to capture large rainfall variations over the Indian mainland.

## 3.2. Comparison of GSMaP Rainfall Against Independent Rainfall Products

After the preliminary verification of GSMaP_CPC and GSMaP_IMD derived rainfall against IMD gauges, the GSMaP_CPC and GSMaP_IMD rainfall products were validated using TRMM/PR and GPM/DPR products as independent satellite data sets. Due to the strong spatiotemporal rainfall heterogeneity, the use of instantaneous observations (here TRMM/PR and GPM/DPR) for verification contribute to large uncertainties. So, the TRMM/PR and GPM/DPR rainfall products are used here with averaging over a larger time period (here 3-hr) and spatial scale (here 0.1°) that reduces the rainfall uncertainties as compared to instantaneous verification. In order to compared with TRMM/PR and GPM/DPR, the GSMaP_CPC and GPM_IMD data are extracted along with the TRMM/PR and GPM/DPR orbits in the target domain, as shown in Figure 1. Figure 6 shows the comparison of RMSD and correlation between GSMaP_CPC and GSMaP_IMD in a diurnal cycle. It was found that the value of RMSD (Figure 6a) decreased in GSMaP_IMD compared with GSMaP_CPC throughout the day. The mean RMSD values of GSMaP_CPC and GSMaP_IMD were 1.03 mm hr<sup>−1</sup> and 0.95 mm hr<sup>−1</sup>, respectively. This result indicates that adjusting the satellite-based GSMaP rainfall with a localized gauge data set can improve the GSMaP quantitative accuracy by approximately 10%, more effectively than using the global gauge data set of NOAA CPC. In addition, the spatial correlation coefficient (Figure 6b) of GSMaP_IMD was better than GSMaP_CPC even though the IMD adjustment worsened the results in 15–21 LT slightly; the mean values of the spatial correlation coefficient for GSMaP_CPC and GSMaP_IMD were 0.236 and 0.241, respectively. This result indicates that the spatial pattern of rainfall can be detected more closely by IMD adjustment than NOAA CPC adjustment.

KUMAR ET AL.

11 of 18


---


23335084, 2022, 12, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2022EA002595 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU ADVANCING EARTH AND SPACE SCIENCE logo

# Earth and Space Science

10.1029/2022EA002595

It is also important to mention here that the hourly GSMaP rainfall is adjusted here from daily IMD gridded rainfall using the MLE method, whereas direct methods are adjusted rainfall at the same time period. However, it should be noted that the spatial correlation can vary depending on the limitation of observation sampling of TRMM/PR and GPM/DPR overpasses.

## 3.3. Comparison of GSMaP Rainfall Against NMSG Gridded Rainfall

The density plots of GSMaP_CPC and GSMaP_IMD daily rainfall against NMSG merged daily rainfall (Table 1) during JJAS 2017–2020 are shown in Figure 7. The NMSG rainfall product is available at 0.25° spatial resolution, requiring interpolation of GSMaP rainfall at the same resolution. The total number of collocations is 2.2 million. The value of RMSD (bias) improved from 13.9 (−0.2) mm day<sup>−1</sup> for GSMaP_CPC to 12.5 (−0.0) mm day<sup>−1</sup> in GSMaP_IMD rainfall. The correlation coefficient improved from 0.61 in GSMaP_CPC to 0.71 in GSMaP_IMD against the NMSG merged rainfall product. The verification with NMSG rainfall was also extended for monthly statistics. The values of RMSD and correlation for different months during ISM suggested that RMSD values are larger in July and August (peak monsoon months) and least in September. Generally, the correlation improved in GSMaP_IMD over GSMaP_CPC rainfall for all months (figure not shown). These results suggested that the GSMaP_IMD is closer to direct method based gauge adjusted rainfall.

<table>
  <thead>
    <tr>
        <th>Panel</th>
        <th>Metric</th>
        <th>Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>(a) GSMaP_CPC vs NMSG</td>
<td>BIAS (mm day^-1)</td>
<td>-0.2</td>
    </tr>
<tr>
        <td>(a) GSMaP_CPC vs NMSG</td>
<td>RMSD (mm day^-1)</td>
<td>13.9</td>
    </tr>
<tr>
        <td>(a) GSMaP_CPC vs NMSG</td>
<td>CORR</td>
<td>0.61</td>
    </tr>
<tr>
        <td>(a) GSMaP_CPC vs NMSG</td>
<td>NOB</td>
<td>2269688</td>
    </tr>
<tr>
        <td>(b) GSMaP_IMD vs NMSG</td>
<td>BIAS (mm day^-1)</td>
<td>-0.0</td>
    </tr>
<tr>
        <td>(b) GSMaP_IMD vs NMSG</td>
<td>RMSD (mm day^-1)</td>
<td>12.5</td>
    </tr>
<tr>
        <td>(b) GSMaP_IMD vs NMSG</td>
<td>CORR</td>
<td>0.71</td>
    </tr>
<tr>
        <td>(b) GSMaP_IMD vs NMSG</td>
<td>NOB</td>
<td>2269688</td>
    </tr>
  </tbody>
</table>

Figure 7. Comparison of daily (a) GSMaP_CPC and (b) GSMaP_IMD rainfall versus NMSG rainfall for JJAS 2017–2020.

## 3.4. Comparison of GSMaP Rainfall Against KSNDMC Dense Gauge Network

The dense rain gauge network of KSNDMC was also utilized to validate daily rainfall from IMERG final-run, GSMaP_CPC, and GSMaP_IMD during JJAS 2016–2020. There was an average of 5,800 gauges in Karnataka during this period. These gauges are well distributed over Karnataka, covering rainfall ranging from extremely high over the western Ghats to low in the rain-shadow regions. The density plot of IMERG and GSMaP rainfalls

against KSNDMC gauges observed rainfall is shown in Figure 8. The value of RMSD (bias) decreased from 15.8 (−2.9) mm day<sup>−1</sup> in GSMaP_CPC (Figure 8b) to 14.0 (−0.8) mm day<sup>−1</sup> in GSMaP_IMD rainfall (Figure 8c). Slightly fewer errors were found in the IMERG final-run rain (Figure 8a), with RMSD (bias) values of 15.0 (−0.4) mm day<sup>−1</sup>, than GSMaP_CPC rain. The correlation coefficient also improved from 0.52 in IMERG final-run and 0.4 in GSMaP_CPC to 0.56 in GSMaP_IMD rainfall. These results suggested that the GSMaP rainfall data improved considerably after IMD gauge adjustment in the state of Karnataka with independent gauges.

Further, these results are also extended for hourly rainfall verifications over Karnataka for JJAS 2018 only (Figure 9). In general, the bias is less in IMERG final-run and GSMaP_IMD rain than GSMaP_CPC rain (Figure 9a). These results reconfirmed that the GSMaP_IMD rainfall has less RMSD (Figure 9b) and a higher correlation (Figure 9c) than GSMaP_CPC rainfall. It is important to note that for this period (JJAS 2018), the performance of the GSMaP_CPC was better than IMERG final-run rain, having less RMSD and higher correlation values. These improvements were recognized for different synoptic hours. These statistics suggest that the GSMaP_IMD is more skillful in capturing the large spatiotemporal variation of rainfall over India and can be extended to diverse applications. Moreover, these results suggest improving hourly GSMaP_IMD rainfall estimation with the help of daily IMD gridded rainfall. These kinds of improvements are not possible with direct methods generally used for adjusting daily rainfall. Kumar et al. (2021) also suggested the evolution of input rainfall error in consideration in addition to the MLE method that may be a scope for further improvements in future work.

KUMAR ET AL. 12 of 18


---



23335084, 2022, 12, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2022EA002595 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU ADVANCING EARTH AND SPACE SCIENCE logo

# Earth and Space Science

# 10.1029/2022EA002595

<table>
  <thead>
    <tr>
        <th>Panel</th>
        <th>BIAS (mm day⁻¹)</th>
        <th>RMSD (mm day⁻¹)</th>
        <th>CORR</th>
        <th>NOB</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>(a) IMERG final-run</td>
<td>-0.4</td>
<td>15.0</td>
<td>0.52</td>
<td>3541744</td>
    </tr>
<tr>
        <td>(b) GSMaP_CPC</td>
<td>-2.9</td>
<td>15.8</td>
<td>0.40</td>
<td>3541744</td>
    </tr>
<tr>
        <td>(c) GSMaP_IMD</td>
<td>-0.8</td>
<td>14.0</td>
<td>0.56</td>
<td>3541744</td>
    </tr>
  </tbody>
</table>

**Figure 8.** Comparison of (a) IMERG final-run, (b) GSMaP_CPC, and (c) GSMaP_IMD daily rainfall versus KSNDMC dense rain gauge network for JJAS 2016–2020.

To examine the spatial characteristics of IMERG final-run, GSMaP_CPC, and GSMaP_IMD rain, KSNDMC gauges were divided as being in four meteorological zones—*Malnad* (the western Ghats), *Coastal* (a region of heavy rainfall), *NIK*, and *SIK* (rain-shadow region). The rainfall values are maximum in the coastal and Malnad regions and are considerably lower in the NIK and SIK rain-shadow regions. Further details about these regions are available in Kumar et al. (2021). Figure 10 compares IMERG final-run, GSMaP_CPC, and GSMaP_IMD rain to the KSNDMC dense gauge network for Malnad (Figures 10a, 10c, and 10e) and coastal (Figures 10b, 10d, and 10f) regions, mostly in high rainfall regions. The values of RMSD (bias) changed from 26.3 (−9.9) mm day<sup>−1</sup> in GSMaP_CPC to 23.1 (−4.3) mm day<sup>−1</sup> in GSMaP_IMD rain in Malnad regions during the summer monsoons 2016–2020. The RMSD (bias) errors are 24.3 (−4.1) mm day<sup>−1</sup> in IMERG final-run rain and have less bias than GSMaP_CPC rain. The correlation values improved from 0.29 in GSMaP_CPC and 0.41 in IMERG final-run rain to 0.45 in GSMaP_IMD rain for the Malnad region. The errors are slightly larger in the coastal regions, mainly for GSMaP_CPC rain. The RMSD (bias) value is 25.7 (−6.0) mm day<sup>−1</sup> in IMERG final-run, 31.2 (−16.1) mm day<sup>−1</sup> in GSMaP_CPC rain and 24.6 (−3.1) mm day<sup>−1</sup> in GSMaP_IMD products for JJAS 2016–2020. A large negative bias (−16.1 mm day<sup>−1</sup>) in GSMaP_CPC indicates that it needs further modifications to capture high rainfall over western Ghat regions that decrease after IMD gauge adjustment. In general, correlation values improved

KUMAR ET AL.

13 of 18

13 of 18


---



23335084, 2022, 12, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2022EA002595 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU ADVANCING EARTH AND SPACE SCIENCE logo

Earth and Space Science

10.1029/2022EA002595

<table>
  <thead>
    <tr>
        <th colspan="4">(a) Bias</th>
    </tr>
<tr>
        <th>Time (Local Time)</th>
        <th>IMERG Final</th>
        <th>GSMaP CPC</th>
        <th>GSMaP IMD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>00</td>
<td>-0.02</td>
<td>-0.05</td>
<td>-0.04</td>
    </tr>
<tr>
        <td>03</td>
<td>-0.07</td>
<td>-0.08</td>
<td>-0.07</td>
    </tr>
<tr>
        <td>06</td>
<td>-0.09</td>
<td>-0.12</td>
<td>-0.11</td>
    </tr>
<tr>
        <td>09</td>
<td>0.06</td>
<td>-0.05</td>
<td>-0.04</td>
    </tr>
<tr>
        <td>12</td>
<td>0.04</td>
<td>-0.02</td>
<td>-0.01</td>
    </tr>
<tr>
        <td>15</td>
<td>-0.05</td>
<td>-0.06</td>
<td>-0.05</td>
    </tr>
<tr>
        <td>18</td>
<td>-0.04</td>
<td>-0.08</td>
<td>-0.07</td>
    </tr>
<tr>
        <td>21</td>
<td>0.02</td>
<td>-0.10</td>
<td>-0.04</td>
    </tr>
<tr>
        <th colspan="4">(b) RMSD</th>
    </tr>
<tr>
        <th>Time (Local Time)</th>
        <th>IMERG Final</th>
        <th>GSMaP CPC</th>
        <th>GSMaP IMD</th>
    </tr>
<tr>
        <td>00</td>
<td>1.2</td>
<td>1.5</td>
<td>1.4</td>
    </tr>
<tr>
        <td>03</td>
<td>1.7</td>
<td>1.6</td>
<td>1.7</td>
    </tr>
<tr>
        <td>06</td>
<td>3.6</td>
<td>3.5</td>
<td>2.0</td>
    </tr>
<tr>
        <td>09</td>
<td>1.8</td>
<td>1.7</td>
<td>1.6</td>
    </tr>
<tr>
        <td>12</td>
<td>1.4</td>
<td>1.3</td>
<td>1.4</td>
    </tr>
<tr>
        <td>15</td>
<td>1.5</td>
<td>1.4</td>
<td>1.5</td>
    </tr>
<tr>
        <td>18</td>
<td>2.0</td>
<td>1.9</td>
<td>1.4</td>
    </tr>
<tr>
        <td>21</td>
<td>1.7</td>
<td>1.3</td>
<td>1.2</td>
    </tr>
<tr>
        <th colspan="4">(c) Correlation</th>
    </tr>
<tr>
        <th>Time (Local Time)</th>
        <th>IMERG Final</th>
        <th>GSMaP CPC</th>
        <th>GSMaP IMD</th>
    </tr>
<tr>
        <td>00</td>
<td>0.42</td>
<td>0.28</td>
<td>0.38</td>
    </tr>
<tr>
        <td>03</td>
<td>0.35</td>
<td>0.25</td>
<td>0.32</td>
    </tr>
<tr>
        <td>06</td>
<td>0.28</td>
<td>0.15</td>
<td>0.25</td>
    </tr>
<tr>
        <td>09</td>
<td>0.30</td>
<td>0.28</td>
<td>0.34</td>
    </tr>
<tr>
        <td>12</td>
<td>0.38</td>
<td>0.28</td>
<td>0.32</td>
    </tr>
<tr>
        <td>15</td>
<td>0.42</td>
<td>0.38</td>
<td>0.48</td>
    </tr>
<tr>
        <td>18</td>
<td>0.52</td>
<td>0.42</td>
<td>0.45</td>
    </tr>
<tr>
        <td>21</td>
<td>0.52</td>
<td>0.08</td>
<td>0.46</td>
    </tr>
  </tbody>
</table>

**Figure 9.** The hourly (a) Bias, (b) RMSD, and (c) Correlation statistics of IMERG final-run, GSMaP_CPC, and GSMaP_IMD rainfall versus KSNDMC hourly gauges during JJAS 2018.

for both Malnad and the coastal regions. These results suggest that gauge corrections are crucial over orographic and coastal regions where IR-MW retrieved rainfall is more inaccurate. Moreover, results also suggest better performance of daily gauge adjustment as compared to monthly gauge adjustment. Similar to the verification of IMERG final-run, GSMaP_CPC, and GSMaP_IMD rain in high rainfall regions, these rain products were also compared over rain-shadow regions where rainfall is much less during the summer monsoon season (Figure 11). Marginal changes are observed in error statistics for both SIK (Figures 11a, 11c, and 11e) and NIK (Figures 11b, 11d, and 11f) regions between GSMaP_CPC and GSMaP_IMD rain. In general, IMERG final-run rain has larger errors over these regions. Moreover, bias values are negligible over these regions, except in IMERG final-run rain (1.2 mm day<sup>−1</sup>) over NIK regions. The correlation is the maximum for IMERG final-run rain over these regions. Overall, these results suggest that the adjustment of satellite retrievals with gauges is most crucial in mountainous regions.

# 4. Conclusions

This study aims to adjust the GSMaP rainfall using IMD gauges over the Indian mainland and compare the performance of the GSMaP_IMD rainfall product to the operational GSMaP_CPC rainfall product adjusted by NOAA/CPC rainfall. The daily rain gauges adjust the GSMaP hourly data with a 0.1° × 0.1° resolution. In the preliminary verification, GSMaP_IMD rainfall was close to IMD gridded rainfall and IMD stations rainfall. These verifications were performed at different spatial and temporal scales for JJAS 2000–2020 and evaluated by various statistical scores. In the long-term verifications of GSMaP rainfalls against IMD gauges, the improvements were significant over orographic regions with high rainfall amounts, mainly western Ghats and northeast India. The IMERG final-run and GSMaP_CPC rainfall captured high rainfall over western Ghats but missed spatial distribution of high rainfall over the northeastern part of India and the foothills of the Himalayas. However, the GSMaP_IMD rainfall that most closely replicates the high rainfalls over these regions demonstrated the successful adjustment of the GSMaP rainfall with IMD gauge data.

Moreover, various independent sources of rainfall from gauges (the KSNDMC dense gauge network), space-borne precipitation radar retrievals (TRMM/PR and GPM/DPR), and merged rainfall products (IMERG final-run

KUMAR ET AL.

14 of 18


---



23335084, 2022, 12, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2022EA002595 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU ADVANCING EARTH AND SPACE SCIENCE logo

Earth and Space Science

10.1029/2022EA002595

<table>
  <thead>
    <tr>
        <th>Region</th>
        <th>Satellite Product</th>
        <th>Panel</th>
        <th>BIAS (mm day⁻¹)</th>
        <th>RMSD (mm day⁻¹)</th>
        <th>CORR</th>
        <th>NOB</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>Malnad</td>
<td>IMERG Final Run</td>
<td>(a)</td>
<td>4.1</td>
<td>24.3</td>
<td>0.41</td>
<td>522117</td>
    </tr>
<tr>
        <td>Coastal</td>
<td>IMERG Final Run</td>
<td>(b)</td>
<td>-6.0</td>
<td>25.7</td>
<td>0.62</td>
<td>256910</td>
    </tr>
<tr>
        <td>Malnad</td>
<td>GSMaP_CPC Rain</td>
<td>(c)</td>
<td>-9.9</td>
<td>26.3</td>
<td>0.29</td>
<td>522117</td>
    </tr>
<tr>
        <td>Coastal</td>
<td>GSMaP_CPC Rain</td>
<td>(d)</td>
<td>-16.1</td>
<td>31.2</td>
<td>0.52</td>
<td>256910</td>
    </tr>
<tr>
        <td>Malnad</td>
<td>GSMaP_IMD Rain</td>
<td>(e)</td>
<td>4.3</td>
<td>23.1</td>
<td>0.45</td>
<td>522117</td>
    </tr>
<tr>
        <td>Coastal</td>
<td>GSMaP_IMD Rain</td>
<td>(f)</td>
<td>-3.1</td>
<td>24.6</td>
<td>0.63</td>
<td>256910</td>
    </tr>
  </tbody>
</table>

**Figure 10.** Comparison of IMERG final-run, GSMaP_CPC, and GSMaP_IMD rain versus KSNDMC dense rain gauge network for (a, c, e) Malnad and (b, d, f) coastal regions for JJAS 2016–2020.

and NMSG) were utilized for rigorous verification at different temporal scales. In the three-hour mean analysis with TRMM/PR and the GPM/DPR data, it was found that the value of RMSD decreased in GSMaP_IMD with respect to GSMaP_CPC throughout the day. The statistics against the KSNDMC hourly gauges suggested that the GSMaP_IMD was more effective in capturing large spatiotemporal rainfall variation over India. Thus, validation results with the independent sources suggested that GSMaP_IMD rainfall generally improved over GSMaP_CPC rainfall. These large improvements in GSMaP_IMD rainfall are largely due to quality control gauge observations from IMD, India. The magnitude of improvements was the maximum over orographic regions compared with independent gauge observations.

The direct methods (e.g., Cressman method) are generally useful to adjust daily/monthly rainfall products. To adjust the hourly GSMaP_MVK rainfall at finer spatial resolution, the MLE method provides an optimal solution for linear as well as nonlinear forward operators (Lewis et al., 2006). It is an example of an inverse problem with infinite solution with the constraints of Gaussian distribution. Kumar et al. (2021) also presented the better performance of the MLE based method over direct method. Few methods (like Particle Filter) exist that are applicable for non-linear and non-Gaussian distribution (Kumar, 2020), but operational implementation of such methods are not feasible due to large computational requirements when emphasizing near real-time products. The large computational requirements may be mitigated in the future environment.

KUMAR ET AL.

15 of 18


---



23335084, 2022, 12, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2022EA002595 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU ADVANCING EARTH AND SPACE SCIENCE logo

Earth and Space Science

10.1029/2022EA002595

<table>
  <thead>
    <tr>
        <th>Region</th>
        <th>SIK</th>
        <th>NIK</th>
    </tr>
<tr>
        <th>Product</th>
        <th>Statistics</th>
        <th>Statistics</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>IMERG Final Rain</td>
<td>(a) BIAS = 0.4 mm day<sup>-1</sup><br/>RMSD = 8.7 mm day<sup>-1</sup><br/>CORR = 0.51<br/>NOB = 1277867</td>
<td>(b) BIAS = 1.2 mm day<sup>-1</sup><br/>RMSD = 12.4 mm day<sup>-1</sup><br/>CORR = 0.44<br/>NOB = 1513158</td>
    </tr>
<tr>
        <td>GSMaP CPC Rain</td>
<td>(c) BIAS = -0.2 mm day<sup>-1</sup><br/>RMSD = 8.5 mm day<sup>-1</sup><br/>CORR = 0.50<br/>NOB = 1277867</td>
<td>(d) BIAS = -0.5 mm day<sup>-1</sup><br/>RMSD = 11.3 mm day<sup>-1</sup><br/>CORR = 0.40<br/>NOB = 1513158</td>
    </tr>
<tr>
        <td>GSMaP IMD Rain</td>
<td>(e) BIAS = -0.1 mm day<sup>-1</sup><br/>RMSD = 8.4 mm day<sup>-1</sup><br/>CORR = 0.48<br/>NOB = 1277867</td>
<td>(f) BIAS = 0.1 mm day<sup>-1</sup><br/>RMSD = 10.9 mm day<sup>-1</sup><br/>CORR = 0.41<br/>NOB = 1513158</td>
    </tr>
  </tbody>
</table>

Figure 11. Same as Figure 10, but for (a, c, e) SIK and (b, d, f) NIK regions.

In this study IMD gridded rainfall is re-sampled at coarser resolution (0.5° × 0.5°) for adjusting GSMaP_MVK rainfall in place of using native high resolution (0.25° × 0.25°) IMD gridded rainfall. The implementation of native high-resolution IMD rainfall in Mega et al. (2019) algorithm may further improve GSMaP_IMD rainfall. Moreover, IMD gridded rainfall with information of the number of gauges in each grid may further improve GSMaP_IMD rainfall. Kumar et al. (2021) suggested making use of evolution of input rainfall (here GSMaP_MVK) error with Kalman filter to determine precise estimation of input rainfall error that may be a scope for future research.

## Data Availability Statement

The IMD gridded rainfall is available from [https://cdsp.imdpune.gov.in/home_gridded_data.php](https://cdsp.imdpune.gov.in/home_gridded_data.php). The GSMaP_Gauge rainfall is available from [https://sharaku.eorc.jaxa.jp/GSMaP/](https://sharaku.eorc.jaxa.jp/GSMaP/). The rainfall data and codes are available from [https://zenodo.org/record/7268165](https://zenodo.org/record/7268165).

KUMAR ET AL.

16 of 18


---


23335084, 2022, 12, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2022EA002595 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU ADVANCING EARTH AND SPACE SCIENCE logo

# Earth and Space Science

10.1029/2022EA002595

### Acknowledgments

The authors are thankful to the Director of the Space Applications Centre, ISRO, India. The authors also thank the Deputy Director of the EPSA and the Group Director of AOSG/EPSA, Space Applications Centre, ISRO, India. Thanks are also due to the KSNDMC and IMD teams for providing the rain gauge observations used in this study. The research described in this paper was carried out under the Implementation Arrangement between the ISRO and the JAXA concerning collaborative activities on improved rainfall products. Authors are also thankful to anonymous reviewers for their valuable comments.

### References

Adler, R. F., Kidd, C., Petty, G., Morissey, M., & Goodman, H. M. (2001). Intercomparison of global precipitation products: The third Precipitation Intercomparison Project (PIP-3). Bulletin of the American Meteorological Society, 82(7), 1377–1396. https://doi.org/10.1175/1520-0477(2001)082<1377:iogppt>2.3.co;2082<1377:iogppt>2.3.co;2)

Beck, H. E., Pan, M., Roy, T., Weedon, G. P., Pappenberger, F., Van Dijk, A. I., et al. (2019). Daily evaluation of 26 precipitation datasets using Stage-IV gauge-radar data for the CONUS. Hydrology and Earth System Sciences, 23(1), 207–224. [https://doi.org/10.5194/hess-23-207-2019](https://doi.org/10.5194/hess-23-207-2019)

Beck, H. E., Vergopolan, N., Pan, M., Levizzani, V., Van Dijk, A. I., Weedon, G. P., et al. (2017). Global-scale evaluation of 22 precipitation datasets using gauge observations and hydrological modeling. Hydrology and Earth System Sciences, 21(12), 6201–6217. [https://doi.org/10.5194/hess-21-6201-2017](https://doi.org/10.5194/hess-21-6201-2017)

Bhomia, S., Kumar, P., & Kishtawal, C. M. (2019). Evaluation of the weather research and forecasting model forecasts for Indian summer monsoon rainfall of 2014 using ground-based observations. Asia-Pacific Journal of Atmospheric Sciences, 55(4), 617–628. [https://doi.org/10.1007/s13143-019-00107-y](https://doi.org/10.1007/s13143-019-00107-y)

Brown, J. E. (2006). An analysis of the performance of hybrid infrared and microwave satellite precipitation algorithms over India and adjacent regions. Remote Sensing of Environment, 101(1), 63–81. [https://doi.org/10.1016/j.rse.2005.12.005](https://doi.org/10.1016/j.rse.2005.12.005)

Bushair, M. T., Kumar, P., & Gairola, R. M. (2019). Evaluation and assimilation of various satellite-derived rainfall products over India. International Journal of Remote Sensing, 40(14), 5315–5338. [https://doi.org/10.1080/01431161.2019.1579389](https://doi.org/10.1080/01431161.2019.1579389)

Ebert, E. E., Janowiak, J. E., & Kidd, C. (2007). Comparison of near-real-time precipitation estimates from satellite observations and numerical models. Bulletin of the American Meteorological Society, 88(1), 47–64. [https://doi.org/10.1175/bams-88-1-47](https://doi.org/10.1175/bams-88-1-47)

Gairola, R. M., Prakash, S., & Pal, P. K. (2015). Improved rainfall estimation over the Indian monsoon region by synergistic use of Kalpana-1 and rain gauge data. Atmósfera, 28(1), 51–61. [https://doi.org/10.20937/atm.2015.28.01.05](https://doi.org/10.20937/atm.2015.28.01.05)

Hou, A. Y., Kakar, R. K., Neeck, S., Azarbarzin, A. A., Kummerow, C. D., Kojima, M., et al. (2014). The global precipitation measurement mission. Bulletin of the American Meteorological Society, 95(5), 701–722. [https://doi.org/10.1175/bams-d-13-00164.1](https://doi.org/10.1175/bams-d-13-00164.1)

Huffman, G. J., Bolvin, D. T., Braithwaite, D., Hsu, K. L., Joyce, R. J., Kidd, C., et al. (2020). Integrated multi-satellite retrievals for the global precipitation measurement (GPM) mission (IMERG). In *Satellite precipitation measurement* (pp. 343–353). Springer.

Jena, P., Garg, S., & Azad, S. (2020). Performance analysis of IMD high-resolution gridded rainfall (0.25° × 0.25°) and satellite estimates for detecting cloudburst events over the northwest Himalayas. Journal of Hydrometeorology, 21(7), 1549–1569. [https://doi.org/10.1175/jhm-d-19-0287.1](https://doi.org/10.1175/jhm-d-19-0287.1)

Joyce, R. J., Janowiak, J. E., Arkin, P. A., & Xie, P. (2004). CMORPH: A method that produces global precipitation estimates from passive microwave and infrared data at high spatial and temporal resolution. Journal of Hydrometeorology, 5(3), 487–503. https://doi.org/10.1175/1525-7541(2004)005<0487:camtpg>2.0.co;2005<0487:camtpg>2.0.co;2)

Kelkar, R. R., & Sreejith, O. P. (2020). Meteorological sub-divisions of India and their geopolitical evolution from 1875 to 2020. Mausam, 71(4), 571–584.

Kidd, C., Huffman, G., Maggioni, V., Chambon, P., & Oki, R. (2021). The global satellite precipitation constellation: Current status and future requirements. Bulletin of the American Meteorological Society, 102(10), E1844–E1861. [https://doi.org/10.1175/bams-d-20-0299.1](https://doi.org/10.1175/bams-d-20-0299.1)

Kirstetter, P. E., Petersen, W. A., Kummerow, C. D., & Wolff, D. B. (2020). Integrated multi-satellite evaluation for the global precipitation measurement: Impact of precipitation types on spaceborne precipitation estimation. In *Satellite precipitation measurement* (pp. 583–608). Springer.

Kozu, T., Reddy, K. K., Mori, S., Thurai, M., Teong Ong, J., Narayana Rao, D., & Shimomai, T. (2006). Seasonal and diurnal variations of raindrop size distribution in Asian monsoon region. Journal of the Meteorological Society of Japan. Ser. II, 84(2006), 195–209. [https://doi.org/10.2151/jmsj.84a.195](https://doi.org/10.2151/jmsj.84a.195)

Kubota, T., Aonashi, K., Ushio, T., Shige, S., Takayabu, Y. N., Kachi, M., & Oki, R. (2020). Global satellite mapping of precipitation (GSMaP) products in the GPM era. In *Satellite precipitation measurement* (pp. 355–373). Springer.

Kubota, T., Shige, S., Hashizume, H., Aonashi, K., Takahashi, N., Seto, S., et al. (2007). Global precipitation map using satellite-borne microwave radiometers by the GSMaP project: Production and validation. IEEE Transactions on Geoscience and Remote Sensing, 45(7), 2259–2275. [https://doi.org/10.1109/tgrs.2007.895337](https://doi.org/10.1109/tgrs.2007.895337)

Kubota, T., Ushio, T., Shige, S., Kida, S., Kachi, M., & Okamoto, K. I. (2009). Verification of high-resolution satellite-based rainfall estimates around Japan using a gauge-calibrated ground-radar dataset. Journal of the Meteorological Society of Japan. Ser. II, 87, 203–222. [https://doi.org/10.2151/jmsj.87a.203](https://doi.org/10.2151/jmsj.87a.203)

Kumar, P. (2020). Assimilation of the rain gauge measurements using particle filter. Earth and Space Science, 7(10), e2020EA001212. [https://doi.org/10.1029/2020ea001212](https://doi.org/10.1029/2020ea001212)

Kumar, P., Gairola, R., Kubota, T., & Kishtawal, C. (2021). Hybrid assimilation of satellite rainfall product with high density gauge network to improve daily estimation: A case of Karnataka, India. Journal of the Meteorological Society of Japan. Ser. II, 99(3), 741–763. [https://doi.org/10.2151/jmsj.2021-037](https://doi.org/10.2151/jmsj.2021-037)

Kumar, P., & Varma, A. K. (2017). Assimilation of INSAT-3D hydro-estimator method retrieved rainfall for short-range weather prediction. Quarterly Journal of the Royal Meteorological Society, 143(702), 384–394. [https://doi.org/10.1002/qj.2929](https://doi.org/10.1002/qj.2929)

Kummerow, C., Barnes, W., Kozu, T., Shiue, J., & Simpson, J. (1998). The tropical rainfall measuring mission (TRMM) sensor package. Journal of Atmospheric and Oceanic Technology, 15(3), 809–817. https://doi.org/10.1175/1520-0426(1998)015<0809:ttrmmt>2.0.co;2015<0809:ttrmmt>2.0.co;2)

Lewis, J. M., Lakshmivarahan, S., & Dhall, S. (2006). Dynamic data assimilation: A least squares approach (Vol. 13). Cambridge University Press.

Maggioni, V., Massari, C., & Kidd, C. (2022). Errors and uncertainties associated with Quasi-Global satellite precipitation products. In *Precipitation science* (pp. 377–390). Elsevier.

Maggioni, V., Meyers, P. C., & Robinson, M. D. (2016). A review of merged high-resolution satellite precipitation product accuracy during the Tropical Rainfall Measuring Mission (TRMM) era. Journal of Hydrometeorology, 17(4), 1101–1117. [https://doi.org/10.1175/jhm-d-15-0190.1](https://doi.org/10.1175/jhm-d-15-0190.1)

Mega, T., Ushio, T., Matsuda, T., Kubota, T., Kachi, M., & Oki, R. (2019). Gauge-adjusted global satellite mapping of precipitation. IEEE Transactions on Geoscience and Remote Sensing, 57(4), 1928–1935. [https://doi.org/10.1109/tgrs.2018.2870199](https://doi.org/10.1109/tgrs.2018.2870199)

Mitra, A. K., Bohra, A. K., Rajeevan, M. N., & Krishnamurti, T. N. (2009). Daily Indian precipitation analysis formed from a merge of rain-gauge data with the TRMM TMPA satellite-derived rainfall estimates. Journal of the Meteorological Society of Japan. Ser. II, 87, 265–279. [https://doi.org/10.2151/jmsj.87a.265](https://doi.org/10.2151/jmsj.87a.265)

Mitra, A. K., Momin, I. M., Rajagopal, E. N., Basu, S., Rajeevan, M. N., & Krishnamurti, T. N. (2013). Gridded daily Indian monsoon rainfall for 14 seasons: Merged TRMM and IMD gauge analyzed values. Journal of Earth System Science, 122(5), 1173–1182. [https://doi.org/10.1007/s12040-013-0338-3](https://doi.org/10.1007/s12040-013-0338-3)

KUMAR ET AL. 17 of 18


---


23335084, 2022, 12, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2022EA002595 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU ADVANCING EARTH AND SPACE SCIENCE logo

# Earth and Space Science

10.1029/2022EA002595

Pai, D. S., Rajeevan, M., Sreejith, O. P., Mukhopadhyay, B., & Satbha, N. S. (2014). Development of a new high spatial resolution (0.25 × 0.25) long period (1901–2010) daily gridded rainfall data set over India and its comparison with current data sets over the region. *Mausam*, 65(1), 1–18. [https://doi.org/10.54302/mausam.v65i1.851](https://doi.org/10.54302/mausam.v65i1.851)

Pai, D. S., Sridhar, L., Badwaik, M. R., & Rajeevan, M. (2015). Analysis of the daily rainfall events over India using a new long period (1901–2010) high resolution (0.25 × 0.25) gridded rainfall data set. *Climate Dynamics*, 45(3), 755–776. [https://doi.org/10.1007/s00382-014-2307-1](https://doi.org/10.1007/s00382-014-2307-1)

Piyush, D. N., Varma, A. K., Pal, P. K., & Liu, G. (2012). An analysis of rainfall measurements over different spatio-temporal scales and potential implications for uncertainty in satellite data validation. *Journal of the Meteorological Society of Japan. Ser. II*, 90(4), 439–448. [https://doi.org/10.2151/jmsj.2012-401](https://doi.org/10.2151/jmsj.2012-401)

Prakash, S., Mitra, A. K., AghaKouchak, A., Liu, Z., Norouzi, H., & Pai, D. S. (2018). A preliminary assessment of GPM-based multi-satellite precipitation estimates over a monsoon dominated region. *Journal of Hydrology*, 556, 865–876. [https://doi.org/10.1016/j.jhydrol.2016.01.029](https://doi.org/10.1016/j.jhydrol.2016.01.029)

Reddy, M. V., Mitra, A. K., Momin, I. M., Mitra, A. K., & Pai, D. S. (2019). Evaluation and inter-comparison of high-resolution multi-satellite rainfall products over India for the southwest monsoon period. *International Journal of Remote Sensing*, 40(12), 4577–4603. [https://doi.org/10.1080/01431161.2019.1569786](https://doi.org/10.1080/01431161.2019.1569786)

Schneider, U., Becker, A., Finger, P., Meyer-Christoffer, A., Ziese, M., & Rudolf, B. (2014). GPCC's new land surface precipitation climatology based on quality-controlled in situ data and its role in quantifying the global water cycle. *Theoretical and Applied Climatology*, 115(1), 15–40. [https://doi.org/10.1007/s00704-013-0860-x](https://doi.org/10.1007/s00704-013-0860-x)

Seto, S., Iguchi, T., Meneghini, R., Awaka, J., Kubota, T., Masaki, T., & Takahashi, N. (2021). The precipitation rate retrieval algorithms for the GPM Dual-frequency Precipitation Radar. *Journal of the Meteorological Society of Japan. Ser. II*, 99(2), 205–237. [https://doi.org/10.2151/jmsj.2021-011](https://doi.org/10.2151/jmsj.2021-011)

Sharifi, E., & Brocca, L. (2022). Monitoring precipitation from space: Progress, challenges, and opportunities. In *Precipitation science* (pp. 239–255). Elsevier.

Sharifi, E., Saghafian, B., & Steinacker, R. (2019). Downscaling satellite precipitation estimates with multiple linear regression, artificial neural networks, and spline interpolation techniques. *Journal of Geophysical Research: Atmospheres*, 124(2), 789–805. [https://doi.org/10.1029/2018jd028795](https://doi.org/10.1029/2018jd028795)

Sharma, N., Varma, A. K., & Liu, G. (2022). Percentage occurrence of global tilted deep convective clouds under strong vertical wind shear. *Advances in Space Research*, 69(6), 2433–2442. [https://doi.org/10.1016/j.asr.2021.12.040](https://doi.org/10.1016/j.asr.2021.12.040)

Shepard, D. (1968). A two-dimensional interpolation function for irregularly-spaced data. In *Proceedings of the 23rd ACM national conference* (pp. 517–524).

Shige, S., Kida, S., Ashiwake, H., Kubota, T., & Aonashi, K. (2013). Improvement of TMI rain retrievals in mountainous areas. *Journal of Applied Meteorology and Climatology*, 52(1), 242–254. [https://doi.org/10.1175/jamc-d-12-074.1](https://doi.org/10.1175/jamc-d-12-074.1)

Shige, S., & Kummerow, C. D. (2016). Precipitation-top heights of heavy orographic rainfall in the Asian monsoon region. *Journal of the Atmospheric Sciences*, 73(8), 3009–3024. [https://doi.org/10.1175/jas-d-15-0271.1](https://doi.org/10.1175/jas-d-15-0271.1)

Shige, S., Yamamoto, M. K., & Taniguchi, A. (2014). Improvement of TMI rain retrieval over the Indian subcontinent. *Remote Sensing of the Terrestrial Water Cycle*, 206, 27–42. [https://doi.org/10.1002/9781118872086.ch2](https://doi.org/10.1002/9781118872086.ch2)

Singh, A. K., Tripathi, J. N., Singh, K. K., Singh, V., & Sateesh, M. (2019). Comparison of different satellite-derived rainfall products with IMD gridded data over Indian meteorological subdivisions during Indian Summer Monsoon (ISM) 2016 at weekly temporal resolution. *Journal of Hydrology*, 575, 1371–1379. [https://doi.org/10.1016/j.jhydrol.2019.02.016](https://doi.org/10.1016/j.jhydrol.2019.02.016)

Skofronick-Jackson, G., Petersen, W. A., Berg, W., Kidd, C., Stocker, E. F., Kirschbaum, D. B., et al. (2017). The Global Precipitation Measurement (GPM) mission for science and society. *Bulletin of the American Meteorological Society*, 98(8), 1679–1695. [https://doi.org/10.1175/bams-d-15-00306.1](https://doi.org/10.1175/bams-d-15-00306.1)

Sun, Q., Miao, C., Duan, Q., Ashouri, H., Sorooshian, S., & Hsu, K. L. (2018). A review of global precipitation data sets: Data sources, estimation, and intercomparisons. *Reviews of Geophysics*, 56(1), 79–107. [https://doi.org/10.1002/2017rg000574](https://doi.org/10.1002/2017rg000574)

Taniguchi, A., Shige, S., Yamamoto, M. K., Mega, T., Kida, S., Kubota, T., et al. (2013). Tomoaki Mega, Satoshi Kida, Takuji Kubota, Misako Kachi, Tomoo Ushio, and Kazumasa Aonashi. "Improvement of high-resolution satellite rainfall product for Typhoon Morakot (2009) over Taiwan. *Journal of Hydrometeorology*, 14(6), 1859–1871. [https://doi.org/10.1175/jhm-d-13-047.1](https://doi.org/10.1175/jhm-d-13-047.1)

Tashima, T., Kubota, T., Mega, T., Ushio, T., & Oki, R. (2020). Precipitation extremes monitoring using the near-real-time GSMaP product. *IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing*, 13, 5640–5651. [https://doi.org/10.1109/jstars.2020.3014881](https://doi.org/10.1109/jstars.2020.3014881)

Ushio, T., Sasashige, K., Kubota, T., Shige, S., Okamoto, K. I., Aonashi, K., et al. (2009). A Kalman filter approach to the Global Satellite Mapping of Precipitation (GSMaP) from combined passive microwave and infrared radiometric data. *Journal of the Meteorological Society of Japan. Ser. II*, 87, 137–151. [https://doi.org/10.2151/jmsj.87a.137](https://doi.org/10.2151/jmsj.87a.137)

Varma, A. K. (2018). Measurement of precipitation from satellite radiometers (visible, infrared, and microwave): Physical basis, methods, and limitations. In *Remote sensing of aerosols, clouds, and precipitation* (pp. 223–248). Elsevier.

Varma, A. K., & Liu, G. (2006). Small-scale horizontal rain-rate variability observed by satellite. *Monthly Weather Review*, 134(10), 2722–2733. [https://doi.org/10.1175/mwr3185.1](https://doi.org/10.1175/mwr3185.1)

Varma, A. K., & Liu, G. (2010). On classifying rain types using satellite microwave observations. *Journal of Geophysical Research*, 115(D7), D07204. [https://doi.org/10.1029/2009jd012058](https://doi.org/10.1029/2009jd012058)

Varma, A. K., Liu, G., & Noh, Y. J. (2004). Subpixel-scale variability of rainfall and its application to mitigate the beam-filling problem. *Journal of Geophysical Research*, 109(D18), D18210. [https://doi.org/10.1029/2004jd004968](https://doi.org/10.1029/2004jd004968)

Wilks, D. S. (2006). *Statistical methods in the atmospheric sciences* (2nd ed., 627). Academic Press.

Yamaji, M., Kubota, T., & Yamamoto, M. K. (2021). An approach to reliability characterization of GSMaP near-real-time precipitation product. *Journal of the Meteorological Society of Japan. Ser. II*, 99(3), 673–684. [https://doi.org/10.2151/jmsj.2021-033](https://doi.org/10.2151/jmsj.2021-033)

Yamamoto, M. K., & Shige, S. (2015). Implementation of an orographic/nonorographic rainfall classification scheme in the GSMaP algorithm for microwave radiometers. *Atmospheric Research*, 163, 36–47. [https://doi.org/10.1016/j.atmosres.2014.07.024](https://doi.org/10.1016/j.atmosres.2014.07.024)

Yamamoto, M. K., Shige, S., Yu, C.-K., & Chen, L.-W. (2017). Further improvement of the heavy orographic rainfall retrievals in the GSMaP algorithm for microwave radiometers. *Journal of Applied Meteorology and Climatology*, 56(9), 2607–2619. [https://doi.org/10.1175/JAMC-D-16-0332.1](https://doi.org/10.1175/JAMC-D-16-0332.1)

You, Y., Wang, N. Y., Kubota, T., Aonashi, K., Shige, S., Kachi, M., et al. (2020). Comparison of TRMM microwave imager rainfall datasets from NASA and JAXA. *Journal of Hydrometeorology*, 21(3), 377–397. [https://doi.org/10.1175/jhm-d-19-0022.1](https://doi.org/10.1175/jhm-d-19-0022.1)

KUMAR ET AL. 18 of 18
