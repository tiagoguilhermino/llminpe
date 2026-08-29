# A review of the different operational applications of spaceborne precipitation radars within the International Precipitation Working Group (IPWG) community

10 June 2021

Contributors by alphabetical order:

Kazumasa Aonashi<sup>1</sup>, Alessandro Battaglia<sup>2,3,4</sup>, David T. Bolvin<sup>5,6</sup>, Mary Borderies<sup>7</sup>, Philippe Chambon<sup>7</sup>, Ralph R. Ferraro<sup>8</sup>, Alan Geer<sup>9</sup>, Ziad Haddad<sup>10</sup>, George J. Huffman<sup>5</sup>, Yasutaka Ikuta<sup>11</sup>, Benjamin T. Johnson<sup>12</sup>, Misako Kachi<sup>1</sup>, Chris Kidd<sup>5,13</sup>, Pierre Kirstetter<sup>14</sup>, Takuji Kubota<sup>1</sup>, Christian Kummerow<sup>15</sup>, Valentin Louf<sup>16</sup>, Viviana Maggioni<sup>17</sup>, Rohit Mangla<sup>7</sup>, Kozo Okamoto<sup>11</sup>, Alain Protat<sup>16</sup>, Shoichi Shige<sup>18</sup>

Report coordinated by IPWG co-Chairs:
**Philippe Chambon<sup>7</sup> and Viviana Maggioni<sup>17</sup>**

1. Japan Aerospace Exploration Agency/Tsukuba Space Center, Tsukuba, Japan

2. Earth Observation Science Group, Department of Physics and Astronomy, University of Leicester, UK

3. National Centre for Earth Observation, University of Leicester, UK

4. DIATI, Politecnico di Torino, Italy

5. NASA Goddard Space Flight Center, Greenbelt, MD, USA

6. Science Systems and Applications, Inc., MD, USA

7. Centre National de Recherches Météorologiques, Université de Toulouse, Météo-France and CNRS, Toulouse, France

8. Center for Satellite Applications and Research (STAR), NOAA/NESDIS, College Park, MD, USA

9. European Centre for Medium-Range Weather Forecasts, Reading, UK

10. Jet Propulsion Laboratory, California Institute of Technology, California, USA

11. Meteorological Research Institute, Department of Observation and Data Assimilation Japan Meteorological Agency, Tsukuba, Japan

12. Joint Center for Satellite Data Assimilation at the National Oceanic and Atmospheric Administration, NOAA Center for Weather and Climate Prediction, College Park, MD, USA

13. Earth System Science Interdisciplinary Center, University of Maryland, MD, USA

14. Advanced Radar Research Center / National Severe Storms Laboratory, National Weather Center (NWC), Norman, OK, USA

15. Cooperative Institute for Research in the Atmosphere, Colorado State University, Fort Collins, CO, USA

16. Australian Bureau of Meteorology, Melbourne, Australia

17. Department of Civil, Environmental and Infrastructure Engineering, George Mason University, Fairfax, VA, USA

18. Kyoto University, Kyoto, Japan

---

# Executive summary

Spaceborne precipitation radars such as the instruments currently onboard the Global Precipitation Measurement (GPM) core observatory, the CloudSat satellite, and the future Earth Clouds, Aersols and Radiation Explorer (EarthCARE) mission all offer unique profiling capabilities of clouds and precipitation at a global scale. While being a precious source of information for atmospheric research (Hou et al., 2014; Stephens et al., 2018; Illingworth et al., 2015), many applications have also emerged from observations taken by these instruments.

The present document aims at illustrating different applications of cloud and precipitation radar observations that have been fostered by exchanges within the International Precipitation Working Group (IPWG) community since it was established as a permanent Working Group of the Coordination Group for Meteorological Satellites (CGMS) on 20-22 June 2001 in Fort Collins, Colorado.

With years, these applications have reached different degrees of maturity. While the precipitation retrieval community now makes a routine and efficient use of these observations, other communities such as the numerical weather prediction (NWP) community have made significant progress and are getting ready to fully exploit spaceborne precipitation radars. Innovative applications also emerge to benefit from these observations, e.g., to be used as a reference for the inter-calibration of non-homogeneous networks of instruments on the ground.

While summarizing some key findings in the development of applications of precipitation radars, this report also highlights the need for continuity of such observations after the GPM, CloudSat, and EarthCARE era for (i) continuing the production of state-of-the-art inter-calibrated multi-platform precipitation products, (ii) pursuing the assimilation of this kind of observations into weather forecasts, and (iii) standardizing calibration procedures of ground networks.

Regarding instrumental details, this report also advocates for improvements in the current generation of sensors for filling science gaps in the current observing system (Battaglia et al., 2020). Among them, a wider swath for space radars would improve the sampling, enhance calibration procedures and magnify their impact on weather forecasts. Improvements in sensitivity, vertical and horizontal resolutions and multi-frequency capabilities would allow overcoming some limitations in retrieving precipitation and facilitate cloud-resolving model validation. New capabilities such as Doppler measurements would also be beneficial to several applications, in particular to NWP, which lacks observational constraints on cloud-scale dynamical fields.

2


---

# Table of contents

**EXECUTIVE SUMMARY** 2
**TABLE OF CONTENTS** 3
**1. INTRODUCTION** 4
**2. USE OF PRECIPITATION RADARS FOR OPERATIONAL RETRIEVAL ALGORITHMS** 5
**2.1 USE AS CALIBRATORS FOR RADIOMETER ALGORITHMS** 5
**2.2 VALIDATION OF RETRIEVALS WHERE NO OTHER REFERENCE DATA EXIST** 8
**3. USE OF PRECIPITATION RADARS FOR NUMERICAL WEATHER PREDICTION APPLICATIONS** 11
**3.1 STATUS OF NWP OBSERVATION OPERATORS FOR PRECIPITATION RADARS** 11
**3.2 USE OF PRECIPITATION RADARS FOR VALIDATION OF NWP MODELS** 13
**3.3 DATA ASSIMILATION OF PRECIPITATION RADAR DATA** 16
**4. A PERSPECTIVE OF OPERATIONAL APPLICATIONS: DEVELOPMENT OF TECHNIQUES TO MONITOR THE CALIBRATION OF GROUND RADAR NETWORKS** 19
**5. CONCLUSIONS AND RECOMMENDATIONS FOR FUTURE SPACEBORNE PRECIPITATION RADARS** 23
**6. REFERENCES** 25
**7. ACRONYMS LIST** 35

3


---

# 1. Introduction

Spaceborne precipitation radars such as the instruments currently onboard the Global Precipitation Measurement mission, CloudSat, and the future EarthCARE mission offer unique profiling capabilities of clouds and precipitation at a global scale. While being a precious source of information for atmospheric research (Hou et al., 2014; Stephens et al., 2018; Illingworth et al., 2015), many applications have also emerged from these instruments (Levizzani et al., 2020a, 2020b).

The present document aims at illustrating different applications of cloud and precipitation radar observations that have been fostered by exchanges within the IPWG community since it was established as a permanent Working Group of the Coordination Group for Meteorological Satellites (CGMS) on 20-22 June 2001 in Fort Collins, CO.

The first section of this report summarizes the very mature use that the precipitation retrieval community makes of cloud and precipitation radars, to generate operational rainfall estimation products that are then used for various applications.

The second section describes how these active remote sensing observations are currently used within the Numerical Weather Prediction (NWP) community, which started to explore the usefulness of such data more recently, but that is also eager to move forward and improve their applications with cloud and precipitation radar data.

A third section gives an example of an emerging application regarding the intercalibration of ground-based radars with this unique source of observations.

A recommendation section regarding potential improvements of future instruments concludes the report.

4


---

# 2. Use of precipitation radars for operational retrieval algorithms

## 2.1 Use as calibrators for radiometer algorithms

### 2.1.1 The Goddard PROFiling (GPROF) algorithm

*By Christian Kummerow*

Passive microwave retrievals of precipitation have a long history encompassing statistical, physical, and hybrid methods to derive relationships between rainwater and brightness temperatures (e.g., Wilheit et al., 1991, Petty, 2001, Hilburn and Wentz, 2008). To overcome performance issues related to insufficient information content, a number of Bayesian techniques were developed in the late 1990’s that relied on Cloud Resolving Models to construct a-priori databases of possible precipitation profiles to help constrain the retrieval problem (e.g. Bauer et al., 2001, Kummerow et al., 2001, Marzano et al. 1999). With the advent of the Tropical Rainfall Measuring Mission (TRMM), and later the Global Precipitation Measurement (GPM) mission, these methods were generally adapted to use observed satellite radar/radiometer retrievals (Haddad et al., 1997) to construct more robust a-priori databases (see Figure 1). When the vertical profiles of rainfall were constrained by the TRMM Precipitation Radar (PR) as was done in Kummerow et al. (2006) for the GPROF algorithm, the potential biases introduced by the cloud-resolving model are reduced significantly as described in that paper. In the case of TRMM, however, these databases were limited to rainfall structures observed in the tropics, and cloud resolving models continued to be used for extratropical precipitation. This changed with GPM, which covers up to 66° latitude. While not covering the entire globe, the GPROF databases used by the GPM program are constructed databases not on the basis of latitude and longitude, but on the basis of 2-meter temperature and column integrated water vapor. The entire range of temperatures and water vapor are more or less covered by the 66° coverage which makes for a complete database. Some issues with the databases have nonetheless persisted. The GPM Ka- and Ku-band radars (14 and 35 GHz, respectively) have limited sensitivity (12 and 18 dBZ, respectively) (Hamada and Takayabu, 2016). These are not sufficiently sensitive to capture drizzle or light snowfall. While the W-band (94 GHz) CloudSat Profiling Radar (Stephens et al., 2018) does have sufficient sensitivity, its narrow beam observed along a single nadir track is not sufficient to fully cover a radiometer footprint and other assumptions must be made before these data can be used to complete the a-priori databases. All radars also have known underestimation issues in orographic situations where heavy, but very shallow precipitation is often masked by ground clutter from the complex terrain (Houze et al., 2017).

GPROF’s original database was created from a full year of TRMM data spanning June 1, 1999 to May 31, 2000. The above procedure created roughly 6.2•10<sup>7</sup> raining and non-raining profiles. This database was updated with every revision of the radar/radiometer combined product through the TRMM era. It has since been replaced with the radar/radiometer combined product produced by GPM for the period of Sept. 1, 2014 to Aug. 31, 2015. Here too, the GPROF database is updated with each iteration of the combined radar/radiometer product from the same time period in order not to interleave changes in the database from changes in the product upgrades. However, GPROF has occasionally used the radar/radiometer product that is one

5


---

version older because the product needed to construct the databases and testing was not available in time. The GPROF output header always provides information as to the combined radar/radiometer product used to construct the a-priori database.

Two side-by-side satellite precipitation maps of Kamchatka on November 7th, 2014. The left map is titled "Precipitation GMI" and the right map is titled "Precipitation GMI + Comb MS", showing a radar swath overlay. A color scale on the right indicates precipitation intensity from 0.5 to 64.

Figure 1: An example of GPROF Retrieval is shown on the left. On the Right is the same GPROF retrieval but the radar/radiometer product used to create the database is shown in the radar swath.

To date, the impact of changing rainfall characteristics on the database (i.e. using stable algorithms but creating new databases for each year) has not been examined. This is because both the combined radar/radiometer algorithms as well as GPROF have still been evolving and changes from one version to the next are still larger than those expected from subtle changes in year-to-year makeup of the a-priori databases. Updates to the combined radar/radiometer product in particular, have been consistently larger than climate model predictions of 2-3% precipitation increase per degree warming. Such trends are therefore not yet detectable.

Nonetheless, this will be an important experiment once the GPM radar and combined radar/radiometer algorithms have stabilized sufficiently, and the issue of light and orographic precipitation that are only being addressed with V5 and V7 of GPROF, respectively, have been adequately resolved.

## 2.1.2 The IMERG combined product: further calibration for merging multiple source Level-2 products

**By George J. Huffman, David T. Bolvin and Chris Kidd**

The precipitation datasets described above and used as input for the Integrated Multi-satellitE Retrievals for GPM mission (IMERG) are inter-calibrated to the TRMM or GPM combined-sensor estimates from the Combined Radar-Radiometer Algorithm (CORRA), which are deemed the highest quality following Huffman et al. (2007). As TRMM and GPM have precessing orbits, time/space coincidences between the narrow radar swaths and the partner polar-

6


---

orbit satellite radiometer swaths are too sparse to provide stable seasonal-scale calibrations. In contrast, the CORRA-TMI/GMI coincidences with the partner satellites are continuous as the PR/DPR swath is embedded in the TMI/GMI swath. Therefore, IMERG intersatellite calibration is performed in two steps.

First, seasonal climatological calibrations are computed between TMI/GMI and the rest of the partner radiometers. This is possible because of (a) reasonable overlap of the (wider) TMI/GMI swath with the other radiometer swaths, and (b) the reasonably consistent match between TMI/GMI radiometer characteristics and those of the partner radiometers. The TMI- and GMI-to-partner-satellite calibrations are computed using 22 15° zonal histogram bands overlapping at 5° increments for ocean to enhance sampling. A single histogram is used for land due to sampling concerns.

Second, dynamic 45-day calibrations are computed between CORRA and TMI/GMI at the end of each pentad, due to variations in regional relationships between active and passive sensors for different weather/climate regimes. The TMI- and GMI-to-CORRA matched histograms are accumulated and computed at the 1°x1° grid resolution, using a 3°x3° template to smooth the field, and then converted to a calibration look-up table.

Finally, these calibrations are applied sequentially to approximate a CORRA-partner radiometer calibration that varies in space and time.

In the TRMM era there is no explicit calibration outside the latitude band 33°N-S, so background monthly climatological GPM-era GMI-CORRA histograms and correction curves are used to fill in the corrections for the latitude bands 33º-90º N and S. The resulting corrections are based on TRMM for the latitude band 25ºN-25ºS, volume-adjusted GPM for the latitude bands 33º-90º N and S, and a blend of the two in the latitude bands 25º-33º N and S. The goal is to match the GPM correction structure outside the TRMM coverage area, while maintaining the volume of the TRMM estimates. This was necessary, as directly extrapolating the TRMM region calibrations to the poles created artificially low precipitation values.

# 2.1.3 The Global Satellite Mapping of Precipitation (GSMaP) product

*By Shoichi Shige, Kazumasa Aonashi, and Takuji Kubota*

The GSMaP microwave algorithm (Aonashi et al. 2009) derives the optimal precipitation for which brightness temperatures (TBs) calculated by a Radiative Transfer Model (RTM) best fit with the observed TBs. The RTM requires a priori models for precipitation-related variables (precipitation profile, particle size distributions (PSDs), frozen particle densities etc.). We have used TRMM/GPM radar data to construct the precipitation-type classification method (Takayabu 2006), and drop size distribution model (Kozu et al. 2009; Yamaji et al. 2020), which have been renewed after the major updates of the TRMM/GPM radar level-2 data sets. TRMM/GPM radar data are also used in evaluating retrievals from the passive microwave radiometers (Kubota et al. 2007;2009, Kida et al. 2009). In order to evaluate the impacts of climate change on the precipitation-related variables, the GSMaP team is now working on estimating the precipitation-related variable variations in terms of atmospheric temperature and humidity,derived from global analysis (GANAL) and forecast (FCST) data by the Japan Meteorological Agency (JMA; Kubota et al. 2020). One additional feature of the algorithm is orographic rain classification. Previously, conspicuous underestimation of rainfall was found

7


---

over coastal mountain regions of the Asian monsoon region, including Japan (Kubota et al. 2009b), Korea (Kwon et al. 2008), Taiwan (Taniguchi et al. 2013), and India (Shige et al. 2015). Spaceborne precipitation radars revealed that heavy rainfall in these areas is frequently associated with low precipitation-top heights (PTHs), which is inconsistent with the look-up tables (LUTs), where heavy rainfall is associated with high PTHs.

Therefore, an orographic/non-orographic rainfall classification scheme to identify orographic rainfall with low PTHs and select an appropriate LUT has been incorporated into the GSMaP algorithm (Shige et al. 2013; 2015; Taniguchi et al. 2013; Yamamoto and Shige 2015; Yamamoto et al. 2017). This classification scheme is based on topographically forced upward motion and convergence of surface moisture flux and results in improvement of rainfall estimation over the entire Asian region. However, the initial scheme misclassified cold orographic rainfall with high PTHs and caused overestimation of rainfall over regions with strong lightning activity, leading to switching off of the scheme over the regions (Yamamoto and Shige 2015).

Misclassification of the scheme implied that topographically forced upward motion initiates rainfall, but it does not fully constrain PTHs. Shige and Kummerow (2016) examined relationships between the thermodynamic characteristics of the atmosphere and the PTHs of heavy orographic rainfall in coastal mountains in the tropics and inferred that low-level static stability is the key parameter determining PTH. Low-level static stability is now being introduced to the scheme of the GSMaP algorithm instead of convergence of surface moisture flux, leading to detection of orographic rainfall with low PTHs even in the regions with strong lightning activity where the scheme has been switched off. The scheme might take into consider changes of precipitation characteristics due to the changes of low-level static stability associated with climate change.

## 2.2 Validation of retrievals where no other reference data exist

*By Pierre-Emmanuel Kirstetter, Viviana Maggioni*

Current validation efforts of satellite rain retrievals use ground-based references (from rain gauges measurements and/or weather radar observations) to assess random and systematic errors associated with multi-satellite precipitation products. Thus, such efforts are limited to local and regional applications and to the availability of those reference datasets. Nevertheless, an accurate mapping of global precipitation and associated uncertainties is fundamental for an effective use of satellite products in any application, from natural hazard mitigation, to water resources management, and vector-borne disease monitoring (Kirstetter et al. 2014). Furthermore, the performance of satellite precipitation products highly depends on the local geography (e.g., topography) and climate (e.g., seasonality), which is also why having a unique global reference for assessing such performance is extremely precious (Maggioni et al. 2016).

Spaceborne radars offer not only a global, but also high-resolution benchmark for evaluating multi-satellite precipitation products that fuse microwave and geostationary-based precipitation measurements. A recent study by Khan et al. (2018) explored this idea and investigated the viability of using the GPM Dual-frequency Precipitation Radar (DPR) as a reference for evaluating a suite of IMERG products. They demonstrate that DPR could provide a valid benchmark for quantifying random errors associated with the infrared component of the

8


---

IMERG precipitation estimates. They also concluded that a climatic zone-specific error characterization would be preferable when estimating errors and uncertainties associated with the IMERG products. Other non-profiling spaceborne radar systems such as the period of record from microwave scatterometer observations (Wentz et al., 2017) are potential sources to expand over-ocean (Ghosh et al., 2014) and over-land (Turk et al., 2015) surface precipitation measurement.

The use of global space-based precipitation radar as a reference measurement is an important contribution to initiatives such as the Global Space-Based Inter-Calibration System (GSICS). Although promising, using precipitation radar retrievals as a reference to validate multi-satellite precipitation products needs to be carefully carried out and can be challenging. First off, satellite radars do not provide the independent set of observations that is required for an objective assessment of multi-satellite product performances. As calibrators of the passive microwave (PMW) sensors that equip most of the satellite platforms in the GPM constellation, they are used to populate the retrieval databases and train the PMW retrieval algorithms, as explained in Section 2.1. The characteristics of the radar instruments (e.g., the sensitivity which defines the detection of rain and snow) and the design of the radar algorithms (e.g., the identification of precipitation types which impacts estimation biases) condition the detection and quantification of precipitation by PMW sensors used in multi-satellite products. Nevertheless, there exist several levels of processing from the radar estimates to the merged products (like the calibration procedure performed for the IMERG product explained in Section 2.1.3), making the latter significantly different from the original radar inputs. Plus, the radar algorithms are constantly evolving, and PMW training data are often built with a different (former) version of current radar precipitation estimates. However, this also implies that the outcomes of any validation exercise are only fully representative of the radar and multi-satellite algorithm versions that are used in the comparison.

Second, spaceborne radars require care in use for the evaluation of multi-satellite precipitation products due to spatial discrepancies. Radars offer orbital precipitation estimates at a spatial resolution from 1.5-km to 5-km (footprint size), which needs to be spatially regridded for comparison with multi-satellite merged products like IMERG (0.1° resolution). While that can be simply accomplished by averaging all the radar values falling within a specific multi-satellite pixel, this process adds a level of uncertainty and potentially introduces new errors.

Third, radar observations are near-instantaneous and therefore would have to be aggregated to the temporal scale of the merged products (e.g., 30-min for IMERG). Because the revisit time of satellite platforms is exceedingly long with respect to typical temporal variability of precipitation at the multi-satellite product resolution, there is currently no robust way to extend the temporal representativeness of instantaneous radar estimates to the desired temporal resolution. The temporal discrepancy adds undesirable errors that can compromise the performance assessment. In other words, even if the radar and merged products were free of any error, they would not yield the same precipitation rates because of uncertainties in the temporal and spatial matching.

Spaceborne radars are particularly suited to perform the validation of multi-satellite precipitation product components because the spatio-temporal discrepancies can be better constrained (e.g., Rysman et al. 2017; You et al., 2020). Level-2 PMW precipitation estimates from individual radiometers that constitute the backbone of the GPM constellation provide also instantaneous estimates. Acknowledging that none of the instantaneous observations produced from these sensors are unambiguously sensitive to the underlying near-surface precipitation, the un-

9


---

certainties that originate from the limited sensitivity of the radiometer channels directly prop-agate into the multi-satellite estimates. While challenging, establishing an absolute assessment of error with a common reference dataset that is globally available can only be achieved through spaceborne radars. Such comparisons can be performed over regions lacking precipitation references such as oceans, and intercompare the values of sensor types in the constellation (e.g., imagers versus sounders) in order to prioritize their inputs into Level-3 multi-satellite products. This approach provides insight on the error introduced at early steps when computing the Level 3 product, rather than on the accumulated error obtained by carrying out a comparison at the end of this process.

In conclusion, acknowledging the limitations highlighted above, assessing how multi-satellite precipitation products perform with respect to spaceborne radar estimates can still be extremely informative, especially in regions where ground observations are sparse or missing altogether.

10


---

# 3. Use of precipitation radars for Numerical Weather Pre-diction applications

## 3.1 Status of NWP observation operators for precipitation radars

The use of space-based radars in NWP is still a nascent application. Because of the current limited space and time sampling of these instruments, the NWP community has indeed given, so far, a lower priority to their assimilation compared to passive microwave instruments. The usage of the latter instruments for initializing NWP models becoming very mature (Geer et al., 2017b), NWP centers are now making steps toward the operational assimilation of space precipitation radars. For instance, the appropriate tools to include space-based radars within NWP applications are currently being integrated into several routinely used observation operators. Indeed, many forward operators have been developed within the international community to support the simulation of cloud and precipitation radars (e.g. Bodas-Salcedo et al., 2011), including the advanced modeling of complex effects like sub-grid cloud variability (e.g. Webb et al., 2001) or multiple scattering (e.g. Hogan and Battaglia, 2008). Nonetheless, there are only a few observation operators for space-based radar which are compatible with operational NWP requirements (e.g. fast enough, equipped with linearized versions, ...). Three examples are presented in sections 3.1.1 to 3.1.3: the JCSDA Community Radiative Transfer Model (CRTM) using the Community Active Sensor Module (CASM, Johnson 2016); the RTTOV-SCATT model and the ZmVar software, which provide a suitable basis for the forward operator in that they simulate both radar reflectivity and attenuation arising from hydrometeors; and the operator developed by JMA, which led to the first worldwide operational assimilation of DPR data, and is presented in section 3.3.

## 3.1.1 CRTM and the Community Active Sensor Module (CASM)

*By Benjamin T. Johnson*

Figure 2 below demonstrates the simulation capabilities of the CRTM+CASM combination for accurate simulation of radar reflectivities. The scattering properties are derived from either Mie Theory, in the case of spherical particles, or from the discrete dipole approximation (DDA; i.e., using the DDSCAT model of Draine and Flatau, 1994). Two-way path-integrated attenuation is computed from both hydrometeor and gaseous absorption, the latter being non-negligible at Ka-band and higher frequencies. In addition to the reflectivity computations, CASM provides the tangent-linear, adjoint, and Jacobians (K Matrix values), which are computed at each vertical level with respect to the various hydrometeor properties. At present there is no Jacobian computation for the surface reflection, and radar multiple scattering is not explicitly computed. Similar to RTTOV, the CRTM provides a "cloud fraction" capability, which partitions cloud water content in a given cloud layer. CASM has not been tested with variable cloud fractions, and it is expected that it could significantly impact the computed reflectivities and associated Jacobians.

To date, no operational center in the United States has attempted assimilating radar observations using CRTM+CASM. Some efforts have been made toward operational assimilation of radar reflectivities in the Gridpoint Statistical Interpolation (GSI) DA system, such as Wang and Wang (2017), but their approach was done without linearized elements. U.S. assimilation

11


---

of radar-derived products is common in research applications (e.g., Pan et al. 2018, Lai et al. 2019, Li and Wang 2008). However, operational assimilation of satellite-based radar observations and derived products remains as a challenge. In the near future, CASM will be tested within the Joint Effort for Data assimilation Integration (JEDI) framework (https://www.jcsda.org/jcsda-project-jedi), recently released by the JCSDA, which will enable testing in a variety of NWP systems that are connected through JEDI.

Heatmap comparison of CASM simulated vs DPR observed radar reflectivity. Top panel (a) shows CASM @ Ku simulation, bottom panel (b) shows DPR @ Ku observations. Both plots show altitude in km on the y-axis (0-6) and a horizontal dimension on the x-axis (0-140). Color scale indicates reflectivity Zc [dBZ] from 10 to 35.

Figure 2: Example of (a) the CRTM + CASM simulation, compared with (b) the GPM DPR observations at Ku-Band. This includes attenuation correction using the dual-wavelength ratio approach of Meneghini, and near-surface noise removal described in Johnson, 2007.

## 3.1.2 The RTTOV-SCATT software

*By Philippe Chambon and Alan Geer*

As mentioned above, similar efforts to the CASM software have been conducted under the EUMETSAT NWP SAF. In the past 15 years, the RTTOV-SCATT software (Bauer et al., 2006) has been continuously improved to support new instruments as well as providing more accurate simulations for a broad range of frequencies. This includes the possibility of using advanced radiative properties to represent hydrometeors, such as three dimensional particle shapes and a variety of particle size distributions (e.g. Geer and Baordo, 2014, Geer et al., 2021a) ; these are highly variable in nature and the settings require some degree of tuning or parameter estimation (e.g. Geer, 2021b). Recently, RTTOV-SCATT capabilities have been augmented to simulate cloud and precipitation radar observations, thanks to a collaboration between ECMWF and Météo-France. In its first implementation this simulator suffers from a few limitations, like not realistically simulating the effects of melting hydrometeors or the effect of multiple scattering. Nonetheless, it is likely to be broadly used for the assimilation of spaceborne precipitation radars into NWP models because it is equipped with the necessary Tangent Linear and Adjoint versions of the non-linear operator, and because it will provide

12


---

macrophysical (e.g. cloud overlap) and microphysical (e.g. PSD and particle shape) consistency with the equivalent RTTOV operators for passive microwave. Work will continue to add features including all those available in the ZmVar operator, such as more sophisticated cloud overlap (see below). With the availability of the recently released RTTOV V13, including this radar observation operator, Météo-France is planning to set up the monitoring of current (GPM-DPR) and future (EarthCARE) precipitation radars. This monitoring will be a useful tool for future physics developments (see Section 3.2). This simulator will also be used at ECMWF as described below, and is also in testing at JMA.

## 3.1.3 The ZmVar simulator

*By Alan Geer*

Developments towards assimilating EarthCARE data at ECMWF have produced an additional operational quality radar operator, known as ZmVar (DiMichele et al., 2012; Fielding and Janiskova, 2020, and references therein). This provides simulations at W-band (and lidar) and has been proven in experimental direct assimilation of CloudSat observations (Janiskova and Fielding, 2020). Microphysical assumptions are simulated in a similar way to RTTOV, albeit with different choices of PSD and frozen particle shape. There are two cloud overlap options, one similar to RTTOV’s random overlap, one a more sophisticated two-column approach (Fielding and Janiskova, 2020). Multiple scattering is not represented. ZmVar represents the state of the art for operational radar operators but it is not publicly available. The radar part of ZmVar will potentially be replaced by RTTOV at ECMWF once the same level of functionality is available, making it easier to ensure consistent assumptions across passive and active microwave observation operators.

## 3.2 Use of precipitation radars for validation of NWP models

*By Alan Geer, Philippe Chambon and Mary Borderies*

Away from the areas covered by ground radar systems, space radar offers unique observations for validating and informing the development of forecast models. Increasingly, this validation is done in the observation space, using observation (forward) operators to simulate radar observables from the model fields. In this context, validation and model development are closely linked to the data assimilation process used in weather forecasting. The forward approach means that the information content of the observations is used most optimally, since validating against retrievals implicitly incorporates the assumptions made in the retrieval along with the observing limitations of the instruments (as an example, Duncan and Eriksson, 2018, have shown large differences in ice water path products due to varying microphysical assumptions and instrument sensitivities). In the forward validation approach, a good match between simulated and observed precipitation radar would clearly confirm that the model can simulate the types of rain and snow to which the instrument is sensitive, as long as microphysical and macrophysical assumptions can be made consistent with the model under validation, and as long as there are no compensating errors elsewhere in the modelling. However, a precipitation radar at just one or two frequencies could not validate all rain and snow in the model, from the lightest to the heaviest. For instance, as mentioned in Section 2.1.2, the GPM precipitation radars have a limited sensitivity, therefore the comparisons to the model with the forward approach

13


---

will not allow conclusions on light precipitation. It is therefore difficult to draw conclusions about precipitation occurrence and/or precipitation intensity model issues with these single instruments. To fill any gaps requires additional instrumentation - so Ka/Ku band radar would be used to validate heavier rain and W band for lighter rain.

Diagram showing cloud and precipitation sensitive observations across different spectral bands (Microwave, Radar/Lidar, Sub-mm, Infrared, Solar, Earth radiation budget) and their sensitivities to various atmospheric parameters like cloud particles, liquid water, ice, and lightning.

Figure 3: Cloud and precipitation sensitive observations: now and near future (Source: A. Geer and S. English, ECMWF)

A comprehensive model validation strategy includes radar as a key part of the full range of available operational observations from ground and space, including passive measurements from the microwave to the solar wavelengths (Figure 3). With sufficient observation types giving varied but overlapping sensitivities, observations will eventually become capable of constraining both the resolved fields in forecast models (e.g. the hydrometeor mixing ratios) and the macro-physical and micro-physical assumptions made in moist parameterizations and observation operators, such as sub-grid heterogeneity and overlap, along with particle shapes and size distributions (e.g. Geer et al., 2017a). This ambitious goal is known as “macrophysical and microphysical closure”.

In order to facilitate such a multi-instrument validation, one goal could be to have all these observations simulated and compared to the model within a single unified framework. This is something a data assimilation framework can offer to process all observation types in a consistent way. In addition, observations do not need to be active in those frameworks (in the sense of them contributing to the cost function of a DA system and therefore to its analyses) but can also contribute to the simple monitoring of the model. This way, observations and their model equivalent are systematically computed and ready to be used for model diagnostics. As mentioned in Section 3.1, spaceborne precipitation radars have received less attention than some other observations within the NWP community, likely because of their current narrow swaths and sparse overpasses, but this may change in the future based on the very fruitful studies which have been performed in the community.

14


---

Ku-band DPR reflectivity maps comparing AROME simulations (top) and GPM/DPR observations (bottom) at 2.5 km, 3 km, and 4.5 km altitudes over southwestern Europe on 2 October 2020.

Figure 4 :Ku-band DPR reflectivity at different altitude above sea level (from left to right: 2.5 km, 3 km and 4.5 km) over southwestern Europe on 2 October 2020. Observations are in the bottom panels. The co-located AROME simulations (using RTTOV13) are depicted in the top panels. The altitude above sea level is represented by the shadings in the background.

Spaceborne precipitation and cloud radars provide valuable information about microphysical properties and are a clear asset to validate kilometer-scale NWP models. Because of their higher sensitivity to the smallest particles and their finer vertical resolution, they also complement ground-based precipitation radar data over land. As an example, the GPM DPR was used to validate the Météo-France operational kilometer-scale NWP model AROME for a heavy rainfall event which occurred over southern Europe in early October 2020. The RTTOV-SCATT forward operator is applied to AROME 1-h forecasts to simulate the Ku-band DPR reflectivity. Attenuation by hydrometeors and water vapor is accounted for. Figure 4 shows in the top panels (bottom panels) maps of the simulated (observed) Ku-band radar reflectivity at 2.5 km, 3 km and 4.5 km above sea level (from left to right) on 2 October 2020. Figure 4 indicates that the overall simulated reflectivity pattern matches the observations well. However, there is a clear underestimation of the reflectivity at an altitude of about 3 km, which is probably due to the inaccurate representation of the bright-band used in RTTOV13 to simulate the reflectivity in the melting layer. Indeed, as shown in Figure 5, the melting layer is located at an altitude of approximately 3 km. Therefore, the use of spaceborne radars in and above the melting layer requires further investigation before operational use (monitoring or data assimilation).

15


---

Height of the 0°C isotherm for AROME (left) and GPM DPR observations (right)

Figure 5: Height of the 0°C isotherm for the Météo-France km-scale NWP model AROME (left) and for the observations (right).

A sophisticated example of model-to-observation validation using a single sensor is given by Di Michele et al. (2012). Here, Cloudsat was used to reveal potential issues in the ECMWF model, such as deficient occurrence of precipitation in the Southern Hemisphere storm track. The uncertainty of assumptions in the forward modelling (such as cloud overlap and particle size distributions) was quantified, allowing a more confident discrimination of features thought to be biases in the forecast model. There is great potential for validating models in this type of framework, but the ultimate aim must be to improve the forecast models.

This can be achieved through trial and error and scientific intuition, but the combination of information from many different observational sources will likely require fully automated and objective model development techniques on the boundaries of machine learning and data assimilation (Schneider et al., 2017, Geer, 2020a). Existing development of such approaches has focused on parameter estimation, a type of data assimilation. This is difficult for many reasons and has not yet been applied to space radar, but its potential can be seen in recent work. One example is the tuning of the autoconversion parameter in a large-scale condensation scheme using observations of outgoing long wave and shortwave radiation (Kotsuki et al., 2020). Another is the simultaneous tuning of six different assumptions in the RTTOV all-sky passive modelling, based on model-observation departures from SSMIS (Geer, 2020b). In this kind of work, precipitation radars are expected to better constrain the vertical description of precipitation profiles, the particle size distributions at each level, and hence to indirectly constrain aspects of the forecast model, such as evaporation processes.

## 3.3 Data assimilation of precipitation radar data

**By Yasutaka Ikuta, Kozo Okamoto and Alan Geer**

As mentioned in previous sections, spaceborne precipitation radar such as GPM DPR provides valuable observations of precipitation systems in three dimensions. The assimilation of DPR data is becoming an important technique for improving the accuracy of forecasting to complement scarce ground-based radar observation for example over the ocean.

As a data assimilation method for the radar data, an indirect assimilation method that combines 1D Bayesian (1D-Bay) estimation and 3D / 4D variational data assimilation has been adopted,

16


---

and it has led to improved forecast accuracy. Firstly, the 1D-Bay estimation with 3D-Var assimilation was developed as a ground-based radar assimilation technique (Caumont et al., 2010, Wattrelot et al., 2014). In addition, 1D-Bay+3D/4DVar has proven to be effective in assimilating many other remote sensing assimilation (Augros et al., 2018; Borderies et al., 2019, Duruisseau et al. 2019).

Three maps showing 3-hour accumulated precipitation for (a) observation, (b) forecast without DPR, and (c) forecast with DPR.

Figure 6: The 3-hour accumulated precipitation of (a) observation, (b) T+33hr forecast without DPR and (c) with DPR at 0900 UTC on 9 September 2015.

JMA has employed the one-dimensional maximum likelihood estimation (1D-MLE) method (Ikuta et al. 2021) that was developed from the 1D-Bay method. 1D-MLE enables the estimation of relative humidity (RH) profiles according to a non-Gaussian probability density function. In the 1D-MLE, the vertical profile of RH is first obtained from reflectivity profiles. Next, the estimated RH profiles are assimilated as conventional observations in the 4D-Var. The 1D-MLE performs correctly if 1D-Bay underestimates RH near supersaturation and overestimates RH in the case of bimodal-distribution.

The impact of data assimilation using estimated RH profiles from DPR was evaluated on JMA’s mesoscale NWP system. The result showed that the effect on the upper atmosphere verified against radiosonde observations was neutral and the forecast of precipitation was improved over the one without DPR. For example, precipitation forecasts with DPR assimilation were improved in severe weather events that caused large floods (Figure 6). It was also found that forecasting accuracy was maintained for a narrow DPR swath and low revisit frequency by repeating the assimilation-forecast cycle. Since the effectiveness of DPR assimilation was confirmed, JMA operationally began assimilating DPR data with the 1D-MLE approach, starting in March 2016.

The issues of DPR assimilation at JMA remains that the estimated RH is not assimilated in regions where the background temperature is below 0 deg C. Therefore, DPR data are rarely assimilated in winter. This data screening was adopted due to both the model bias at the ice phase as pointed out in Okamoto et al. (2016) and the simplified observation operator based on spherical particle shape.

Recently, JMA has been developing the radar simulator for non-spherical particles. In addition, the biases caused by the NWP model were reduced by improving the cloud microphysics scheme itself (Ikuta et al. 2020). JMA is also developing a 4DVAR system using a Tangent-

17


---

linear/Adjoint model of the cloud physics scheme, and keeps the research on the direct assim-
ilation of reflectivity for future JMA operational system.

In addition to the operational development, JMA has been investigating the direct assimilation
of reflectivities of GPM/DPR in a research-based data assimilation system (Okamoto et al.
2016). In their study, assimilation of reflectivities of KuPR and KaPR corrected hydrometeors
as well as dynamic field and relative humidity in ensemble-based variational scheme (EnVar;
Aonashi et al. 2016). Note that this research also excluded reflectivities in the ice scattering
regions because of difficult treatment of significant overestimation of frozen hydrometeors in
the forecast model. Single-cycle assimilation experiments suggested that the reflectivity assim-
ilation produced analysis increment with fine horizontal structure of hydrometeor and vertical
wind and complemented a broad analysis increment of humidity and dynamic field from col-
located GMI microwave imager data. It should be noted that DPR was able to make detailed
analysis but with limited spatial impacts because of relatively narrow observation coverage and
strict quality control in the assimilation system to avoid contamination from model bias. Thus,
effective usage of precipitation radar requires synergetic use of observations with wide cover-
age such as microwave imagers and reliable background fields. This was demonstrated in better
analysis and TC track forecasts from synergetic usage of DPR and GMI compared with use of
the individual sensors (Okamoto et al. 2016).

Direct assimilation of radar reflectivity for weather forecasting has recently been demonstrated
by Janiskova and Fielding (2020), who assimilated CloudSat observations (along with Calipso
lidar) into the ECMWF forecasting system. The impact on forecast quality was broadly neutral,
but this is still considered a positive result. When the observations are part of the data assimi-
lation system they become routinely available for model validation and development activities,
as mentioned in Section 3.2. Further, passive all-sky radiance assimilation also had small im-
pact initially, but after many years of development, and with the availability of larger numbers
of sensors, it now provides almost 20% of short-range forecast impact in the ECMWF system
(Geer et al, 2017b). Hence it is envisaged that further development of precipitation radar as-
similation will also lead to clearer positive impacts on forecasts. The CloudSat results were
obtained in the framework of a long-running project to prepare for the launch of EarthCARE.
With the techniques now proven and most of the tools in place, the EarthCARE data is expected
to be assimilated soon after launch, assuming that trials show a positive or neutral forecast
impact.

ECMWF is also preparing to assimilate the DPR, although this activity is less mature than the
EarthCARE work. This approach will use the RTTOV radar operator and will exploit synergies
with the existing all-sky passive microwave assimilation (particularly GMI) by using exactly
the same microphysical and macrophysical assumptions. The 245 km swath of DPR is expected
to help increase the direct impact of assimilation more than the single nadir beam of CloudSat
or EarthCARE. The indirect benefit on model development is also expected to be substantial
as it will help to further characterize biases such as the imperfect diurnal cycle of convection
over tropical land surfaces in the ECMWF model (e.g. Chambon and Geer, 2017).

18


---

# 4. A perspective of operational applications: development of techniques to monitor the calibration of ground radar networks

*By Alain Protat and Valentin Louf*

The quantitative use of operational data from weather radar networks requires accurate calibration procedures to achieve radar calibration to better than 1 dB. The cost of maintaining such a high calibration standard using radar engineers' time for regular onsite checks is becoming prohibitive for very large networks, such as in Europe (>200 radars), China (>200 radars), the U.S. (~160 radars) or even Australia (~65 radars).

In this context, the development of calibration monitoring techniques not requiring human intervention onsite is critical. The following techniques have been explored, all with specific advantages and challenges:

*   Using an external target (metal spheres, trihedral reflector, e.g., Atlas 2002; Chandrasekar et al. 2015) of known backscatter cross-section. Although it has been demonstrated to provide accurate calibration measurements, there are several practical challenges that need to be overcome, such as the management of receiver saturation, location of target within the radar beam, optimal distance to reflector, signal-to-clutter ratio, and the impact of the atmospheric state between the radar and the reflector.

*   Using drop size distribution measurements from surface disdrometers, from which reflectivities can be simulated using scattering calculations. An advantage of this technique is that calibration can be checked every time there is a rainfall event over the disdrometer sites. The main challenges are the uncertainties in scattering calculations and the fact that the volumes sampled by disdrometers and radar are very different and not collocated, requiring strong assumptions on the horizontal and vertical variability of the drop size distribution.

*   Using the so-called Relative Calibration Adjustment (RCA) technique, which employs the 95<sup>th</sup> percentile of ground clutter reflectivities at close range from the radar to track calibration changes (Rinehart, 1978; Silberstein et al. 2008; Marks et al. 2009; Louf et al. 2019). The main advantage of this technique is that it provides a very accurate tracking of calibration change (to within 0.2-0.3 dB, Louf et al. 2019). The main challenges are that it does not provide an absolute calibration, which needs to be established by another calibration technique, and the fact that a change in the 95<sup>th</sup> percentile of ground clutter can also be attributed to other factors (a change in azimuth and elevation pointing, anomalous propagation, or a sudden change in the nature of the ground clutter around the radars).

*   Using the measured reflectivity of the Sun (e.g., Huuskonen and Holleman, 2007). This well-proven technique provides a means to track changes in measured sun power and radar pointing angles. However, it is not an end-to-end calibration technique, as it only provides information about the receiver chain calibration, not the transmitting part of the radar.

19


---

$\Rightarrow$ Using the "self-consistency" relationship between dual-polarization variables (e.g., Gorgucci et al. 1992; Goddard et al. 1994; Gourley et al. 2009). Although more work needs to be done to better understand the regional variability of such relationships (Louf et al. 2019), there is potential to achieve the required accuracy of 1 dB with such technique. A main limitation is that it requires high-quality dual-polarization observations.

$\Rightarrow$ Using a calibrated airborne or spaceborne radar (Schwaller and Morris, 2011; Smalley et al., 2014; Norin et al., 2015; Smalley et al., 2017; Warren et al. 2018; Louf et al. 2019). If such data are available within range of a ground-based radar, statistical comparisons between collocated volumes can be used to calibrate the ground-based radar.

In this section, the potential of the last approach, namely using spaceborne radars to calibrate operational weather radar networks is discussed. The major advantage of such a technique is that it provides a single source of reference for all surface radars, for any given national radar network, and allows comparisons of calibration procedures used for different operational radar networks, potentially providing an international benchmark. The other advantage is that the calibration of spaceborne radars is monitored very closely by national space agencies responsible for the spaceborne radar missions. The main challenges with such techniques are 1) the assumption that the spaceborne radar is itself well calibrated, and 2) the difference in size and acquisition times of the sampled volumes, requiring the development of volume matching techniques.

Upon the launch of the first precipitation (Ku-band) radar in space as part of TRMM (Simpson et al. 1996) and of the first cloud radar (W-band) in space (CloudSat, Stephens et al. 2018; Tanelli et al. 2008), satellite / surface radar comparisons were initially used as part of the ground validation programs of these satellite radar missions with the goal of establishing and monitoring the calibration of the satellite radar using airborne or ground-based radars as the reference (e.g., Protat et al. 2009). However, the successful development of accurate calibration techniques unique to the satellite and aircraft viewing geometries (e.g., Durden et al. 2003; Tanelli et al. 2008), backed by internal and external calibration checks (Takahashi et al. 2003) has unlocked the potential to confidently use these spaceborne radars in the opposite direction, as single sources of reference to calibrate surface weather radar networks.

The idea of using spaceborne radars to calibrate research-grade ground radars was first exploited in pioneering studies of Anagnostou et al. (2001) and Bolen and Chandrasekar (2000) for TRMM, and Protat et al. (2011) for CloudSat. Many researchers have initially taken the simple approach of remapping ground and satellite radar data to a common three-dimensional Cartesian grid (e.g., Anagnostou et al. 2001; Bolen and Chandrasekar 2003; Park et al. 2015). A more accurate approach, known as the Volume Matching Method (VMM), has been developed as part of the Ground Validation program of GPM (Hou et al. 2014) by Schwaller and Morris (2011) to better account for differences in sampling volumes, partial beam filling effects within the matched volumes, frequency differences, minimum detectable signal differences, and temporal mismatches. Settings of the VMM have been carefully assessed and refined by Warren et al. (2018) and Louf et al. (2019) to develop the first operational implementation of a spaceborne radar calibration monitoring for the Australian weather radar network. Figure 7 shows the operational dashboard developed for the Australian operational radar network, which hosts a patchwork from very old to very advanced S-band and C-band radars, located near capital cities or in extremely remote regions. Until Figure 7 was produced, radar engineers from the Bureau of Meteorology would have expected little variation in calibration between

20


---

radars, and even more so within each state or territory of Australia, given that they are all calibrated using the same procedures and by the same radar engineers within each region.

Providing an exact number for the accuracy of the satellite VMM calibration technique is a challenging task. The standard deviation of the calibration error estimate is found to be quite variable from one satellite overpass to another, as it depends on the number of collocated volumes within an overpass and how well the underlying assumptions of the VMM are satisfied. Broadly speaking, the standard deviation of the distribution of calibration error estimates from all volumes matched of an overpass is generally between 2.0 and 3.0 dB, which is higher than the requirement of 1 dB. However, when averaging all individual satellite overpass estimates for a known stable period of calibration (using the RCA calibration tracking technique discussed previously), this error can generally be reduced to better than 1 dB (e.g., Louf et al. 2019). This is illustrated in Figure 8, showing a time series of individual DPR estimates for the Sydney (Terrey Hills) radar over a stable 3-month period. In this example, the mean standard deviation for each point in the time series is 2.8 dB, but the overall standard deviation of the mean calibration error over the stable period is only 0.75 dB (from 12 overpasses).

This example from Figure 8 illustrates the main lesson learned from the operational development of the GPM calibration technique in Australia, which is that the optimal framework for accurate calibration of a radar network is to combine the strengths of multiple techniques. Australia has settled on a combination of three techniques. The RCA (ground clutter) technique provides an accurate tracking of calibration changes, but the solar calibration technique is needed to ensure that a change in ground clutter reflectivity is not due to a change in azimuth or elevation pointing accuracy or anomalous propagation. Once stable periods of relative calibration are established with the combined RCA and solar calibration techniques, all satellite estimates from individual overpasses are used to estimate an absolute calibration error.

Such a combined approach using CloudSat (and future follow-up spaceborne cloud radar missions) is also being developed to calibrate long-term observations from the cloud radars operated by the U.S. Atmospheric Radiation Measurement (ARM; see Kollias et al. 2019 for the satellite comparisons; Hunzinger et al. 2020 for the RCA technique applied to higher-frequency radars).

21


---

A map of Australia showing the locations of weather radars with color-coded dots indicating calibration errors. A color scale on the right indicates the magnitude of the error in dB.

Figure 7: A map of Australia summarizing the calibration errors of all radars of the Australian weather radar network (as of September 2020). Current calibration procedures seem to underestimate calibration, with only a quarter of the radars being calibrated to the 1 dB standard.

### 71. THills

<table>
  <thead>
    <tr>
        <th>Date</th>
        <th>$\Delta Z = Z_{GR} - Z_{DPR}$ (dB)</th>
        <th>Sample Size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>2018-03-31</td>
<td>1.5</td>
<td>$150 &lt; size &lt; 250$</td>
    </tr>
<tr>
        <td>2019-04-30</td>
<td>2.0</td>
<td>$Sample size &gt; 250$</td>
    </tr>
<tr>
        <td>2019-08-31</td>
<td>1.8</td>
<td>$100 &lt; size &lt; 150$</td>
    </tr>
<tr>
        <td>2019-09-30</td>
<td>2.2</td>
<td>$100 &lt; size &lt; 150$</td>
    </tr>
<tr>
        <td>2019-07-31</td>
<td>1.2</td>
<td>$60 &lt; size &lt; 100$</td>
    </tr>
  </tbody>
</table>

### 71. THills accumulated.

<table>
  <thead>
    <tr>
        <th>$\Delta Z = Z_{GR} - Z_{DPR}$</th>
        <th>Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>-10.0</td>
<td>0</td>
    </tr>
<tr>
        <td>-7.5</td>
<td>5</td>
    </tr>
<tr>
        <td>-5.0</td>
<td>20</td>
    </tr>
<tr>
        <td>-2.5</td>
<td>80</td>
    </tr>
<tr>
        <td>0.0</td>
<td>250</td>
    </tr>
<tr>
        <td>2.5</td>
<td>350</td>
    </tr>
<tr>
        <td>5.0</td>
<td>100</td>
    </tr>
<tr>
        <td>7.5</td>
<td>20</td>
    </tr>
<tr>
        <td>10.0</td>
<td>0</td>
    </tr>
  </tbody>
</table>

Figure 8: Time series of DPR calibration error estimates (left) and the distribution of calibration error estimates over the whole stable calibration period (right) for the Sydney (Terrey Hills) operational weather radar.

22


---

# 5. Conclusions and recommendations for future space-borne precipitation radars

This report highlighted both very mature and emerging applications of spaceborne cloud and precipitation radars. These applications require a <mark>continuity of precipitation radar observations</mark> in the future to sustain development and/or operations:

*   Precipitation retrievals from passive microwave instruments require databases of co-located passive and active microwave observations. These databases will need to be repeatedly updated to account for an evolving climate. Multiplatform combined products also benefit from a continuous intercalibration of precipitation retrievals from the various radiometers before merging and therefore constantly require recent radar observations.

*   Following the pioneering work of JMA, NWP centers are getting prepared to monitor and/or assimilate spaceborne precipitation radars. Major steps have recently been made by releasing to the international community observation operators with capabilities adapted to this endeavor. By definition, weather prediction always needs the most recent observations to operate. Cubesat-sized Ka-band precipitation profiling radars have been successfully deployed and operated from low Earth orbit (Sy et al., 2021), and recent initiatives from within the private sector bolster the belief that precipitation radars in space are useful for forecast improvements.

*   Spaceborne precipitation profiling radar provides the weather forecasting community with a capability to identify severe weather conditions such as hail and extreme rain, and over time, to gather climatologies of these events (Bang and Cecil, 2021). Other applications are emerging, like the pioneering work of the BoM on the use of spaceborne precipitation radars to monitor ground-based radar networks, which can be challenging in large regions by any other means. These techniques will require continuous space radar observations to operate on a routine basis.

A number of aspects of the current generation of radars which could be improved in future instruments have also been highlighted in this report:

*   Several applications would benefit from future instruments with <mark>a wider swath</mark> compared to the TRMM, GPM, and CloudSat instruments (or a constellation of such radars with the current swath). Spaceborne precipitation radars have received less attention than other observations within the NWP community because of their current narrow swaths. Radars providing higher rates of time/space sampling provide a higher capacity for significantly improving numerical weather forecast skills. Considering the intercalibration required for combined precipitation retrievals, time/space coincidences between the present narrow radar swaths and the LEO satellite radiometer swaths preclude stable calibrations at the seasonal (or shorter) timescale. Intercalibration frameworks (e.g., GSICS) would therefore benefit from a wider radar swath.

*   An <mark>improved sensitivity, resolution</mark>, and <mark>multi frequency capabilities</mark> of future instruments would also benefit several applications (Battaglia et al., 2020). The partitioning of hydrometeors (rain, snow, cloud water, ice water) performed by microphysical schemes used in numerical models are becoming more and more complex and require

23


---

validation on a global scale. While intermittent coincident observations from the CloudSat and GPM radars has been utilized for improvement to cold-season precipitation estimation (Turk et al., 2021), expanded multi-frequency radar observations would provide the necessary observations to validate rain and snow as inferred in models, from the lightest to the heaviest. Similarly, in precipitation retrieval techniques, issues remain with the databases based on the current generation of radars. The PR and DPR radars are not sufficiently sensitive to capture drizzle or light snowfall, while CloudSat has sufficient sensitivity, but its nadir-only track of fine-scale footprints is not sufficient to cover a radiometer footprint.

➔ **Improving the capabilities of instruments to observe closer to the surface** would also be very beneficial to several applications. Current radars have known underestimation issues in orographic regions, where heavy, but very shallow precipitation is often masked by ground clutter from the complex topographic terrain. Side-lobe clutter also contaminates a non-negligible fraction of observations when observing close to the ground, which reduces their current sampling of shallow precipitation, no matter how intense. A similar problem affects radars when detecting low clouds and shallow drizzling stratocumulus clouds (Lamer et al., 2020).

➔ New **capabilities such as Doppler measurements** would also be very welcome for a number of applications. For instance, the NWP community has shown that constraining physical (condensed water mass, humidity) and dynamical (winds) fields together within initial conditions leads to positive impacts on the longest forecast ranges. Novel missions involving differential absorption radars (Lebsock et al., 2015), frequent high-resolution radar sampling (Haddad et al., 2017) and conically scanning Doppler cloud radars (Illingworth et al., 2018) have been recently proposed to provide such measurements.

The authors are aware that all the potential improvements highlighted in this report are very challenging to achieve, both technically and financially, for space agencies. Nevertheless, addressing these issues in a prioritized way across the agencies’ programs would greatly benefit the development and use of current and future applications of spaceborne precipitation radars.

24


---

# 6. References

Anagnostou, E. N., Morales, C. A., & Dinku, T. (2001). The use of TRMM precipitation radar observations in determining ground radar calibration biases. *Journal of Atmospheric and Oceanic Technology*, 18(4), 616-628. DOI: https://doi.org/10.1175/1520-0426(2001)018<0616:TUOTPR>2.0.CO;2018<0616:TUOTPR>2.0.CO;2)

Aonashi, K., Awaka, J., Hirose, M., Kozu, T., Kubota, T., Liu, G., ... & Takayabu, Y. N. (2009). GSMaP passive microwave precipitation retrieval algorithm: Algorithm description and validation. *Journal of the Meteorological Society of Japan. Ser. II*, 87, 119-136. DOI: https://doi.org/10.2151/jmsj.87A.119

Aonashi, K., Okamoto, K., Tashima, T., Kubota, T., & Ito, K. (2016). Sampling error damping method for a cloud-resolving model using a dual-scale neighboring ensemble approach. *Monthly Weather Review*, 144(12), 4751-4770. DOI: https://doi.org/10.1175/MWR-D-15-0410.1

Atlas, D. (2002). Radar calibration: Some simple approaches. *Bulletin of the American Meteorological Society*, 83(9), 1313-1316. DOI: https://doi.org/10.1175/1520-0477-83.9.1313

Augros, C., Caumont, O., Ducrocq, V., & Gaussiat, N. (2018). Assimilation of radar dual-polarization observations in the AROME model. *Quarterly Journal of the Royal Meteorological Society*, 144(714), 1352-1368. DOI: https://doi.org/10.1002/qj.3269

Bang, S.D., Cecil, D.J., 2021. Testing Passive Microwave-Based Hail Retrievals Using GPM DPR Ku-Band Radar. *Journal of Applied Meteorology and Climatology* 60, 255–271. https://doi.org/10.1175/JAMC-D-20-0129.1

Battaglia, A., Kollias, P., Dhillon, R., Roy, R., Tanelli, S., Lamer, K., ... & Furukawa, K. (2020). Spaceborne Cloud and Precipitation Radars: Status, Challenges, and Ways Forward. *Reviews of Geophysics*, 58(3), e2019RG000686. DOI: https://doi.org/10.1029/2019RG000686

Bauer, P., Amayenc, P., Kummerow, C. D., & Smith, E. A. (2001). Over-ocean rainfall retrieval from multisensor data of the Tropical Rainfall Measuring Mission. Part II: Algorithm implementation. *Journal of Atmospheric and Oceanic Technology*, 18(11), 1838-1855. DOI: https://doi.org/10.1175/1520-0426(2001)018<1838:OORRFM>2.0.CO;2018<1838:OORRFM>2.0.CO;2)

Bodas-Salcedo, A., Webb, M. J., Bony, S., Chepfer, H., Dufresne, J. L., Klein, S. A., ... & John, V. O. (2011). COSP: Satellite simulation software for model assessment. *Bulletin of the American Meteorological Society*, 92(8), 1023-1043. DOI: https://doi.org/10.1175/2011BAMS2856.1

Bolen, S. M., & Chandrasekar, V. (2003). Methodology for aligning and comparing spaceborne radar and ground-based radar observations. *Journal of Atmospheric and Oceanic Technology*, 20(5), 647-659. DOI: https://doi.org/10.1175/1520-0426(2003)20<647:MFAACS>2.0.CO;220<647:MFAACS>2.0.CO;2)

Bolen, S. M., & Chandrasekar, V. (2000). Quantitative cross validation of space-based and ground-based radar observations. *Journal of Applied Meteorology*, 39(12), 2071-2079. DOI: https://doi.org/10.1175/1520-0450(2001)040<2071:QCVOSB>2.0.CO;2040<2071:QCVOSB>2.0.CO;2)

25


---

Borderies, M., Caumont, O., Delanoë, J., Ducrocq, V., Fourrié, N., & Marquet, P. (2019). Impact of airborne cloud radar reflectivity data assimilation on kilometre-scale numerical weather prediction analyses and forecasts of heavy precipitation events. *Natural Hazards and Earth System Sciences*, 19(4), 907-926. DOI : https://doi.org/10.5194/nhess-19-907-2019

Caumont, O., Ducrocq, V., Wattrelot, É., Jaubert, G., & Pradier-Vabre, S. (2010). 1D+ 3DVar assimilation of radar reflectivity data: A proof of concept. *Tellus A: Dynamic Meteorology and Oceanography*, 62(2), 173-187. DOI: https://doi.org/10.1111/j.1600-0870.2009.00430.x

Chambon, P., & Geer, A. J. (2017). All-sky assimilation of Megha-Tropiques/SAPHIR radiances in the ECMWF numerical weather prediction system. European Centre for Medium-Range Weather Forecasts, Tech. Memo. 802.

Chandrasekar, V., Baldini, L., Bharadwaj, N., & Smith, P. L. (2015). Calibration procedures for global precipitation-measurement ground-validation radars. *URSI Radio Science Bulletin*, 2015(355), 45-73. DOI: https://doi.org/10.23919/URSIRSB.2015.7909473

Di Michele, S., Ahlgrimm, M., Forbes, R., Kulie, M., Bennartz, R., Janisková, M., & Bauer, P. (2012). Interpreting an evaluation of the ECMWF global model with CloudSat observations: Ambiguities due to radar reflectivity forward operator uncertainties. *Quarterly Journal of the Royal Meteorological Society*, 138(669), 2047-2065. DOI: https://doi.org/10.1002/qj.1936

Duncan, D. I., & Eriksson, P. (2018). An update on global atmospheric ice estimates from satellite observations and reanalyses. *Atmospheric Chemistry and Physics*, 18(15), 11205-11219. DOI: https://doi.org/10.5194/acp-18-11205-2018

Durden, S. L., Im, E., Haddad, Z. S., & Li, L. (2003). Comparison of TRMM precipitation radar and airborne radar data. *Journal of Applied Meteorology*, 42(6), 769-774. DOI: https://doi.org/10.1175/1520-0450(2003)042<0769:COTPRA>2.0.CO;2042<0769:COTPRA>2.0.CO;2)

Duruisseau, F., Chambon, P., Wattrelot, E., Barreyat, M., & Mahfouf, J. F. (2019). Assimilating cloudy and rainy microwave observations from SAPHIR on board Megha Tropiques within the ARPEGE global model. *Quarterly Journal of the Royal Meteorological Society*, 145(719), 620-641. DOI: https://doi.org/10.1002/qj.3456

Fielding, M. D., & Janisková, M. (2020). Direct 4D-Var assimilation of space-borne cloud radar reflectivity and lidar backscatter. Part I: Observation operator and implementation. *Quarterly Journal of the Royal Meteorological Society*, 146(733), 3877-3899. DOI: https://doi.org/10.1002/qj.3878

Geer, A., Ahlgrimm, M., Bechtold, P., Bonavita, M., Bormann, N., English, S., ... & Weston, P. (2017a). *Assimilating observations sensitive to cloud and precipitation*. European Centre for Medium-Range Weather Forecasts, Tech. Memo. 815.

Geer, A. J., Baordo, F., Bormann, N., Chambon, P., English, S. J., Kazumori, M., ... & Lupu, C. (2017b). The growing impact of satellite observations sensitive to humidity, cloud and precipitation. *Quarterly Journal of the Royal Meteorological Society*, 143(709), 3189-3206. DOI : https://doi.org/10.1002/qj.3172

26


---

Geer, A. J. (2021a). Learning earth system models from observations: machine learning or data assimilation?. *Philosophical Transactions of the Royal Society A*, 379(2194), 20200089. DOI : https://doi.org/10.1098/rsta.2020.0089

Geer, A. J. (2021b). Physical characteristics of frozen hydrometeors inferred with parameter estimation. *Atmospheric Measurement Techniques Discussions*, 1-40. Submitted. DOI: https://doi.org/10.5194/amt-2021-50

Geer, A. J., Bauer, P., Lonitz, K., Barlakas, V., Eriksson, P., Mendrok, J., Doherty, A., Hocking, J. & Chambon, P. (2021). Hydrometeor optical properties for microwave ans sub-mm radiative transfer in RTTOV V13.0. *Geoscientific Model Development*. Submitted.

Ghosh, A., Varma, A.K., Shah, S., Gohil, B.S. & Pal, P.K. (2014). Rain identification and measurement using Oceansat-II scatterometer observations. *Remote Sensing of Environment* 142, 20–32. https://doi.org/10.1016/j.rse.2013.10.033.

Goddard, J. W. F., Tan, J., & Thurai, M. (1994). Technique for calibration of meteorological radars using differential phase. *Electronics Letters*, 30(2), 166-167. DOI: https://doi.org/10.1049/el:19940119

Gorgucci, E., Scarchilli, G., & Chandrasekar, V. (1992). Calibration of radars using polarimetric techniques. *IEEE transactions on geoscience and remote sensing*, 30(5), 853-858. DOI: https://doi.org/10.1109/36.175319

Gourley, J. J., Illingworth, A. J., & Tabary, P. (2009). Absolute calibration of radar reflectivity using redundancy of the polarization observations and implied constraints on drop shapes. *Journal of Atmospheric and Oceanic Technology*, 26(4), 689-703. DOI: https://doi.org/10.1175/2008JTECHA1152.1

Haddad, Z.S., Sy, O.O., Hristova-Veleva, S., Stephens, G.L., 2017. Derived Observations From Frequently Sampled Microwave Measurements of Precipitation—Part I: Relations to Atmospheric Thermodynamics. *IEEE Transactions on Geoscience and Remote Sensing* 55, 3441–3453. https://doi.org/10.1109/TGRS.2017.2671598

Haddad, Z. S., Smith, E. A., Kummerow, C. D., Iguchi, T., Farrar, M. R., Durden, S. L., ... & Olson, W. S. (1997). The TRMM ‘day-1’radar/radiometer combined rain-profiling algorithm. *Journal of the Meteorological Society of Japan. Ser. II*, 75(4), 799-809. DOI: https://doi.org/10.2151/jmsj1965.75.4_799

Hamada, A., Takayabu, Y.N. (2016). Improvements in Detection of Light Precipitation with the Global Precipitation Measurement Dual-Frequency Precipitation Radar (GPM DPR). *J. Atmos. Oceanic Technol.* 33, 653–667. https://doi.org/10.1175/JTECH-D-15-0097.1

Hilburn, K. A., & Wentz, F. J. (2008). Intercalibrated passive microwave rain products from the unified microwave ocean retrieval algorithm (UMORA). *Journal of Applied Meteorology and Climatology*, 47(3), 778-794. DOI: https://doi.org/10.1175/2007JAMC1635.1

Hogan, R. J., & Battaglia, A. (2008). Fast lidar and radar multiple-scattering models. Part II: Wide-angle scattering using the time-dependent two-stream approximation. *Journal of the Atmospheric Sciences*, 65(12), 3636-3651. DOI: https://doi.org/10.1175/2008JAS2643.1

27


---

Hou, A. Y., Kakar, R. K., Neeck, S., Azarbarzin, A. A., Kummerow, C. D., Kojima, M., ... & Iguchi, T. (2014). The global precipitation measurement mission. *Bulletin of the American Meteorological Society*, 95(5), 701-722. DOI: https://doi.org/10.1175/BAMS-D-13-00164.1

Houze Jr, R. A., McMurdie, L. A., Petersen, W. A., Schwaller, M. R., Baccus, W., Lundquist, J. D., ... & Chandrasekar, V. (2017). The olympic mountains experiment (OLYMPEX). *Bulletin of the American Meteorological Society*, 98(10), 2167-2188. DOI: https://doi.org/10.1175/BAMS-D-16-0182.1

Huuskonen, A., & Holleman, I. (2007). Determining weather radar antenna pointing using signals detected from the sun at low antenna elevations. *Journal of Atmospheric and Oceanic Technology*, 24(3), 476-483. DOI: https://doi.org/10.1175/JTECH1978.1

Hunzinger, A., Hardin, J. C., Bharadwaj, N., Varble, A., & Matthews, A. (2020). An extended radar relative calibration adjustment (eRCA) technique for higher-frequency radars and range–height indicator (RHI) scans. *Atmospheric Measurement Techniques*, 13(6), 3147-3166. DOI: https://doi.org/10.5194/amt-13-3147-2020

Ikuta, Y., Kusabiraki, H., Kawano, K., Anzai, T., Sawada, M., Ujiie, M., Nishimoto, S., Ota, Y., Narita, M. (2020). A new data assimilation system and upgrading of physical processes in JMA’s mesoscale NWP system. Working Group on Numerical Experimentation. Report No. 50. WCRP Report No.6/2020. WMO, Geneva. 01.07–01.08. http://bluebook.meteoinfo.ru/uploads/2020/docs/01_Ikuta_Yasutaka_MAMSM2003.pdf, Accessed on October 13, 2020.

Ikuta, Y., Okamoto, K., & Kubota, T. (2021). One-dimensional maximum-likelihood estimation for spaceborne precipitation radar data assimilation. *Quarterly Journal of the Royal Meteorological Society*, 147(735), 858-875. DOI: https://doi.org/10.1002/qj.3950

Illingworth, A.J., Battaglia, A., Bradford, J., Forsythe, M., Joe, P., Kollias, P., Lean, K., Lori, M., Mahfouf, J.-F., Melo, S., Midthassel, R., Munro, Y., Nicol, J., Potthast, R., Rennie, M., Stein, T.H.M., Tanelli, S., Tridon, F., Walden, C.J., Wolde, M. (2018). WIVERN: A New Satellite Concept to Provide Global In-Cloud Winds, Precipitation, and Cloud Properties. *Bull. Amer. Meteor. Soc.* 99, 1669–1687. https://doi.org/10.1175/BAMS-D-16-0047.1

Illingworth, A. J., Barker, H. W., Beljaars, A., Ceccaldi, M., Chepfer, H., Clerbaux, N., ... & Van Zadelhoff, G. J. (2015). The EarthCARE satellite: The next step forward in global measurements of clouds, aerosols, precipitation, and radiation. *Bulletin of the American Meteorological Society*, 96(8), 1311-1332. DOI : https://doi.org/10.1175/BAMS-D-12-00227.1

Janisková, M., & Fielding, M. D. (2020). Direct 4D-Var assimilation of space-borne cloud radar and lidar observations. Part II: Impact on analysis and subsequent forecast. *Quarterly Journal of the Royal Meteorological Society*, 146(733), 3900-3916. DOI: https://doi.org/10.1002/qj.3879

Khan, S., Maggioni, V., & Kirstetter, P. E. (2018). Investigating the potential of using satellite-based precipitation radars as reference for evaluating multisatellite merged products. *Journal of Geophysical Research: Atmospheres*, 123(16), 8646-8660. DOI: https://doi.org/10.1029/2018JD028584

28


---

Kida, S., Shige, S., Kubota, T., Aonashi, K., & Okamoto, K. I. (2009). Improvement of rain/no-rain classification methods for microwave radiometer observations over the ocean using a 37 GHz emission signature. *Journal of the Meteorological Society of Japan. Ser. II*, 87, 165-181. DOI: https://doi.org/10.2151/jmsj.87A.165

Kirstetter, P. E., Hong, Y., Gourley, J. J., Cao, Q., Schwaller, M., & Petersen, W. (2014). Research framework to bridge from the Global Precipitation Measurement Mission core satellite to the constellation sensors using ground-radar-based national mosaic QPE. *Remote Sensing of the Terrestrial Water Cycle, Geophys. Monogr*, 206, 61-79. DOI: https://doi.org/10.1002/9781118872086.ch4

Kollias, P., Puigdomènech Treserras, B., & Protat, A. (2019). Calibration of the 2007–2017 record of ARM Cloud Radar Observations using CloudSat. *Atmospheric Measurement Techniques Discussions*, 1-30. DOI: https://doi.org/10.5194/amt-2019-34

Kotsuki, S., Sato, Y., & Miyoshi, T. (2020). Data Assimilation for Climate Research: Model Parameter Estimation of Large₋Scale Condensation Scheme. *Journal of Geophysical Research: Atmospheres*, 125(1), e2019JD031304. DOI: https://doi.org/10.1029/2019JD031304

Kummerow, C., Berg, W., Thomas-Stahle, J., & Masunaga, H. (2006). Quantifying global uncertainties in a simple microwave rainfall algorithm. *Journal of Atmospheric and Oceanic Technology*, 23(1), 23-37. DOI: https://doi.org/10.1175/JTECH1827.1

Kummerow, C., Hong, Y., Olson, W. S., Yang, S., Adler, R. F., McCollum, J., ... & Wilheit, T. T. (2001). The evolution of the Goddard Profiling Algorithm (GPROF) for rainfall estimation from passive microwave sensors. *Journal of Applied Meteorology*, 40(11), 1801-1820. DOI: https://doi.org/10.1175/1520-0450(2001)040<1801:TEOTGP>2.0.CO;2040%3C1801:TEOTGP%3E2.0.CO;2)

Kozu, T., Iguchi, T., Kubota, T., Yoshida, N., Seto, S., Kwiatkowski, J., & Takayabu, Y. N. (2009). Feasibility of raindrop size distribution parameter estimation with TRMM precipitation radar. *Journal of the Meteorological Society of Japan. Ser. II*, 87, 53-66. DOI: https://doi.org/10.2151/jmsj.87A.53

Kubota, T., Shige, S., Hashizume, H., Aonashi, K., Takahashi, N., Seto, S., ... & Okamoto, K. I. (2007). Global precipitation map using satellite-borne microwave radiometers by the GSMaP project: Production and validation. *IEEE Transactions on Geoscience and Remote Sensing*, 45(7), 2259-2275. DOI: https://doi.org/10.1109/TGRS.2007.895337

Kubota, T., Shige, S., Aonashi, K., & Okamoto, K. I. (2009). Development of nonuniform beamfilling correction method in rainfall retrievals for passive microwave radiometers over ocean using TRMM observations. *Journal of the Meteorological Society of Japan. Ser. II*, 87, 153-164. DOI: https://doi.org/10.2151/jmsj.87A.153

Kubota, T., Ushio, T., Shige, S., Kida, S., Kachi, M., & Okamoto, K. I. (2009). Verification of high-resolution satellite-based rainfall estimates around Japan using a gauge-calibrated ground-radar dataset. *Journal of the Meteorological Society of Japan. Ser. II*, 87, 203-222. DOI: https://doi.org/10.2151/jmsj.87A.203

29


---

Kubota, T., Aonashi, K., Ushio, T., Shige, S., Takayabu, Y. N., Kachi, M., ... & Oki, R. (2020). Global Satellite Mapping of Precipitation (GSMaP) products in the GPM era. In *Satellite precipitation measurement* (pp. 355-373). Springer, Cham. DOI : https://doi.org/10.1007/978-3-030-24568-9_20

Kwon, E. H., Sohn, B. J., Chang, D. E., Ahn, M. H., & Yang, S. (2008). Use of numerical forecasts for improving TMI rain retrievals over the mountainous area in Korea. *Journal of applied meteorology and climatology*, *47*(7), 1995-2007. DOI: https://doi.org/10.1175/2007JAMC1857.1

Lai, A., Gao, J., Koch, S. E., Wang, Y., Pan, S., Fierro, A. O., ... & Min, J. (2019). Assimilation of radar radial velocity, reflectivity, and Pseudo–Water Vapor for convective-scale NWP in a variational framework. *Monthly Weather Review*, *147*(8), 2877-2900. DOI: https://doi.org/10.1175/MWR-D-18-0403.1

Lamer, K., Kollias, P., Battaglia, A., & Preval, S. (2020). Mind the gap–Part 1: Accurately locating warm marine boundary layer clouds and precipitation using spaceborne radars. *Atmospheric Measurement Techniques*, *13*(5), 2363-2379. DOI : https://doi.org/10.5194/amt-13-2363-2020

Lebsock, M. D., Suzuki, K., Millán, L. F., & Kalmus, P. M. (2015). The feasibility of water vapor sounding of the cloudy boundary layer using a differential absorption radar technique. *Atmospheric Measurement Techniques*, *8*(9), 3631-3645. DOI: https://doi.org/10.5194/amt-8-3631-2015

Levizzani, V., C. Kidd, D.B. Kirschbaum, C.D. Kummerow, K. Nakamura, F.J. Turk (2020a). *Satellite Precipitation Measurement: Volume 1*. Springer Academic Publishers, V. Levizzani (Ed). Advances in Global Change Research 67, ISBN 978-3-030-24568-9, 450 pp.

Levizzani, V., C. Kidd, D.B. Kircshbaum, C.D. Kummerow, K. Nakamura, F.J. Turk (2020b). *Satellite Precipitation Measurement: Volume 2*. Springer Academic Publishers, V. Levizzani (Ed). Advances in Global Change Research 69, ISBN 978-3-030-35798-6, 725 pp.

Li, Y., Wang, X., & Xue, M. (2012). Assimilation of radar radial velocity data with the WRF hybrid ensemble–3DVAR system for the prediction of Hurricane Ike (2008). *Monthly Weather Review*, *140*(11), 3507-3524. DOI: https://doi.org/10.1175/MWR-D-12-00043.1

Louf, V., Protat, A., Warren, R. A., Collis, S. M., Wolff, D. B., Raunyiar, S., ... & Petersen, W. A. (2019). An integrated approach to weather radar calibration and monitoring using ground clutter and satellite comparisons. *Journal of Atmospheric and Oceanic Technology*, *36*(1), 17-39. DOI: https://doi.org/10.1175/JTECH-D-18-0007.1

Maggioni, V., Meyers, P. C., & Robinson, M. D. (2016). A review of merged high-resolution satellite precipitation product accuracy during the Tropical Rainfall Measuring Mission (TRMM) era. *Journal of Hydrometeorology*, *17*(4), 1101-1117. DOI: https://doi.org/10.1175/JHM-D-15-0190.1

Marks, D. A., Wolff, D. B., Carey, L. D., & Tokay, A. (2011). Quality control and calibration of the dual-polarization radar at Kwajalein, RMI. *Journal of Atmospheric and Oceanic Technology*, *28*(2), 181-196. DOI: https://doi.org/10.1175/2010JTECHA1462.1

30


---

Marks, D. A., Wolff, D. B., Silberstein, D. S., Tokay, A., Pippitt, J. L., & Wang, J. (2009). Availability of high-quality TRMM ground validation data from Kwajalein, RMI: A practical application of the relative calibration adjustment technique. *Journal of Atmospheric and Oceanic Technology*, 26(3), 413-429. DOI: https://doi.org/10.1175/2008JTECHA1174.1

Marzano, F. S., Mugnai, A., Panegrossi, G., Pierdicca, N., Smith, E. A., & Turk, J. (1999). Bayesian estimation of precipitating cloud parameters from combined measurements of spaceborne microwave radiometer and radar. *IEEE Transactions on Geoscience and Remote Sensing*, 37(1), 596-613. DOI: https://doi.org/10.1109/36.739124

Norin, L., Devasthale, A., L'Ecuyer, T. S., Wood, N. B., & Smalley, M. (2015). Intercomparison of snowfall estimates derived from the CloudSat Cloud Profiling Radar and the ground-based weather radar network over Sweden. *Atmospheric Measurement Techniques*, 8(12), 5009-5021. DOI: https://doi.org/10.5194/amt-8-5009-2015

Okamoto, K., Aonashi, K., Kubota, T., & Tashima, T. (2016). Experimental assimilation of the GPM Core Observatory DPR reflectivity profiles for Typhoon Halong (2014). *Monthly Weather Review*, 144(6), 2307-2326. DOI: https://doi.org/10.1175/MWR-D-15-0399.1

Pan, S., Gao, J., Stensrud, D. J., Wang, X., & Jones, T. A. (2018). Assimilation of radar radial velocity and reflectivity, satellite cloud water path, and total precipitable water for convective-scale NWP in OSSEs. *Journal of Atmospheric and Oceanic Technology*, 35(1), 67-89. DOI: https://doi.org/10.1175/JTECH-D-17-0081.1

Park, S., Jung, S. H., & Lee, G. (2015). Cross validation of TRMM PR reflectivity profiles using 3D reflectivity composite from the ground-based radar network over the Korean Peninsula. *Journal of Hydrometeorology*, 16(2), 668-687. DOI: https://doi.org/10.1175/JHM-D-14-0092.1

Petty, G. W. (2001). Physical and microwave radiative properties of precipitating clouds. Part I: Principal component analysis of observed multichannel microwave radiances in tropical stratiform rainfall. *Journal of Applied Meteorology*, 40(12), 2105-2114. DOI: https://doi.org/10.1175/1520-0450(2001)040<2105:PAMRPO>2.0.CO;2040<2105:PAMRPO>2.0.CO;2)

Protat, A., Bouniol, D., O’Connor, E. J., Klein Baltink, H., Verlinde, J., & Widener, K. (2011). CloudSat as a global radar calibrator. *Journal of atmospheric and oceanic technology*, 28(3), 445-452. DOI: https://doi.org/10.1175/2010JTECHA1443.1

Protat, A., Bouniol, D., Delanoë, J., O’Connor, E., May, P. T., Plana-Fattori, A., ... & Heymsfield, A. J. (2009). Assessment of CloudSat reflectivity measurements and ice cloud properties using ground-based and airborne cloud radar observations. *Journal of Atmospheric and Oceanic Technology*, 26(9), 1717-1741. DOI: https://doi.org/10.1175/2009JTECHA1246.1

Rinehart, R. E. (1978). On the use of ground return targets for radar reflectivity factor calibration checks. *Journal of Applied Meteorology and Climatology*, 17(9), 1342-1350. DOI: https://doi.org/10.1175/1520-0450(1978)017<1342:OTUOGR>2.0.CO;2017<1342:OTUOGR>2.0.CO;2)

31


---

Rysman, J. F., Panegrossi, G., Sanò, P., Marra, A. C., Dietrich, S., Milani, L., & Kulie, M. S. (2018). SLALOM: An all-surface snow water path retrieval algorithm for the GPM Microwave Imager. *Remote Sensing*, *10*(8), 1278. DOI: https://doi.org/10.3390/rs10081278

Rysman, J. F., Panegrossi, G., Sanò, P., Marra, A. C., Dietrich, S., Milani, L., ... & Edel, L. (2019). Retrieving surface snowfall with the GPM Microwave Imager: a new module for the SLALOM algorithm. *Geophysical Research Letters*, *46*(22), 13593-13601. DOI : https://doi.org/10.1029/2019GL084576

Schneider, T., Lan, S., Stuart, A., & Teixeira, J. (2017). Earth system modeling 2.0: A blueprint for models that learn from observations and targeted high-resolution simulations. *Geophysical Research Letters*, *44*(24), 12-396. DOI: https://doi.org/10.1002/2017GL076101

Schwaller, M. R., & Morris, K. R. (2011). A ground validation network for the Global Precipitation Measurement mission. *Journal of Atmospheric and Oceanic Technology*, *28*(3), 301-319. DOI: https://doi.org/10.1175/2010JTECHA1403.1

Shige, S., Kida, S., Ashiwake, H., Kubota, T., & Aonashi, K. (2013). Improvement of TMI rain retrievals in mountainous areas. *Journal of Applied Meteorology and Climatology*, *52*(1), 242-254. DOI: https://doi.org/10.1175/JAMC-D-12-074.1

Shige, S., Yamamoto, M. K., & Taniguchi, A. (2014). Improvement of TMI rain retrieval over the Indian subcontinent. *Remote Sensing of the Terrestrial Water Cycle, Geophys. Monogr*, *206*, 27-42. DOI: https://doi.org/10.1002/9781118872086.CH2.

Shige, S., & Kummerow, C. D. (2016). Precipitation-top heights of heavy orographic rainfall in the Asian monsoon region. *Journal of the Atmospheric Sciences*, *73*(8), 3009-3024. DOI: https://doi.org/10.1175/JAS-D-15-0271.1

Silberstein, D. S., Wolff, D. B., Marks, D. A., Atlas, D., & Pippitt, J. L. (2008). Ground clutter as a monitor of radar stability at Kwajalein, RMI. *Journal of Atmospheric and Oceanic Technology*, *25*(11), 2037-2045. DOI: https://doi.org/10.1175/2008JTECHA1063.1

Simpson, J., Kummerow, C., Tao, W. K., & Adler, R. F. (1996). On the tropical rainfall measuring mission (TRMM). *Meteorology and Atmospheric physics*, *60*(1), 19-36. DOI: https://doi.org/10.1007/BF01029783

Skofronick-Jackson, G., Petersen, W. A., Berg, W., Kidd, C., Stocker, E. F., Kirschbaum, D. B., ... & Wilheit, T. (2017). The Global Precipitation Measurement (GPM) mission for science and society. *Bulletin of the American Meteorological Society*, *98*(8), 1679-1695. DOI: https://doi.org/10.1175/BAMS-D-15-00306.1

Smalley, M., L'Ecuyer, T., Lebsock, M., & Haynes, J. (2014). A comparison of precipitation occurrence from the NCEP Stage IV QPE product and the CloudSat Cloud Profiling Radar. *Journal of Hydrometeorology*, *15*(1), 444-458. DOI: https://doi.org/10.1175/JHM-D-13-048.1

Smalley, M., Kirstetter, P. E., & L’Ecuyer, T. (2017). How frequent is precipitation over the contiguous United States? Perspectives from ground-based and spaceborne radars. *Journal of Hydrometeorology*, *18*(6), 1657-1672. DOI: https://doi.org/10.1175/JHM-D-16-0242.1

32


---

Stephens, G., Winker, D., Pelon, J., Trepte, C., Vane, D., Yuhas, C., L’Ecuyer, T., Lebsock, M. (2018). CloudSat and CALIPSO within the A-Train: Ten Years of Actively Observing the Earth System. *Bulletin of the American Meteorological Society*, 99, 569–581. https://doi.org/10.1175/BAMS-D-16-0324.1

Sy, O.O., Tanelli, S., Durden, S.L., Peral, E., Sacco, G.-F., Chahat, N.E., Hristova-Veleva, S., Heymsfield, A.J., Bansemer, A., Knosp, B., Dobrowalski, G., Li, P.P., Vu, Q. (2021). Scientific Products From the First Radar in a CubeSat (RainCube): Deconvolution, Cross-Validation, and Retrievals. *IEEE Transactions on Geoscience and Remote Sensing* 1–20. https://doi.org/10.1109/TGRS.2021.3073990

Takahashi, N., Kuroiwa, H., & Kawanishi, T. (2003). Four-year result of external calibration for Precipitation Radar (PR) of the Tropical Rainfall Measuring Mission (TRMM) satellite. *IEEE transactions on geoscience and remote sensing*, *41*(10), 2398-2403. DOI: https://doi.org/10.1109/TGRS.2003.817180

Takayabu, Y. N. (2008). Observing rainfall regimes using TRMM PR and LIS data. *GEWEX News*, *18*(2), 9-10.

Tanelli, S., Durden, S. L., Im, E., Pak, K. S., Reinke, D. G., Partain, P., ... & Marchand, R. T. (2008). CloudSat's cloud profiling radar after two years in orbit: Performance, calibration, and processing. *IEEE Transactions on Geoscience and Remote Sensing*, *46*(11), 3560-3573. DOI: https://doi.org/10.1109/TGRS.2008.2002030

Taniguchi, A., Shige, S., Yamamoto, M. K., Mega, T., Kida, S., Kubota, T., ... & Aonashi, K. (2013). Improvement of high-resolution satellite rainfall product for Typhoon Morakot (2009) over Taiwan. *Journal of Hydrometeorology*, *14*(6), 1859-1871. DOI: https://doi.org/10.1175/JHM-D-13-047.1

Turk, F.J., Ringerud, S.E., Camplani, A., Casella, D., Chase, R.J., Ebtehaj, A., Gong, J., Kulie, M., Liu, G., Milani, L., Panegrossi, G., Padullés, R., Rysman, J.-F., Sanò, P., Vahedizade, S., Wood, N.B. (2021). Applications of a CloudSat-TRMM and CloudSat-GPM Satellite Coincidence Dataset. *Remote Sensing*, 13, 2264. https://doi.org/10.3390/rs13122264

Turk, F.J., Sikhakolli, R., Kirstetter, P. & Durden, S.L. (2015). Exploiting Over-Land OceanSat-2 Scatterometer Observations to Capture Short-Period Time-Integrated Precipitation. *Journal of Hydrometeorology*, 16, 2519–2535. https://doi.org/10.1175/JHM-D-15-0046.1

Wang, Y., & Wang, X. (2017). Direct assimilation of radar reflectivity without tangent linear and adjoint of the nonlinear observation operator in the GSI-based EnVar system: Methodology and experiment with the 8 May 2003 Oklahoma City tornadic supercell. *Monthly Weather Review*, *145*(4), 1447-1471. DOI: https://doi.org/10.1175/MWR-D-16-0231.1

Warren, R. A., Protat, A., Siems, S. T., Ramsay, H. A., Louf, V., Manton, M. J., & Kane, T. A. (2018). Calibrating ground-based radars against TRMM and GPM. *Journal of Atmospheric and Oceanic Technology*, *35*(2), 323-346. DOI: https://doi.org/10.1175/JTECH-D-17-0128.1

Wattrelot, E., Caumont, O., & Mahfouf, J. F. (2014). Operational implementation of the 1D+ 3D-Var assimilation method of radar reflectivity data in the AROME model. *Monthly Weather Review*, *142*(5), 1852-1873. DOI: https://doi.org/10.1175/MWR-D-13-00230.1

33


---

Webb, M., Senior, C., Bony, S., & Morcrette, J. J. (2001). Combining ERBE and ISCCP data to assess clouds in the Hadley Centre, ECMWF and LMD atmospheric climate models. *Climate Dynamics*, 17(12), 905-922. DOI: https://doi.org/10.1007/s003820100157

Wentz, F.J., Ricciardulli, L., Rodriguez, E., Stiles, B.W., Bourassa, M.A., Long, D.G., Hoffman, R.N., Stoffelen, A., Verhoef, A., O’Neill, L.W., Farrar, J.T., Vandemark, D., Fore, A.G., Hristova-Veleva, S.M., Turk, F.J., Gaston, R., Tyler, D. (2017). Evaluating and Extending the Ocean Wind Climate Data Record. *IEEE J. Selected Topics Applied Earth Observations & Remote Sensing*, 10, 2165–2185. https://doi.org/10.1109/JSTARS.2016.2643641

Wilheit, T. T., Chang, A. T., & Chiu, L. S. (1991). Retrieval of monthly rainfall indices from microwave radiometric measurements using probability distribution functions. *Journal of Atmospheric and Oceanic Technology*, 8(1), 118-136. DOI: https://doi.org/10.1175/1520-0426(1991)008<0118:ROMRIF>2.0.CO;2008<0118:ROMRIF>2.0.CO;2)

You, Y., Petkovic, V., Tan, J., Kroodsma, R., Berg, W., Kidd, C., & Peters-Lidard, C. (2020). Evaluation of V05 precipitation estimates from GPM constellation radiometers using KuPR as the reference. *Journal of Hydrometeorology*, 21(4), 705-728. DOI: https://doi.org/10.1175/JHM-D-19-0144.1

34


---

# 7. Acronyms list

**ARM** : ATMOSPHERIC RADIATION MEASUREMENT

**CASM** : COMMUNITY ACTIVE SENSOR MODULE

**CGMS** : COORDINATION GROUP FOR METEOROLOGICAL SATELLITES

**CORRA** : COMBINED RADAR-RADIOMETER ALGORITHM

**CPR** : CLOUDSAT PRECIPITATION RADAR

**CRTM** : COMMUNITY RADIATIVE TRANSFER MODEL

**DA** : DATA ASSIMILATION

**DPR** : DUAL FREQUENCY PRECIPITATION RADAR

**EARTHCARE**: EARTH CLOUDS, AEROSOL AND RADIATION EXPLORER

**ECMWF** : EUROPEAN CENTRE FOR MEDIUM-RANGE WEATHER FORECASTS

**GMI** : GPM MICROWAVE IMAGER

**GPM** : GLOBAL PRECIPITATION MEASUREMENT MISSION

**GPROF** : GODDARD PROFILING ALGORITHM

**GSI** : GRIDPOINT STATISTICAL INTERPOLATION

**GSICS**: GLOBAL SPACE-BASED INTER-CALIBRATION SYSTEM

**GSMAP** : GLOBAL SATELLITE MAPPING OF PRECIPITATION

**IMERG** : INTEGRATED MULTI-SATELLITE RETRIEVALS FOR GPM

**IPWG** : INTERNATIONAL PRECIPITATION WORKING GROUP

**JAXA** : JAPAN AEROSPACE EXPLORATION AGENCY

**JCSDA** : JOINT CENTER FOR SATELLITE DATA ASSIMILATION

**JEDI** : JOINT EFFORT FOR DATA ASSIMILATION INTEGRATION

**JMA** : JAPAN METEOROLOGICAL AGENCY

**MLE** : MAXIMUM LIKELIHOOD ESTIMATION

**NASA** : NATIONAL AERONAUTICS AND SPACE ADMINISTRATION

**NWP** : NUMERICAL WEATHER PREDICTION

**PMW** : PASSIVE MICROWAVE

**RCA** : RELATIVE CALIBRATION ADJUSTMENT

**RH** : RELATIVE HUMIDITY

**RTTOV** : RADIATIVE TRANSFER FOR TOVS

**SSMIS** : SPECIAL SENSOR MICROWAVE IMAGER / SOUNDER

**TMI** : TRMM MICROWAVE IMAGER

**TOVS** : TELEVISION INFRARED OBSERVATION SATELLITE (TIROS) OPERATIONAL VERTICAL SOUNDER

**TRMM** : TROPICAL RAINFALL MEASURING MISSION

**VMM** : VOLUME MATCHING METHOD

35
