AGU PUBLICATIONS logo JGR logo

# Journal of Geophysical Research: Atmospheres

**RESEARCH ARTICLE**

10.1002/2017JD027527

# Consistency Between Convection Allowing Model Output and Passive Microwave Satellite Observations

**Key Points:**

* The GPM satellite provides opportunities for assessing model-produced cloud and storm structures

* Simulated microwave brightness temperatures from model output have biases of opposite sign in different parts of convective storms

* Increasing supercooled liquid hydrometeor contents results in simulated Tbs that more closely match the observations

**J. L. Bytheway<sup>1,2</sup> ORCID icon and C. D. Kummerow<sup>1</sup> ORCID icon**

<sup>1</sup>Department of Atmospheric Science, Colorado State University, Fort Collins, CO, USA, <sup>2</sup>Now at Cooperative Institute for Research in Environmental Science (CIRES), Boulder, CO, USA

**Abstract** Observations from the Global Precipitation Measurement (GPM) core satellite were used along with precipitation forecasts from the High Resolution Rapid Refresh (HRRR) model to assess and interpret differences between observed and modeled storms. Using a feature-based approach, precipitating objects were identified in both the National Centers for Environmental Prediction Stage IV multisensor precipitation product and HRRR forecast at lead times of 1, 2, and 3 h at valid times corresponding to GPM overpasses. Precipitating objects were selected for further study if (a) the observed feature occurred entirely within the swath of the GPM Microwave Imager (GMI) and (b) the HRRR model predicted it at all three forecast lead times. Output from the HRRR model was used to simulate microwave brightness temperatures (Tbs), which were compared to those observed by the GMI. Simulated Tbs were found to have biases at both the warm and cold ends of the distribution, corresponding to the stratiform/anvil and convective areas of the storms, respectively. Several experiments altered both the simulation microphysics and hydrometeor classification in order to evaluate potential shortcomings in the model’s representation of precipitating clouds. In general, inconsistencies between observed and simulated brightness temperatures were most improved when transferring snow water content to supercooled liquid hydrometeor classes.

**Correspondence to:**

J. L. Bytheway,
janice.bytheway@noaa.gov

**Citation:**

Bytheway, J. L., & Kummerow, C. D. (2018). Consistency between convection allowing model output and passive microwave satellite observations. *Journal of Geophysical Research: Atmospheres*, 123, 1065–1078. [https://doi.org/10.1002/2017JD027527](https://doi.org/10.1002/2017JD027527)

Received 28 JUL 2017
Accepted 29 DEC 2017
Accepted article online 5 JAN 2018
Published online 18 JAN 2018

## 1. Introduction

Recent advances in numerical weather prediction (NWP) models have resulted in increased model resolution, both spatially and temporally. In the United States, the National Centers for Environmental Prediction (NCEP) High Resolution Rapid Refresh (HRRR) model is run operationally every hour at 3 km horizontal resolution, providing 18 h forecasts over the continental United States (CONUS; Benjamin et al., 2016). The HRRR model aims to provide accurate forecasts of convective precipitation in the short term (on the order of a few hours). Such forecasts are needed for a variety of uses with varying degrees of desired accuracy, including urban and rural water management, flood forecasting, and initialization of streamflow forecast models (Ebert, Janowiak, & Kidd, 2007; Fritsch & Carbone, 2004; Shrestha et al., 2013). Accurate forecasts of convective precipitation are also necessary to meet the National Weather Service’s (NWS) “warn-on-forecast” objectives for such severe weather events as severe thunderstorms, tornadoes, and flash flooding (Stensrud et al., 2009).

Accurate short-term forecasts of convective precipitation are challenging due to its spatially heterogeneous and rapidly varying nature (Shrestha et al., 2013; Sun et al., 2014). In fact, Lin et al. (2005) point out that, on scales of a few hours, simple advection of radar echoes often provide a better forecast than NWP output. While increased model resolution and update frequency is expected to mitigate some of these challenges, many microphysical, radiative, and dynamic processes within convective systems occur on smaller scales than models can currently resolve (Bryan & Morrison, 2012; Shrestha et al., 2013). In fact, Burghardt et al. (2014) point out that further improvement to the representation of convective precipitation systems by NWP models will require more than simply increasing model resolution to the order of a few hundred meters.

In addition to the difficulties caused by the behavior of convective precipitation systems themselves, such systems are also difficult to forecast due to the challenges that are inherent to the accurate representation of precipitation in the initial forecast state as well as the need for NWP models to “spin-up” from that initial state (Errico et al., 2007; Rogers et al., 2000; Sheng et al., 2006; Stensrud et al., 2009; Sugimoto et al., 2009; Sun et al., 2014; Weygandt & Benjamin, 2007; Weygandt et al., 2008). Rapidly updating NWP models that include precipitation-effected observations in the analysis time step can help to improve the representation of convective systems in the initial model state and reduce spin-up time. Currently, ground-based radar is the only

©2018. American Geophysical Union. All Rights Reserved.

BYTHEWAY AND KUMMEROW 1065


---



AGU logo Journal of Geophysical Research: Atmospheres 10.1002/2017JD027527

21698996, 2018, 2, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1002/2017JD027527 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
BYTHEWAY AND KUMMEROW 1066

Central U.S. study domain map with GMI 89 GHz Tbs and Ku Rainfall data

**Figure 1.** Central U.S. study domain with GMI 89 GHz Tbs and 2AKu (V05) radar surface rain rate estimate for a GPM overpass on 18 August 2015 at 21 UTC.

instrument available for frequent assimilation cycles of precipitation used in the HRRR model (Errico et al., 2007; Sun et al., 2014).

Studies by Sheng et al. (2006), Xaio and Sun (2007), Sugimoto et al. (2009), Sun et al. (2014), and Craig et al. (2012), among others, have shown improved short-range forecasts resulting from the assimilation of radar data. Direct assimilation of reflectivity to calculate rain rates via a Z-R relationship is not particularly desirable, however, due to the nonlinear and highly variable relationship between the two. Instead, Sun et al. (2014) suggest diabatic assimilation, in which radar reflectivity is used to determine a perturbation in latent heating within the column. This methodology is preferred because the change in latent heating translates to other model variables, and the introduction of the large uncertainty in the Z-R relationship can be avoided. Diabatic assimilation of radar has been employed in the HRRR since 2013 (Benjamin et al., 2016).

With the HRRR model’s increased spatial and temporal resolution and assimilation of radar data, improved quantitative precipitation forecasts (QPFs) are to be expected. Such improvements can be documented through validation studies, yet the key to continued model advancement lies in understanding why the model does or does not perform well. As such, Bytheway and Kummerow (2015) (hereafter BK15) suggest the idea of a model “assessment,” a process by which the model forecast of a particular atmospheric variable is not only validated, but an explanation for successful or poor forecast results is also sought.

ticular atmospheric variable is not only validated, but an explanation for successful or poor forecast results is also sought.

The key to improving forecasts of precipitation lies in understanding the physical and microphysical processes occurring within the precipitating cloud and accurately representing those processes within the cloud-resolving model (CRM). Since direct observations of cloud processes are typically limited to aircraft measurements taken during field campaigns, it is difficult to evaluate the accuracy of the CRM’s in-cloud processes. Observations from remote sensing platforms are thus the next best option for assessing the in-cloud processes simulated by CRMs.

The launch of the Global Precipitation Measurement (GPM) core satellite in early 2014 added a valuable source of observations of the 3-dimensional structure of storms. While ground-based radars are generally useful for identifying larger hydrometeors (such as raindrops, large snowflakes, and hail), their data are not as suitable for discriminating between smaller particles (such as cloud drops versus cloud ice). Additionally, ground-based radars tend to be less reliable in complex terrain, where beam blockage by orographic features can be an issue. Space-based observations, such as those from the GPM core satellite, can be used to infer both profiles and integrated quantities of liquid and ice as well as hydrometeor size distribution parameters, without being susceptible to interference from terrain and ground clutter. These properties can then be compared to those produced by the model, in an attempt to understand how well the model represents in cloud processes and hydrometeor distributions.

This study will aim to continue the work of BK15, evaluating model performance in the early hours of the forecast (hours 1–3) and seeking to understand differences between forecast and observed precipitating objects. Specifically, differences between observed GMI radiances and those simulated using HRRR hydrometeor and atmospheric output will be examined, and possible explanations for those differences will be sought. The current study will continue the feature-based methodology described by BK15, identifying precipitating objects in both the forecast and observations and calculating biases and location errors in the forecast. Then, using model output, microwave brightness temperatures (Tbs) at frequencies matching those present on the GPM Microwave Imager (GMI) will be calculated, compared to the observed, and possible explanations for large inconsistencies will be explored. As in BK15, this study continues to focus on warm season (June, July, and August) convective precipitation over the U.S. Central Plains (29°–49°N, 105°–85°W, Figure 1) using the NCEP Stage IV multisensor precipitation estimate to identify reference-precipitating objects. Forecasts at 1, 2, and 3 h lead times will be examined to ensure that inconsistencies at the shortest lead times are not solely a result of the model spin-up.



---



21698996, 2018, 2, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1002/2017JD027527 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU logo

# Journal of Geophysical Research: Atmospheres

10.1002/2017JD027527

The remainder of this manuscript shall be structured as follows: data set descriptions will be presented in the next section, followed by a brief discussion of both the feature matching methodology and the radiative transfer calculations. Results will then be discussed, followed by concluding remarks.

## 2. Data

### 2.1. High Resolution Rapid Refresh Model

The HRRR model has served as the NWS's operational rapid update forecast model since September 2014. It is a storm-resolving model with 3 km horizontal grid spacing and 40 vertical pressure levels. The HRRR domain covers the CONUS and is nested within the 13 km Rapid Refresh model domain, from which boundary conditions are received (Benjamin et al., 2013). The HRRR was designed to provide rapid update model guidance on convective storms in order to improve severe weather forecasting, air traffic management and aviation hazard forecasting, and warning dissemination (ESRL, 2015). Full details of the HRRR model are given in Benjamin et al. (2016).

This study makes use of both 2 and 3-dimensional output from the 2014 and 2015 experimental versions of the model. Because the model did not become operational until late 2014, only the experimental version was available for use in both years. Output variables of interest include profiles of temperature, dew point, and mixing ratios for the five hydrometeor classes (cloud and rainwater, cloud ice, snow, and graupel), as well as hourly accumulated rainfall. While there were several upgrades made to the model in April 2015 (most notably upgrading from Advanced Research WRF (WRF-ARW) v3.5.1 to v3.6 and upgrading to aerosol-aware microphysics; Thompson & Eidhammer, 2014), the behaviors observed in the forecast precipitation discussed herein were evident in both years.

### 2.2. NCEP Stage IV Multisensor QPE

The NCEP Stage IV Multisensor precipitation analysis (Lin & Mitchell, 2005; Nelson et al., 2016) provides hourly accumulated precipitation over the CONUS at 4 km horizontal resolution and is used in this study to identify observed precipitating features and evaluate HRRR precipitation forecasts. The Stage IV product consists of a mosaic of regional radar analyses produced by NWS River Forecast Centers. The analyses are adjusted to gauge measurements and are archived by the National Center for Atmospheric Research. Although the Stage IV product has been used as a reference data set in a number of studies, Nelson et al. (2016) describe the production of the Stage IV product in detail and discuss several potential sources of uncertainty within the product. Smalley et al. (2014) and Prat and Nelson (2015) also provide discussion of Stage IV uncertainties. However, since the focus of this study is on the consistency of the storm structure with respect to that observed by the GPM core satellite, and the domain of interest has good radar coverage (Maddox et al., 2002), Stage IV can be considered to be of adequate accuracy to identify precipitating objects and evaluate the relative performance of the HRRR QPFs.

### 2.3. GPM Microwave Imager

The GPM Core Observatory was launched on 27 February 2014 from Tanagashima Island, Japan, and represents a joint effort between the U.S. National Aeronautics and Space Agency (NASA) and the Japan Aerospace Exploration Agency. It flies in a nonsun-synchronous orbit with at 65° inclination and altitude of 407 km. The satellite carries a passive microwave imager and a dual-frequency precipitation radar (DPR) operating at both Ka (35 GHz) and Ku (13.6 GHz) bands, the data from which can be used to retrieve atmospheric parameters of interest. These retrieved parameters, as well as observed reflectivity and Tbs, are available as a variety of products from the NASA Precipitation Measurements Mission website ([https://pmm.nasa.gov/data-access](https://pmm.nasa.gov/data-access)).

The GPM Microwave Imager (GMI) is a conical scanning microwave radiometer featuring channels ranging from 10 to 183 GHz and an Earth incidence angle of 52.8°. The GMI swath is 904 km wide and is overlapped in the middle by both the Ka and Ku band radars. An example GMI and Ku radar swath is shown in Figure 1.

The 1CGMI product contains calibrated brightness temperatures from the GMI instrument. This study focuses on comparing observed and simulated brightness temperatures at the 36.5 (nominally 37 GHz), 89.0, and 166.0 GHz channels. These channels were selected for their relative insensitivity to surface parameters,

BYTHEWAY AND KUMMEROW

1067


---



21698996, 2018, 2, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1002/2017JD027527 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU logo

# Journal of Geophysical Research: Atmospheres

10.1002/2017JD027527

such that assumptions about surface emissivity in the Tb simulations would be less important than they might be at lower frequency channels, as well as for their sensitivity to the ice hydrometeors typically abundant in warm season convective storms. Although brightness temperatures always represent integrated hydrometeor quantities, the large frequency range implies radiometric sensitivity to a broad spectrum of cloud and precipitation particles. GMI footprints at 89 and 166 GHz are 4.4 km in the along-scan direction and 7.2 km in the cross-track direction and are approximately half the size of the 37 GHz footprints.

## 2.4. GPM 2AKu Radar Product

In addition to the microwave imager, the GPM satellite also carries a dual-frequency precipitation radar (DPR). The 2AKu radar product (V05) provides estimates of surface precipitation as well as profiles of reflectivity at 13.6 GHz. The Ku radar swath overlaps the center of the GMI swath, with a reduced width of 245 km (Figure 1). Ku footprints are approximately 4 km with 125 m vertical resolution. Here the Ku radar data will be used to compare GPM Tb-rain rate relationships against those simulated using the HRRR, and to investigate observed and simulated reflectivity.

# 3. Methodology

In order to compare the CRM output to the observed brightness temperatures, precipitating features were identified in both the HRRR output and the Stage IV product at times coinciding with a GPM core satellite overpass. Objects were identified in HRRR forecasts produced 1, 2, and 3 h prior to the satellite overpass in order to evaluate model performance and storm development with varying forecast lead times. Objects were selected for further study if (a) the HRRR produced a precipitating feature that matched the observed at all three forecast lead times and (b) the observed feature was located completely within both the study domain and the GMI swath. Further details of the feature identification and matching and the Tb simulation are given below.

## 3.1. Feature Matching and Evaluation

As a first step to feature matching and evaluation, GPM core satellite overpasses within the study domain were identified. Only those cases where the overpass occurred within 15 min of the top of the hour (i.e., the forecast valid time) were used to look for precipitating features. By enforcing this criterion, it is likely that there would be minimal change in the feature structure between the satellite overpass and the valid forecast hour. Next, both the HRRR forecast and Stage IV precipitation fields were linearly averaged to a 0.05° (~5 km) grid in order to place both data sets on the same frame of reference while maintaining the majority of heterogeneity within the observed and forecast features. Since the HRRR is produced at 3 km grid spacing and Stage IV is produced at 4 km resolution, this regridding serves as only a minor degradation in resolution.

Observed and forecast features were identified in a manner similar to the Method of Object-based Diagnostic Evaluation (Davis et al., 2006, 2009) as detailed in BK15. A 15 km smoothing is applied to both the observed and forecast fields, and precipitating objects are then defined as contiguous regions within the smoothed field having rain rates exceeding 1 mm/h and an aerial extent greater than 500 km<sup>2</sup>. The locations of the observed and identified features are stored as binary masks.

After the features are identified, descriptive statistics, including bounding latitude and longitude, latitude, and longitude of the feature center of mass, aerial extent, and feature total, mean, and maximum rainfall, are stored in separate databases for the observed and forecast features. These statistics were then used to search for a forecast precipitation feature to correspond to each observed feature (see Figure 3 of BK15). The matching algorithm first searches for forecast features that overlap observed features, selecting the forecast feature that overlaps the highest percentage of the observed feature as a match. If there are no forecast features collocated with an observed feature, the algorithm then searches for forecast precipitation in the vicinity, seeking features with centers of mass within a search radius of 2.0 times the effective radius of the observed feature (effective radius defined as the radius of a circle having the same area as the precipitating feature; Ebert & McBride 2000). If any forecast precipitation features are identified within the search radius, the feature with the most similar total rainfall to the observed is selected as a match. If no forecast features are found that match an observed feature, the model is considered to have missed that rainfall event and it is not considered for this study.

BYTHEWAY AND KUMMEROW

1068



---


21698996, 2018, 2, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1002/2017JD027527 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU logo

# Journal of Geophysical Research: Atmospheres

10.1002/2017JD027527

## HRRR 2 h Forecast Valid June 17, 2015 15 UTC

Simulated brightness temperatures at 37, 89, and 166 GHz for a storm in East Texas with surface emissivities of 0.9 and 0.8, and the change in Tbs.

Figure 2. Simulated brightness temperatures at 37, 89, and 166 GHz for a storm in East Texas with surface emissivities of (a–c) 0.9 and (d–f) 0.8, as well as (g–i) the change in Tbs that resulted from the reduced emissivity.

## 3.2. Simulated Radiances

The HRRR model output contains three-dimensional fields of cloud water, rainwater, cloud ice, graupel, and snow mixing ratios which can be used in forward radiative transfer models to simulate Tbs at frequencies matching those used on the GMI. Tb simulations were performed using the 2-stream slant-path plane-parallel Eddington approximation (Kummerow, 1993) assuming spherical particles. Because the microwave frequencies used in this study have wavelengths comparable to particle size, asymmetric scattering is expected to be minimal and the 2-stream approximation accurate to within a few K.

Care was taken in the simulations to match the microphysical properties as closely as possible to those used in the HRRR. This included using the mixing ratios of graupel and rain to calculate the intercepts ($N_o$) of those particle size distributions (PSDs) and using the layer temperature and snow mixing ratio to determine the number concentration of snow particles, as described in Thompson et al. (2008). Additional properties, such the slope and shape parameters of each species' PSD and particle densities, were also given in Thompson et al. (2008), or culled directly from the WRF v3.6.1 code. Surface emissivity for the Tb calculations was assumed to be 0.9, a reasonable assumption over land surfaces that will generally affect the simulated Tbs at lower frequency radiometer channels (e.g., 10 and 19 GHz) much more strongly than those at the higher frequencies being considered in this study. Figure 2 displays an example of the brightness temperatures simulated at 37, 89, and 166 GHz using surface emissivity values of both 0.9 and 0.8 from an HRRR 2 h forecast valid at 15 UTC on 7 June 2015. As expected, the 37 GHz Tbs are most affected by the change in surface emissivity, while the 166 GHz Tbs do not change at all. Changes at 37 and 89 GHz are generally small (<10 K) and are not affected in the regions of heaviest precipitation in the storm (indicated by the coldest Tb regions at 89 and 166 GHz).

While the HRRR model operates with double moment microphysics for rain hydrometeors (Benjamin et al., 2016), hydrometeor number concentrations were not included in the model output at the time of this

BYTHEWAY AND KUMMEROW

1069


---



21698996, 2018, 2, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1002/2017JD027527 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU logo

# Journal of Geophysical Research: Atmospheres

10.1002/2017JD027527

### Case Biases by Forecast Hour

<table>
  <tbody>
    <tr>
        <td>Forecast Lead Time [hours]</td>
<td>Mean</td>
<td>Max.</td>
<td>Area</td>
<td>Total</td>
    </tr>
<tr>
        <td>1</td>
<td>10</td>
<td>120</td>
<td>20</td>
<td>110</td>
    </tr>
<tr>
        <td>2</td>
<td>15</td>
<td>130</td>
<td>25</td>
<td>120</td>
    </tr>
<tr>
        <td>3</td>
<td>20</td>
<td>140</td>
<td>30</td>
<td>130</td>
    </tr>
  </tbody>
</table>

Figure 3. Calculated biases in (black) mean, (blue) maximum, and (green) total rainfall as well as (red) raining area for the eight selected study cases at 1, 2, and 3 h forecast lead times.

writing. Therefore, with the exception of snow number concentrations, which are calculated based on mixing ratio and temperature (Thompson et al., 2008), the Tb simulations were performed using single moment microphysics. Since we are focusing on convective storms that are expected to have at least some ice in the column, it is probable that the ice scattering signal will dominate any uncertainties in the simulated radiances caused by the lack of explicit raindrop size distributions.

## 4. Results and Discussion

Over the course of the 2014 and 2015 warm seasons in the central United States, 114 features were identified that met the required criteria. In comparing the observed and forecast/simulated rainfall and brightness temperatures, there tended to be two "categories" of cases: Those where the model produced relatively good precipitation forecasts at all three lead times (i.e., storms were in approximately the

right place and were approximately the right size with reasonably represented intensity), but the observed and simulated Tbs were different, and those where the model forecast precipitation changed significantly at each of the three forecast lead times. In this study we will focus on the former, that is, cases in which the forecast at 1, 2, and 3 h lead times is a fairly good representation of the observed storm. Eight cases were selected for further study: 5 from the 2014 warm season and 3 from the 2015 warm season. Bias statistics for each case at 1, 2, and 3 h forecast lead times are shown in Figure 3. Overall, biases in areal extent are reasonably small, which is by design given the case selection criteria in which "good" forecasts were identified visually. Additionally, biases in raining area are generally smaller for forecasts with 1 h lead time than for longer lead times. This is a good indicator of the effects of radar data assimilation on the forecast. With respect to intensity, biases in maximum and total hourly rainfall are for the most part positive, while storm mean rainfall is almost always positive. Thus, even when the HRRR produces storms of approximately the right size in the right place through multiple forecast runs, it does not always accurately predict the intensity of the storms and often produces storms that are too intense.

Microwave brightness temperatures at 37, 89, and 166 GHz were simulated for each HRRR forecast at each lead time. The simulated Tbs were then compared to those observed by the GMI. For each 1 K observed (simulated) Tb bin, average observed (simulated) rain rates were calculated, with the results at 89 and 166 GHz shown in Figure 4. As expected, the observed Tbs (plus signs) decrease slowly at first through light rainfall, then begin to decrease more rapidly for heavier rain rates, since stronger, more convective regions are expected to have more effects from ice scattering. In contrast, the simulated Tbs (asterisks) are generally warmer than observed in very light rain, then decrease rapidly in light rain up to ~1 mm/h, after which they

### Mean Observed/Forecast Rain Rate per K
### Observed (+)/Simulated (*) Tb

<table>
  <tbody>
    <tr>
        <td>Brightness Temperature [K]</td>
<td>HRRR 89 GHz</td>
<td>2AKu 89 GHz</td>
<td>HRRR 166 GHz</td>
<td>2AKu 166 GHz</td>
    </tr>
<tr>
        <td>300</td>
<td>0.1</td>
<td>0.1</td>
<td>0.1</td>
<td>0.1</td>
    </tr>
<tr>
        <td>280</td>
<td>0.5</td>
<td>0.3</td>
<td>0.2</td>
<td>0.2</td>
    </tr>
<tr>
        <td>260</td>
<td>1.5</td>
<td>1.0</td>
<td>0.8</td>
<td>0.6</td>
    </tr>
<tr>
        <td>240</td>
<td>3.0</td>
<td>2.5</td>
<td>2.0</td>
<td>1.5</td>
    </tr>
<tr>
        <td>220</td>
<td>5.0</td>
<td>4.5</td>
<td>4.0</td>
<td>3.5</td>
    </tr>
<tr>
        <td>200</td>
<td>7.0</td>
<td>6.5</td>
<td>6.0</td>
<td>5.5</td>
    </tr>
<tr>
        <td>180</td>
<td>8.5</td>
<td>8.0</td>
<td>7.5</td>
<td>7.0</td>
    </tr>
<tr>
        <td>160</td>
<td>9.5</td>
<td>9.0</td>
<td>8.5</td>
<td>8.0</td>
    </tr>
  </tbody>
</table>

Figure 4. Average rain rates corresponding to (plus sign) observed and (asterisk) simulated Tbs at (red) 89 and (blue) 166 GHz.

continue to decrease at a rate similar to the observed. The rapid decrease in Tbs for light rain results in overall colder Tbs simulated using HRRR hydrometeor output than would be observed for the same surface rain rate. An example of this is shown in Figure 5 for hourly rainfall ending at 16UTC on 23 July 2014 from a precipitating feature identified along the Kansas/Nebraska border. The HRRR forecast with a 3 h lead time is shown for the same feature. After 3 h, the effects of data assimilation should be diminished, and the model should generally be spun up, with microphysics packages having the most influence on cloud structure. With a 3 h lead time, the model produces a feature in approximately the correct location with approximately the correct size, but with lower hourly rainfall than observed.

Despite the lower rain maximum rates produced by the model, the Tbs simulated using the model hydrometeor output are similar to those observed by the GPM satellite. Additionally, areas with light rainfall are warmer than observed. The warm and cold biases in the

BYTHEWAY AND KUMMEROW

1070
1070


---



21698996, 2018, 2, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1002/2017JD027527 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU logo

# Journal of Geophysical Research: Atmospheres

10.1002/2017JD027527

Forecast Initialized 13 UTC July 23, 2014, Valid 16 UTC

Forecast and observed rainfall and brightness temperatures maps

Figure 5. (a–c) Observed and (d–f) forecast/simulated hourly rainfall (Figures 5a and 5d) and Tbs at 89 (Figures 5b and 5e) and 166 GHz (Figures 5c and 5f) for the hour ending at 16 UTC on 23 July 2014. Forecast rainfall is from the HRRR initialized at 13 UTC (i.e., a 3 h lead time).

simulated Tbs are also evident in Figure 6, which shows 2-D histograms of the distribution of observed Tbs for rain rates up to 10 mm/h and the difference between the simulated and observed distributions for each channel and lead time for the eight cases selected for this study. The warm bias for lighter rain rates is particularly evident at 89 and 166 GHz, as is the larger percentage of cold pixels (<250 K at 37 GHz and <200 K at 89 and 166 GHz) produced in the Tb simulations. The tendency for a cold bias is most pronounced at the 37 and 89 GHz channels (Figures 6e, 6f, 6h, 6i, 6k, and 6l)—channels whose signal comes from lower in the cloud than the 166 GHz.

The results shown in Figures 4–6 indicate a cold bias in the simulated Tbs in and around regions of moderate to heavy rainfall, and a warm bias in simulated Tbs in regions with lighter rainfall. In order to understand potential areas where the microphysics scheme incorrectly represents the cloud structure, a series of experiments (Table 1) was performed in which either a microphysical parameter or the distribution of water among hydrometeor classes was altered in the Tb simulations. The effects of different hydrometeor types on microwave brightness temperatures at different frequencies are fairly well understood (Bennartz & Bauer, 2003; Burns et al., 1997; Gasiewski, 1992; Skofronick-Jackson & Wang, 2000); however, the relationships are nonlinear in nature. As such, while several of the performed experiments have expected outcomes, they were performed in order to estimate the magnitude of the resulting changes in different parts of the storms. In a manner similar to Skofronick-Jackson and Wang (2000), hydrometeor profiles and their microphysical properties were altered to attempt to bring simulated Tbs more in line with the observed. One major difference from the previous study is the performance of the current study over land and the resulting focus on channels with minimal sensitivity to surface emission. Changes to microphysical parameters included increasing or decreasing the particle density or intercept parameter (*N<sub>o</sub>*) of the PSD of various hydrometeors, while changes to the hydrometeor distribution maintained the same total water content from the original HRRR, altering only how the water is distributed among the various hydrometeor species. The redistribution of hydrometeors was done somewhat arbitrarily but was done in a manner that would maintain an increasing proportion of frozen hydrometeors with increasing altitude (decreasing temperature) as one would expect. While most of the changes to the microphysical properties had the same effect over the entire storm (either increasing or

BYTHEWAY AND KUMMEROW

1071



---



21698996, 2018, 2, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1002/2017JD027527 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU logo

# 

 Journal of Geophysical Research: Atmospheres

10.1002/2017JD027527

Figure 6: Two-dimensional histograms of observed Tbs and differences between simulated and observed distributions at various frequencies and forecast hours.

Figure 6. (a–c) Two-dimensional histogram of observed Tbs as a function of rain rate and the difference between simulated and observed distributions at HRRR forecast hours (d–f) 1, (g–i) 2, and (j–l) 3.

decreasing Tbs, thus reducing the warm (cold) bias while increasing the cold (warm) bias), the transfer of snow hydrometeors to supercooled cloud or rainwater tended to increase simulated brightness temperatures in the interior of the storm (i.e., heavier rain), while decreasing Tbs around the edges of the storm (i.e., light rain). This differential effect in different areas of the storm arises from the reduction of ice scattering in the heavier precipitation cores, while at the same time increasing emission from liquid

BYTHEWAY AND KUMMEROW

1072


---



21698996, 2018, 2, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1002/2017JD027527 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU logo

# Journal of Geophysical Research: Atmospheres

10.1002/2017JD027527

Table 1

*Changes Made to Microphysical Parameters and Hydrometeor Distributions to Determine Their Impact on Simulated Brightness Temperatures*

<table>
  <thead>
    <tr>
        <th> </th>
        <th>Experiment number</th>
        <th>Experiment description</th>
        <th>Outcome</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td rowspan="4">Microphysical property<br/>changes</td>
<td><strong>1(2)</strong></td>
<td><strong>Double (half) snow density from original<br/>value of 100 kg/m<sup>3</sup></strong> (Figures 7a–7f)</td>
<td><strong>Decrease (increase) in 37, 89, and 166 GHz<br/>Tbs by several tens of K storm-wide</strong></td>
    </tr>
<tr>
        <td>3(4)</td>
<td>Increase (decrease) graupel density by<br/>50% from original value of 500 kg/m<sup>3</sup></td>
<td>Decrease (increase) in 37, 89, and 166 GHz Tbs<br/>by 5–30 K storm-wide</td>
    </tr>
<tr>
        <td>5(6)</td>
<td>Increase (decrease) rain intercept<br/>parameter ($N_0$) by 50%</td>
<td>No change at any channel</td>
    </tr>
<tr>
        <td>7(8)</td>
<td>Increase (decrease) graupel intercept<br/>parameter ($N_0$) by 50%</td>
<td>Decrease (increase) in 89 and 166 GHz Tbs and increase<br/>(decrease) 37 GHz Tbs by a few K storm-wide</td>
    </tr>
<tr>
        <td rowspan="4">Redistribution of water<br/>content</td>
<td><strong>9</strong></td>
<td><strong>Transfer all snow to rain at $T$<br/>&gt; 270 K</strong> (Figures 7g–7i)</td>
<td><strong>Overall improvement at 89 and 166 GHz<br/>(increased Tbs in heavy rain cores and<br/>decreased Tbs in stratiform/anvil up to ~15 K).<br/>Approximately 37 GHz Tbs reduced storm-wide.</strong></td>
    </tr>
<tr>
        <td>10</td>
<td>Transfer all snow to graupel</td>
<td>Decrease 37, 89, and 166 GHz Tbs several tens to<br/>&gt;100 K storm-wide</td>
    </tr>
<tr>
        <td><strong>11</strong></td>
<td><strong>Transfer of snow to cloud<br/>(Figures 7j–7l): 100% at $T$<br/>&gt; 270 K 50% at 260 &lt; $T$ &lt; 270</strong></td>
<td><strong>Increase in 37 GHz Tbs storm-wide. Increase in 89 and<br/>166 GHz Tbs with some slight cooling at storm edges.<br/>Increases of a few tens of K, cooling of a few K.</strong></td>
    </tr>
<tr>
        <td>12</td>
<td>Transfer snow: 100% to rain at $T$ &gt; 270 K 30%<br/>to rain, 30% to cloud at 260 K &lt; $T$ &lt; 270 K,<br/>10% to rain, 10% to cloud at 255 K &lt; $T$ &lt; 260 K</td>
<td>Similar to above, with slightly less warming in cores and<br/>slightly more cooling at edges including at 37 GHz</td>
    </tr>
  </tbody>
</table>

Note. Effects of changes to the Tb simulations highlighted in bold are shown in Figure 7.

hydrometeors near the melting layer of the cloud. Near the edges of the storm, where there is generally less snow present, scattering is less prevalent and warmer surface radiation reaches the top of the atmosphere. Transferring snow water to liquid hydrometeors near the freezing level raises the height of the emitted radiation in these regions, thus reducing the simulated Tbs somewhat. Figure 7 shows a sample of the changes to the simulated brightness temperatures at 37, 89, and 166 GHz for the experiments highlighted in bold in Table 1 for the case shown in Figure 5. The uniform storm-wide changes associated with changes to particle density and the diverse effects in different regions of the storm that result from changes to the hydrometeor distribution are both shown. Figure 8 shows the difference between the distributions of simulated and observed Tbs for all eight cases when snow is transferred to rain in layers where $T$ > 270 K (experiment 9). The cold bias at higher rain rates has been nearly eliminated at all channels. While the warm bias still remains when considering all of the cases, there is some evidence of improvement, particularly at 89 GHz. Individual cases demonstrated more or less improvement in the warm bias depending on the amount of ice the HRRR model produced outside of convective cores.

There are many possible microphysical explanations for the mismatch between observed and simulated Tbs; however, the improved representation of high-frequency simulated microwave brightness temperatures that results in most regions of the storm (cooling regions with warm Tb biases and warming regions with cold Tb biases) from the transfer of snow to cloud or rain suggests an absence of liquid hydrometeors above the freezing level (supercooled liquid). The GPM Ku radar can be used to test this hypothesis. Using the HRRR output, reflectivities at 13.6 GHz were simulated using QuickBeam (Haynes et al., 2007). As with the simulated Tbs, single moment microphysics were used, but all microphysical parameters were kept as close to those used in the model as possible. Figure 9 shows the observed reflectivity at 4 km, approximately the bottom of the freezing level, and at 6 km, above the freezing level, along with the simulated reflectivity at the same heights both from the original HRRR output and with snow water transferred to rainwater at temperatures >270 K (third row in Figure 7). Given that the observed and forecast storms had different intensities, and distributions of rainfall, an exact match is not expected. However, it can be seen in the left column of Figure 5 that similar intensities exist in the center of the forecast feature and the western portion of the observed feature, but the simulated reflectivities at 4 km (near the freezing level) are ~10 dBZ lower than observed for the same rain rates. Transferring snow to supercooled liquid increases the reflectivities, bringing them a bit more in line with the observed, although a bit too high. At 6 km the observed reflectivities are again higher than the simulated in regions of heavier rainfall, but in regions with lighter rainfall, the values

BYTHEWAY AND KUMMEROW

1073


---



AGU logo

Journal of Geophysical Research: Atmospheres

10.1002/2017JD027527

21698996, 2018, 2, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1002/2017JD027527 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

<table>
  <thead>
    <tr>
        <th>Experiment</th>
        <th>37 GHz ΔTbs</th>
        <th>89 GHz ΔTbs</th>
        <th>166 GHz ΔTbs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>Exp. 1 (Snow density 100 to 200 kg/m³)</td>
<td>[Spatial Plot: -100 to 100 K]</td>
<td>[Spatial Plot: -100 to 100 K]</td>
<td>[Spatial Plot: -100 to 100 K]</td>
    </tr>
<tr>
        <td>Exp. 2 (Snow density 100 to 50 kg/m³)</td>
<td>[Spatial Plot: -50 to 50 K]</td>
<td>[Spatial Plot: -50 to 50 K]</td>
<td>[Spatial Plot: -50 to 50 K]</td>
    </tr>
<tr>
        <td>Exp. 9 (Snow to rain &gt; 270 K)</td>
<td>[Spatial Plot: -50 to 50 K]</td>
<td>[Spatial Plot: -50 to 50 K]</td>
<td>[Spatial Plot: -50 to 50 K]</td>
    </tr>
<tr>
        <td>Exp. 11 (Snow to cloud)</td>
<td>[Spatial Plot: -50 to 50 K]</td>
<td>[Spatial Plot: -50 to 50 K]</td>
<td>[Spatial Plot: -50 to 50 K]</td>
    </tr>
  </tbody>
</table>

**Figure 7.** Changes in simulated brightness temperatures (experiment-control) for the case shown in Figure 5 when (top) snow density is increased from 100 kg/m<sup>3</sup> to 200 kg/m<sup>3</sup> (Exp. 1), (second row) snow density is reduced from 100 kg/m<sup>3</sup> to 50 kg/m<sup>3</sup> (Exp. 2), (third row) all snow water is transferred to rainwater for layers with temperatures greater than 270 K (Exp. 9), and (bottom) snow water is transferred to cloud in temperature dependent amounts (Exp. 11).

BYTHEWAY AND KUMMEROW

1074


---



21698996, 2018, 2, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1002/2017JD027527 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU logo

# 

 Journal of Geophysical Research: Atmospheres

10.1002/2017JD027527

a) 166 GHz Forecast Hour 1

<table>
  <thead>
    <tr>
        <th>Rain Rate [mm/h]</th>
        <th>0</th>
        <th>1</th>
        <th>2</th>
        <th>3</th>
        <th>4</th>
        <th>5</th>
        <th>6</th>
        <th>7</th>
        <th>8</th>
        <th>9</th>
        <th>10</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>Tb [K] 300</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
<tr>
        <td>Tb [K] 275</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
<tr>
        <td>Tb [K] 250</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
<tr>
        <td>Tb [K] 225</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
<tr>
        <td>Tb [K] 200</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
<tr>
        <td>Tb [K] 175</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
<tr>
        <td>Tb [K] 150</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
  </tbody>
</table>

b) 89 GHz Forecast Hour 1

<table>
  <thead>
    <tr>
        <th>Rain Rate [mm/h]</th>
        <th>0</th>
        <th>1</th>
        <th>2</th>
        <th>3</th>
        <th>4</th>
        <th>5</th>
        <th>6</th>
        <th>7</th>
        <th>8</th>
        <th>9</th>
        <th>10</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>Tb [K] 300</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
<tr>
        <td>Tb [K] 275</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
<tr>
        <td>Tb [K] 250</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
<tr>
        <td>Tb [K] 225</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
<tr>
        <td>Tb [K] 200</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
<tr>
        <td>Tb [K] 175</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
<tr>
        <td>Tb [K] 150</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
  </tbody>
</table>

c) 37 GHz Forecast Hour 1

<table>
  <thead>
    <tr>
        <th>Rain Rate [mm/h]</th>
        <th>0</th>
        <th>1</th>
        <th>2</th>
        <th>3</th>
        <th>4</th>
        <th>5</th>
        <th>6</th>
        <th>7</th>
        <th>8</th>
        <th>9</th>
        <th>10</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>Tb [K] 300</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
<tr>
        <td>Tb [K] 275</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
<tr>
        <td>Tb [K] 250</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
<tr>
        <td>Tb [K] 225</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
<tr>
        <td>Tb [K] 200</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
<tr>
        <td>Tb [K] 175</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
<tr>
        <td>Tb [K] 150</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
  </tbody>
</table>

d) 166 GHz Forecast Hour 2

<table>
  <thead>
    <tr>
        <th>Rain Rate [mm/h]</th>
        <th>0</th>
        <th>1</th>
        <th>2</th>
        <th>3</th>
        <th>4</th>
        <th>5</th>
        <th>6</th>
        <th>7</th>
        <th>8</th>
        <th>9</th>
        <th>10</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>Tb [K] 300</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
<tr>
        <td>Tb [K] 275</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
<tr>
        <td>Tb [K] 250</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
<tr>
        <td>Tb [K] 225</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
<tr>
        <td>Tb [K] 200</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
<tr>
        <td>Tb [K] 175</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
<tr>
        <td>Tb [K] 150</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
  </tbody>
</table>

e) 89 GHz Forecast Hour 2

<table>
  <thead>
    <tr>
        <th>Rain Rate [mm/h]</th>
        <th>0</th>
        <th>1</th>
        <th>2</th>
        <th>3</th>
        <th>4</th>
        <th>5</th>
        <th>6</th>
        <th>7</th>
        <th>8</th>
        <th>9</th>
        <th>10</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>Tb [K] 300</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
<tr>
        <td>Tb [K] 275</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
<tr>
        <td>Tb [K] 250</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
<tr>
        <td>Tb [K] 225</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
<tr>
        <td>Tb [K] 200</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
<tr>
        <td>Tb [K] 175</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
<tr>
        <td>Tb [K] 150</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
  </tbody>
</table>

f) 37 GHz Forecast Hour 2

<table>
  <thead>
    <tr>
        <th>Rain Rate [mm/h]</th>
        <th>0</th>
        <th>1</th>
        <th>2</th>
        <th>3</th>
        <th>4</th>
        <th>5</th>
        <th>6</th>
        <th>7</th>
        <th>8</th>
        <th>9</th>
        <th>10</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>Tb [K] 300</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
<tr>
        <td>Tb [K] 275</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
<tr>
        <td>Tb [K] 250</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
<tr>
        <td>Tb [K] 225</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
<tr>
        <td>Tb [K] 200</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
<tr>
        <td>Tb [K] 175</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
<tr>
        <td>Tb [K] 150</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
  </tbody>
</table>

g) 166 GHz Forecast Hour 3

<table>
  <thead>
    <tr>
        <th>Rain Rate [mm/h]</th>
        <th>0</th>
        <th>1</th>
        <th>2</th>
        <th>3</th>
        <th>4</th>
        <th>5</th>
        <th>6</th>
        <th>7</th>
        <th>8</th>
        <th>9</th>
        <th>10</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>Tb [K] 300</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
<tr>
        <td>Tb [K] 275</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
<tr>
        <td>Tb [K] 250</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
<tr>
        <td>Tb [K] 225</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
<tr>
        <td>Tb [K] 200</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
<tr>
        <td>Tb [K] 175</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
<tr>
        <td>Tb [K] 150</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
  </tbody>
</table>

h) 89 GHz Forecast Hour 3

<table>
  <thead>
    <tr>
        <th>Rain Rate [mm/h]</th>
        <th>0</th>
        <th>1</th>
        <th>2</th>
        <th>3</th>
        <th>4</th>
        <th>5</th>
        <th>6</th>
        <th>7</th>
        <th>8</th>
        <th>9</th>
        <th>10</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>Tb [K] 300</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
<tr>
        <td>Tb [K] 275</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
<tr>
        <td>Tb [K] 250</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
<tr>
        <td>Tb [K] 225</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
<tr>
        <td>Tb [K] 200</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
<tr>
        <td>Tb [K] 175</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
<tr>
        <td>Tb [K] 150</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
  </tbody>
</table>

i) 37 GHz Forecast Hour 3

<table>
  <thead>
    <tr>
        <th>Rain Rate [mm/h]</th>
        <th>0</th>
        <th>1</th>
        <th>2</th>
        <th>3</th>
        <th>4</th>
        <th>5</th>
        <th>6</th>
        <th>7</th>
        <th>8</th>
        <th>9</th>
        <th>10</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>Tb [K] 300</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
<tr>
        <td>Tb [K] 275</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
<tr>
        <td>Tb [K] 250</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
<tr>
        <td>Tb [K] 225</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
<tr>
        <td>Tb [K] 200</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
<tr>
        <td>Tb [K] 175</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
<tr>
        <td>Tb [K] 150</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
    </tr>
  </tbody>
</table>

**Figure 8.** As in Figures 6d–6l, for Tbs simulated after transferring al snow water content to rain in layers with T > 270 K (Exp. 9 in Table 1).

are similar. This suggests a more appropriate representation of hydrometeor species above the freezing level and supports the hypothesis that a lack of supercooled liquid near the freezing level is at least part of the reason for inconsistencies between observed and simulated Tbs.

There are several possible explanations for the apparent improper partitioning of water content between liquid and frozen hydrometeor species. At the root of some potential explanations lies the fact that the Thompson microphysics scheme “cuts off” the cloud ice category at particles reaching 200 μm. This not only serves to eliminate the need to consider the growth of cloud ice by riming (thus considering only growth by deposition) but also creates many extremely small snow particles. It should be noted that the GMI channels considered in this study are not very sensitive to the small (on the order of a few tens of microns) cloud ice particles typically found in storm anvils, and therefore, experiments in which snow was transferred to the cloud ice category were not performed. The tiny snow particles formed at the upper levels of the cloud as a result of the 200 μm “cutoff” grow by vapor deposition and fall through the cloud as they became larger. Upon descending to levels where supercooled liquid would be expected, they are typically large enough to grow efficiently by riming, depleting much of the supercooled liquid (Thompson et al., 2008).

Although not examined herein, it is worth noting that there is likely some contribution to the discrepancy between observed and simulated Tbs that results from the assumption of spherical ice particles in the radiative transfer calculations. Many studies (e.g., Kulie et al., 2010; Liu, 2008; Olson et al., 2016; Petty & Huang, 2010) have shown significant impacts to simulated Tbs when extinction by nonspherical ice particles (e.g., columns and dendrites) is considered. These effects were most significant at higher frequencies and

BYTHEWAY AND KUMMEROW

1075


---



21698996, 2018, 2, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1002/2017JD027527 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU logo

# Journal of Geophysical Research: Atmospheres

10.1002/2017JD027527

<table>
    <tr>
        <th>Height</th>
        <th>(a, d) Ku Reflectivity [dBZ]</th>
        <th>(b, e) Simulated Reflectivity [dBZ]</th>
        <th>(c, f) Simulated Reflectivity [dBZ]</th>
    </tr>
<tr>
        <td>**4 km**</td>
<td>Observed reflectivity at 4km</td>
<td>Simulated reflectivity at 4km (Original)</td>
<td>Simulated reflectivity at 4km (Exp. 1)</td>
    </tr>
<tr>
        <td>**6 km**</td>
<td>Observed reflectivity at 6km</td>
<td>Simulated reflectivity at 6km (Original)</td>
<td>Simulated reflectivity at 6km (Exp. 1)</td>
    </tr>
</table>

Figure 9. Observed reflectivity from the GPM Ku radar at (a) 4 km and (d) 6 km. (b and e) Simulated reflectivity at the same heights using the original HRRR output and (c and f) when transferring snow water to rain in layers with temperature >270 K (Exp. 1 in Table 1) for the case shown in Figure 5.

cannot be discounted from at least partially explaining the simulated Tb behavior at 89 and 166 GHz found in this study.

## 5. Conclusions

This study evaluated forecasts of warm season convective precipitation from the HRRR model over the central United States, using observed radiances from the GPM Microwave Imager to evaluate consistency between observed and forecast storms. Forecasts at 1, 2, and 3 h lead times were considered. Several storms that were forecast with relative accuracy at all three lead times were selected for further study, and comparison of the raining area and maximum, mean, and total storm rainfall to that given by the NCEP Stage IV multisensor precipitation product showed that the selected cases were generally correctly located with positive biases in forecast hourly rainfall.

Brightness temperatures at GMI frequencies were simulated using plane-parallel radiative transfer assuming a typical land surface emissivity value of 0.9. In order to minimize the effects of this assumption on the results, this study focuses on brightness temperatures at 37, 89, and 166 GHz because these frequencies are less sensitive to the surface and more sensitive to cloud hydrometeor contents. Overall, the simulated brightness temperatures were colder than observed Tbs at the same rain rate with the exception of a warm bias in regions of very light rain. This pattern was visible in Tb maps created for the eight cases examined in this study. In order to understand possible reasons why the simulated brightness temperatures were different than the observed, a series of sensitivity tests were conducted in which either microphysical parameters or the hydrometeor distribution was altered and the effects on the simulated Tbs were examined. Generally, changes to the microphysics had the same impact over the entire storm, whereas changes to the hydrometeor distribution tended to impact the interior and exterior of the storms (i.e., convective cores versus light

BYTHEWAY AND KUMMEROW

1076


---



21698996, 2018, 2, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1002/2017JD027527 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU logo

# Journal of Geophysical Research: Atmospheres

10.1002/2017JD027527

rain regions) in opposite ways, generally depending on whether the emission signal was dominated by ice scattering. In reality, the inconsistency between simulated and observed Tbs in warm season convective precipitation is likely due to a combination of effects, including things not considered in this study. Different processes occur within the convective, stratiform, and anvil regions of a given storm, and so a one-size fits all explanation for the Tb biases is not to be expected. However, given the results of the experiments discussed herein and the behavior of the simulated reflectivity at and above the freezing level, it seems that the absence of supercooled liquid is at least partially responsible for the large differences between simulated and observed brightness temperatures. Sensitivity tests to determine whether the redistribution of hydrometeors from snow to supercooled liquid results in improved forecasts of precipitation intensity will be left to future work, as will further exploration of the data and products from the GPM DPR, which can provide additional information about the presence and location of bright bands and estimates of the observed PSD parameters.

In addition to assumptions about surface emissivity, other assumptions in the radiative transfer could have an effect on the simulated brightness temperatures and reflectivities, including the use of single moment microphysics, whereas the HRRR model uses double moment. While the microphysical parameters in the radiative transfer were treated as similarly as possible to the Thompson et al. (2008) microphysics, the unavailability of the number concentration output means that the PSDs in the Tb and reflectivity simulations will not exactly match those in the model.

As the HRRR (and other convection allowing NWP) model continues to undergo development, comparisons to spaceborne sensors can be a useful tool to evaluate the representation of cloud systems. In this study we focused on cases where the model performed relatively well, in terms of producing a convective storm system in the right place at the right time but that had simulated Tbs inconsistent with the observed. Inconsistencies between simulated and observed microwave Tbs could also help developers understand how misrepresentation of precipitating clouds in the model may lead to bad forecasts.

## Acknowledgments

The authors would like to thank Curtis Alexander for access to the HRRR model output and for his valuable input regarding our results. We would also like to thank Greg Thompson for his thoughts on the model microphysical behavior. NCEP Stage IV data are obtained from [https://data.eol.ucar.edu/dataset/21.093](https://data.eol.ucar.edu/dataset/21.093). GPM brightness temperatures and 2AKu data are available at [https://pmm.nasa.gov/data-access/downloads/GPM](https://pmm.nasa.gov/data-access/downloads/GPM). This work was supported by a Cooperative Institute for Research in the Atmosphere (CIRA) graduate student fellowship.

## References

Benjamin, S., Alexander, C., Hu, M., Weygandt, S., Hofmann, P., Brown, J., ... Jamison, B. (2013). Data assimilation and model updates in the 2013 Rapid Refresh (RAP) and High-Resolution Rapid Refresh (HRRR) analysis and forecast systems. Paper presented at NCEP/EMC meeting, June 6. Retrieved from [http://ruc.noaa.gov/pdf/NCEP_HRRR_RAPv2_6jun2013-Benj-noglob.pdf](http://ruc.noaa.gov/pdf/NCEP_HRRR_RAPv2_6jun2013-Benj-noglob.pdf)

Benjamin, S. G., Weygandt, S. S., Brown, J. M., Hu, M., Alexander, C. R., Smirnova, T. G., ... Kenyon, J. S. (2016). A North American hourly assimilation and model forecast cycle: The rapid refresh. *Monthly Weather Review*, 144(4), 1669–1694. [https://doi.org/10.1175/MWR-D-15-0242.1](https://doi.org/10.1175/MWR-D-15-0242.1)

Bennartz, R., & Bauer, P. (2003). Sensitivity of microwave radiances at 85–183 GHz to precipitating ice particles. *Radio Science*, 38(4), 2075. [https://doi.org/10.1029/2002RS002626](https://doi.org/10.1029/2002RS002626)

Bryan, G. H., & Morrison, H. (2012). Sensitivity of a simulated squall line to horizontal resolution and parameterization of microphysics. *Monthly Weather Review*, 140(1), 202–225. [https://doi.org/10.1175/MWR-D-11-00046.1](https://doi.org/10.1175/MWR-D-11-00046.1)

Burghardt, B. J., Evans, C., & Roebber, P. J. (2014). Assessing the predictability of convection initiation in the High Plains using an object-based approach. *Weather and Forecasting*, 29(2), 403–418. [https://doi.org/10.1175/WAF-D-13-00089.1](https://doi.org/10.1175/WAF-D-13-00089.1)

Burns, B. A., Wu, X., & Diak, G. R. (1997). Effects of precipitation and cloud ice on brightness temperatures in AMSU moisture channels. *IEEE Transactions on Geoscience and Remote Sensing*, 35(6), 1429–1437. [https://doi.org/10.1109/36.649797](https://doi.org/10.1109/36.649797)

Bytheway, J. L., & Kummerow, C. D. (2015). Toward an object-based assessment of high-resolution forecasts of long-lived convective precipitation in the central US. *Journal of Advances in Modeling Earth Systems*, 07(3), 1248–1264. https://doi.org/10.1002/2015MS000497

Craig, G. C., Keil, C., & Leuenberger, D. (2012). Constraints on the impact of radar rainfall data assimilation on forecasts of cumulus convection. *Quarterly Journal of the Royal Meteorological Society*, 138(663), 340–352. [https://doi.org/10.1002/qj.929](https://doi.org/10.1002/qj.929)

Davis, C., Brown, B., & Bullock, R. (2006). Object-based verification of precipitation forecasts. Part I: Methodology and Application to Mesoscale Rain Areas. *Monthly Weather Review*, 134(7), 1772–1784. [https://doi.org/10.1175/MWR3145.1](https://doi.org/10.1175/MWR3145.1)

Davis, C. A., Brown, B. G., Bullock, R., & Halley-Gotway, J. (2009). The method for object-based diagnostic evaluation (MODE) applied to numerical forecasts from the 2005 NSSL/SPC spring program. *Weather and Forecasting*, 24(5), 1252–1267. [https://doi.org/10.1175/2009WAF2222241.1](https://doi.org/10.1175/2009WAF2222241.1)

Ebert, E., & McBride, J. (2000). Verification of precipitation in weather systems: Determination of systematic errors. *Journal of Hydrology*, 239(1-4), 179–202. [https://doi.org/10.1016/S0022-1694(00)00343-7](https://doi.org/10.1016/S0022-1694(00)00343-7)00343-7)

Ebert, E. E., Janowiak, J., & Kidd, C. (2007). Comparison of near-real-time precipitation estimates from satellite observations and numerical models. *Bulletin of the American Meteorological Society*, 88(1), 47–64. [https://doi.org/10.1175/BAMS-88-1-47](https://doi.org/10.1175/BAMS-88-1-47)

Errico, R. M., Bauer, P., & Mahfouf, J.-F. (2007). Issues regarding the assimilation of cloud and precipitation data. *Journal of the Atmospheric Sciences*, 64(11), 3785–3798. [https://doi.org/10.1175/2006JAS2044.1](https://doi.org/10.1175/2006JAS2044.1)

ESRL (2015). High-Resolution Rapid Refresh (HRRR). Retrieved from [http://ruc.noaa.gov/hrrr](http://ruc.noaa.gov/hrrr). (Accessed February 7, 2015).

Fritsch, J., & Carbone, R. (2004). Improving quantitative precipitation forecasts in the warm season: A USWRP research and development strategy. *Bulletin of the American Meteorological Society*, 85(7), 955–965. [https://doi.org/10.1175/BAMS-85-7-955](https://doi.org/10.1175/BAMS-85-7-955)

Gasiewski, A. J. (1992). Numerical sensitivity analysis of passive EHF and SMMW channels to tropospheric water vapor, clouds, and precipitation. *IEEE Transactions on Geoscience and Remote Sensing*, 30(5), 859–870. [https://doi.org/10.1109/36.175320](https://doi.org/10.1109/36.175320)

Haynes, J. M., Marchand, R. T., Luo, Z., Bodas-Salcedo, A., & Stephens, G. L. (2007). A multipurpose radar simulation package: QuickBeam. *Bulletin of the American Meteorological Society*, 88(11), 1723–1727. [https://doi.org/10.1175/BAMS-88-11-1723](https://doi.org/10.1175/BAMS-88-11-1723)

BYTHEWAY AND KUMMEROW

1077


---



21698996, 2018, 2, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1002/2017JD027527 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU logo

# Journal of Geophysical Research: Atmospheres

10.1002/2017JD027527

Kulie, M. S., Bennartz, R., Greenwald, T. J., Chen, Y., & Weng, F. (2010). Uncertainties in microwave properties of frozen precipitation: Implications for remote sensing and data assimilation. *Journal of the Atmospheric Sciences*, 67(11), 3471–3487. [https://doi.org/10.1175/2010JAS3520.1](https://doi.org/10.1175/2010JAS3520.1)

Kummerow, C. (1993). On the accuracy of the Eddington approximation for radiative transfer in the microwave frequencies. *Journal of Geophysical Research*, 98(D2), 2757–2765. [https://doi.org/10.1029/92JD02472](https://doi.org/10.1029/92JD02472)

Lin, C., Vasic, S., Kilambi, A., Turner, B., & Zawadzki, I. (2005). Precipitation forecast skill of numerical weather prediction models and radar nowcasts. *Geophysical Research Letters*, 32, L14801. [https://doi.org/10.1029/2005GL023451](https://doi.org/10.1029/2005GL023451)

Lin, Y., & Mitchell, K. (2005). The NCEP stage II/IV hourly precipitation analyses: Development and applications. *Preprints of the 19th conference on hydrology, American Meteorological Society annual meeting* (pp. 2–5). 9–13 January. San Diego, CA, Pap. 1.2.

Liu, G. (2008). A database of microwave single-scattering properties for nonspherical ice particles. *Bulletin of the American Meteorological Society*, 89(10), 1563–1570. [https://doi.org/10.1175/2008BAMS2486.1](https://doi.org/10.1175/2008BAMS2486.1)

Maddox, R. A., Zhang, J., Gourley, J. J., & Howard, K. W. (2002). Weather radar coverage over the contiguous United States. *Weather and Forecasting*, 17(4), 927–934. https://doi.org/10.1175/1520-0434(2002)017<0927:WRCOTC>2.0.CO;2017%3C0927:WRCOTC%3E2.0.CO;2)

Nelson, R. R., Prat, O. P., Seo, D.-J., & Habib, E. (2016). Assessment and implications of NCEP stage IV quantitative precipitation estimates for product intercomparisons. *Weather and Forecasting*, 31(2), 371–394. [https://doi.org/10.1175/WAF-D-14-00112.1](https://doi.org/10.1175/WAF-D-14-00112.1)

Olson, W. S., Tian, L., Grecu, M., Kuo, K.-S., Johnson, B. T., Heymsfield, A. J., … Meneghini, R. (2016). The microwave radiative properties of falling snow derived from nonspherical ice particle models. Part II: Initial testing using radar, radiometer and in situ observations. *Journal of Applied Meteorology and Climatology*, 55(3), 709–722. [https://doi.org/10.1175/JAMC-D-15-0131.1](https://doi.org/10.1175/JAMC-D-15-0131.1)

Petty, G. W., & Huang, W. (2010). Microwave backscatter and extinction by soft ice spheres and complex snow aggregates. *Journal of the Atmospheric Sciences*, 67, 769–787. [https://doi.org/10.1175/2009JAS3146.1](https://doi.org/10.1175/2009JAS3146.1)

Prat, O. P., & Nelson, B. R. (2015). Evaluation of precipitation estimates over CONUS derived from satellite, radar, and rain gauge data sets at daily to annual scales (2002–2012). *Hydrology and Earth System Sciences*, 19(4), 2037–2056. [https://doi.org/10.5194/hess-19-2037-2015](https://doi.org/10.5194/hess-19-2037-2015)

Rogers, R. F., Fritsch, J. M., & Lambert, W. C. (2000). A simple technique for using radar data in the dynamic initialization of a mesoscale model. *Monthly Weather Review*, 128(7), 2560–2574. https://doi.org/10.1175/1520-0493(2000)128<2560:ASTFUR>2.0.CO;2128%3C2560:ASTFUR%3E2.0.CO;2)

Sheng, C., Gao, S., & Xue, M. (2006). Short-range prediction of a heavy precipitation event by assimilating Chinese CINRAD-SA radar reflectivity data using complex cloud analysis. *Meteorology and Atmospheric Physics*, 94(1-4), 167–183. https://doi.org/10.1007/s00703-005-0177-0

Shrestha, D. L., Robertson, D. E., Wang, Q. J., Pagano, T. C., & Hapaurachchi, H. A. P. (2013). Evaluation of numerical weather prediction model precipitation forecasts for short-term streamflow forecasting purpose. *Hydrology and Earth System Sciences*, 17(5), 1913–1931. [https://doi.org/10.5194/hess-17-1913-2013](https://doi.org/10.5194/hess-17-1913-2013)

Skofronick-Jackson, G. M., & Wang, J. R. (2000). The estimation of hydrometeor profiles from wideband microwave observations. *Journal of Applied Meteorology*, 39(10), 1645–1656. [https://doi.org/10.1175/1520-0450-39.10.1645](https://doi.org/10.1175/1520-0450-39.10.1645)

Smalley, M., L’Ecuyer, T., Lebsock, M., & Haynes, J. (2014). A comparison of precipitation occurrence from the NCEP stage IV QPE product and the CloudSat profiling radar. *Journal of Hydrometeorology*, 15(1), 444–458. [https://doi.org/10.1175/JHM-D-13-048.1](https://doi.org/10.1175/JHM-D-13-048.1)

Stensrud, D. J., Xue, M., Wicker, L. J., Kelleher, K. E., Foster, M. P., Schaefer, J. T., … Tuell, J. P. (2009). Convective-scale warn-on-forecast system: A vision for 2020. *Bulletin of the American Meteorological Society*, 90(10), 1487–1499. [https://doi.org/10.1175/2009BAMS2795.1](https://doi.org/10.1175/2009BAMS2795.1)

Sugimoto, S., Crook, N. A., Sun, J., Xiao, Q., & Barker, D. M. (2009). An examination of WRF 3DVAR radar data assimilation on its capability in retrieving unobserved variables and forecasting precipitation through observing system simulation experiments. *Monthly Weather Review*, 137(11), 4011–4029. [https://doi.org/10.1175/2009MWR2839.1](https://doi.org/10.1175/2009MWR2839.1)

Sun, J., Xue, M., Wilson, J. W., Zawadzki, I., Ballard, S. P., Onvlee-Hooimeyer, J., … Pinto, J. (2014). Use of NWP for nowcasting convective precipitation: Recent progress and challenges. *Bulletin of the American Meteorological Society*, 95(3), 409–426. [https://doi.org/10.1175/BAMS-D-11-00263.1](https://doi.org/10.1175/BAMS-D-11-00263.1)

Thompson, G., & Eidhammer, T. (2014). A study of aerosol impacts on clouds and precipitation development in a large winter cyclone. *Journal of the Atmospheric Sciences*, 71(10), 3636–3658. [https://doi.org/10.1175/JAS-D-13-0305.1](https://doi.org/10.1175/JAS-D-13-0305.1)

Thompson, G., Field, P. R., Rasmussen, R. M., & Hall, W. D. (2008). Explicit forecasts of winter precipitation using an improved bulk microphysics scheme. Part II: Implementation of a New Snow Parameterization. *Monthly Weather Review*, 136(12), 5095–5115. [https://doi.org/10.1175/2008MWR2387.1](https://doi.org/10.1175/2008MWR2387.1)

Weygandt, S., & Benjamin, S. (2007). Radar reflectivity-based initialization of precipitation systems using a diabatic digital filter within the rapid update cycle, preprints of the 18th American Meteorological Society conference on numerical weather prediction. June 25–29, Park City, UT.

Weygandt, S. S., Benjamin, S. G., Smirnova, T. G., & Brown, J. M. (2008). Assimilation of radar reflectivity data using a diabatic digital filter within the rapid update cycle, Preprints of the American Meteorological Society 12th conference on IOAS-AOLS. January 20–24, New Orleans, LA.

Xaio, Q., & Sun, J. (2007). Multiple-radar data assimilation and short-range quantitative precipitation forecasting of a squall line observed during IHOP_2002. *Monthly Weather Review*, 135(10), 3381–3404. [https://doi.org/10.1175/MWR3471.1](https://doi.org/10.1175/MWR3471.1)

BYTHEWAY AND KUMMEROW

1078
