

Remote Sensing in Earth Systems Sciences (2019) 2:18–38
https://doi.org/10.1007/s41976-019-0008-6

ORIGINAL PAPER

CrossMark logo

# Earth Observations and Integrative Models in Support of Food and Water Security

Stephanie Schollaert Uz<sup>1</sup> • Alex C. Ruane<sup>2</sup> • Bryan N. Duncan<sup>1</sup> • Compton J. Tucker<sup>1</sup> • George J. Huffman<sup>1</sup> • Iliana E. Mladenova<sup>1,3</sup> • Batuhan Osmanoglu<sup>1</sup> • Thomas R. H. Holmes<sup>1</sup> • Amy McNally<sup>1,3</sup> • Christa Peters-Lidard<sup>1</sup> • John D. Bolten<sup>1</sup> • Narendra Das<sup>4</sup> • Matthew Rodell<sup>1</sup> • Sean McCartney<sup>1,5</sup> • Martha C. Anderson<sup>6</sup> • Brad Doorn<sup>7</sup>

Received: 19 October 2018 / Revised: 26 December 2018 / Accepted: 17 January 2019 / Published online: 11 February 2019
© The Author(s) 2019

## Abstract

Global food production depends upon many factors that Earth observing satellites routinely measure about water, energy, weather, and ecosystems. Increasingly sophisticated, publicly available satellite data products can improve efficiencies in resource management and provide earlier indication of environmental disruption. Satellite remote sensing provides a consistent, long-term record that can be used effectively to detect large-scale features over time, such as a developing drought. Accuracy and capabilities have increased along with the range of Earth observations and derived products that can support food security decisions with actionable information. This paper highlights major capabilities facilitated by satellite observations and physical models that have been developed and validated using remotely sensed observations. Although we primarily focus on variables relevant to agriculture, we also include a brief description of the growing use of Earth observations in support of aquaculture and fisheries.

**Keywords** Earth observations . Food security . Water resources . Air quality . Societal and economic benefits

## 1 Introduction

For decades, the United States (US) National Aeronautics and Space Administration (NASA) has worked in partnership with agencies such as the US Department of Agriculture (USDA), the US Agency for International Development (USAID), and the National Oceanographic and Atmospheric Administration (NOAA), as well as international organizations and private industry to support and advance the use of remotely sensed data for more informed decision-making and societal benefit. A changing profile of extreme weather hazards and societal exposure increasingly require the large-scale view afforded by a fleet of satellites observing Earth as a system, particularly when set against a backdrop of challenges that include a growing world population, rapid socioeconomic development, and the need to sustainably manage finite natural resources. For example, the United Nations estimates that the world’s population will increase by 2.2 billion by 2050, with most of that growth occurring in tropical and subtropical areas, especially Africa.

Despite substantial progress over the last few decades, world hunger has been rising since 2014, and the combined threats of conflict, population growth, limited arable land, and climate variability and change will exacerbate this situation [43]. For example, seafood is an important source of protein for a significant number of people. Wild catches cannot match increasing demand and, in fact, their sustainability is in question. Therefore, aquaculture is an ever more important complement to agriculture to feed the human population. At the same time, however, the increased use of fertilizer for

\* Stephanie Schollaert Uz
stephanie.uz@nasa.gov

<sup>1</sup> NASA Goddard Space Flight Center, Greenbelt, MD, USA

<sup>2</sup> NASA Goddard Institute for Space Studies, Climate Impacts Group, New York, NY, USA

<sup>3</sup> Earth System Science Interdisciplinary Center, University of Maryland, College Park, MD, USA

<sup>4</sup> NASA Jet Propulsion Laboratory, Pasadena, CA, USA

<sup>5</sup> Science Systems and Applications, Inc., Lanham, MD, USA

<sup>6</sup> USDA-ARS Hydrology and Remote Sensing Laboratory, Beltsville, MD, USA

<sup>7</sup> NASA Headquarters, Washington, DC, USA

Springer logo


---



Remote Sens Earth Syst Sci (2019) 2:18–38

19

agriculture has led to increased runoff of nitrogen and phosphorus causing the eutrophication of water bodies, threatening aquatic ecosystems. Aside from production, lack of access to nutritious food choices or clean water and sanitation can exacerbate food insecurity and lead to malnutrition. Clearly, monitoring food production and distribution systems, in addition to water quantity and quality in support of food security, requires a global perspective.

Earth observing satellites provide the unique ability to simultaneously monitor these and other interrelated systems. Advances in our ability to measure multiple variables, combined with integrative models that help us understand the connections between these systems, provide a unique opportunity to support food security assessments. For example, ongoing international efforts on crop monitoring by the Group on Earth Observations Global Agricultural Monitoring (GEOGLAM) and others integrate remote sensing data into global and regional crop production projections, as detailed elsewhere (i.e., [22, 76]). Toward the objective of highlighting satellite data products that may be applied in support of smarter agriculture or aquaculture, we review the current status of several remotely sensed observables: variables related to vegetation, land degradation, water quantity, water quality, and air quality, as well as data assimilation and modeling efforts that combine observations with hydrodynamic, geophysical, and sometimes socioeconomic models to yield a more complete picture. This review is intended to inform the larger science community, resource managers, and policymakers from those unfamiliar with satellite data to those already using some but perhaps not the full suite of the observables presented here.

# 2 Observable: Primary Production

Estimates of gross primary production (GPP) provide valuable information on the spatial distribution and temporal variability of primary production, which in an agricultural setting, determines crop yields and fodder production for animals. Agricultural food security requires measured or modeled agricultural GPP to determine important crop and fodder production for areas of interest. Observations and models are both used to support food security solutions.

The normalized difference vegetation index (NDVI) is the ratio of the difference in surface reflectances measured in the red and near-infrared spectral bands and their sum [122]. NDVI distinguishes vegetated areas from other surface types (Figs. 1 and 2), but is not necessarily linked to GPP.

There are several techniques that use satellite observations to determine primary production, and here we describe just a few. For example, one technique involves extrapolating net carbon exchange from eddy-covariance flux tower observations using satellite measured absorbed photosynthetically active radiation at the 1 km scale [23, 62]; a second technique

<table>
  <thead>
    <tr>
        <th colspan="4">Saskatchewan (45% of wheat production)</th>
    </tr>
<tr>
        <th>Month</th>
        <th>Mean</th>
        <th>2017</th>
        <th>2018</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>May</td>
<td>0.25</td>
<td>0.25</td>
<td>0.25</td>
    </tr>
<tr>
        <td>Jun</td>
<td>0.45</td>
<td>0.40</td>
<td>0.42</td>
    </tr>
<tr>
        <td>Jul</td>
<td>0.68</td>
<td>0.62</td>
<td>0.65</td>
    </tr>
<tr>
        <td>Aug</td>
<td>0.55</td>
<td>0.50</td>
<td>0.52</td>
    </tr>
<tr>
        <td>Sep</td>
<td>0.35</td>
<td>0.32</td>
<td>0.33</td>
    </tr>
<tr>
        <td>Oct</td>
<td>0.28</td>
<td>0.28</td>
<td>0.28</td>
    </tr>
<tr>
        <th colspan="4">Alberta (31% of wheat production)</th>
    </tr>
<tr>
        <th>Month</th>
        <th>Mean</th>
        <th>2017</th>
        <th>2018</th>
    </tr>
<tr>
        <td>May</td>
<td>0.25</td>
<td>0.25</td>
<td>0.25</td>
    </tr>
<tr>
        <td>Jun</td>
<td>0.42</td>
<td>0.38</td>
<td>0.40</td>
    </tr>
<tr>
        <td>Jul</td>
<td>0.65</td>
<td>0.60</td>
<td>0.62</td>
    </tr>
<tr>
        <td>Aug</td>
<td>0.52</td>
<td>0.48</td>
<td>0.50</td>
    </tr>
<tr>
        <td>Sep</td>
<td>0.38</td>
<td>0.35</td>
<td>0.36</td>
    </tr>
<tr>
        <td>Oct</td>
<td>0.30</td>
<td>0.30</td>
<td>0.30</td>
    </tr>
<tr>
        <th colspan="4">Manitoba (13% of wheat production)</th>
    </tr>
<tr>
        <th>Month</th>
        <th>Mean</th>
        <th>2017</th>
        <th>2018</th>
    </tr>
<tr>
        <td>May</td>
<td>0.22</td>
<td>0.22</td>
<td>0.22</td>
    </tr>
<tr>
        <td>Jun</td>
<td>0.40</td>
<td>0.35</td>
<td>0.38</td>
    </tr>
<tr>
        <td>Jul</td>
<td>0.62</td>
<td>0.58</td>
<td>0.60</td>
    </tr>
<tr>
        <td>Aug</td>
<td>0.50</td>
<td>0.45</td>
<td>0.48</td>
    </tr>
<tr>
        <td>Sep</td>
<td>0.32</td>
<td>0.30</td>
<td>0.31</td>
    </tr>
<tr>
        <td>Oct</td>
<td>0.25</td>
<td>0.25</td>
<td>0.25</td>
    </tr>
  </tbody>
</table>

Fig. 1 This NDVI time series produced on August 30, 2018 compares 2017 and 2018 wheat growing in three Canadian provinces [127]. The historical record of MODIS data since 2000 enables quantitative agricultural food and fodder production estimates using minimum value, maximum value, and the historical mean value by time period, calculated in very close to real time

uses MODIS satellite observations in conjunction with a light-use efficiency model to produce GPP estimates at the 1 km scale [140]; a third technique uses satellite observations directly to determine both GPP and agricultural production at the native 250 m resolution of MODIS using spectral vegetation indices through the growing season [127] (Fig. 1); and a fourth technique uses chlorophyll fluorescence from the GOME-2 satellite to estimate agricultural production in combination with optical, thermal, and microwave satellite data [53].

An advantage of these four approaches is that the satellite observations also provide realistic surface conditions of vegetation photosynthetic capacity, phenology, disturbances, recovery, and human management. A limitation of the chlorophyll fluorescence approach is the spatial resolution of these data is < 1 km, while MODIS is now producing 250 m spectral vegetation indices data, and sustained land imaging is now producing 30 m spectral vegetation indices data [68].

Springer logo


---



20

Remote Sens Earth Syst Sci (2019) 2:18–38

Fig. 2 Landsat 8 scenes showing field-scale RBG and changes in NDVI over the 2017 growing season, advancing global food security to the field level. Source: Landsat-8 Project Office, NASA Goddard Space Flight Center

Landsat 8 scenes showing field-scale RGB and NDVI changes over the 2017 growing season

Agricultural production estimates must be restricted to crop-specific areas to avoid confusion from other crops, natural vegetation, and areas of no vegetation. This translates into being able to follow specific crops through time with continued observations (Fig. 2). This capability is available from space, now at greater accuracy and lower latency, with sustained land imaging and multi-spectral 30 m data from Landsat-8, Sentinel-2a and Sentinel-2b. The Harmonized Landsat and Sentinel-2 (HLS) project is now producing 30 m time series multi-spectral observations with an equatorial revisit frequency of 3.7 days at the equator [68]. Landsat-9 is planned for launch at the end of 2020 to join the sustained land imaging instrument suite, at which point the equatorial revisit frequency will drop to 3 days. It is highly likely that a combination of chlorophyll fluorescence and 250 and 30 m multi-spectral satellite data will be developed in the near future to predict global agricultural crop and fodder production.

# 3 Observable: Land Degradation

Land degradation has been highlighted as a key development challenge by numerous international bodies, including the United Nations Convention to Combat Desertification, the Convention on Biological Diversity, the United Nations Framework Convention on Climate Change, and the Sustainable Development Goals. These conventions seek to avoid, reduce, and reverse land degradation, especially desertification and deforestation, by supporting better practices. Sustainable land management seeks to maintain vegetative cover, build soil organic matter, make efficient use of inputs, such as water, nutrients, and pesticides, and minimize off-site impacts [25].

Three indicators have been identified as metrics for quantifying land degradation that are also geophysical variables measured by Earth-orbiting satellites: land cover, carbon stocks, and land productivity or gross primary production. A review of these three land degradation indicators led Tucker and Pinzon [123] to focus on land productivity or gross primary production during a pilot study in four countries: Senegal, Uganda, Kenya, and Tanzania. NDVI from several

satellite data sources at spatial scales ranging from 30 m to 8 km was evaluated and found to be well-suited for identifying degrading areas.

Time integrals of spectral vegetation indices were compared to time integrals of GOME-2 chlorophyll fluorescence from Joiner et al. [60] and found to be linearly and very highly correlated for 22 test areas. This confirmed the validity of using NDVI as a direct measurement of gross primary productivity. Growing season integrals of NDVI were regressed against growing season integrals of soil moisture over the AVHRR, SeaWiFS, and MODIS records for Kenya, Senegal, Tanzania, and Uganda. Consistent negative residuals were identified as areas of land degradation following the method of Ibrahim et al. [57]. Aggregations of pixels with negative residuals were studied with Landsat 30 m and 50 cm commercial satellite data for all four countries, to confirm or refute the occurrence of land degradation and to identify its cause [123].

# 4 Observable: Precipitation

The rain and snow that fall on the Earth’s surface provide the water upon which agriculture depends, whether directly or in replenishing stores as snowpack, lakes, reservoirs, and ground water that are later used. The occurrence of precipitation is governed at large scales by atmospheric constraints on moisture convergence and vertical motions, but how it actually gets released at the small scales displays a great deal of variability right down to the microphysical processes that govern conversions among vapor, liquid, and ice phases. Because precipitation events are so strongly driven by these small-scale processes, and the fact that much of the time there is no precipitation, the resulting statistics are far from Gaussian, highly skewed, and multi-scaled, rendering the analysis of precipitation challenging (Fig. 3).

A relatively long history of precipitation data is available from surface gauges, which provide point measurements as a function of time. Because they provide actual measurements of precipitation, gauges are considered the standard, even with significant limitations. This includes the lack of correlation

Springer logo

Springer


---



Remote Sens Earth Syst Sci (2019) 2:18–38

21

Global long-term average precipitation patterns map

Fig. 3 Global long-term average precipitation patterns. Source: Global Precipitation Climatology Project

with surrounding areas on short time scales, which makes point-to-area analyses challenging. The typical under-reporting of amounts is due to both wind effects reducing the effectiveness to capture precipitation and the inability of some gauge technologies to correctly record snowfall. The problem of representativeness is exacerbated by a lack of sufficiently dense gauge networks over most of the globe.

A second approach to developing precipitation records is to use surface-based radar measurements from which the precipitation amount must be estimated. These estimates can be locally useful in the U.S. and western Europe, but systematic coverage elsewhere is lacking.

The third approach to obtaining global precipitation information is to use satellite sensors. Over the past couple of decades, this has become the dominant approach for many applications due to the quasi-global coverage by satellites, an acceptably fine time/space scale of results, and relatively short latencies. One important advantage for satellites is that they typically provide precipitation estimates over both land and ocean, versus the land siting for most gauges and land/coastal coverage for radars. At present, passive microwave sensors flying on a virtual (because uncoordinated) constellation of low-Earth orbit satellites provide observations every 3 h or less about 90% of the time, with footprint sizes on the order of 10–20 km. The resulting data are processed into precipitation estimates for the individual sensors and then combined into multi-satellite products that are typically useful for agricultural applications. Estimates of precipitation that use infrared sensor data from geosynchronous orbit satellites are

considered less accurate than microwave-based data. However, they are typically available for the entire latitude belt 60° N-S every half hour, so they can be used in combination with the microwave or as stand-alone products. Some products are created within about 4 h after observation time, but longer latencies of 12–24 h in other products are usually satisfactory and allow more complete estimates to be assembled.

Many satellite-based algorithms have been developed over the years and a number are routinely used to create publicly available datasets. The International Precipitation Working Group (IPWG) maintains a listing of freely available, quasi-global, long-term datasets at [http://www.isac.cnr.it/~ipwg/data/datasets.html](http://www.isac.cnr.it/~ipwg/data/datasets.html). For most users, the multi-satellite datasets with and without explicit use of surface gauge data are the most relevant. It is somewhat challenging for new users to determine the fitness of use for the various datasets for their particular application; see "How Do I Choose a Data Set?" for pointers. In general, data will be more accurate when time/space-averaged; are most representative of typical behavior, as opposed to extremes; and show reduced skill in mountainous regions and cold seasons.

Taking the NASA Global Precipitation Measurement (GPM) project’s Integrated Multi-satellitE Retrievals for GPM (IMERG) datasets as examples, there are three latencies available: 4 h, 12 h, and 3.5 months (Early, Late, and Final, respectively), each on a 0.1° × 0.1° latitude/longitude grid every half hour. Longer latencies use more data and should therefore be more accurate. The page https://pmm.nasa.gov/

Springer logo


---



22 Remote Sens Earth Syst Sci (2019) 2:18–38

data-access/downloads/gpm provides several format options and hot links to documentation. Currently, Version 05 covers the period March 2014 to the present, but Version 06 (planned for early 2019) will extend back to June 2000. All three IMERG products are provided for the entire period of record so that products such as crop yield models can be assured of a relatively homogeneous data record for developing calibrations.

# 5 Observable: Terrestrial Water Storage

Food cannot be grown on land without freshwater, so monitoring and understanding how freshwater storage is distributed across the land and how it changes over time is essential to assessing food security. A portion of the water that precipitates onto the land surface is stored as surface water, snow, ice, soil moisture, or groundwater. The sum of these is known as terrestrial water storage (TWS). The importance of TWS is obvious, but it is difficult to monitor at regional to global scales using ground-based networks because installation of automated observing systems for all of the components is expensive and labor intensive, and because most countries do not share the data that they do collect [42].

The NASA/German Gravity Recovery and Climate Experiment (GRACE) mission and its successor, the GRACE Follow On Mission, measure temporal changes in Earth’s gravity field that can be interpreted to determine variations in TWS [119]. The GRACE and GRACE Follow On based TWS data have significantly lower spatial (~ 150,000 km² at mid-latitudes) and temporal (~monthly) resolutions than other Earth observing satellite measurements, and they provide only the departures from the period-mean TWS state (known as TWS anomalies) as opposed to estimates of the total amount of water stored in each TWS component. Nevertheless, because satellite gravimetry is the only remote sensing technology able to detect changes in the storage of water below the first few centimeters of the soil column, including groundwater, GRACE proved to be enormously valuable for hydrological science and related applications. GRACE launched in 2002 and delivered 15 years of TWS data before the mission ended in 2017. GRACE Follow On, which launched on 22 May 2018, is expected to extend the TWS data record for at least another 5 years.

Among many scientific discoveries enabled by GRACE, it was used to quantify groundwater depletion in several major food producing regions around the world. In particular, Rodell et al. [93] and Tiwari et al. [120] documented shocking rates of groundwater decline in northern India caused primarily by extensive and intense agricultural irrigation supported by aquifers where groundwater recharge cannot keep up with extractions. Considering that hundreds of millions of people live there and depend on these crops, the situation is dire.

Subsequent studies applied GRACE data to quantify groundwater losses associated with irrigated agriculture in California’s Central Valley [41], the Middle East [133], Saudi Arabia [118], the North China Plain [44], and other regions. Richey et al. [92] and Rodell et al. [94] provide global overviews, and the latter also discusses the combined effects of natural interannual variability, climate change, and human water management and consumption on TWS.

To overcome the challenges of low spatial and temporal resolution and data latency (which was typically 2–5 months with GRACE but is expected to be significantly reduced with GRACE Follow On), Zaitchik et al. [139] introduced a data assimilation approach for integrating data from GRACE and other, timelier and higher resolution observations in order to produce fields of groundwater, soil moisture, and snow water equivalent in near-real-time. Since 2011, variants of that approach have been applied to deliver wetness/drought indicator fields for the contiguous U.S. (Fig. 4) that are disseminated by the National Drought Mitigation Center, used by farmers, ranchers, other agricultural interests, public agencies, and private consultants, among others [55]. Global, GRACE data assimilation-based wetness/drought indicators have recently been developed as well, which will help to satisfy the need for timely freshwater availability data worldwide [67].

# 6 Observable: Snow Water Equivalent

Worldwide more than 1.2 billion people rely on seasonal water runoff coming from snow pack and glaciers [18]. The Indus Basin in Asia is the largest irrigation system in the world; its snow melt is essential for the rice production in the basin and estimated to have contributed about 13 km³ to agricultural irrigation in 2008 (~ 1/3 of Lake Mead) (Grogan personal communication, [52]). Since 1967, one million square miles of spring snow cover has disappeared from the northern hemisphere, an area roughly the size of Argentina [28]. This change in the global snow cover has a significant impact on food production. Reduced seasonal runoff cause increased reliance on ground water across the world for sustained agricultural production, leading to land subsidence in some parts of the world [70].

NASA sensors like Advanced Microwave Scanning Radiometer-2 (AMSR2) and the Airborne Snow Observatory (ASO) can measure snow water equivalent (SWE) remotely. AMSR2 provides 99% coverage of Earth every 2 days, providing a SWE retrieval at 25 km global resolution with about 80% accuracy over flat areas covered in dry snow. Also, ASO can provide SWE measurements at a spatial resolution of 50 m with an accuracy of 5–8% over limited geographic regions [37].

There are about 800 snow telemetry (SNOTEL) sites located in remote, high-elevation mountain watersheds in the

Springer


---



Remote Sens Earth Syst Sci (2019) 2:18–38

23

**Fig. 4** Groundwater wetness/ drought indicator (wetness percentile relative to all Augusts during the period 1948–present) based on the assimilation of GRACE data into a land surface model for August 15, 2011. Note the severe drought encompassing most of New Mexico, Texas, Louisiana, and the Southeast

Geographical map of the United States showing groundwater wetness/drought indicator for August 15, 2011.

western U.S. as a part of the U.S. Department of Agriculture (USDA) Natural Resources Conservation Service. These sites provide valuable information to forecast downstream water supply. Some stations also include a snow pillow, which records the weight of the snow on top of it, and thereby the water equivalent, but these sites are limited to flat ground and do not represent the terrain very well [36]. Remote sensing of SWE by airborne instruments like ASO provide an alternative to better understand the entire picture for effective management of water resources during both dry and high snow pack years.

One way to calculate SWE is to multiply snow depth with its density over a snow covered area. However, direct measurements are often lacking especially in remote areas. Therefore, agroclimatologists use remotely sensed measurements and models to infer where there might be flooding when snow melts, and how much water can be expected for irrigation during the growing season [74].

SWE is monitored both for its potential to give advanced warning of natural disasters such as flooding due to rapid melting of winter snow in spring, but also its beneficial role as much needed water supply and is thus used in crop monitoring and early warning activities (e.g., GEOGLAM Crop Monitor; FEWS-NET). The impact of drought on crop revenues in California alone was $856 million in the year 2015 [56]. Monitoring and understanding SWE using ground measurements, remote sensing, and modeling allows scientists to better forecast changes in SWE.

# 7 Observable: Soil Moisture

Soil moisture, defined as the amount of water stored in the soil profile, is an essential climate variable that plays a key role in the Earth’s water, energy, and carbon cycles. Soil moisture is a

dynamic boundary condition between the land surface and atmosphere and controls the exchange of water and heat fluxes and storages between the land surface and the atmosphere. Thus, soil moisture has important impacts on water availability, ecosystem exchange processes, vegetation growth, and more. To this end, the availability of adequate and timely soil moisture information is of great importance for numerous applications, including weather forecasting, and drought and flood mapping which are tightly linked to crop health and yield formation monitoring. Water availability is also vital for crop growth and yield formation. Timely, within-season information on expected end-of-season crop production is critical for food security and related decision-making activities as well as identifying approaches for reducing the yield gap. Change in soil moisture conditions is a direct response to weather variability and can be used to detect the occurrence of water-related stress that can potentially hamper plant growth and lead to suboptimal yield production.

Soil moisture monitoring can be achieved through the following techniques [79]:

(1) *Ground-based monitoring using in situ sensors:*

Observations collected using in situ stations characterize with high accuracy, but provide limited spatial coverage.

(2) *Satellite-based soil moisture estimation using radiative transfer modeling:*

This approach generates reliable global datasets with typical accuracy of 0.04 m³/m³. The corresponding soil moisture estimates are representative of the top few centimeters of the soil profile (2–5 cm). Temporal coverage is limited to the operational life span of the mission, which typically do not enable long-term stable climatologies based on individual sensors. Several passive- and

Springer logo Springer


---



24

Remote Sens Earth Syst Sci (2019) 2:18–38

active-based systems currently provide operational global soil moisture data sets, including AMSR2, SMOS, SMAP, and ASCAT.

(3) *Model-based estimation using water or energy balance models:*

The model-based approach provides data with global coverage. Reliability of the model-based soil moisture observations is highly susceptible to the accuracy of the precipitation quality. GLDAS, NLDAS, and FLDAS generated by the NASA’s LDAS system are examples of model-based soil moisture data products [75, 137, 138], detailed in the later section on modeling and assimilation.

(4) *Soil moisture monitoring using data assimilation techniques:*

These datasets are generated by integrating airborne- or satellite-based soil moisture observations into a hydrologic model, which enhances the model performance and corrects for precipitation related inaccuracies [26]. Examples of such data sets are the SMAP L4 Root-zone soil moisture and the NASA-USDA Global Soil Moisture Data [26, 79, 105]. The latter is operationally used by the U.S. Department of Agriculture-Foreign Agricultural Service (USDA-FAS) for assessing the impact of drought on crop production (Figs. 5 and 6) and generating the agency’s global crop statistics. These data are also utilized by the U.S. Department of Agriculture-National Agricultural Statistics Service (NASS) and the Group on Earth Observations Global Agricultural Monitoring (GEOGLAM).

# 8 Observable: Evapotranspiration

Evapotranspiration (ET) describes the exchange of water vapor between the land surface and the atmosphere and includes

water evaporated from the soil, water bodies, and other surfaces (E) and water used by plants through the process of transpiration (T). ET is central to processes that constrain agricultural food production, linking the energy, water, and carbon cycles in mutually dependent relationships [46]. An increase in energy (i.e., lengthening days, reduced cloud cover) favors carbon assimilation through photosynthesis (primary production) and also increases ET, extracting available water from the soil, representing the largest component of consumptive water use in the US.

If the soil water is not replenished through rain or irrigation, plants close their stomata to conserve water and primary production is reduced. The associated reduction in transpiration shifts the surface energy balance from latent heat (water exchange with the atmosphere) to sensible heat (heat exchange). By comparing observed ET to a modeled expectation of crop water requirements, ET observations can be used to schedule irrigation applications and improve agricultural water management. In rain-fed agriculture, reductions in actual ET are often a leading indicator that drought may impact food production [10, 11, 86]. Similarly, the link between transpiration and primary production can be used to inform agricultural yield predictions, and assess agricultural water use efficiency (crop per drop).

Despite the importance of ET in understanding the agricultural food system, it is also one of the least constrained components of the hydrological cycle. The lack of regular, spatially dense ET observations makes ET the greatest remaining data gap in water resources management. ET may play a key role in providing accurate and timely drought forecasts to water managers [47]. The ET-based Evaporative Stress Index (ESI) [6, 7, 9] is one of the few drought metrics to capture the magnitude, intensity, and timing of the 2012 US drought at resolutions applicable for management (~ 5 km) [86]. For retrospective studies, there are several other approaches available at spatial resolutions on the order of 25 km, e.g., the LandFlux evaluation [59, 81]. Continental scale estimates of ET are based on more readily available

Map of South Africa showing sub-surface soil moisture anomalies for August 2016

Map of South Africa showing sub-surface soil moisture anomalies for August 2017

Fig. 5 Sub-surface soil moisture (SM) anomalies over South Africa developed using the USDA-FAS Palmer model and satellite observations from the NASA Soil Moisture Active Passive (SMAP) mission. South Africa has been experiencing a decline in rainfall, which reached record

low amounts during the 2017 growing season, and had an adverse impact on the wheat production in the area. This is captured by the negative anomaly values (i.e., brown colored end of the scale bar) indicative of water deficiency for crop production

Springer logo Springer


---



Remote Sens Earth Syst Sci (2019) 2:18–38

25

Fig. 6 Sub-surface soil moisture (SM) anomalies over Australia at the end of July 2018 developed using the USDA-FAS Palmer model and satellite observations from the NASA Soil Moisture Active Passive (SMAP) mission. Soil was especially dry over New South Wales where the drought had impacted large areas of grazing and cropland

Map of Australia showing sub-surface soil moisture anomalies in July 2018, with severe drought conditions in New South Wales.

meteorological and hydrological observations and require a significant process model or statistical framework. Long records of these observation-based estimates improve our understanding of the feedbacks within the climate system that directly affect our food system (e.g., [65, 78]).

Because ET can differ from field to field, a spatial resolution of 50–100 m is needed to infer actionable information for individual farmers. At that resolution, the most direct diagnostic of ET is the surface temperature observed through thermal infrared sensors, most notably Landsat. There are various different approaches with long legacy that estimate ET from surface temperature observations in combination with an analysis of the surface energy balance (EB). Many of these approaches have found wide application in agricultural studies or water management applications (e.g., [3, 8, 21]).

The first group of larger scale EB approaches treat evaporation as a single bulk flux that includes soil and vegetation sources, and applies a scene-based scaling (e.g., SEBAL [20], SEBS [117], METRIC [4], and SSEB [110]). These approaches evaluate the energy balance at “dry” and “wet” extremes and estimate ET between these extremes based on the spatial variation of internally calibrated temperature within the scene of the satellite image. In order to also assess agricultural water use efficiency, it is essential to distinguish between beneficial water use (transpiration) and non-beneficial water use (evaporation from the soil). Two-source EB approaches consider soil and vegetation as separate “sources” for heat and water exchange [63, 64, 84]. ALEXI/DisALEXI combines the regional scale ALEXI ET estimate with high-resolution observations (e.g., Landsat).

The processing and calibration of large sets of Landsat images is computationally demanding and impacts the availability and latency of high-resolution ET estimates for stakeholders. The use of cloud computing now allows for the processing of Landsat images at a greater scale. An example of this is the adaptation of METRIC to work on Google Earth Engine (GEE) allowing for the calibration of Landsat images with weather station data, and generation of Earth Engine Evapotranspiration Flux (EEFlux) [5].

Now anyone with Internet can access Landsat data, choose a location, and see an evapotranspiration map within seconds. The OpenET effort builds on the initial success of EEFlux, adding additional ET models (both single- and two-source) to a GEE framework for ensemble assessment of predicted consumptive water use. OpenET will allow ready intercomparison between multiple high-resolution ET models over a broad range in climatic and vegetation cover conditions, enabling users to select a model that performs best in their area of interest or extracting a multi-model average.

## 9 Observable: Water Quality

Water quality is as important to food production as water quantity, but is harder to measure from space because many of its characteristics are invisible. Fresh and clean water is needed for agriculture production while fresh or salt water with a balanced, healthy ecosystem is critical for aquaculture as a sustainable food source. Land use choices control nutrient, sediment, salt, and pollution runoff to water bodies. When those are impacted in a significant way, restrictions have to be imposed on agriculture to improve water quality. In this way, water quality can also impact water availability for agriculture. Additionally, the quality of water in catchments and reservoirs is important for healthy crops and livestock.

In recent years, coastal and inland water quality has been declining with population growth, expanded human activities near waterways, and climate change [124, 125]. In the U.S., the declining quality of freshwater systems has led to estimated annual economic losses of $4.6 billion for sectors including agriculture, aquaculture, and fishing, as well as tourism, real estate, and healthcare [33]. Other parts of the world have

Springer logo Springer


---



26

Remote Sens Earth Syst Sci (2019) 2:18–38

greater population pressure on their water quality, e.g., from raw sewage. Worldwide, the combination of warmer temperatures, increased intensity of storms causing flooding, erosion, and an overabundance of nutrient runoff from land have compromised adjacent waters with severe environmental impacts such as harmful algal blooms, dead zones with little or no oxygen, and the loss of biodiversity.

Harmful blooms of blue-green algae or cyanobacteria respond quickly to ecosystem changes and are an increasing problem due to warming temperatures and water column stratification combined with excess nutrients [87]. These harmful algal blooms have become a global health issue through fish and shellfish diseases and mortality as well as illness in humans and animals that eat them [13, 51, 77]. Livestock drinking water containing cyanobacteria can suffer reductions in growth, lactation, and reproduction or even mortality. Consuming fresh vegetables that have been irrigated with water containing cyanobacteria can also cause illness and mortality in humans.

The importance of water quality for food safety and security lends urgency to the need to remotely sense its parameters. Land use change, urban sprawl, ecosystem health, vegetation, and crop cover have been monitored by the Landsat Thematic Mapper and Enhanced Thematic Mapper at 30 m resolution about twice a month for several decades. Although not optimized for aquatic measurements, the NASA/USGS Landsat 8 Operational Land Imager (OLI) has added new spectral bands that can be applied to water resources and coastal zone investigations of water clarity, turbidity, chlorophyll-a, and surface temperature [49, 88, 89]. Furthermore, the frequency of these 30 m measurements can increase toward 3 days when Landsat OLI is harmonized with the European Space Agency (ESA) Sentinel-2 Multi-Spectral Imager (MSI) [32]. Water quality indicators derived from these sensors are gradually being applied to aquaculture decisions. One of the earliest attempts addresses water clarity. Since 1866, water clarity has been quantified at discreet locations by the depth at which a Secchi disk lowered into the water from the surface disappears from view [91]. The deeper the Secchi depth, the better the water clarity. Satellite data are now used to remotely estimate this variable over large areas (Fig. 7) as a water quality indicator for fishing, crabbing, and shellfish aquaculture sites [114].

Aquatic ecosystems in the open ocean have been continuously monitored from space for the past 20 years by NASA ocean color spectrometers [73]. These satellite-borne sensors were designed to provide a nearly daily view of the open ocean where sampling opportunities are rare and expensive. The color measured at the ocean’s surface is used to derive chlorophyll-a concentrations, the primary photosynthetic pigment in phytoplankton. Continuously monitoring the whole Earth from the visible to near-infrared portions of the

spectrum at 1–10 km spatial resolution advanced our understanding of mechanisms fostering global primary production. Ocean color sensors were not optimized for monitoring water quality in coastal and inland waters where the myriad of constituents in the water and overlying atmosphere are optically challenging, further confounded by land adjacency effects and their spatial resolution is too large for most inland water bodies. These technical issues as well as confidence in satellite data continuity have limited their adoption by water quality managers [80, 106]. Yet the great demand for this information has led to some clever adaptations in the coastal ocean, large estuaries, lakes, and rivers. Remotely sensed observations from the visible to near-infrared portions of the spectrum include water clarity, turbidity, sediments and detritus, chlorophyll-a, and other pigments indicating phytoplankton biomass and community composition, shallow submerged and floating aquatic vegetation, surface oil slicks, and other variables estimated or inferred through regional correlations between field measurements and remotely sensed proxies (e.g., harmful algal blooms) [58, 83, 106]. Additionally, surface temperature from remotely sensed infrared measurements is another important variable related to water quality. Invisible variables that cannot be directly sensed remotely include nutrients, dissolved oxygen, acidity or pH, microbes, and pollutants.

Although satellite observations do not detect the presence of toxins, they are useful for estimating cyanobacterial abundance and directing in situ sampling [116]. The ESA MEdium Resolution Imaging Spectrometer (MERIS) spectrometer, 2002–2012, followed by the Ocean and Land Color Instrument (OLCI) sensor on the Sentinel-3 that launched in 2016 [35], were designed with additional spectral resolution that enables the detection of algal blooms of cyanobacteria (Fig. 8) [77, 115]. Increased spectral resolution by MERIS followed by OLCI enable monitoring the likelihood of these cyanobacterial harmful algal blooms and their frequency of occurrence, yet have been limited to about 6% of continental U.S. freshwater lakes and reservoirs by their 300 m bin size [31, 128]. Thirty-meter bin size would resolve more than 60% of freshwater lakes and reservoirs [31]. Thus, a combination of sensors with additional spectral resolution and new methods to synthesize multiple types of measurements could improve this coverage in the future.

Airborne and upcoming satellite-borne hyperspectral remote sensing present options for the detection of dissolved organic carbon and additional water quality variables (e.g. [45, 71]). After 2022 when NASA launches the Plankton, Aerosol, Cloud, ocean Ecosystem (PACE) satellite, information from its hyperspectral Ocean Color Imager at 1 km resolution may be combined with higher spatial resolution data, and perhaps LiDAR for vertical information [24]. Coupling

Springer logo


---



Remote Sens Earth Syst Sci (2019) 2:18–38

27

Secchi depth of the upper Chesapeake Bay and several tributaries derived from the Landsat OLI (left) and the same April 13, 2016 Landsat scene in true color (right).

Fig. 7 Secchi depth of the upper Chesapeake Bay and several tributaries derived from the Landsat OLI (left) and the same April 13, 2016 Landsat scene in true color (right). Credit: Lachlan McKinna and NASA Earth Observatory

these sophisticated synoptic observations with in situ biophysical and bio-optical measurements and long-term datasets from sensor networks and monitoring programs will inform water resource planning to address goals of water and food security, biodiversity, and sustainable ecosystem management

[54, 80, 109]. Challenges to global water quality monitoring by satellites remain, yet increasingly accessible Earth observations have the potential to significantly advance near-real-time water quality indicators in support of decisions related to food production and security around the world.

NOAA Lake Erie Harmful Algal Bloom Bulletin for July 30, 2018 showing cyanobacterial density.

Fig. 8 NOAA Lake Erie Harmful Algal Bloom Bulletin for July 30, 2018 shows medium cyanobacterial density in the southwestern lake, with a threshold for cyanobacteria detection of 20,000 cells/ml. Gray indicates

clouds or missing data. Source: [http://tidesandcurrents.noaa.gov/hab/lakeerie.html](http://tidesandcurrents.noaa.gov/hab/lakeerie.html)

Springer logo Springer


---



28

Remote Sens Earth Syst Sci (2019) 2:18–38

# 10 Observable: Air Quality

Food security programs usually focus on water, nutrition, and disruptions to food distribution systems, while the impact of air pollution on crops is often overlooked. The economic impact of crop yield loss due to pollution is significant all over the world, including in regions that experience food insecurity [2, 16, 130]. Most losses occur from one pollutant, tropospheric ozone (O₃), which can lower photosynthetic rates and decrease yield and yield quality [2]. Emberson et al. [40] define O₃ damage hot spots as regions with more than 3 months exposure to surface O₃ concentrations above 44 ppbv. Global crop yield losses for wheat, corn, and soybeans are estimated to range from $11–26 billion (U.S. 2000) annually, with the greatest economic loss estimated to occur in the United States ($3.1 billion). Yield reductions may be as high as 50% for some crops in highly polluted areas such as India [29]. The greatest economic loss is estimated to occur in the United States ($3.1 billion) despite the fact that scientists have been working with farmers for decades to identify and propagate O₃-tolerant varieties for high crop productivity (e.g., [2]). Crop losses associated with air pollution exposure are projected to increase for many world regions over the next decade, including in areas most vulnerable to food insecurity [17].

Surface-level O₃, at elevated concentrations above injury thresholds, reduces crop yields following uptake through a plant’s stomata (i.e., tiny pores on the lower leaf surface) and chemical reaction with plant cells. O₃ injury to plants is evident often as a fine tan to dark colored stippling pattern on the upper leaf surface that accumulates throughout the growing season (Fig. 9). However, the impact of O₃ on plants is not always obvious to the naked eye. When O₃ air pollution

exceeds injury thresholds during air stagnations, the pollutant can seriously affect overall plant health, ultimately reducing growth and yields. This effect is referred to as "hidden" O₃ injury.

Although it is not currently feasible to infer surface O₃ from satellite data of O₃, satellites provide information on the chemical precursors that lead to O₃ formation, including nitrogen oxides (NOₓ = NO + NO₂). NOₓ occurs naturally in the atmosphere, but human activities, such as the burning of fossil fuels, elevate its concentrations, allowing unhealthy levels of surface O₃ to form. Nitrogen dioxide (NO₂) serves as a proxy for NOₓ and is observable from space [66, 132]. Satellite data of NO₂ are used as input to computer simulations of atmospheric chemistry and transport to estimate surface O₃ pollution. These simulations give valuable information on O₃ levels in agricultural areas, the long-range transport of O₃ from urban to agricultural areas, and how O₃ levels are evolving over time. Current and future O₃ concentrations can then be fed into crop modules equipped with next-generation O₃ response modules, enabling a more detailed examination of plant response to elevated O₃ during different phenological stages or in combination with additional drought and heat stresses [40]. The model output may then be used to inform stakeholder decisions related to agricultural planning and air pollution management.

NO₂ data from the Dutch-Finnish Ozone Monitoring Instrument (OMI), a spectrometer that observes solar backscatter radiation in the visible and ultraviolet wavelengths, have given us an unprecedented look at how NO₂ has varied around the world, including over agricultural regions (Fig. 10); OMI is on the NASA Aura polar-orbiting satellite, which was launched in 2004 [38]. Several new satellite instruments of similar heritage as OMI were recently launched or are nearing launch and promise to provide even better NO₂ data. For instance, the ESA TROPOspheric Monitoring Instrument (TROPOMI; launched in 2017) on the polar-orbiting Sentinel-5 Precursor satellite collects data on NO₂ at suburban spatial resolutions (e.g., a few kilometers), a much finer resolution than OMI [131]. Additionally, a fleet of satellites in geosynchronous orbit over East Asia (Korean Space Agency Geostationary Environment Monitoring Spectrometer (GEMS)), North America (NASA Tropospheric Emissions: Monitoring Pollution (TEMPO)), and Europe (European Space Agency Sentinel-4) will provide much needed information on how air pollutant concentrations and emissions vary throughout the day; launches are expected in the early 2020s. Given the potential of air pollution to increase with projected population growth in the tropics and subtropics, geosynchronous satellites with similar capabilities are needed over the megacities and agricultural regions of the tropical and subtropical land masses as well.

Observations of atmospheric ammonia (NH₃) from satellite instruments give complementary information to NO₂ data by

Characteristic O₃-induced injury on green bean plant leaves showing stippling pattern.

Fig. 9 Characteristic O₃-induced injury on the topside of green bean plant leaves. The stippling, which does not occur on veins, is associated with dark pigments accumulating within injured cells. O₃ injury symptoms often vary with different crops. Photo Credit: Emerson Sirk/NASA

Springer logo Springer
2


---



Remote Sens Earth Syst Sci (2019) 2:18–38

29

Map showing NO2 levels over the United States in 2005

Map showing NO2 levels over the United States in 2016

Fig. 10 From [38], OMI data show that NO<sub>2</sub> levels have decreased from 2005 to 2016 by about 20–60% over most U.S. cities as a result of environmental regulations. As a national average, surface monitors

indicate that O<sub>3</sub> decreased by about 15% as a consequence, good news for both human and plant health. However, increasing trends in O<sub>3</sub> pollution in other regions of the world pose a threat to food security

indicating when and where nitrogen-based fertilizers are applied [135]. While thermal power plants and automobiles are the dominant NO<sub>x</sub> sources, the application of nitrogen-based fertilizers may also be an important source of NO<sub>x</sub> to the atmosphere in agricultural regions, potentially allowing high levels of surface O<sub>3</sub> to form. Instruments observe NH<sub>3</sub> using infrared wavelengths, e.g., IASI [30], CrIS [112], and AIRS [135]. While the impact of O<sub>3</sub> pollution has a clear, negative impact on plant health, the impact of particulate matter (PM) pollution from dust and smoke is more complicated (e.g., [107]). Depending on concentration, PM in the atmosphere can either reduce or enhance crop yields by scattering light. For instance, PM can diffuse sunlight, creating a more even and efficient distribution of photons, which can offset the haze-induced reduction in total sunlight reaching the plant.

# 11 Physical Model: Hydrology Data Assimilation

Monitoring and forecasting drought and its impacts on crops requires an objective definition of drought or a "convergence of evidence" process by which drought may be defined. The Land Data Assimilation System (LDAS) is an effort that take many of these satellite-derived observations and assimilate them with other observations and model output for use in regularly gridded retrospective and current assessments and forecasts.

The NASA Land Information System (LIS) software provide data to both NOAA’s North American Land Data Assimilation System (NLDAS) Drought Monitor and the associated National Integrated Drought System [137, 138], and FEWS-NET via the FEWS-NET LDAS (FLDAS; [75]). These LDAS systems use optimal inputs (forcing and parameters) to produce estimates of the water balance (precipitation, runoff, evapotranspiration, soil moisture) and energy balance (evapotranspiration, temperature, radiation). These data can

then be used to derive indices, like soil moisture anomalies (Figs. 11 and 12) and QuickDRI that inform drought and crop growing conditions.

In 1999, the U.S. Drought Monitor (USDM) was established as a weekly map of drought conditions produced jointly by the National Oceanic and Atmospheric Administration (NOAA), the U.S. Department of Agriculture (USDA), and the National Drought Mitigation Center at the University of Nebraska-Lincoln. Internationally, the Famine Early Warning Systems Network (FEWS-NET), established in 1985 by US Agency for International Development (USAID), produces a weekly map of drought conditions for Africa, Central Asia, and Latin America. Other international drought monitors include the Middle East and North Africa Drought Platform (e.g., [1, 111]). A number of other organizations collate data from other sources, including FEWS-NET, e.g., the UN Food and Agriculture Organization (FAO) Global Information and Early Warning System on Food and Agriculture (GIEWS), the Global Drought Information System Portal [90], and the GEOGLAM Crop Monitor led by the University of Maryland [22].

Given that different Earth observation products that rely on various sensors and models may not agree, analysts use a "convergence of evidence" approach. Evidence from different products is weighed by experts, who ultimately decide the classification and extent shown in both on the US Drought Monitor and FEWS-NET Hazards maps. The US Drought Monitor employs a classification scheme where a category/description has associated impacts as well as thresholds for different metrics including the Palmer Drought Severity Index (PDSI), soil moisture percentiles, streamflow percentiles, the standardized precipitation index (SPI), and a composite index. Similarly, FEWS-NET has criteria for determining levels of dryness that increase in severity from abnormal dryness, to drought, to severe drought. The criteria for "drought" classification for example are (1) the area must have previously been defined as "abnormal dryness"; (2) are must reginate

Springer logo Springer


---



30

Remote Sens Earth Syst Sci (2019) 2:18–38

# Soil Moisture (10-40 cm) Anomaly
# July 2018

Geographical map of Africa showing soil moisture anomalies for July 2018 with a legend in m³/m³ ranging from < -0.06 to > 0.06. Source: version final. Map produced by USGS/EROS.

Fig. 11 Within FEWS-NET: FLDAS Soil moisture anomaly derived from CHIRPS rainfall, MERRA-2 meteorology, forcing the Noah land surface model. Source: USGS/EROS

season precipitation, soil moisture, and runoff deficits below 20<sup>th</sup> percentile; and (3) reports of developing drought conditions and impacts on crop and water resources from the field.

The NLDAS and FLDAS system are updated routinely and provide long-term estimates of relevant conditions so that standardized indices and percentiles (i.e., precipitation, soil moisture) can be computed and provide decision support to analysts that generate the drought hazard maps.

## 12 Impact Models: Retrospective, Real-Time, and Future Analysis of Crops

Process-based crop models simulate day-to-day crop growth and development over the course of an agricultural season in response to environment, management, and genetics as determined by fundamental biophysical processes [61]. Environmental drivers include conditions within the soil

profile (texture, temperature, and moisture within 5–10 soil layers extending to nearly 2 m below the surface) and surface meteorology (typically daily maximum and minimum temperatures, precipitation, and solar radiation; more advanced models also include relative humidity or vapor pressure and wind speed). Management information includes data on planting (dates, row spacing, row depth, etc.), inputs (irrigation, fertilizers), and harvest (equipment and limiting dates). Genetic information describes the fundamental traits of the crop variety (characteristics universal to a given species and those specific to the selected cultivar, typically represented as genetic parameters). Crop development depends on balanced flows of water, energy, carbon, and nutrients, which drive and respond to crop processes depending on phenological stage and the potential presence of stress factors (e.g., water, temperature, or nitrogen stress). Crop models can predict yield and resource use (water and nitrogen) to help optimize current and alternative systems under a variety of priority criteria.

Springer logo


---



Remote Sens Earth Syst Sci (2019) 2:18–38

31

NLDAS Soil moisture anomaly map of the United States

Quick Drought Response Index (QuickDRI) map of the United States

Fig. 12 **a** NLDAS Soil moisture anomaly derived from NCEP’s Eta model-based Data Assimilation System (EDAS) [[95]](https://doi.org/10.1175/BAMS-85-3-339) meteorological forcing, and a merged precipitation product derived from stations, radar

and reanalysis, and the Noah land surface model. **b** The QuickDRI is derived from NLDAS soil moisture, in addition to evapotranspiration, precipitation, and vegetation conditions from other sources

Earth information is critical to the configuration, evaluation, and application of crop models to meet a variety of stakeholder needs. Remote sensing data can determine the date and area planted for many crop species. In situ networks and remote sensing platforms provide meteorological observations, while weather and climate models fill in gaps and expand beyond observations with forecasts and projections. Crop models are often quite sensitive to common biases within atmospheric models, requiring additional bias-adjustment for improved fidelity [101, 102]. Simulated crop progress and status may also be compared against field and remotely sensed observations of crop conditions.

A well-configured and -evaluated crop model serves a variety of stakeholder-driven applications that range across a continuum of time scales and alternative farm systems. Models operating under historical conditions utilize (and potentially assimilate) multiple observations to attribute observed anomalies, establish climatological expectations, and potentially reconcile biases across diverse observational datasets within a physically consistent crop process framework. Crop models applied in the near-real-time contribute to monitoring and early warning efforts while also potentially providing timely forecasts of seasonal outcomes and intervention opportunities. Crop models may also project future climate conditions, alternative farming systems, or the response to hypothetical extreme events.

The Agricultural Model Intercomparison and Improvement Project (AgMIP) is an international community of 1000+ experts working to develop agricultural system frameworks for applications related to resilient production and food security (C. [[97]](https://doi.org/10.1016/j.agsy.2012.07.001)). AgMIP facilitates the use of cutting-edge earth information and encourages ensemble modeling activities at the

field scale [14, 15, 19, 48, 69, 72, 113] as well as across global grids [39, 82, 98]. Crop model output can be combined with broader integrated assessment models to evaluate the implications of large-scale policy and investment decisions [103], can include further impact factors (e.g., pests, diseases, and ozone damages; [34, 40]), and can directly link with other disciplines, scales, and models within coordinated assessments [99, 100, 104].

# 13 Damage Models: Pests and Disease

Agricultural lands respond strongly to anomalies in temperature, precipitation, and solar radiation, but additional biotic and abiotic pressures can also have acute impacts on short- and long-term production with broad consequences for local and global stakeholders. Here, we examine the unique threats posed by pests, diseases, and elevated ozone concentrations affecting agricultural production, as well as the observations and models that are needed to understand and apply earth information to improve decision-making.

While there are millions of specific pests and diseases that affect crop systems, these may be generalized according to critical climatological thresholds for their spread and the ways in which they affect plants [27, 34]. Earth information can identify conditions that are conducive to pest and disease spread, as well as to recognize affected plants as an element of early warning systems that allow corrective or preparatory interventions. Pests are often limited by total rainfall amounts and annual minimum temperatures that can interfere with reproductive and development cycles. Plants are more receptive to disease when the stem and leaf

Springer logo


---



32

Remote Sens Earth Syst Sci (2019) 2:18–38

canopy is wet, with key sensitivities to diurnal cycles of relative humidity and temperature as well as extended periods of precipitation or flooding. Some pest vectors and disease spores are also carried by prevailing winds, with jet stream patterns shifting affected areas from year-to-year. Analysis of these metrics helps us identify hazardous climate conditions which we can monitor, forecast, and project into the future.

Remote sensing can pick up declines in productivity and crop failures in affected areas, and technology empowers corporations and citizens to observe and document outbreaks using social media. Pest and disease modules are increasingly being added or coupled to crop models in recent years to forecast likely outbreaks and their likely ramifications and attribute observed losses, leading to new decision support systems that could help users identify and prioritize actions [34]. Pest and disease modules coupled with crop and climate models also help stakeholders understand how climate variability, such as the El Niño/Southern Oscillation, and climate change shift the probability of outbreaks, aiding in the determination of preventative measures [96].

# 14 Risk Models: Sector Shocks and Disasters

The agricultural system is vulnerable to a wide array of natural and man-made hazards that can disrupt production, processing, transportation, and prices with direct and indirect implications for food security. Identifying and anticipating these shock events helps stakeholders respond to ongoing disasters, prepare for likely shocks, and build resilience in order to ensure food system stability.

Decision support systems may utilize NASA earth information in attributing, monitoring, and forecasting major agroclimatological hazards. Meteorological observations and atmospheric models track heat waves, cold snaps, floods, drought, heavy storms, hail, and freezing rain events that can decrease yield, damage production quality, or kill crops before harvest can even occur. The level of shock depends on the magnitude, spatial extent, duration, and timing of these extremes in comparison to critical crop development stages. More subtle weather sequences can be equally disruptive, as illustrated by two examples. First, "false starts" to the monsoon season occur when the initiation of seasonal precipitation encourages farmers to transplant, only to watch seedlings die as dry conditions return ahead of the persistent monsoon arriving weeks later. Second, late winter warming can melt snow cover and entice blooming of fruit trees, exposing vulnerable plants to frost damage when normal winter and early spring conditions return (Grotjahn et al., In review).

Models and observational products may also be used to track important external hazards affecting the food system. Weather products can identify conditions conducive to the

spread of pests and diseases, while satellites can observe their net reductions in agricultural productivity. Satellites are also important elements of response and recovery efforts following major disasters that can affect agricultural transportation networks, including hurricanes, landslides, earthquakes, tsunamis, and floods. Agricultural risks are a growing element of new efforts to examine interactions between disasters as part of the United Nations Sendai Framework for Disaster Risk Reduction 2015–2030 [126]. Nations that are a party to the Sendai Framework have also committed to increased reporting of agricultural disasters, which will provide new ground-truth datasets that may be used to develop and evaluate next-generation decision support products.

While guarding against shock and disaster risk in one's own region is critical, it is also important to remain vigilant against shocks and disaster risk affecting distant agricultural regions given the increasingly interconnected nature of the global agricultural sector which builds reliance on food baskets and major trading partners. A diverse trade networks can act to disperse shocks but also spread risk widely given elevated global exposure and streamlined flows of goods that has tended to concentrate regions of production for key agricultural commodities. Assessment of current and future risk therefore requires regional and global disaster information to be placed in the context of markets and consumer populations while also recognizing the potential human toll of food insecurity.

The agricultural sector faces long-term shifts in its risk profile due to population growth, the rapid expansion of agricultural lands and infrastructure, socioeconomic development, technological innovations, geopolitical events, and global environmental changes including climate change and the degradation of soil and water resources. Changes in shock and disaster risk can be explored using a combination of climate projections (e.g., [108]), bias-adjustment of climate model outputs [101, 102, 121], process-based crop models [61, 97], and integrated assessment models incorporating future socioeconomic conditions [85, 129].

# 15 Climate Change Models

Future agricultural systems will be shaped by overlapping pressures from climate change, population growth, socioeconomic development, and technological innovation. Long-term climate impact projections also shed light on present extreme events, elucidating likely trends and shifts in probability as the climate pushes toward a new equilibrium. Anticipating agricultural production and food security implications provides critical information for policymakers debating action to mitigate climate change, but also informs a variety of current stakeholder decisions with time scales of a decade or more.

Springer


---



Remote Sens Earth Syst Sci (2019) 2:18–38

33

To illustrate the types of decisions under consideration today, take an example agricultural region where climate projections indicate warmer mean temperatures, declines in precipitation, and a later rainy season. Current crop varieties may no longer be suitable under the changed conditions; however, it typically takes 8 to 15 years to mass-produce targeted seeds and even longer if key traits do not already exist in current varieties’ germplasm. This region may also require new water storage and distribution facilities for irrigation that can take a decade to construct and would be expected to last for a century or more even as the climate changes. Farmers and extension services may also recognize the growing need to change farm systems toward more suitable agricultural commodities, altering value chains and the utility of established processing plants and transportation facilities. Changing climate zones and food demand will also place tremendous pressure on water, land, and energy resources, with widespread implications for food prices and agricultural encroachment into natural ecosystems.

Anticipating climate change impacts on agricultural production requires a combination of process understanding to resolve the mechanics of production and resource use changes, present-day observations of climate and agriculture, probabilistic climate scenario generation, coherent coupling between multi-disciplinary systems (climate, biophysical, socioeconomic, and geopolitical), and consistent scenarios to place climate changes in the context of other global change pressures. Earth information products provide critical information about the world’s agricultural systems, current climate [50, 101, 102], and future climate projections [101, 102, 108, 121]. Process-based crop models driven by earth information inputs are particularly useful for climate impact studies given their ability to capture non-linear responses outside of observed conditions [61].

The Agricultural Model Intercomparison and Improvement Project (AgMIP) fosters an international community of climate, crop, livestock, economics, and nutrition experts to develop and apply multi-discipline, multi-scale, and multi-model frameworks to assess future agricultural production and food security (C. [97]). AgMIP activities incorporate cutting-edge products and track the implications of climate changes and uncertainties [134] as impacts reverberate between local and global markets and the populations that depend on agricultural systems for adequate and stable food supply [100, 104, 136]. AgMIP has assessed agricultural responses to core climate change factors (i.e., shifts in temperature, precipitation, and CO<sub>2</sub> concentrations) across local and global gridded crop model ensembles [103]. Transient simulations also elucidate shifting patterns of global production and water use [39, 98], and are useful in conjunction with pathways of agricultural system transformation that help stakeholders shape a more productive and resilient future [12, 129].

# 16 Conclusions

As the world’s population grows and climate changes, food security is a growing global problem, inextricably tied to water and energy, demanding a multi-sectoral, global solution. Global satellite data products and integrated models are required to better understand and manage resources in the food-water-energy nexus. Global monitoring of geophysical variables from satellites provide near-real-time quantification of the Earth system that can be assimilated into early warning and predictive tools. Here, we have highlighted several of the Earth observational products related to vegetation, water quantity, water quality, and air quality that can be combined with additional information to inform decisions around food production. Remote sensing by satellite and airborne sensors yields measurements over large areas on a regular, consistent basis, providing the ability to monitor changes over time. Published literature shows recent progress in the adoption of Earth observations for agriculture and aquaculture applications, the former more quickly than the latter. As we gradually overcome challenges associated with calibrating and validating new measurements and new applications of existing measurements, confidence in these capabilities will increase, leading to wider use and better understanding of the benefits of remote sensing in support of food security. Sensors are currently being planned and built with finer spectral, spatial, or temporal resolution that can be integrated with increasingly sophisticated data assimilation and modeling to support informed decisions by farmers, fishers, humanitarian aid organizations, first responders, and more. New and emerging science and technology can foster solutions for some of society’s challenges regarding current and future hunger, malnutrition, and instability due to food shortages.

**Abbreviations** AgMIP, Agricultural Model Intercomparison and Improvement Project; AMSR-2, Advanced Microwave Scanning Radiometer-2; ASCAT, Advanced Scatterometer; ASO, Airborne Snow Observatory; ALEXI, Atmospheric Land EXchange Inverse; AVHRR, Advanced Very High Resolution Radiometer; CHIRPS, Climate Hazards Group InfraRed Precipitation with Station data; EB, Energy balance; EDAS, Eta model-based Data Assimilation System; EEFLUX, Earth Engine Evapotranspiration Flux; ESA, European Space Agency; ESI, Evaporative Stress Index; ET, Evapotranspiration; FAO, UN Food and Agriculture Organization; FEWS-NET, Famine Early Warning Systems Network; FLDAS, FEWS-NET Land Data Assimilation System; GEE, Google Earth Engine; GEMS, Geostationary Environment Monitoring Spectrometer; GEOGLAM, Group on Earth Observations Global Agricultural Monitoring; GIEWS, Global Information and Early Warning System on Food and Agriculture; GLDAS, Global Land Data Assimilation System; GOME-2, Global Ozone Monitoring Experiment – 2; GPM, Global Precipitation Measurement; GPP, Gross primary production; IMERG, Integrated Multi-satellitE Retrievals for GPM; IPWG, International Precipitation Working Group; LDAS, Land Data Assimilation System; LiDAR, Light Detection and Ranging; LIS, Land Information System; MERIS, MEdium Resolution Imaging Spectrometer; MERRA-2, Modern-Era

Springer logo


---



34

Remote Sens Earth Syst Sci (2019) 2:18–38

Retrospective analysis for Research and Applications, Version 2; MODIS, Moderate Resolution Imaging Spectroradiometer; MSI, Multi-Spectral Imager; NASA, National Aeronautics and Space Administration; NDVI, Normalized Difference Vegetation Index; NLDAS, North American Land Data Assimilation System; NOAA, National Oceanic and Atmospheric Administration; OCI, Ocean Color Imager; OLCI, Ocean and Land Color Instrument; OMI, Ozone Monitoring Instrument; PACE, Plankton, Aerosol, Cloud, ocean Ecosystem; PDSI, Palmer Drought Severity Index; PM, Particulate matter; SeaWiFS, Sea-Viewing Wide Field-of-View Sensor; SM, Soil moisture; SMAP, Soil Moisture Active Passive; SMOS, Soil Moisture and Ocean Salinity; SNOTEL, Snow telemetry; SPI, Standardized Precipitation Index; SWE, Snow water equivalent; TEMPO, Tropospheric Emissions: Monitoring Pollution; TROPOMI, TROPOspheric Monitoring Instrument; UNESCO, United Nations Educational, Scientific and Cultural Organization; USDA, U.S. Department of Agriculture; USDA-FAS, U.S. Department of Agriculture–Foreign Agricultural Service; USDA-NASS, U.S. Department of Agriculture–National Agricultural Statistics Service; USDM, U.S. Drought Monitor; USGS, United States Geological Survey

**Open Access** This article is distributed under the terms of the Creative Commons Attribution 4.0 International License (http://creativecommons.org/licenses/by/4.0/), which permits unrestricted use, distribution, and reproduction in any medium, provided you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made.

**Publisher’s Note** Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

# References

1. Aadhar S, Mishra V (2017) High-resolution near real-time drought monitoring in South Asia. Sci Data 4:170145. [https://doi.org/10.1038/sdata.2017.145](https://doi.org/10.1038/sdata.2017.145)

2. Ainsworth EA (2017) Understanding and improving global crop response to ozone pollution. Plant J 90(5):886–897. [https://doi.org/10.1111/tpj.13298](https://doi.org/10.1111/tpj.13298)

3. Allen R, Irmak A, Trezza R, Hendrickx JM, Bastiaanssen W, Kjaersgaard J (2011) Satellite-based ET estimation in agriculture using SEBAL and METRIC. Hydrol Process 25(26):4011–4027

4. Allen RG, Tasumi M, Trezza R (2007) Satellite-based energy balance for mapping evapotranspiration with internalized calibration (METRIC)—model. J Irrig Drain Eng 133(4):380–394

5. Allen RG, Morton C, Kamble B, Kilic A, Huntington J, Thau D, Gorelick N, Erickson T, Moore R, Trezza R, Ratcliffe I, Robison C (2015) EEFlux: a Landsat-based evapotranspiration mapping tool on the Google Earth Engine, ASABE/IA Irrigation Symposium: Emerging Technologies for Sustainable Irrigation - A Tribute to the Career of Terry Howell, Sr. Conference Proceedings. [https://doi.org/10.13031/irrig.20152143511](https://doi.org/10.13031/irrig.20152143511)

6. Anderson MC, Norman JM, Mecikalski JR, Otkin JA, Kustas WP (2007) A climatological study of evapotranspiration and moisture stress across the continental United States based on thermal remote sensing: 2. Surface moisture climatology. J Geophys Res Atmos 112(D11). [https://doi.org/10.1029/2006JD007507](https://doi.org/10.1029/2006JD007507)

7. Anderson MC, Hain C, Wardlow B, Pimstein A, Mecikalski JR, Kustas WP (2011) Evaluation of drought indices based on thermal remote sensing of evapotranspiration over the continental United States. J Clim 24(8):2025–2044

8. Anderson MC, Allen RG, Morse A, Kustas WP (2012) Use of Landsat thermal imagery in monitoring evapotranspiration and

managing water resources. Remote Sens Environ 122:50–65. [https://doi.org/10.1016/j.rse.2011.08.025](https://doi.org/10.1016/j.rse.2011.08.025)

9. Anderson MC, Hain C, Otkin J, Zhan X, Mo K, Svoboda M, Wardlow B, Pimstein A (2013) An intercomparison of drought indicators based on thermal remote sensing and NLDAS-2 simulations with U.S. drought monitor classifications. J Hydrometeorol 14(4):1035–1056. [https://doi.org/10.1175/JHM-D-12-0140.1](https://doi.org/10.1175/JHM-D-12-0140.1)

10. Anderson MC, Hain CR, Jurecka F, Trnka M, Hlavinka P, Dulaney W, Otkin JA, Johnson D, Gao F (2016a) Relationships between the evaporative stress index and winter wheat and spring barley yield anomalies in the Czech Republic. Clim Res 70(2–3): 215–230

11. Anderson MC, Zolin CA, Sentelhas PC, Hain CR, Semmens K, Yilmaz MT, Gao F, Otkin JA, Tetrault R (2016b) The evaporative stress index as an indicator of agricultural drought in Brazil: an assessment based on crop yield impacts. Remote Sens Environ 174:82–99

12. Antle JM, Valdivia RO, Boote KJ, Janssen S, Jones JW, Porter CH, Rosenzweig C, Ruane AC, Thorburn PJ (2015) AgMIP’s transdisciplinary agricultural systems approach to regional integrated assessment of climate impacts, vulnerability, and adaptation, pp 27–44. [https://doi.org/10.1142/9781783265640_0002](https://doi.org/10.1142/9781783265640_0002)

13. Ashworth CT, Mason MF (1946) Observations on the pathological changes produced by a toxic substance present in blue-green algae (*Microcystis aeruinosa*). Am J Pathol 22:369–380

14. Asseng S, Ewert F, Martre P, Rötter RP, Lobell DB, Cammarano D, Kimball BA et al (2015) Rising temperatures reduce global wheat production. Nat Clim Chang 5(2):143–147. [https://doi.org/10.1038/nclimate2470](https://doi.org/10.1038/nclimate2470)

15. Asseng S, Ewert F, Rosenzweig C, Jones JW, Hatfield JL, Ruane AC, Boote KJ et al (2013) Uncertainty in simulating wheat yields under climate change. Nat Clim Chang 3(9). [https://doi.org/10.1038/nclimate1916](https://doi.org/10.1038/nclimate1916)

16. Avnery S, Mauzerall DL, Liu J, Horowitz LW (2011a) Global crop yield reductions due to surface ozone exposure: 1. Year 2000 crop production losses and economic damage. Atmos Environ 45(13): 2284–2296

17. Avnery S, Mauzerall DL, Liu J, Horowitz LW (2011b) Global crop yield reductions due to surface ozone exposure: 2. Year 2030 potential crop production losses and economic damage under two scenarios of O₃ pollution. Atmos Environ 45(13):2297–2309

18. Barnett TP, Adam JC, Lettenmaier DP (2005) Potential impacts of a warming climate on water availability in snow-dominated regions. Nature 438(7066):303–309. [https://doi.org/10.1038/nature04141](https://doi.org/10.1038/nature04141)

19. Bassu S, Brisson N, Durand J-L, Boote K, Lizaso J, Jones JW, Rosenzweig C et al (2014) How do various maize crop models vary in their responses to climate change factors? Glob Chang Biol 20(7). [https://doi.org/10.1111/gcb.12520](https://doi.org/10.1111/gcb.12520)

20. Bastiaanssen WG, Menenti M, Feddes RA, Holtslag AAM (1998) A remote sensing surface energy balance algorithm for land (SEBAL). 1. Formulation. J Hydrol 212:198–212

21. Bastiaanssen WGM, Noordman EJM, Pelgrum H, Davids G, Thoreson BP, Allen RG (2005) SEBAL model with remotely sensed data to improve water-resources management under actual field conditions. J Irrig Drain Eng 131(1):85–93

22. Becker-Reshef I, Justice C, Sullivan M, Vermote E, Tucker C, Anyamba A, Small J, Pak E, Masuoka E, Schmaltz J, Hansen M (2010) Monitoring global croplands with coarse resolution earth observations: the global agriculture monitoring (GLAM) project. Remote Sens 2(6):1589–1609

23. Beer C, Reichstein M, Tomelleri E, Ciais P, Jung M, Carvalhais N, Rödenbeck C, Arain MA, Baldocchi D, Bonan GB (2010) Terrestrial gross carbon dioxide uptake: global distribution and covariation with climate. Science 329:834–838

Springer logo


---



Remote Sens Earth Syst Sci (2019) 2:18–38

35

24. Behrenfeld MJ, Hu Y, O'Malley RT, Boss ES, Hostetler CA, Siegel DA, Sarmineto JL, Schulien J, Hair JW, Lu XM, Scarino AJ, (2016), Annual boom-bust cycles of polar phytoplankton biomass revealed by space-based lidar. Nat. Geosci. [https://doi.org/10.1038/ngeo2861](https://doi.org/10.1038/ngeo2861)

25. Bierbaum R et al (2014) Delivering global environmental benefits for sustainable development, Washington, D.C., Global Environment Facility

26. Bolten J, Crow W (2012) Improved prediction of quasi-global vegetation conditions using remotely-sensed surface soil moisture. Geophys Res Lett 39(19):L19406. [https://doi.org/10.1029/2012GL053470](https://doi.org/10.1029/2012GL053470)

27. Boote KJ, Jones JW, Mishoe JW, Berger RD (1983) Coupling pests to crop growth simulators to predict yield reductions. Phytopathology. [https://doi.org/10.1094/Phyto-73-1581](https://doi.org/10.1094/Phyto-73-1581)

28. Brown R, Robinson D (2011) Northern hemisphere spring snow cover variability and change over 1922–2010 including an assessment of uncertainty. Cryosphere 5(1):219–229. [https://doi.org/10.5194/tc-5-219-2011](https://doi.org/10.5194/tc-5-219-2011)

29. Burney J, Ramanathan V (2014) Recent climate and air pollution impacts on Indian agriculture. Proc Natl Acad Sci 1111:46. [https://doi.org/10.1073/pnas.1317275111](https://doi.org/10.1073/pnas.1317275111)

30. Clarisse L, Clerbaux C, Dentener F, Hurtmans D, Coheur P-F (2009) Global ammonia distribution derived from infrared satellite observations. Nat Geosci 2:479–483. [https://doi.org/10.1038/ngeo551](https://doi.org/10.1038/ngeo551)

31. Clark J et al (2017) Satellite monitoring of cyanobacterial harmful algal bloom frequency in recreational waters and drinking water sources. Ecological Indicators, vol 80. Elsevier Science Ltd, New York, pp 84–95

32. Claverie M, Ju J, Masek J (2017) Harmonized Landsat-8 Sentinel-2 (HLS) Product User’s Guide. [https://doi.org/10.13140/rg.2.2.33017.26725](https://doi.org/10.13140/rg.2.2.33017.26725)

33. Dodds W et al (2009) Eutrophication of U.S. freshwaters: analysis of potential economic damages. Environ Sci Technol 43:12–19

34. Donatelli M, Magarey RD, Bregaglio S, Willocquet L, Whish JPM, Savary S (2017) Modelling the impacts of pests and diseases on agricultural systems. Agric Syst 155(July):213–224. [https://doi.org/10.1016/J.AGSY.2017.01.019](https://doi.org/10.1016/J.AGSY.2017.01.019)

35. Donlon C, Berruti B, Buongiomo A, Ferreira M-H, Femenias P, Frerick J, Goryl P, Klein U, Laur H, Mavrocordatos C, Nieke J, Rebhan H, Seitz B, Stroede J, Sciarra R (2012) The global monitoring for environment and security (GMES) Sentinel-3 mission. Rem Sens Environ 120:37–57. [https://doi.org/10.1016/j.rse.2011.07.024](https://doi.org/10.1016/j.rse.2011.07.024)

36. Dozier J, Painter TH, Rittger K, Frew JE (2008) Time-space continuity of daily maps of fractional snow cover and albedo from MODIS. Adv Water Resour 31:1,515–1,526. [https://doi.org/10.1016/j.advwatres.2008.08.011](https://doi.org/10.1016/j.advwatres.2008.08.011)

37. Dozier J, Bair EH, Davis RE (2016) Estimating the spatial distribution of snow water equivalent in the world's mountains. Wiley Interdiscip Rev Water 3(3):461–474

38. Duncan BN, Lamsal LN, Thompson AM, Yoshida Y, Lu Z, Streets DG, Hurwitz MM, Pickering KE (2016) A space-based, high-resolution view of notable changes in urban NOₓ pollution around the world (2005-2014). J Geophys Res. [https://doi.org/10.1002/2015JD024121](https://doi.org/10.1002/2015JD024121)

39. Elliott J, Deryng D, Müller C, Frieler K, Konzmann M, Gerten D, Glotter M et al (2014) Constraints and potentials of future irrigation water availability on agricultural production under climate change. Proc Natl Acad Sci U S A 111(9):3239–3244. [https://doi.org/10.1073/pnas.1222474110](https://doi.org/10.1073/pnas.1222474110)

40. Emberson LD, Pleijel H, Ainsworth EA, van den Berg M, Ren W, Osborne S, Mills G et al (2018) Ozone effects on crops and consideration in crop models. Eur J Agron. [https://doi.org/10.1016/J.EJA.2018.06.002](https://doi.org/10.1016/J.EJA.2018.06.002)

41. Famiglietti JS, Lo M, Ho SL, Bethune J, Anderson KJ, Syed TH, Swenson SC, de Linage CR, Rodell M (2011) Satellites measure recent rates of groundwater depletion in California’s central valley. Geophys Res Lett 38:L03403. [https://doi.org/10.1029/2010GL046442](https://doi.org/10.1029/2010GL046442)

42. Famiglietti JS, Cazenave A, Eicker A, Reager JT, Rodell M, Velicogna I (2015) Satellites provide the big picture. Science 349:684–685. [https://doi.org/10.1126/science.aac9238](https://doi.org/10.1126/science.aac9238)

43. FAO, IFAD, UNICEF, WFP and WHO (2018) The State of Food Security and Nutrition in the World, 2018. Building climate resilience for food security and nutrition. Rome, FAO

44. Feng W, Zhong M, Lemoine JM, Biancale R, Hsu HT, Xia J (2013) Evaluation of groundwater depletion in North China using the Gravity Recovery and Climate Experiment (GRACE) data and ground-based measurements. Water Resour Res 49(4):2110–2118

45. Fichot CG, Downing BD, Bergamaschi BA, Windham-Myers L, Marvin-DiPasquale M, Thompson DR, Gierach MM (2016) High-resolution remote sensing of water quality in the San Francisco Bay–Delta Estuary. Environ Sci Technol 50(2):573–583. [https://doi.org/10.1021/acs.est.5b03518](https://doi.org/10.1021/acs.est.5b03518)

46. Fisher JB (2013) Land-atmosphere interactions: evapotranspiration. In: Njoku E (ed) Encyclopedia of remote sensing. Springer, Berlin, pp 1–5

47. Fisher JB, Melton F, Middleton E, Hain C, Anderson M, Allen R, McCabe MF et al (2017) The future of evapotranspiration: global requirements for ecosystem functioning, carbon and climate feedbacks, agricultural management, and water resources. Water Resour Res 53(4):2618–2626

48. Fleisher DH, Condori B, Quiroz R, Alva A, Asseng S, Barreda C, Bindi M et al (2017) A potato model intercomparison across varying climates and productivity levels. Glob Chang Biol 23(3). [https://doi.org/10.1111/gcb.13411](https://doi.org/10.1111/gcb.13411)

49. Franz BA, Bailey SW, Kuring N, Werdell PJ (2015) Ocean color measurements with the Operational Land Imager on Landsat-8: implementation and evaluation in SeaDAS. J Appl Remote Sens 9(1):096070

50. Gelaro R, McCarty W, Suárez MJ, Todling R, Molod A, Takacs L, Randles CA et al (2017) The modern-era retrospective analysis for research and applications, version 2 (MERRA-2). J Clim 30(14): 5419–5454. [https://doi.org/10.1175/JCLI-D-16-0758.1](https://doi.org/10.1175/JCLI-D-16-0758.1)

51. Gilroy DJ, Kauffman KW, Hall RA, Huang X, Chu FS (2000) Assessing potential health risks from microcystin toxins in blue-green algae dietary supplements. Environ Health Perspect 108: 435–439

52. Grogan DS, Wisser D, Proussevitch AA, Lammers RB, Frolking SE (2016) Meltwater contributions to irrigation in high mountain Asia under a changing climate. In AGU Fall Meeting Abstracts

53. Guan K, Wu J, Kimball JS, Anderson MC, Frolking S, Li B, Hain CR, Lobell DB (2017) The shared and unique values of optical, fluorescence, thermal and microwave satellite data for estimating large-scale crop yields. Remote Sens Environ 1999:333–349

54. Hestir EL, Brando VE, Bresciani M, Giardino C, Matta E, Villa P, Dekker AG (2015) Measuring freshwater aquatic ecosystems: the need for a hyperspectral global mapping satellite mission. Remote Sens Environ 167:181–195. [https://doi.org/10.1016/j.rse.2015.05.023](https://doi.org/10.1016/j.rse.2015.05.023)

55. Houborg R, Rodell M, Li B, Reichle R, Zaitchik B (2012) Drought indicators based on model assimilated GRACE terrestrial water storage observations. Water Resour Res 48:W07525. [https://doi.org/10.1029/2011WR011291](https://doi.org/10.1029/2011WR011291)

56. Howitt R, MacEwan D, Medellín-Azuara J, Lund JR, Sumner D (2014) Economic analysis of the 2015 drought for California agriculture. Center for Watershed Sciences, University of California, Davis, CA

57. Ibrahim Y et al (2015) Land degradation assessment using residual trend analysis of GIMMS NDVI3g, soil moisture and rainfall in

Springer logo


---



36

Remote Sens Earth Syst Sci (2019) 2:18–38

sub-Saharan West Africa from 1982 to 2012. Remote Sens 7: 5471–5494

58. IOCCG (2018) Earth observations in support of global water quality monitoring. In: Greb S, Dekker A, Binding C (eds) IOCCG Report Series, No. 17. International Ocean Colour Coordinating Group, Dartmouth

59. Jiménez C, Prigent C, Mueller B, Seneviratne SI, McCabe MF, Wood EF, Rossow WB, Balsamo G, Betts AK, Dirmeyer PA (2011, 1984–2012) Global intercomparison of 12 land surface heat flux estimates. J Geophys Res Atmos 116(D2). [https://doi.org/10.1029/2010JD014545](https://doi.org/10.1029/2010JD014545)

60. Joiner J et al (2011) First observations of global and seasonal terrestrial chlorophyll fluorescence from space. Biogeosciences 8:637–651

61. Jones JW, Antle JM, Basso B, Boote KJ, Conant RT, Foster I, Charles H, Godfray J et al (2017) Toward a new generation of agricultural system data, models, and knowledge products: state of agricultural systems science. Agric Syst 155(July):269–288. [https://doi.org/10.1016/J.AGSY.2016.09.021](https://doi.org/10.1016/J.AGSY.2016.09.021)

62. Jung M, Reichstein M, Margolis HA, Cescatti A, Richardson AD, Arain MA, Arneth A, Bernhofer C, Bonal D, Chen J (2011) Global patterns of land atmosphere fluxes of carbon dioxide, latent heat, and sensible heat derived from eddy covariance, satellite, and meteorological observations. J Geophys Res Biogeosci 116. [https://doi.org/10.1029/2010JG001566](https://doi.org/10.1029/2010JG001566)

63. Kustas WP, Anderson MC, Alfieri JG, Knipper K, Torres-Rua A, Parry C, Hieto H, Agam N, White A, Gao F, McKee L, Prueger J, Hipps L, Los S, Alsina M, Sanchez L, Sams B, Dokoozlian N, McKee M, Jones S, Yang Y, Wilson T, Lei F, McElrone A, Heitman J, Howard A, Post K, Melton F, Hain C (2018) The grape remote sensing atmospheric profile and evapotranspiration eXperiment (GRAPEX). Bull Am Meteor Soc. [https://doi.org/10.1175/BAMS-D-16-0244.1](https://doi.org/10.1175/BAMS-D-16-0244.1)

64. Kustas WP, Norman JM (1999) Evaluation of soil and vegetation heat flux predictions using a simple two-source model with radiometric temperatures for partial canopy cover. Agric For Meteorol 94(1):13–29

65. Lei F, Crow WT, Holmes TRH, Hain C, Anderson MC (2018) Global investigation of soil moisture and latent heat flux coupling strength. Water Resour Res

66. Leue C, Wenig M, Wagner T, Klimm O, Platt U, Jahne B (2001) Quantitative analysis of NOₓ emissions from GOME satellite image sequences. J Geophys Res 106:5493–5505

67. Li B, Rodell M, Kumar SV, Beaudoing HK, Getirana A, Zaitchik BF, Goncalves LG, Ferreira C, Bhanja S, Mukherjee A et al (2018) Global GRACE data assimilation for groundwater and drought monitoring: advances and challenges. Water Resour Res in review

68. Li J, Roy DP (2017) A global analysis of sentinel-2A, sentinel-2B and Landsat-8 data revisit intervals and implications for terrestrial monitoring. Remote Sens 9:902. [https://doi.org/10.3390/rs9090902](https://doi.org/10.3390/rs9090902)

69. Li T, Hasegawa T, Yin X, Zhu Y, Boote K, Adam M, Bregaglio S et al (2015) Uncertainties in predicting rice yield by current crop models under a wide range of climatic conditions. Glob Chang Biol 21(3):1328–1341. [https://doi.org/10.1111/gcb.12758](https://doi.org/10.1111/gcb.12758)

70. Mankin JS, Viviroli D, Singh D, Hoekstra AY, Diffenbaugh NS (2015) The potential for snow to supply human water demand in the present and future. Environ Res Lett 10(11):114016. [https://doi.org/10.1088/1748-9326/10/11/114016](https://doi.org/10.1088/1748-9326/10/11/114016)

71. Mannino A, Signorini SR, Novak MG, Wilkin J, Friedrichs MAM, Najjar RG (2016) Dissolved organic carbon fluxes in the Middle Atlantic Bight: an integrated approach based on satellite data and ocean model products. J Geophys Res Biogeosci 121: 312–336. [https://doi.org/10.1002/2015JG003031](https://doi.org/10.1002/2015JG003031)

72. Martre P, Wallach D, Asseng S, Ewert F, Jones JW, Rötter RP, Boote KJ et al (2015) Multimodel ensembles of wheat growth: 

 many models are better than one. Glob Chang Biol 21(2). [https://doi.org/10.1111/gcb.12768](https://doi.org/10.1111/gcb.12768)

73. McClain C (2009) A decade of satellite ocean color observations. Annu Rev Mar Sci 1:13–42

74. McNally A, et al. (2015) Land surface modeling applications for famine early warning. In: AGU Fall Meeting Abstracts

75. McNally A, Arsenault K, Kumar S, Shukla S, Peterson P, Wang S, Funk C, Peters-Lidard CD, Verdin JP (2017) A land data assimilation system for sub-Saharan Africa food and water security applications. Sci Data 4:170012

76. McNally A, McCartney S, Ruane AC, Mladenova IE, Whitcraft AK, Becker-Reshef I, Bolten JD, Peters-Lidard CD, Rosenzweig C, Schollaert Uz S (In review) Hydrologic and Agricultural Earth Observations and Modeling for the Water-Food Nexus. Front Environ Sci

77. Miller MA, Kudela RM, Mekebri A, Crane D, Oates SC, Tinker MT, Staedler M, Miller WA, Toy-Choutka S, Dominik C, Hardin D, Langlois G, Murray M, Ward K, Jessup DA (2010) Evidence for a novel marine harmful algal bloom: cyanotoxin (microcystin) transfer from land to sea otters. PLoS One 5(9):e12576. [https://doi.org/10.1371/journal.pone.0012576](https://doi.org/10.1371/journal.pone.0012576)

78. Miralles DG, van den Berg MJ, Gash JH, Parinussa RM, de Jeu RAM, Beck HE, Holmes TRH, Jiménez C, Verhoest NEC, Dorigo WA, Teuling AJ, Johannes Dolman A (2014) El Niño–La Niña cycle and recent trends in continental evaporation. Nat Clim Chang 4(2):122–126

79. Mladenova IE, Bolten JD, Crow WT et al (2017) Intercomparison of soil moisture, evaporative stress, and vegetation indices for estimating corn and soybean yields over the U.S. IEEE J Select Top Appl Earth Observ Remote Sens 10(4):1328–1343. [https://doi.org/10.1109/jstars.2016.2639338](https://doi.org/10.1109/jstars.2016.2639338)

80. Mouw CB et al (2015) Aquatic color radiometry remote sensing of coastal and inland waters: challenges and recommendations for future satellite missions. Remote Sens Environ 160:15–30. issn: 0034-4257. [https://doi.org/10.1016/j.rse.2015.02.001](https://doi.org/10.1016/j.rse.2015.02.001)

81. Mueller B, Hirschi M, Jimenez C, Ciais P, Dirmeyer PA, Dolman AJ, Fisher JB, Jung M, Ludwig F, Maignan F et al (2013) Benchmark products for land evapotranspiration: LandFlux-EVAL multi-data set synthesis. Hydrol Earth Syst Sci. [https://doi.org/10.5194/hess-17-3707-2013](https://doi.org/10.5194/hess-17-3707-2013)

82. Müller C, Elliott J, Chryssanthacopoulos J, Arneth A, Balkovic J, Ciais P, Deryng D et al (2017) Global gridded crop model evaluation: benchmarking, skills, deficiencies and implications. Geosci Model Dev 10(4). [https://doi.org/10.5194/gmd-10-1403-2017](https://doi.org/10.5194/gmd-10-1403-2017)

83. Muller-Karger F (1992) Remote sensing of marine pollution: A challenge for the 1990s. Mar Pollut Bull 25:56–60

84. Norman JM, Kustas WP, Humes KS (1995) Source approach for estimating soil and vegetation energy fluxes in observations of directional radiometric surface temperature. Agric For Meteorol 77(3–4):263–293. [https://doi.org/10.1016/0168-1923(95)02265-Y](https://doi.org/10.1016/0168-1923(95)02265-Y)02265-Y)

85. O’Neill BC, Kriegler E, Riahi K, Ebi KL, Hallegatte S, Carter TR, Mathur R, van Vuuren DP (2014) A new scenario framework for climate change research: the concept of shared socioeconomic pathways. Clim Chang 122(3):387–400. [https://doi.org/10.1007/s10584-013-0905-2](https://doi.org/10.1007/s10584-013-0905-2)

86. Otkin JA, Anderson MC, Hain C, Svoboda M, Johnson D, Mueller R, Tadesse T, Wardlow B, Brown J (2016) Assessing the evolution of soil moisture and vegetation conditions during the 2012 United States flash drought. Agric For Meteorol 218: 230–242

87. Paerl H, Huisman J (2008) Blooms like it hot. Science 320(5872): 57–58. [https://doi.org/10.1126/science.1155398](https://doi.org/10.1126/science.1155398)

88. Pahlevan N, Lee Z, Wei J, Schaaf CB, Schott JR, Berk A (2014) On-orbit radio-metric characterization of OLI (Landsat-8) for applications in aquatic remote sensing. Remote Sens Environ 154: 272–284. [https://doi.org/10.1016/j.rse.2014.08.001](https://doi.org/10.1016/j.rse.2014.08.001)

Springer logo


---



Remote Sens Earth Syst Sci (2019) 2:18–38

37

89. Pahlevan N, Balasubramanian SV, Sarkar S, Franz BA (2018) Toward long-term aquatic science products from heritage Landsat missions. Remote Sens 10:1337. [https://doi.org/10.3390/rs10091337](https://doi.org/10.3390/rs10091337)

90. Pozzi W, Sheffield J, Stefanski R, Cripe D, Pulwarty R, Vogt JV, Heim RR Jr, Brewer MJ, Svoboda M, Westerhoff R, Van Dijk AI (2013) Toward global drought early warning capability: expanding international cooperation for the development of a framework for monitoring and forecasting. Bull Am Meteorol Soc 94(6):776–785

91. Preisendorfer RW (1986) Secchi disk science: visual optics of natural waters. Limnol Oceanogr 31(5):909–926

92. Richey AS, Thomas BF, Lo M-H, Famiglietti JS, Reager JT, Voss K, Swenson S, Rodell M (2015) Quantifying renewable groundwater stress with GRACE. Water Resour Res 51:5217–5238. [https://doi.org/10.1002/2015WR017349](https://doi.org/10.1002/2015WR017349)

93. Rodell M, Velicogna I, Famiglietti JS (2009) Satellite-based estimates of groundwater depletion in India. Nature 460:999–1002. [https://doi.org/10.1038/nature08238](https://doi.org/10.1038/nature08238)

94. Rodell M, Famiglietti JS, Wiese DN, Reager JT, Beaudoing HK, Landerer FW, Lo M-H (2018) Emerging trends in global freshwater availability. Nature 557:651–659. [https://doi.org/10.1038/s41586-018-0123-1](https://doi.org/10.1038/s41586-018-0123-1)

95. Rogers E, Deaven DG, Dimego GS (1995) The regional analysis system for the operational "early" Eta model: original 80-km configuration and recent changes. Weather Forecast 10(4):810–825

96. Rosenzweig C, Tubiello FN (2007) Adaptation and mitigation strategies in agriculture: an analysis of potential synergies. Mitig Adapt Strateg Glob Chang 12(5):855–873. [https://doi.org/10.1007/s11027-007-9103-8](https://doi.org/10.1007/s11027-007-9103-8)

97. Rosenzweig C, Jones JW, Hatfield JL, Ruane AC, Boote KJ, Thorburn P, Antle JM et al (2013) The agricultural model intercomparison and improvement project (AgMIP): protocols and pilot studies. Agric For Meteorol 170(March):166–182. [https://doi.org/10.1016/J.AGRFORMET.2012.09.011](https://doi.org/10.1016/J.AGRFORMET.2012.09.011)

98. Rosenzweig C, Elliott J, Deryng D, Ruane AC et al (2014) Assessing agricultural risks of climate change in the 21st century in a global gridded crop model intercomparison. Proc Natl Acad Sci U S A 111(9):3268–3273. [https://doi.org/10.1073/pnas.1222463110](https://doi.org/10.1073/pnas.1222463110)

99. Rosenzweig C, Antle J, Elliott J (2016) Assessing impacts of climate change on food security worldwide. Eos 97 [https://doi.org/10.1029/2016EO047387](https://doi.org/10.1029/2016EO047387)

100. Rosenzweig C, Ruane AC, Antle J, Elliott J, Ashfaq M, Chatta AA, Ewert F et al (2018) Coordinating AgMIP data and models across global and regional scales for 1.5°C and 2.0°C assessments. Philos Trans R Soc A Math Phys Eng Sci 376(2119). [https://doi.org/10.1098/rsta.2016.0455](https://doi.org/10.1098/rsta.2016.0455)

101. Ruane AC, Goldberg R, Chryssanthacopoulos J (2015a) Climate forcing datasets for agricultural modeling: merged products for gap-filling and historical climate series estimation. Agric For Meteorol 200(January):233–248. [https://doi.org/10.1016/J.AGRFORMET.2014.09.016](https://doi.org/10.1016/J.AGRFORMET.2014.09.016)

102. Ruane AC, Winter JM, McDermid SP, Hudson NI (2015b) AgMIP climate data and scenarios for integrated assessment, pp 45–78. [https://doi.org/10.1142/9781783265640_0003](https://doi.org/10.1142/9781783265640_0003)

103. Ruane AC, Rosenzweig C, Asseng S, Boote KJ, Elliott J, Ewert F, Jones JW et al (2017) An AgMIP framework for improved agricultural representation in integrated assessment models. Environ Res Lett 12(12):125003. [https://doi.org/10.1088/1748-9326/aa8da6](https://doi.org/10.1088/1748-9326/aa8da6)

104. Ruane AC, Antle J, Elliott J, Folberth C, Hoogenboom G, Mason-D'Croz D, Müller C et al (2018) AgMIP coordinated global and regional assessments of biophysical and economic implications of +1.5 and +2.0°C global warming on agriculture. Clim Res. [https://doi.org/10.3354/cr01520](https://doi.org/10.3354/cr01520)

105. Sazib N, Mladenova I, Bolten J (2018) Leveraging the Google Earth Engine for Drought Assessment Using Global Soil Moisture Data. Remote Sens 10(8):1265

106. Schaeffer B, Hagy J, Stumpf R (2013) An approach to developing numeric water quality criteria for coastal waters: a transition from SeaWiFS to MODIS and MERIS satellites. J Appl Remote Sens 7: 073544

107. Schiferl LD, Heald CL (2018) Particulate matter air pollution may offset ozone damage to global crop production. Atmos Chem Phys 18(8):5953–5966

108. Schmidt GA et al (2014) Configuration and assessment of the GISS ModelE2 contributions to the CMIP5 archive. J Adv Model Earth Syst 6(1):141–184. [https://doi.org/10.1002/2013MS000265](https://doi.org/10.1002/2013MS000265)

109. Schollaert Uz S, Turner W, Werdell PJ, Mannino A, Tzortziou M, Wilson C (In review) Developing a community of practice for applied uses of future PACE data to address food security challenges. Front Earth Sci

110. Senay GB, Friedrichs M, Singh RK, Velpuri NM (2016) Evaluating Landsat 8 evapotranspiration for water use mapping in the Colorado River Basin. Remote Sens Environ 185:171–185

111. Sheffield J, Wood EF, Chaney N, Guan K, Sadri S, Yuan X, Olang L, Amani A, Ali A, Demuth S, Ogallo L (2014) A drought monitoring and forecasting system for sub-Sahara African water resources and food security. Bull Am Meteorol Soc 95(6):861–882

112. Shephard MW, Cady-Pereira KE (2015) Cross-track infrared sounder (CrIS) satellite observations of tropospheric ammonia. Atmos Meas Tech 8(3):1323–1336. [https://doi.org/10.5194/amt-8-1323-2015](https://doi.org/10.5194/amt-8-1323-2015)

113. Singels A, Jones M, Marin F, Ruane A, Thorburn P (2014) Predicting climate change impacts on sugarcane production at sites in Australia, Brazil and South Africa using the Canegro model. Sugar Tech 16(4). [https://doi.org/10.1007/s12355-013-0274-1](https://doi.org/10.1007/s12355-013-0274-1)

114. Snyder J, Boss E, Weatherbee R, Thomas AC, Brady D, Newell C (2017) Oyster aquaculture site selection using landsat 8-derived sea surface temperature, turbidity, and chlorophyll a. Front Mar Sci 4:190 [https://doi.org/10.3389/fmars.2017.00190](https://doi.org/10.3389/fmars.2017.00190)

115. Stumpf R, Wynne T, Baker D, Fahnenstiel G (2012) Interannual variability of cyanobacterial blooms in Lake Erie. PLoS ONE 7(8):e42444

116. Stumpf R, et al. (2016) Challenges for mapping cyanotoxin patterns from remote sensing of cyanobacteria. Harmful Algae 54: 160–173

117. Su Z (2002) The surface energy balance system (SEBS) for estimation of turbulent heat fluxes. Hydrol Earth Syst Sci 6(1):85–100

118. Sultan M, Ahmed M, Wahr J, Yan E, Emil M (2014) Monitoring aquifer depletion from space: cases studies from the Saharan and Arabian aquifers. In: Lakshmi V et al (eds) Remote Sensing of the Terrestrial Water Cycle. John Wiley & Sons, Inc, Hoboken, NJ, pp 349–366

119. Tapley BD, Bettadpur S, Ries JC, Thompson PF, Watkins MM (2004) GRACE measurements of mass variability in the Earth system. Science 305(5683):503–505

120. Tiwari VM, Wahr J, Swenson S (2009) Dwindling groundwater resources in northern India, from satellite gravity observations. Geophys Res Lett 36(18)

121. Thrasher B, Maurer EP, McKellar C, Duffy PB (2012) Technical note: bias correcting climate model simulated daily temperature extremes with quantile mapping. Hydrol Earth Syst Sci 16(9): 3309–3314. [https://doi.org/10.5194/hess-16-3309-2012](https://doi.org/10.5194/hess-16-3309-2012)

122. Tucker CJ (1979) Red and photographic infrared linear combinations for monitoring vegetation. Remote Sens Environ 8:127–150

123. Tucker C and Pinzon J (2017) Using spectral vegetation indices to measure gross primary productivity as an indicator of land degradation. GEF-Land Degradation Monitoring Project, Report One. 70 p

Springer logo


---



38

Remote Sens Earth Syst Sci (2019) 2:18–38

124. UNESCO (2006) Water, a shared responsibility. The United Nations World Water Development Report 2. UNESCO (Paris, France) and Berghahn Books (New York, USA)

125. UNESCO (2012) A Framework for Ocean Observing. By the Task Team for an Integrated Framework for Sustained Ocean Observing, UNESCO 2012, IOC/INF-1284 rev. [https://doi.org/10.5270/OceanObs09-FOO](https://doi.org/10.5270/OceanObs09-FOO)

126. UNISDR (2015) Sendai Framework for Disaster Risk Reduction 2015–2030. [https://www.unisdr.org/files/43291_sendaiframeworkfordrren.pdf](https://www.unisdr.org/files/43291_sendaiframeworkfordrren.pdf). Accessed 15 Oct 2018

127. United States Department of Agriculture (USDA) (2018) World Agricultural Production. Circular Series, WAP 9–18, September 2018. Foreign Agricultural Service, United States Department of Agriculture, 32 p

128. Urquhart EA, Schaeffer BA, Stumpf RP, Loftin KA, Werdell PJ (2017) A method for examining temporal changes in cyanobacterial harmful algal bloom spatial extent using satellite remote sensing. Harmful Algae 67(144–152):1568–9883. [https://doi.org/10.1016/j.hal.2017.06.001](https://doi.org/10.1016/j.hal.2017.06.001)

129. Valdivia RO, Antle JM, Rosenzweig C, Ruane AC, Vervoort J, Ashfaq M, Hathie I et al (2015) Representative Agricultural Pathways and Scenarios for Regional Integrated Assessment of Climate Change Impacts, Vulnerability, and Adaptation, pp 101–145. [https://doi.org/10.1142/9781783265640_0005](https://doi.org/10.1142/9781783265640_0005)

130. Van Dingenen R, Dentener FJ, Raes F, Krol MC, Emberson L, Cofala J (2009) The global impact of ozone on agricultural crop yields under current and future air quality legislation. Atmos Environ 43(3):604–618

131. Veefkind JP, Aben I, McMullan K, Förster H, de Vries J, Otter G, Claas J, Eskes HJ, de Haan JF, Kleipool Q, van Weele M, Hasekamp O, Hoogeveen R, Landgraf J, Snel R, Tol P, Ingmann P, Voors R, Kruizinga B, Vink R, Visser H, Levelt PF (2012) TROPOMI on the ESA Sentinel-5 Precursor: A GMES mission for global observations of the atmospheric composition for climate, air quality and ozone layer applications. Remote Sens Environ 120:70–83. [https://doi.org/10.1016/j.rse.2011.09.027](https://doi.org/10.1016/j.rse.2011.09.027)

132. Velders GJM, Granier C, Portmann RW, Pfeilsticker K, Wenig M, Wagner T, Platt U, Richter A, Burrows JP (2001) Global tropospheric NO₂ column distributions: comparing 3-D model calculations with GOME measurements. J Geophys Res 106:12, 643–12,660

133. Voss KA, Famiglietti JS, Lo M, de Linage C, Rodell M, Swenson SC (2013) Groundwater depletion in the Middle East from GRACE with implications for transboundary water management in the Tigris-Euphrates-Western Iran region. Water Resour Res. [https://doi.org/10.1002/wrcr.20078](https://doi.org/10.1002/wrcr.20078)

134. Wallach D, Mearns LO, Rivington M, Antle JM, Ruane AC (2015) Uncertainty in agricultural impact assessment, pp 223–259. [https://doi.org/10.1142/9781783265640_0009](https://doi.org/10.1142/9781783265640_0009)

135. Warner JX, Wei Z, Strow LL, Dickerson RR, Nowak JB (2016) The global tropospheric ammonia distribution as seen in the 13-year AIRS measurement record. Atmos Chem Phys 16:5467–5479. [https://doi.org/10.5194/acp-16-5467-2016](https://doi.org/10.5194/acp-16-5467-2016)

136. Wiebe K, Lotze-Campen H, Sands R, Tabeau A, van der Mensbrugghe D, Biewald A, Bodirsky B et al (2015) Climate change impacts on agriculture in 2050 under a range of plausible socioeconomic and emissions scenarios. Environ Res Lett 10(8): 085010. [https://doi.org/10.1088/1748-9326/10/8/085010](https://doi.org/10.1088/1748-9326/10/8/085010)

137. Xia Y, Mitchell K, Ek M, Sheffield J, Cosgrove B, Wood E, Luo L, Alonge C, Wei H, Meng J, Livneh B (2012a) Continental-scale water and energy flux analysis and validation for the North American Land Data Assimilation System project phase 2 (NLDAS-2): 1. Intercomparison and application of model products. J Geophys Res Atmos 117(D3)

138. Xia Y, Mitchell K, Ek M, Cosgrove B, Sheffield J, Luo L, Alonge C, Wei H, Meng J, Livneh B, Duan Q (2012b) Continental-scale water and energy flux analysis and validation for North American Land Data Assimilation System project phase 2 (NLDAS-2): 2. Validation of model-simulated streamflow. J Geophys Res Atmos 117(D3)

139. Zaitchik BF, Rodell M, Reichle RH (2008) Assimilation of GRACE terrestrial water storage data into a land surface model: Results for the Mississippi River basin. J Hydrometeorol 9(3): 535–548

140. Zhao M, Running SW (2010) Drought-induced reduction in global terrestrial net primary production from 2000 through 2009. Science 329:940–943

Springer logo
