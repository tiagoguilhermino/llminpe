

Atmospheric Research 218 (2019) 231–244

Elsevier logo

Contents lists available at ScienceDirect

# Atmospheric Research

journal homepage: www.elsevier.com/locate/atmosres

Atmospheric Research journal cover thumbnail

# Grid box-level evaluation of IMERG over Brazil at various space and time scales

Check for updates icon

André N. Gadelha<sup>a,⁎</sup>, Victor Hugo R. Coelho<sup>a,⁎</sup>, Alexandre C. Xavier<sup>b</sup>, Luís Romero Barbosa<sup>c,a</sup>, Davi C.D. Melo<sup>d,e</sup>, Yunqing Xuan<sup>f</sup>, George J. Huffman<sup>g</sup>, Walt A. Petersen<sup>h</sup>, Cristiano das N. Almeida<sup>a</sup>

<sup>a</sup> *Department of Civil and Environmental Engineering, Federal University of Paraíba, João Pessoa, PB 58051-900, Brazil*

<sup>b</sup> *Department of Rural Engineering, Federal University of Espírito Santo, Alegre, ES 29500-000, Brazil*

<sup>c</sup> *Institute of Environmental Science and Geography, University of Potsdam, Potsdam, BB 14476, Germany*

<sup>d</sup> *Department of Soils and Rural Engineering, Federal University of Paraíba, Areia, PB 58397-000, Brazil*

<sup>e</sup> *Department Hydraulics and Sanitary Engineering, University of São Paulo, São Carlos, SP 13566-590, Brazil*

<sup>f</sup> *College of Engineering, Swansea University, Swansea, SA1 8EN, UK*

<sup>g</sup> *NASA Goddard Space Flight Center, Greenbelt, MD 20771, USA*

<sup>h</sup> *NASA Marshall Space Flight Center, Huntsville, AL 35805, USA*

## ARTICLE INFO

## ABSTRACT

*Keywords:*
Gridded rainfall
Global precipitation measurement
Final run
Performance

Rainfall data from the Global Precipitation Measurement (GPM) mission provide a new source of information with high spatiotemporal resolution that overcomes the limitations of ground-based rainfall information worldwide. This study evaluates the performance of the Integrated multi-satellitE Retrievals for GPM (IMERG) Final Run product over Brazil by means of multi-temporal and -spatial analyses. The assessment of the IMERG Final Run product is based on six statistics obtained for the period between January–December 2016 (daily, monthly, and annual basis). The analysis consisted of comparing the satellite-based estimates against a ground-based gridded rainfall product created using daily records from 4911 rain gauges distributed throughout Brazil. Overall, the results show that the IMERG product can effectively capture the spatial patterns of rainfall across Brazil. However, the IMERG product presents a slight tendency in overestimating the ground-based rainfall at all timescales. Furthermore, the performance of the satellite product varies throughout the region. The higher errors and biases are found in the North and Central-West regions, but the low density of rain gauges in those regions can be a source of large deviations between IMERG estimates and observations. A large underestimation of the IMERG data is evident along the coastal zone of the North-east region, probably due to the inability of the passive microwave and infrared sensors to detect warm-rain processes over land. This study shows that the IMERG product can be a good source of rainfall data to complement the ground precipitation measurements in most of Brazil, although some uncertainties are found and need to be further studied

## 1. Introduction

Rainfall plays an important role in the water balance, as it is the main input into the hydrological system (Kidd and Huffman, 2011; Mahmoud et al., 2018; Schneider et al., 2016). Given its spatial and temporal variability, dense daily or sub-daily observations are required to understand specific hydrological processes (Kann et al., 2015; Kidd et al., 2017; McMillan et al., 2011; Meng et al., 2014). However, obtaining a consistent and continuous ground-based rainfall dataset with

an adequate spatiotemporal resolution for such purposes remains a challenge worldwide, mainly because of the costs of operation and maintenance of the rain gauge monitoring network (Terink et al., 2018). Currently, the ground-based rainfall monitoring network in Brazil has approximately 11,820 rain gauges, resulting in an average density of one gauge per 720 km², which is below the threshold of one gauge per 575 km² recommended by the World Meteorological Organization (WMO) for the interior plane and undulating areas (WMO, 1994). However, the gauges are non-uniformly distributed with some

<sup>⁎</sup> Corresponding authors.

*E-mail addresses:* andregadelha5@hotmail.com (A.N. Gadelha), victor-coelho@hotmail.com (V.H.R. Coelho), alexandre.xavier@ufes.br (A.C. Xavier), luisromero.eng@gmail.com (L.R. Barbosa), melo.dcd@gmail.com (D.C.D. Melo), y.xuan@swansea.ac.uk (Y. Xuan), george.j.huffman@nasa.gov (G.J. Huffman), walt.petersen@nasa.gov (W.A. Petersen), almeida74br@yahoo.com.br (C.d.N. Almeida).

https://doi.org/10.1016/j.atmosres.2018.12.001

Received 25 August 2018; Received in revised form 26 October 2018; Accepted 3 December 2018
Available online 12 December 2018

0169-8095/ Crown Copyright © 2018 Published by Elsevier B.V. All rights reserved.


---



A.N. Gadelha et al.

Atmospheric Research 218 (2019) 231–244

Table 1

Summary of relevant studies that evaluated the IMERG products at country-wide scale in relation to the proposed study.

<table>
  <thead>
    <tr>
        <th>Study</th>
        <th>IMERG products</th>
        <th>Location/study area</th>
        <th>Study period</th>
        <th>Number of gauges</th>
        <th>Analysis approach</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>1. Tan and Duan (2017)</td>
<td>Final Run</td>
<td>Singapore/719.9 km²</td>
<td>1/Apr/2014 to 31/Jan/2016</td>
<td>48</td>
<td>Point-cell</td>
    </tr>
<tr>
        <td>2. Muhammad et al. (2018)</td>
<td>Late Run and Final Run</td>
<td>Pakistan/796.1 km²</td>
<td>1/Jan/2015 to 31/12/2016</td>
<td>36</td>
<td>Point-cell</td>
    </tr>
<tr>
        <td>3. Mahmoud et al. (2018)</td>
<td>Early Run, Late Run, and Final Run</td>
<td>Saudi Arabia/2.1 M km²</td>
<td>1/Oct/2015 to 30/Apr/2016</td>
<td>189</td>
<td>Point-cell</td>
    </tr>
<tr>
        <td>4. Tang et al. (2016)</td>
<td>Early Run, Late Run, and Final Run</td>
<td>China/9.3 M km²</td>
<td>1/Jun/2014 to 31/Dec/2014</td>
<td>2200</td>
<td>Grid box</td>
    </tr>
<tr>
        <td>5. Prakash et al. (2018)</td>
<td>Final Run</td>
<td>India/3.3 M km²</td>
<td>1/Jun/2014 to 31/Sep/2014</td>
<td>7000</td>
<td>Grid box</td>
    </tr>
<tr>
        <td>6. Tan and Santo (2018)</td>
<td>Early Run, Late Run, and Final Run</td>
<td>Malaysia/338 km²</td>
<td>12/Mar/2014 to 29/Feb/2016</td>
<td>501</td>
<td>Point-cell</td>
    </tr>
<tr>
        <td>7. Rozante et al. (2018)</td>
<td>Final Run</td>
<td>Brazil/8.5 M km²</td>
<td>1/Apr/2014 to 28/Feb/2017</td>
<td>3400</td>
<td>Point-cell</td>
    </tr>
<tr>
        <td>8. Asong et al. (2017)</td>
<td>Final Run</td>
<td>Southern Canada/6.1 M km²</td>
<td>12/Mar/2014 to 31/Jan/2016</td>
<td>732 and CaPA gridded product</td>
<td>Point-cell and grid box</td>
    </tr>
<tr>
        <td>9. This study</td>
<td>Final Run</td>
<td>Brazil/8.5 M km²</td>
<td>1/Jan/2016 to 31/Dec/2016</td>
<td>4911</td>
<td>Grid box</td>
    </tr>
  </tbody>
</table>

regions in Brazil, such as the Southeast, having densities much higher than the threshold, reaching one gauge per 115 km². Moreover, rain gauges with uninterrupted data in Brazil are few and the rainfall time series often contain temporal gaps. The lack of in-situ rainfall data is more acute in the Northern (which includes the Amazon rainforest) and Central regions of the country, leading to an insufficient characterisation of these regions (Buarque et al., 2011; Collischonn et al., 2008; Curtarelli et al., 2014; Delahaye et al., 2015).

Precipitation observations by alternative methods such as multiple satellite sensors have become a viable solution in the past few decades to overcome the limitations of ground-based data (Hobouchian et al., 2017; Levizzani et al., 2018; O and Kirstetter, 2018). Remotely sensed data can offer global information about precipitation with a range of required spatial and temporal resolutions. Furthermore, many remote sensing products related to rainfall are freely available for the end users (Mahmoud et al., 2018; Skofronick-Jackson et al., 2018; Tang et al., 2016a). One of the first dedicated and most important satellites for this purposes was the Tropical Rainfall Measuring Mission (TRMM), launched in 1997. It was a joint project between NASA (National Aeronautics and Space Administration) and JAXA (Japanese Aerospace Agency) to observe rainfall in the latitude band 50° North to 50° South (Huffman et al., 2007). TRMM provided products with a variety of spatial (0.25° to 5°) and temporal (3-hour to 1-month) resolutions. In the past few years, many studies used the TRMM Multi-satellite Precipitation Analysis (TMPA) for various purposes in Brazil such as hydrological modelling due to the low density and intermittency of rain gauges in some river basins (e.g. Coelho et al., 2017; Collischonn et al., 2008; De Paiva et al., 2013; Falck et al., 2015; Melo et al., 2016). Many other studies worldwide were also carried out using the TMPA products (including Baik and Choi, 2015; Fang et al., 2013; Naumann et al., 2012; Pombo and de Oliveira, 2015; Yang and Nesbitt, 2014). However, some studies highlighted the need to assess the accuracy of TMPA by comparison with ground-based data on a regional basis. For example, Melo et al. (2015) evaluated the TMPA products over Brazil using a 14-year time series for uncertainties in daily and monthly estimates.

Like TRMM, the Global Precipitation Measurement (GPM) mission is also a joint project led by NASA and JAXA; the GPM Core Observatory launched in February 2014. GPM is the successor to TRMM, providing rainfall and snow information globally as contained in the Integrated Multi-satellitE Retrievals for GPM (IMERG) products at 0.1° × 0.1° (spatial) and half-hour (temporal) resolutions (Hou et al., 2014; Liu et al., 2017; Skofronick-Jackson et al., 2017). The IMERG algorithm incorporates microwave and infrared estimates from the GPM constellation, gauge observations, and other ancillary (Huffman et al., 2017a). Currently, there are three IMERG products available, namely: Early Run, Late Run, and Final Run. The Early and Late Run are near-real-time products available from 4 to 12 h after the observation, both being more suitable for time-sensitive applications. On the other hand, the Final Run product is available 3.5 months after the observation, which allows it to incorporate a surface gauge analysis from the Global Precipitation Climatology Centre (GPCC) to improve the satellite estimations. As such, the Final Run is the most suitable product for hydrological modelling purposes (Tang et al., 2016b).

The GPM products open up new opportunities for hydrological investigations, particularly in ungauged areas (Asong et al., 2017). However, the performance of the GPM products needs to be critically evaluated in different regions of the world as sources of information for both end users and data producers (Prakash et al., 2018). Several recent studies evaluated different IMERG products in complex areas under distinct climatic and geographic aspects worldwide by using ground-based data and/or comparisons with other satellite products such as TMPA (Anjum et al., 2018; Asong et al., 2017; Beria et al., 2017; Dezfuli et al., 2017; Gebregiorgis et al., 2018; Hu et al., 2017; Khan et al., 2018; Lelis et al., 2018; Mahmoud et al., 2018; Mayor et al., 2017; Mitra et al., 2018; Muhammad et al., 2018; O and Kirstetter, 2018; Oliveira et al., 2018; Prakash et al., 2018, 2016; Satgé et al., 2017; Sungmin et al.,

232


---



A.N. Gadelha et al.

Atmospheric Research 218 (2019) 231–244

Maps of Brazil showing: (a) Rain gauge density and regions (N, NE, CW, SE, S); (b) Köppen's climate classification and selected subareas (1-5); (c) Annual rainfall for 2016 from rain gauges; (d) Annual rainfall for 2016 from IMERG-V05 Final Run.

Fig. 1. (a) Number and density of rain gauges used as a reference in the study. (b) Köppen's climate classification map for Brazil according to Alvares et al. (2013) and selected subareas. Spatial distributions of the annual rainfall (mm) for 2016 obtained from (c) rain gauges and (d) the IMERG-V05 Final Run product. The climatic symbols A, B, and C stand for Tropical, Dry, and Humid Subtropical, respectively.

2017; Tan et al., 2017; Tan and Duan, 2017; Tan and Santo, 2018; Tang et al., 2016b, Tang et al., 2016a; Wang et al., 2017; Zhang et al., 2018). Most of the aforementioned studies showed good agreement of the IMERG products with the gauge, radar, and TMPA data. However, other studies found the same or less accuracy for the IMERG products compared to those from TMPA (Satgé et al., 2017). Some studies mentioned

above were carried out at country-wide scale. Table 1 provides a tabular literature review which shows these relevant country-scale studies evaluating the performance of the IMERG products, including those done in Brazil. Countries such as Brazil, United States, Russia, Australia, Canada, and China encompass different climate zones and rainfall patterns due to their vast territories. Consequently, studies carried out

233


---



A.N. Gadelha et al.

Atmospheric Research 218 (2019) 231–244

in these countries may be able to provide more detailed and critical analyses of the IMERG products.

As IMERG products have only become available recently when compared to the TMPA products, the number of studies carried out in Brazil from local-to national-scales is still very small. To our knowledge, only four studies checked the quality of the IMERG products (e.g. Lelis et al., 2018; Oliveira et al., 2018; Oliveira et al., 2016; Rozante et al., 2018), which are significantly fewer than those that evaluated the TRMM products. For instance, Oliveira et al. (2016) used ground-based radar observations to evaluate the rainfall variations of the IMERG Final Run Version 04 product over an area of the Brazilian Amazon rainforest. They observed a satisfactory agreement between the ground-based and the satellite data during the period analysed (from March to September 2014), but IMERG Final Run overestimated the heavier rainfall rates during the wet season. Lelis et al. (2018) analysed the one-year performance of the IMERG product by using rain gauges data for the eastern region of São Paulo State, Brazil. They concluded that the IMERG product generally overestimated over this region. The only national-scale assessment was carried out by Rozante et al. (2018), using around 3400 rain gauges distributed over Brazil. They analysed whether the daily IMERG data can properly replace the daily TMPA data. However, they considered as a reference for the analyses of both products the coarse spatial resolution (0.25°) of the TMPA product. Moreover, they based their studies in a point-to-cell perspective, i.e. without a spatial analysis and considering only 1779 cells of the IMERG product among the > 70,000 available for the Brazilian territory. Clearly, the validation of satellite rainfall data based on a point-to-cell analysis has some limitations, as the gauge stations provide point measurements observed over a continuous period of time, whereas precipitation from satellite observation is an average within the grid cells (Cohen Liechti et al., 2012; Jesus et al., 2015; Toté et al., 2015; Zad et al., 2018). Consequently, the comparison suffers from scale mismatch issues and other validation methods are needed to improve the evaluation and overcome this problem (Guo and Liu, 2016). Interpolation approaches can be also used to transfer point-scale rainfall observations to areal estimates (Vicente-Serrano et al., 2003; Xavier et al., 2016). However, the interpolation methods employed to generate the grid box-level information also bring some uncertainties, with the quality of rainfall data probably affected in grid pixels without gauges (Tang et al., 2018).

Considering the limitations and gaps of the previous studies assessing the IMERG products in Brazil, our aim is to expand and complement the analyses of the IMERG Final Run product across the Brazilian territory, as follows: (1) using a grid box approach based on a gridded observed rainfall product, (2) analysing the spatial variability, and (3) encompassing other variables in the evaluation process such as climate, topography, and density of rain gauges used in the analyses. The IMERG product was compared with a large amount of daily ground-based measurements interpolated over a grid covering the country, with grid boxes matching the IMERG cells. This study addresses the following questions: (a) How does the quality of the IMERG product vary spatially? (b) Are the annual and monthly IMERG rainfall uncertainties smoother than daily estimates due to the averaging process? (c) What ancillary information have more influence on the performance of the IMERG product? In the end, this study intends to provide insights for further applications of the IMERG Final Run product in Brazil at daily, monthly, and annual scales.

# 2. Material and methods

## 2.1. Study area

This study was carried out for the whole Brazil, which covers approximately 8.5 M km<sup>2</sup> between the coordinates 5°16′N-33°45′S and 34°47′W-73°59′W (Fig. 1). Brazil is the largest country in Latin America and the fifth-largest country in the world in area. The Brazilian territory 

 has five official geographical regions, namely: North (N), North-east (NE), Central-west (CW), Southeast (SE), and South (S). Such delimitation has been used to evaluate satellite based rainfall data and report mean statistics per region (Franchito et al., 2009; Melo et al., 2015). Although different rainfall regimes within each geographical region can be identified (Reboita et al., 2010; Rozante et al., 2018), such delimitation is of practical importance (as they are managed by various local/states governments and widely used by stakeholders), hence it was adopted in this study. Region N, where the Amazon rainforest is located, is characterised by prevailing convective rainfall that can be higher than 2000 mm year<sup>-1</sup> and even reach 4000 mm year<sup>-1</sup> in some places (Alvares et al., 2013; Espinoza Villar et al., 2009). In contrast, most of region NE is characterised by a semi-arid climate in the inland area, with rainfall ranging from 380 to 700 mm year<sup>-1</sup> (Alvares et al., 2013). However, along the first 100 km of the Atlantic coastal zone of NE, the rainfall can be as high as 1500 mm year<sup>-1</sup> (Kousky, 1979). The annual rainfall variations are similar in both regions SE and CW, with values ranging from 1000 to 2000 mm and concentrated during the austral summer (Melo et al., 2015). On the other hand, the rainfall is more spatially uniform throughout the year in region S, ranging from 1200 to 2000 mm (Nery and Carfan, 2014). According to Alvares et al. (2013), Brazil has twelve different Koppen's climate types divided into three zones: Tropical (Zone A), Semiarid (Zone B), and Humid Subtropical (Zone C). The mean annual air temperature ranges from < 10 °C to > 26 °C. Besides Brazil as a whole, five different subareas with the same size (1.9° x 1.2°) were also selected to be individually evaluated in this study to check the quality of the IMERG data in small areas with high density of rain gauges (Fig. 1b). Each subarea is located in one of the five official geographical regions and represents different climate zones and/or annual average rainfall depths. Only subarea 2 is meridionally oriented in order to be confined to the Dry Zone and to cover as many rain gauges as possible. Fig. S1 shows the long-term monthly average rainfall obtained from rain gauges within the five selected subareas.

## 2.2. Rain gauge data

This study used daily rainfall data from 4911 rain gauges distributed over Brazil (Fig. 1). The ground-based data for 2016 were acquired from rain gauges that are operated by the Brazilian National Water Agency (ANA), Brazilian National Institute of Meteorology (INMET), and sixteen regional water agencies. The Angular Distance Weighting (ADW) and Inverse Distance Weighting (IDW) interpolation methods were first compared in order to choose the most appropriated to generate the gridded observed data. Then, a cross-validation was carried out to estimate the uncertainties of both methods (see the supplementary material). The ADW interpolation method presented the best results and was used to produce a daily gridded observed rainfall data matching the 0.1° x 0.1° IMERG grid (Hofstra and New, 2009; New et al., 2000; Xavier et al., 2016) (see Table S1). Following the recommendation by Xavier et al. (2016), the weighting means data from the five available surrounding stations were used when applying the ADW method to perform the point-to-grid conversion. The weights for each station were defined by two components: (1) the weight due to the distance from the grid point to the rain gauge, calculated by the correlation decay distance (CDD) and (2) the weight of each station due to its isolation. Detailed information of the interpolation method can be found in Xavier et al. (2016). The gauge data were quality checked for extreme daily values equal to or higher than 450 mm. The missing data throughout the year 2016 represents ~10% of the total dataset recorded in the rain gauges. Gauges with missing data for a specific day were excluded from the interpolation to generate the gridded rainfall product for that day. Hence, the number of rain gauges changed over the study period, ranging from 2975 to 3739 for each day. The daily data were then accumulated to produce the monthly and annual information.

234


---



A.N. Gadelha et al.

Atmospheric Research 218 (2019) 231–244

Table 2
Definition of rainy and non-rainy days for IMERG-V05 and observed data.

<table>
  <thead>
    <tr>
        <th> </th>
        <th> </th>
        <th colspan="2">Gauge</th>
    </tr>
<tr>
        <th> </th>
        <th> </th>
        <th>Rain</th>
        <th>No rain</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>IMERG-V05</td>
<td>Rain</td>
<td>A</td>
<td>B</td>
    </tr>
<tr>
        <td> </td>
<td>No rain</td>
<td>C</td>
<td>–</td>
    </tr>
  </tbody>
</table>

## 2.3. IMERG data

The IMERG dataset evaluated in this study is the Final Run product at the native 0.1° x 0.1° (spatial) and half-hour (temporal) resolution; Version 05 (V05) of the Goddard Profiling Algorithm (GPROF V05) provides precipitation estimates from all microwave sensors onboard the GPM constellation. The main changes between the oldest and newest versions of the IMERG products are summarised by Huffman et al. (2017b). For instance, the IMERG-V05 improved the gauge error estimates to provide proper weighting of monthly gauge and satellite-only estimates. Also, the IMERG-V05 product added the Quality Index for all half-hour and monthly products. The IMERG-V05 Final Run product also uses the GPCC analysis of global ground-based monthly data from the Global Telecommunication System (GTS) and other sources, which is composed of 7000 stations distributed around the world. This study compared gauge and satellite-based data independently by choosing ground-based stations not used by GTS. The comparisons between the IMERG-V05 and rain gauge datasets were performed in this study at daily, monthly, and annual scales. Therefore, we aggregated the 30-minute IMERG-V05 data to match the daily information of the ground-based data, which is collected at 9:00 a.m. local time. The IMERG-V05 data were then accumulated between 9:00 a.m. (local time) and the subsequent 24 h. Similar to the rain gauge data, the daily IMERG-V05 information was monthly and annually accumulated.

## 2.4. Evaluation procedures

Four evaluation procedures were performed to analyse the IMERG-V05 product over the Brazilian territory, so-called: (i) grid-scale, (ii) national-scale, (iii) subarea, and (iv) feature analysis. The grid-scale comparison was carried out using the observed rainfall dataset and the IMERG-V05 product to evaluate the spatial behaviour of the satellite data. The national-scale analysis was performed to asses the satellite product over large areas comparing the national areal average of both ground-based and IMERG-V05 data. The subarea analysis consisted of computing the metrics of average values within each subarea defined in the study area section (see Fig. 1b). This analysis intends to assess how the IMERG-V05 performs in areas with a high density of gauges in each Brazilian region. The feature analysis was carried out to better understand the spatial daily agreement between IMERG-V05 and observed rainfall data, based on the influence of climate, topography, and gauge density. The comparisons between the IMERG-V05 and rain gauge datasets were performed in this study at daily, monthly, and annual scales.

## 2.5. Metrics

Six statistical metrics divided into three main groups were used to assess the quality of the IMERG-V05 product. Considering the temporal resolution of the rain gauge network, the threshold for all daily metric analyses was set to 0.1 mm. Thus, all IMERG-V05 and/or rain gauge data with daily values below 0.1 mm were treated as zero. However, for the monthly and annual analyses, this threshold was not applied because it is of no physical sense. The first group of metrics is related to comparison of detecting the observed rainfall events, including: (i) probability of detection (POD), which exhibits the fraction of rainfall events that the IMERG-V05 product detects and there are ground-based rainfall events; (ii) false alarm ratio (FAR), which gives the fraction of events estimated by IMERG-V05 which are not detected in the surface data; and (iii) critical success index (CSI), which combines the characteristics of false alarms and missed events:

$$ POD = \frac{a}{a + c} $$ (1)

$$ FAR = \frac{b}{a + b} $$ (2)

$$ CSI = \frac{a}{a + b + c} $$ (3)

where a is the rainfall observed by the rain gauge and IMERG-V05 simultaneously, b is the rainfall observed by the IMERG-V05 product but not observed by the rain gauge, and c is the rainfall observed by the rain gauges which was not observed by the satellite. Table 2 shows the definition of rainy and non-rainy days as well as each variable presented in Eqs. (1), (2), and (3). The desirable values of POD and CSI are close to one, while for FAR is near to zero.

The second group of metrics corresponds to the errors of the IMERG-V05 product estimation in comparison with the rain gauge data. It includes: (i) the mean error (ME), which represents the average magnitude of the satellite error, and (ii) the root mean square error (RMSE), which gives the sample standard deviation of the differences between the IMERG-V05 product and the observed rainfall:

$$ ME = \frac{1}{N} \sum_{n=1}^{1} (E_i - O_i) $$ (4)

$$ RMSE = \sqrt{\frac{1}{N} \sum_{i=1}^{n} (E_i - O_i)^2} $$ (5)

where O is the observed rainfall (mm), E is the IMERG-V05 estimated rainfall (mm), i is the index of the number of pairs, and n is the total number of compared pairs. Both ME and RMSE measure the accuracy of the IMERG-V05 product, so values close to zero indicate smaller errors. However, the ME gives an overall indicator of the bias (positive or negative), with the disadvantage that the positive and negative errors can cancel each other. Hence, sometimes a small ME does not means minor errors. The relative errors for both ME and RMSE metrics were also computed to improve the interpretation of data (see the supplementary material for more details).

The third group describes the agreement between IMERG-V05 estimates and ground-based data, which only includes the correlation coefficient (CC):

$$ CC = \frac{\frac{1}{n} \sum_{n+1}^{N} (O_i - \bar{O})(E_i - \bar{E})}{\sigma_O \sigma_E} $$ (6)

where $\bar{O}$ is the average observed rainfall values (mm), $\bar{E}$ is the average estimated rainfall values (mm), and $\sigma$ is the standard deviation (mm). The CC ranges from +1 to -1, with the extremes representing total positive and total negative linear correlation, respectively.

# 3. Results and discussion

## 3.1. Grid-scale evaluation

In this analysis, the IMERG-V05 data was evaluated against the observed rainfall on the native 0.1° x 0.1° IMERG grid. The spatial distributions of POD and CSI suggest a good agreement of the IMERG-V05 product in detecting daily rainfall events in most parts of Brazil, with values generally higher than 0.6 for both metrics (Fig. 2). The exception is along the eastern coast of the Brazilian NE, with many cells presenting values lower than 0.45 for both analysed metrics. The poor POD over coastal areas has also been observed in other studies of

235


---



A.N. Gadelha et al.

Atmospheric Research 218 (2019) 231–244

Spatial distribution maps of daily FAR, POD, CSI, CC, ME, and RMSE over Brazil regions.

Fig. 2. Spatial distributions of daily (a) FAR, (b) POD, (c) CSI, (d) CC, (e) ME, and (f) RMSE.

IMERG (e.g. Asong et al., 2017; Caracciolo et al., 2018). The FAR measures show that the IMERG-V05 product exhibited low false alarms at a daily scale, except for the central part of the NE along the Brazilian driest zone. This eﬀect was probably caused by the low number of rainy days during the study period, as also noticed by Prakash et al. (2018) over southeast peninsular India due to the rain-shadow eﬀects.

The spatial distribution of daily CC shows a good agreement of the IMERG-V05 product with the observed gridded data, wherein most cells presented values equal to or higher than 0.7 (Fig. 2d). The good

agreement is more noticeable in the regions S, SE, and part of the NE. The exception in the region NE was observed along the Atlantic coastal zone, with CC ≤ 0.40 in some cells. This occurred because the IMERG-V05 failed to detect some rainfall events in the NE coast, as mentioned in the POD analysis. Melo et al. (2015) also observed poor agreement along the NE coastal region evaluating the daily rainfall data of the TMPA products using 14-years time series. Similarly, Rozante et al. (2018) also detected large daily underestimation in most cells considered for the Brazilian coastal region by analysing IMERG and TMPA

236


---



A.N. Gadelha et al.

Atmospheric Research 218 (2019) 231–244

Box plots and histograms of metrics (FAR, POD, CSI, CC, ME, RMSE) over observed and estimated rainfall grids at daily temporal resolution.

Fig. 3. Box plots of metrics over observed and estimated rainfall grids at daily temporal resolution: (a) FAR, (b) POD, (c) CSI, (d) CC, (e) ME, and (f) RMSE. The histograms show the distribution of cells for each metric.

products. On the other hand, the worst agreement between the daily IMERG-V05 product and the gridded observed rainfall data was detected across the regions N and CW, with a large number of cells presenting CC values ranging from < 0.1 to 0.6.

The spatial distribution of the IMERG-V05 product errors over Brazil shows that the ME values range between −5.5 (−75%) and 4.5 (110%) mm at daily temporal resolution analysis (Fig. 2e). The largest absolute underestimation and overestimation of the satellite data were observed in the region N for both ME and RMSE error metrics. This was expected because the North region, where the Amazon forest is located, is characterised by the largest amount of rainfall throughout the year. However, the range of relative ME and RMSE for region NE (from −75 to 110% and from 130 to 750%, respectively) is larger than the North region (from −60 to 90% and from 100 to 400%, respectively) (see Fig. S2). This effect can be observed along the coastal zone of the Brazilian NE, where considerable underestimation of the ME (higher than ~1 mm) was also detected, following the similar characteristics of the POD and CSI, which presented low detection in the cells of the area.

Fig. 3 shows the box plots of metrics for the daily comparison for all of Brazil, where each point represents one analysed cell. The box delimits the first (25%) and third (75%) quantiles, while the strip and cross inside symbolise the median and mean, respectively. The whiskers indicate the 10 and 90% percentiles, with the circles after that

representing the outliers. Overall, the three metrics related to detection of observed rainfall events show symmetric results close to each mean (Fig. 3a, b, and c). > 90% of the cells presented values higher than 0.60 for POD and < 0.22 for FAR, which indicates the good skill of the IMERG-V05 product in detecting daily rainfall over most of Brazil. The CC shows that most values are concentrated from 0.5 to 0.8, demonstrating a moderate agreement between observed and estimated rainfall grid values (Fig. 3d). Only 10% of the cells exhibited a CC lower than 0.4 for the daily analysis. The ME also showed strong symmetry at daily temporal resolution, with the mean close to 0 mm (Fig. 3e). This low ME value may have been influenced by compensating positive and negative differences, as also observed by Tang et al. (2016a) in China. The RMSE was relatively high when compared to ME because there is no plus/minus compensation, with a mean value up to 7 mm for the evaluation of the IMERG-V05 product at grid scale. The relative mean of the daily ME and RMSE represent 5 and 200%, respectively (see Fig. S2). This indicates a small net bias, but potentially large uncertainty.

The monthly distribution of the metrics shows a noticeable improvement of the IMERG-V05 product when compared with the daily analysis (Fig. 4). This behaviour confirms longer time averages are more representative, as also seen by Caracciolo et al. (2018), Mayor et al. (2017), Tan et al. (2017), Tang et al. (2016a), among others. Overall, the CC presented values higher than 0.80 for 90% of the cells

237


---



A.N. Gadelha et al.

Atmospheric Research 218 (2019) 231–244

Spatial distributions, box plots, and histograms of monthly CC, ME, and RMSE for Brazil regions.

Fig. 4. Spatial distributions of monthly (a) CC, (c) ME, and (e) RMSE. Box plots and histograms of monthly (b) CC, (d) ME, and (e) RMSE.

available for the Brazilian territory in the monthly analysis, most of them concentrated close to the mean (CC = 0.92) (Fig. 4a). As at the daily scale, the monthly results indicate a poor agreement between rain gauges and satellite rainfall grids observed over the N region and along the Atlantic coastal zone in NE, with CC reaching 0.3 in many cells. For the NE coastal zone, an underestimation of the satellite data was observed. Such underestimation was most likely caused by the prevalence of warm-rain process-dominated systems forced by the topography, which are not well-detected by the passive microwave sensors over land, as noted by Rozante et al. (2018)) and analysed by Palharini and Vila (2017)).

Also, the calibration that works for infrared estimates in other places fails in NE Brazil and is more prone to missing heavy events due to the weakness of cloud top-rain relationship, even if it were calibrated correctly in an average sense. These factors presumably also drive the daily results reported above.

As for the daily analysis, the monthly distribution of ME exhibited symmetric values concentrated close to the mean (~2 mm), with 50% of the sample ranging from −8 to +16 mm (Fig. 4b). Once again, the low average found for ME indicates cancellation between negative and positive values. The spatial distribution of monthly ME shows that the

238


---



A.N. Gadelha et al.

Atmospheric Research 218 (2019) 231–244

<table>
  <thead>
    <tr>
        <th>Theoretical quantiles</th>
        <th>Gauge (mm)</th>
        <th>IMERG (mm)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>-4</td>
<td>0</td>
<td>0</td>
    </tr>
<tr>
        <td>-3</td>
<td>100</td>
<td>100</td>
    </tr>
<tr>
        <td>-2</td>
<td>400</td>
<td>400</td>
    </tr>
<tr>
        <td>-1</td>
<td>1000</td>
<td>1000</td>
    </tr>
<tr>
        <td>0</td>
<td>1800</td>
<td>1800</td>
    </tr>
<tr>
        <td>1</td>
<td>2800</td>
<td>2800</td>
    </tr>
<tr>
        <td>2</td>
<td>3800</td>
<td>3800</td>
    </tr>
<tr>
        <td>3</td>
<td>4300</td>
<td>4300</td>
    </tr>
<tr>
        <td>4</td>
<td>4500</td>
<td>4500</td>
    </tr>
  </tbody>
</table>

Fig. 5. Quantile-quantile (Q-Q) plot comparing the cumulative distribution of the IMERG-V05 Final product and ground-based gridded rainfall data. The solid lines represent theoretical normal distributions.

extreme values larger than $+60\text{ mm}$ and lower than $-60\text{ mm}$ are more concentrated in region N, which is echoed in the spatial distribution of RMSE. The mean relative ME and RMSE for monthly values are 5 and 36%, respectively (see Fig. S3).

Overall, the comparison between the annual rainfall grids shows that the IMERG-V05 product is fairly effective at representing the pattern of rainfall over Brazil (see Fig. 1c and d). However, some discrepancies between the spatial distribution of rainfall are observed, mainly in region N. The disagreements detected in region N both underestimate and overestimate the distributed rain gauge data. This behaviour suggests a problem due to the sparsity of observed data available to interpolate across region N. The cumulative frequency distribution of the observed gridded data demonstrates that 5% of the cells which represent annual rainfall higher than $3000\text{ mm}$ show non-normal distributions, strengthening the case that the discrepancies are concentrated in region N (Fig. 5). Similar behaviour was also observed by Tang et al. (2016a)) over the Tibetan Plateau, where the sparse gauge network used for the interpolation probably reduced the reliability of metrics calculated against such ground reference. Additionally, we observe that the IMERG-V05 product underestimated the annual rainfall along the NE coastal region. This performance follows the general pattern observed in the daily and monthly analyses when the IMERG-V05 product was not successful in detecting the rainfall events across

this area. Additional analyses are necessary in order to assess the possible causes of different performances over Brazil.

## 3.2. National-scale evaluation

This evaluation analysed the national comparison between the series from IMERG-V05 and rain gauge grids using the areal means for the entire country. The analysis reveals a strong agreement for the Brazilian territory as a whole, with the satellite data matching the average rainfall records at daily and monthly time scales (Fig. 6). Generally, the regression line in the scatter plots demonstrates a slight overestimation by the IMERG-V05 product at daily and monthly time scales. Analogous performance analysing the mean areal precipitation was also noticed in others national-scale studies (e.g. Caracciolo et al., 2018; Mayor et al., 2017; Tan and Duan, 2017; Tang et al., 2016a). The national CC at daily and monthly temporal resolutions were 0.96 and 0.99, respectively. These values of the agreement are higher than those from the analysis of the daily and monthly average of individual cells (0.68 and 0.96, respectively). This shows that the areal aggregation leads to an improvement of the satellite product, indicating a good efficacy of the IMERG-V05 product to estimate precipitation over large areas.

Comparisons between ground-based and IMERG-V05 data at national scale show the low variability of ME and RMSE at daily (0.09 and $0.78\text{ mm}$, respectively) and monthly (2.7 and $6.4\text{ mm}$, respectively) time scales. The annual average rainfall at national-scale estimated by the IMERG-V05 product for 2016 was $1647\text{ mm}$, while the average rainfall of the interpolated data for the same year was $1615\text{ mm}$.

## 3.3. Subarea evaluation

Fig. 7 shows the scatter plots and evaluation metrics based on the mean areal rainfall for the five selected subareas. Each subarea was individually analysed in order to expose the problem related to the low density of gauges used for the interpolation in some regions. Also, this analysis provides more detail on the error characteristics of the IMERG-V05 product. Thus, subareas with a relatively high density of ground-based points were carefully chosen. At the daily time scale, the analysis indicates that the IMERG-V05 product presented a very good agreement for all subareas, with CC ranging between 0.80 (N) and 0.92 (NE). Similarly, the high values of POD (from 0.71 to 0.89) and CSI (from 0.65 to 0.88) showed satisfactory performance of the IMERG-V05 product in detecting the ground-based rainfall events in the subareas. The FAR presented values close to zero for almost all subareas, indicating low false alarms when regions with high density of in-situ data are considered for the analyses. The exception was noticed in region NE (FAR = 0.23) because that subarea is placed in a dry zone, where there

<table>
  <thead>
    <tr>
        <th colspan="2">a) Daily Evaluation Metrics: CC=0.964, ME=0.0885, RMSE=0.7755, y=1.0808x-0.2682, R²=0.9293</th>
    </tr>
<tr>
        <th>Rain gauges (mm)</th>
        <th>IMERG-V05 (mm)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>0</td>
<td>0</td>
    </tr>
<tr>
        <td>2</td>
<td>2</td>
    </tr>
<tr>
        <td>4</td>
<td>4</td>
    </tr>
<tr>
        <td>6</td>
<td>6</td>
    </tr>
<tr>
        <td>8</td>
<td>8</td>
    </tr>
<tr>
        <td>10</td>
<td>10</td>
    </tr>
<tr>
        <td>12</td>
<td>12</td>
    </tr>
<tr>
        <td>14</td>
<td>14</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
        <th colspan="2">b) Monthly Evaluation Metrics: CC=0.999, ME=2.698, RMSE=6.367, y=1.0699x-6.7125, R²=0.99974</th>
    </tr>
<tr>
        <th>Rain gauges (mm)</th>
        <th>IMERG-V05 (mm)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>0</td>
<td>0</td>
    </tr>
<tr>
        <td>50</td>
<td>50</td>
    </tr>
<tr>
        <td>100</td>
<td>100</td>
    </tr>
<tr>
        <td>150</td>
<td>150</td>
    </tr>
<tr>
        <td>200</td>
<td>200</td>
    </tr>
<tr>
        <td>250</td>
<td>250</td>
    </tr>
<tr>
        <td>300</td>
<td>300</td>
    </tr>
  </tbody>
</table>

Fig. 6. Scatter plots and metrics of rainfall comparisons for national-scale evaluation over Brazil at (a) daily and (b) monthly timescales.

239


---



A.N. Gadelha et al.

Atmospheric Research 218 (2019) 231–244

<table>
  <thead>
    <tr>
        <th>Region</th>
        <th>Scale</th>
        <th>CC</th>
        <th>ME</th>
        <th>RMSE</th>
        <th>POD</th>
        <th>CSI</th>
        <th>FAR</th>
        <th>Regression Equation</th>
        <th>R²</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>North (1)</td>
<td>Daily (a)</td>
<td>0.80</td>
<td>0.43</td>
<td>5.43</td>
<td>0.89</td>
<td>0.88</td>
<td>0.02</td>
<td>y = 1.0166x - 0.3342</td>
<td>0.6389</td>
    </tr>
<tr>
        <td>North (1)</td>
<td>Monthly (b)</td>
<td>0.99</td>
<td>13.21</td>
<td>20.63</td>
<td> </td>
<td> </td>
<td> </td>
<td>y = 1.0713x - 0.5205</td>
<td>0.9817</td>
    </tr>
<tr>
        <td>Northeast (2)</td>
<td>Daily (c)</td>
<td>0.92</td>
<td>0.39</td>
<td>0.09</td>
<td>0.80</td>
<td>0.65</td>
<td>0.23</td>
<td>y = 1.1593x - 0.1982</td>
<td>0.8791</td>
    </tr>
<tr>
        <td>Northeast (2)</td>
<td>Monthly (d)</td>
<td>0.99</td>
<td>11.96</td>
<td>17.60</td>
<td> </td>
<td> </td>
<td> </td>
<td>y = 1.1615x - 5.9696</td>
<td>0.9868</td>
    </tr>
<tr>
        <td>Central-W (3)</td>
<td>Daily (e)</td>
<td>0.90</td>
<td>0.20</td>
<td>2.92</td>
<td>0.89</td>
<td>0.85</td>
<td>0.06</td>
<td>y = 1.0444x - 5.0501</td>
<td>0.8023</td>
    </tr>
<tr>
        <td>Central-W (3)</td>
<td>Monthly (f)</td>
<td>1.00</td>
<td>6.06</td>
<td>13.67</td>
<td> </td>
<td> </td>
<td> </td>
<td>y = 1.0628x - 0.2790</td>
<td>0.9932</td>
    </tr>
<tr>
        <td>Southeast (4)</td>
<td>Daily (g)</td>
<td>0.89</td>
<td>0.06</td>
<td>4.03</td>
<td>0.71</td>
<td>0.70</td>
<td>0.02</td>
<td>y = 1.1182x - 0.4376</td>
<td>0.7938</td>
    </tr>
<tr>
        <td>Southeast (4)</td>
<td>Monthly (h)</td>
<td>0.99</td>
<td>1.63</td>
<td>11.06</td>
<td> </td>
<td> </td>
<td> </td>
<td>y = 0.9122x - 12.833</td>
<td>0.987</td>
    </tr>
<tr>
        <td>South (5)</td>
<td>Daily (i)</td>
<td>0.89</td>
<td>0.03</td>
<td>5.00</td>
<td>0.72</td>
<td>0.69</td>
<td>0.06</td>
<td>y = 1.0733x - 0.3457</td>
<td>0.7987</td>
    </tr>
<tr>
        <td>South (5)</td>
<td>Monthly (j)</td>
<td>0.93</td>
<td>0.99</td>
<td>23.20</td>
<td> </td>
<td> </td>
<td> </td>
<td>y = 1.0733x - 0.3457</td>
<td>0.7987</td>
    </tr>
  </tbody>
</table>

Fig. 7. Metrics for the subarea analysis at daily (a, c, e, g, and i) and monthly (b, d, f, h, and j) scales based on the mean areal precipitation in the five official geographical regions in Brazil.

240


---



A.N. Gadelha et al.

Atmospheric Research 218 (2019) 231–244

Scatter plots of CC vs gauge density and altitude for five Brazilian regions (N, NE, CW, SE, S) with a color bar indicating normalised concentration of points.

Fig. 8. Scatter plots of CC vs gauge density (left column) and altitude (right column) categorised by the five regions in Brazil, where the number of grid boxes at each point on the plot is normalised by the highest number on the plot, and then coloured according to the color bar at the bottom of the figure.

are fewer events to be correctly detected. Muhammad et al. (2018) also noted low performance of satellite rainfall detection in the driest regions of Pakistan. In addition, more localised rainfall events in semiarid regions can be missed either by rain gauges or reduced to a very low quantity from averaging up to the satellite grid. Conversely, the subarea located in the region NE presented absolute values of ME and RMSE closer to zero due to the low rainfall depth throughout the year, but representing the highest relative values at daily (32.3 and 196%, respectively) and monthly (32.2 and 47.4%, respectively) temporal scales (see Table S2). Once again, the subarea located in region N exhibited the highest absolute values of ME and RMSE because of the largest number of days with rain and the high annual rainfall depth. Nevertheless, the relative ME and RMSE present similar values when compared to regions S, SE, and CW (see Table S2). Overall, all subareas presented a significant improvement of the metrics at the monthly time 

 scale, with most metrics showing near perfect indices by comparing the areal mean of the interpolated gauge data and the IMERG-V05 product.

## 3.4. Feature analysis

A feature analysis was conducted to determine the direct influence of several factors on the daily agreement between the ground-based gridded rainfall data and the IMERG-V05 product. Fig. 8 shows the CC against the density of gauges (left column) and altitude (right column) categorised by the five regions in Brazil. Because of a large number of cells, the concentration of points was coloured in a normalised scale from zero (red) to one (blue), representing the highest and lowest concentrations, respectively. Overall, we observe that the CC directly correlates to the density of gauges in regions N and CW of the country, with values ranging from 0.1 to 0.8 in areas with < 10 gauges per

241


---



A.N. Gadelha et al.

Atmospheric Research 218 (2019) 231–244

Box plots of CC categorised by climate.

Fig. 9. Box plots of CC categorised by climate.

10,000 km<sup>2</sup>. In contrast, the correlations between CC and density of gauges have a tendency to increase from this threshold, with values ranging from 0.6 to 0.8. Regions S and SE presented similar behaviour, with CC mostly higher than 0.6 and reaching 0.9 in some places. However, it is worth highlighting that both regions S and SE present the highest density of gauges used for the interpolation, mostly higher than 10 per 10,000 km<sup>2</sup>. These results reinforce the result in Tang et al. (2018) that the spatiotemporal errors computed by comparing satellite and observed rainfall data increase with the reduction of the gauge density in a grid box approach.

The relation between CC and altitude shows a higher scattering and lower concentration of points with the increasing of elevation. In general, the cells located at altitudes higher than 1000 m above sea level present considerable improvement of CC, which is more noticeable in regions NE, CW, and SE. This finding differs from the study carried out by Anjum et al. (2018) in Pakistan. However, it is similar to the results found by Mayor et al. (2017) in a Mexican region, where IMERG performed better at higher altitudes. Consequently, this type of result found in Brazil can be a potential solution for obtaining rainfall data over complex terrain where ground-based measurement networks are sparse. However, specific error analyses over these complex areas need to be performed, as previously studied by Mei et al. (2016) and Maggioni et al. (2017) over Alpine terrain in Italy. It is also noticeable that the correlations between CC and altitude in both regions S and SE showed analogous behaviour to those observed for the station density analysis, with small ranges of CC variation according to the elevation. Unlike these two regions, larger dispersions are observed in regions N, NE, and CW for a wide range of elevations. Therefore, the similar behaviour of the scatter plots for both feature analyses may suggest that the density of gauges affects the altitude evaluation.

In general, the correlation showed that the IMERG-V05 performed better in regions under Subtropical (Zone C) and Semiarid (Zone B) climates (Fig. 9). The Subtropical climate is found mostly in the regions S and SE; whereas the Semiarid climate prevails in NE Brazil. Three climates (Cwc, Csa, and Csb) were excluded from the analysis because they cover < 0.01% of the Brazilian territory (Alvares et al., 2013). Overall, the climates identified as being part of climatic Zone A (Tropical climate) exhibited the largest dispersions, as well as the lowest means and medians of CC values. Zone A represents the largest climate area in Brazil and covers predominantly regions N and CW. Consequently, the feature analysis by climate may have been once again influenced by the low density of rain gauges, which probably results in a poor performance of the IMERG-V05 estimates.

# 4. Conclusions

This study evaluated the IMERG-V05 Final Run product over Brazil using ground-based gridded rainfall data composed of 4911 gauges as a

reference. All analyses were performed in a distributed fashion at daily, monthly, and annual timescales for 2016. Overall, the results showed that the IMERG-V05 product can effectively capture the spatial patterns of rainfall across Brazil. The main specific findings of this study using a grid box-scale approach are summarised as follows:

(1) IMERG-V05 exhibited better agreement with the observed data at monthly timescale when compared to daily timescale in all analyses. Nevertheless, the IMERG-V05 presented a slight tendency in overestimating the gridded observed data at all analysed timescales.

(2) The performance of IMERG-V05 in the grid-scale and national-scale evaluations presented some variations as a function of the analysed region. Based on these two evaluations, the rainfall estimated by the satellite product exhibited higher errors and biases in regions N and CW, as well as along the Atlantic coast of region NE. The underestimation evident in the satellite product for the region NE is likely associated with topographic forcing that favours warm-rain process systems which cannot be detected very well by passive microwave sensors over land.

(3) The subarea evaluation revealed that the IMERG-V05 product compares well with the interpolated data in specific areas with high density of rain gauges, including region N. The feature analysis confirmed that the low density of rain gauges in regions N and CW can be a source of large deviations, errors, and biases in the evaluation of the satellite rainfall product.

Based on the findings of this study, the IMERG-V05 Final Run product can be used as a source of rainfall data to complement the ground precipitation measurements in most parts of the Brazilian territory. The exception is in the coastal region of the Brazilian NE, where the IMERG-V05 product needs a bias correction procedure due to the large underestimation probably caused by the inability of the microwave and infrared sensors in to properly detect rain-warm events. Moreover, the IMERG-V05 estimates for regions N and CW need to be carefully used because of some uncertainties in the data which are probably associated with the low density of rain gauges used to create the ground-based gridded product.

Finally, this study highlights that the relatively high spatiotemporal resolution of the IMERG-V05 product can favour its application for many purposes in Brazil such as hydrological modelling. However, further improvements of the IMERG-V05 product are needed for providing more accurate rainfall estimates mainly along the coastal zone of NE Brazil. Furthermore, grid box-level studies with longer data period, considering seasonal analysis and exploring the characteristics of hourly and half-hourly estimates of the IMERG-V05 product over Brazil, are strongly recommended.

## Acknowledgements

The authors would like to acknowledge the financial support from FINEP (Brazilian Innovation Agency) granted to the BRAMAR (BRAzil Managed Aquifer Recharge, grant no. 557/2013) project. This study was financed in part by the Coordenação de Aperfeiçoamento de Pessoal de Nível Superior (CAPES) - Finance Code 001. The Brazilian authors are also grateful to the Brazilian National Council for Scientific and Technological Development (CNPq), Paraíba Research Foundation (FAPESQ-PB), and São Paulo Research Foundation (FAPESP, process 2016/23546-7) for the financial support. The NASA authors (GHJ and WAP) were funded under the Precipitation Measurement Missions and Global Precipitation Measurement (GPM) mission projects. Special thanks are given to ANA (Brazilian National Water Agency), INMET (the Brazilian National Institute of Meteorology), and the sixteen Brazilian regional water agencies (specially ADASA, CAESB, DAEE, FUNCEME, and AGUASPARANÁ) for providing the ground-based rainfall data.

242


---



A.N. Gadelha et al.

Atmospheric Research 218 (2019) 231–244

# References

Alvares, C.A., Stape, J.L., Sentelhas, P.C., De Moraes Gonçalves, J.L., Sparovek, G., 2013. Köppen's climate classification map for Brazil. Meteorol. Zeitschrift 22, 711–728. https://doi.org/10.1127/0941-2948/2013/0507.

Anjum, M.N., Ding, Y., Shangguan, D., Ahmad, I., Ijaz, M.W., Farid, H.U., Yagoub, Y.E., Zaman, M., Adnan, M., 2018. Performance evaluation of latest integrated multi-satellite retrievals for global precipitation measurement (IMERG) over the northern highlands of Pakistan. Atmos. Res. 205, 134–146. https://doi.org/10.1016/j.atmosres.2018.02.010.

Asong, Z.E., Razavi, S., Wheater, H.S., Wong, J.S., 2017. Evaluation of integrated multisatellite retrievals for GPM (IMERG) over southern Canada against ground precipitation observations: a preliminary assessment. J. Hydrometeorol. 18, 1033–1050. https://doi.org/10.1175/JHM-D-16-0187.1.

Baik, J., Choi, M., 2015. Spatio-temporal variability of remotely sensed precipitation data from COMS and TRMM: Case study of Korean peninsula in East Asia. Adv. Sp. Res. 56, 1125–1138. https://doi.org/10.1016/j.asr.2015.06.015.

Beria, H., Nanda, T., Bisht, D.S., Chatterjee, C., 2017. Does the GPM mission improve the systematic error component in satellite rainfall estimates over TRMM? An evaluation at a pan-India scale. Hydrol. Earth Syst. Sci. 21, 6117–6134. https://doi.org/10.5194/hess-21-6117-2017.

Buarque, D.C., De Paiva, R.C.D., Clarke, R.T., Mendes, C.A.B., 2011. A comparison of Amazon rainfall characteristics derived from TRMM, CMORPH and the Brazilian national rain gauge network. J. Geophys. Res. Atmos. 116, 1–12. https://doi.org/10.1029/2011JD016060.

Caracciolo, D., Francipane, A., Francesco, V., Noto, L.V., 2018. Performances of GPM satellite precipitation over the two major Mediterranean islands. Atmos. Res. 213, 309–322. https://doi.org/10.1016/j.atmosres.2018.06.010.

Coelho, V.H.R., Montenegro, S., Almeida, C.N., Silva, B.B., Oliveira, L.M., Gusmão, A.C.V., Freitas, E.S., Montenegro, A.A.A., 2017. Alluvial groundwater recharge estimation in semi-arid environment using remotely sensed data. J. Hydrol. 548, 1–15. https://doi.org/10.1016/j.jhydrol.2017.02.054.

Cohen Liechti, T., Matos, J.P., Boillat, J.L., Schleiss, A.J., 2012. Comparison and evaluation of satellite derived precipitation products for hydrological modeling of the Zambezi River Basin. Hydrol. Earth Syst. Sci. 16, 489–500. https://doi.org/10.5194/hess-16-489-2012.

Collischonn, B., Collischonn, W., Tucci, C.E.M., 2008. Daily hydrological modeling in the Amazon basin using TRMM rainfall estimates. J. Hydrol. 360, 207–216. https://doi.org/10.1016/j.jhydrol.2008.07.032.

Curtarelli, M.P., Rennó, C.D., Alcântara, E.H., 2014. Evaluation of the tropical rainfall measuring mission 3B43 product over an inland area in Brazil and the effects of satellite boost on rainfall estimates. J. Appl. Remote. Sens. 8, 083589. https://doi.org/10.1117/1.JRS.8.083589.

De Paiva, R.C.D., Buarque, D.C., Collischonn, W., Bonnet, M.P., Frappart, F., Calmant, S., Bulhões Mendes, C.A., 2013. Large-scale hydrologic and hydrodynamic modeling of the Amazon River basin. Water Resour. Res. 49, 1226–1243. https://doi.org/10.1002/wrcr.20067.

Delahaye, F., Kirstetter, P.E., Dubreuil, V., Machado, L.A.T., Vila, D.A., Clark, R., 2015. A consistent gauge database for daily rainfall analysis over the legal Brazilian Amazon. J. Hydrol. 527, 292–304. https://doi.org/10.1016/j.jhydrol.2015.04.012.

Dezfuli, A.K., Ichoku, C.M., Huffman, G.J., Mohr, K.I., Selker, J.S., van de Giesen, N., Hochreutener, R., Annor, F.O., 2017. Validation of IMERG precipitation in Africa. J. Hydrometeorol. https://doi.org/10.1175/JHM-D-17-0139.1.

Espinoza Villar, J.C., Ronchail, J., Guyot, J.L., Cochonneau, G., Naziano, F., Lavado, W., De Oliveira, E., Pombosa, R., Vauchel, P., 2009. Spatio-temporal rainfall variability in the Amazon basin countries (Brazil, Peru, Bolivia, Colombia, and Ecuador). Int. J. Climatol. 29, 1574–1594. https://doi.org/10.1002/joc.1791.

Falck, A.S., Maggioni, V., Tomasella, J., Vila, D.A., Diniz, F.L.R., 2015. Propagation of satellite precipitation uncertainties through a distributed hydrologic model: a case study in the Tocantins-Araguaia basin in Brazil. J. Hydrol. 527, 943–957. https://doi.org/10.1016/j.jhydrol.2015.05.042.

Fang, J., Du, J., Xu, W., Shi, P., Li, M., Ming, X., 2013. Spatial downscaling of TRMM precipitation data based on the orographical effect and meteorological conditions in a mountainous area. Adv. Water Resour. 61, 42–50. https://doi.org/10.1016/j.advwatres.2013.08.011.

Franchito, S.H., Rao, V.B., Vasques, A.C., Santo, C.M.E., Conforte, J.C., 2009. Validation of TRMM precipitation radar monthly rainfall estimates over Brazil. J. Geophys. Res. Atmos. 114. https://doi.org/10.1029/2007JD009580.

Gebregiorgis, A.S., Kirstetter, P.E., Hong, Y.E., Gourley, J.J., Huffman, G.J., Petersen, W.A., Xue, X., Schwaller, M.R., 2018. To what extent is the day 1 GPM IMERG satellite precipitation estimate improved as compared to TRMM TMPA-RT? J. Geophys. Res. Atmos. 123, 1694–1707. https://doi.org/10.1002/2017JD027606.

Guo, R., Liu, Y., 2016. Evaluation of satellite precipitation products with rain gauge data at different scales: Implications for hydrological applications. Water (Switzerland) 8. https://doi.org/10.3390/w8070281.

Hobouchian, M.P., Salio, P., García Skabar, Y., Vila, D., Garreaud, R., 2017. Assessment of satellite precipitation estimates over the slopes of the subtropical Andes. Atmos. Res. 190, 43–54. https://doi.org/10.1016/j.atmosres.2017.02.006.

Hofstra, N., New, M., 2009. Spatial variability in correlation decay distance and influence on angular-distance weighting interpolation of daily precipitation over Europe. Int. J. Climatol. 29, 1872–1880. https://doi.org/10.1002/joc.1819.

Hou, A.Y., Kakar, R.K., Neeck, S., Azarbarzin, A.A., Kummerow, C.D., Kojima, M., Oki, R., Nakamura, K., Iguchi, T., 2014. The global precipitation measurement mission. Bull. Am. Meteorol. Soc. 95, 701–722. https://doi.org/10.1175/BAMS-D-13-00164.1.

Hu, K., Awange, J.L., Khandu, Forootan, E., Goncalves, R.M., Fleming, K., 2017. Hydrogeological characterisation of groundwater over Brazil using remotely sensed and model products. Sci. Total Environ. 599–600, 372–386. https://doi.org/10.1016/j.scitotenv.2017.04.188.

Huffman, G.J., Bolvin, D.T., Nelkin, E.J., Wolff, D.B., Adler, R.F., Gu, G., Hong, Y., Bowman, K.P., Stocker, E.F., 2007. The TRMM multisatellite precipitation analysis (TMPA): quasi-global, multiyear, combined-sensor precipitation estimates at fine scales. J. Hydrometeorol. 8, 38–55. https://doi.org/10.1175/JHM560.1.

Huffman, G.J., Bolvin, D.T., Nelkin, E.J., 2017a. Integrated Multi-satellitE Retrievals for GPM (IMERG) Technical Documentation.

Huffman, G.J., Bolvin, D.T., Nelkin, E.J., Stocker, E.F., 2017b. V05 IMERG Final Run Release Notes.

Jesus, M., Rinaldo, A., Rodr, I., Jesus, D.E.L., Al, E.T., 2015. Point rainfall statistics for ecohydrological analyses derived from satellite integrated measurements. Water Resour. Res. 2974–2985. https://doi.org/10.1002/2015WR016935.

Kann, A., Meirold-Mautner, I., Schmid, F., Kirchengast, G., Fuchsberger, J., Meyer, V., Tüchler, L., Bica, B., 2015. Evaluation of high-resolution precipitation analyses using a dense station network. Hydrol. Earth Syst. Sci. 19, 1547–1559. https://doi.org/10.5194/hess-19-1547-2015.

Khan, S., Maggioni, V., Kirstetter, P.-E., 2018. Investigating the potential of using satellite-based precipitation radars as reference for evaluating multisatellite merged products. J. Geophys. Res. Atmos. 123, 8646–8660. https://doi.org/10.1029/2018JD028584.

Kidd, C., Huffman, G., 2011. Global precipitation measurement. Meteorol. Appl. 18, 334–353. https://doi.org/10.1002/met.284.

Kidd, C., Becker, A., Huffman, G.J., Muller, C.L., Joe, P., Skofronick-Jackson, G., Kirschbaum, D.B., 2017. So, how much of the Earth's surface is covered by rain gauges? Bull. Am. Meteorol. Soc. 98, 69–78. https://doi.org/10.1175/BAMS-D-14-00283.1.

Kousky, V.E., 1979. Frontal influences on northeast Brazil. Mon. Weather Rev. https://doi.org/10.1175/1520-0493(1979)107<1140:FIONB>2.0.CO;2107<1140:FIONB>2.0.CO;2).

Lelis, L., Bosquilia, R., Duarte, S., 2018. Assessment of precipitation data generated by GPM and TRMM satellites. Rev. Bras. Meteorol. 33, 153–163. https://doi.org/10.1590/0102-7786331004.

Levizzani, V., Kidd, C., Aonashi, K., Bennartz, R., Ferraro, R.R., Huffman, G.J., Roca, R., Turk, F.J., Wang, N.Y., 2018. The activities of the International Precipitation Working Group. Q. J. R. Meteorol. Soc. https://doi.org/10.1002/qj.3214.

Liu, Z., Ostrenga, D., Vollmer, B., Deshong, B., MacRitchie, K., Greene, M., Kempler, S., 2017. Global precipitation measurement mission products and services at the nasa ges disc. Bull. Am. Meteorol. Soc. 98, 437–444. https://doi.org/10.1175/BAMS-D-16-0023.1.

Maggioni, V., Nikolopoulos, E.I., Anagnostou, E.N., Borga, M., 2017. Modeling satellite precipitation errors over mountainous terrain: the influence of gauge density, seasonality, and temporal resolution. IEEE Trans. Geosci. Remote Sens. 55, 4130–4140. https://doi.org/10.1109/TGRS.2017.2688998.

Mahmoud, M.T., Al-Zahrani, M.A., Sharif, H.O., 2018. Assessment of global precipitation measurement satellite products over Saudi Arabia. J. Hydrol. 559, 1–12. https://doi.org/10.1016/j.jhydrol.2018.02.015.

Mayor, Y.G., Tereshchenko, I., Fonseca-Hernández, M., Pantoja, D.A., Montes, J.M., 2017. Evaluation of error in IMERG precipitation estimates under different topographic conditions and temporal scales over Mexico. Remote Sens. 9. https://doi.org/10.3390/rs9050503.

McMillan, H., Jackson, B., Clark, M., Kavetski, D., Woods, R., 2011. Rainfall uncertainty in hydrological modelling: an evaluation of multiplicative error models. J. Hydrol. 400, 83–94. https://doi.org/10.1016/j.jhydrol.2011.01.026.

Mei, Y., Nikolopoulos, E.I., Anagnostou, E.N., Zoccatelli, D., Borga, M., 2016. Error analysis of satellite precipitation-driven modeling of flood events in complex alpine terrain. Remote Sens. 8. https://doi.org/10.3390/rs8040293.

Melo, D.C.D., Xavier, A.C., Bianchi, T., Oliveira, P.T.S., Scanlon, B.R., Lucas, M.C., Wendland, E., 2015. Performance evaluation of rainfall estimates by TRMM Multisatellite precipitation analysis 3B42V6 and V7 over Brazil. J. Geophys. Res. Atmos. 120, 9043–9836. https://doi.org/10.1002/2014JD022963.

Melo, D.D.C.D., Scanlon, B.R., Zhang, Z., Wendland, E., Yin, L., 2016. Reservoir Storage and Hydrologic Responses to Droughts in the Paraná River Basin, South-Eastern Brazil. pp. 4673–4688. https://doi.org/10.5194/hess-20-4673-2016.

Meng, J., Li, L., Hao, Z., Wang, J., Shao, Q., 2014. Suitability of TRMM satellite rainfall in driving a distributed hydrological model in the source region of Yellow River. J. Hydrol. 509, 320–332. https://doi.org/10.1016/j.jhydrol.2013.11.049.

Mitra, A.K., Kaushik, N., Singh, A.K., Parihar, S., Bhan, S.C., 2018. Evaluation of INSAT-3D Satellite derived precipitation estimates for heavy rainfall events and its validation with gridded GPM (IMERG) rainfall dataset over the Indian region. Remote Sens. Appl. Soc. Environ. 9, 91–99. https://doi.org/10.1016/j.rsase.2017.12.006.

Muhammad, W., Yang, H., Lei, H., Muhammad, A., Yang, D., 2018. Improving the regional applicability of satellite precipitation products by ensemble algorithm. Remote Sens. 10, 577. https://doi.org/10.3390/rs10040577.

Naumann, G., Barbosa, P., Carrao, H., Singleton, A., Vogt, J., 2012. Monitoring drought conditions and their uncertainties in Africa using TRMM data. J. Appl. Meteorol. Climatol. 51, 1867–1874. https://doi.org/10.1175/JAMC-D-12-0113.1.

Nery, J.T., Carfan, A.C., 2014. Re-analysis of pluvial precipitation in southern Brazil. Atmosfera 27, 103–115. https://doi.org/10.1016/S0187-6236(14)71104-X71104-X).

New, M., Hulme, M., Jones, P., 2000. Representing twentieth-century space-time climate variability. Part II: Development of 1901-96 monthly grids of terrestrial surface climate. J. Clim. 13, 2217–2238. https://doi.org/10.1175/1520-0442(2000)013<2217:RTCSTC>2.0.CO;2013<2217:RTCSTC>2.0.CO;2).

243


---



A.N. Gadelha et al.

Atmospheric Research 218 (2019) 231–244

Oliveira, R., Maggioni, V., Vila, D., Morales, C., 2016. Characteristics and diurnal cycle of GPM rainfall estimates over the Central Amazon region. Remote Sens. 8. https://doi.org/10.3390/rs8070544.

Oliveira, R., Maggioni, V., Vila, D., Porcacchia, L., 2018. Using satellite error modeling to improve GPM-Level 3 rainfall estimates over the Central Amazon region. Remote Sens. 10. https://doi.org/10.3390/rs10020336.

Palharini, R.S.A., Vila, D.A., 2017. Climatological behavior of precipitating clouds in the northeast region of Brazil. Adv. Meteorol. 17–21.

Pombo, S., de Oliveira, R.P., 2015. Evaluation of extreme precipitation estimates from TRMM in Angola. J. Hydrol. 523, 663–679. https://doi.org/10.1016/j.jhydrol.2015.02.014.

Prakash, S., Mitra, A.K., Aghakouchak, A., Liu, Z., Norouzi, H., Pai, D.S., 2018. A preliminary assessment of GPM-based multi-satellite precipitation estimates over a monsoon dominated region. J. Hydrol. 556, 865–876. https://doi.org/10.1016/j.jhydrol.2016.01.029.

Reboita, M.S., Gan, M.A., Rocha, R.P., Ambrizzi, T., 2010. Precipitation regimes in South America: a bibliography review. Rev. Bras. Meteorol. 25, 185–204.

Rozante, J.R., Vila, D.A., Chiquetto, Júlio Barboza, de Fernandes, A. Alex, Alvim, D.S., 2018. Evaluation of TRMM/GPM blended daily products over Brazil. Remote Sens. 15, 814–815. https://doi.org/10.3390/rs10060882.

Satgé, F., Xavier, A., Zolá, R.P., Hussain, Y., Timouk, F., Garnier, J., Bonnet, M.P., 2017. Comparative assessments of the latest GPM mission's spatially enhanced satellite rainfall products over the main Bolivian watersheds. Remote Sens. 9, 1–16. https://doi.org/10.3390/rs9040369.

Schneider, U., Ziese, M., Meyer-Christoffer, A., Finger, P., Rustemeier, E., Becker, A., 2016. The new portfolio of global precipitation data products of the Global Precipitation Climatology Centre suitable to assess and quantify the global water cycle and resources. Proc. Int. Assoc. Hydrol. Sci. 374, 29–34. https://doi.org/10.5194/piahs-374-29-2016.

Skofronick-Jackson, G., Petersen, W.A., Berg, W., Kidd, C., Stocker, E.F., Kirschbaum, D.B., Kakar, R., Braun, S.A., Huffman, G.J., Iguchi, T., Kirstetter, P.E., Kummerow, C., Meneghini, R., Oki, R., Olson, W.S., Takayabu, Y.N., Furukawa, K., Wilheit, T., 2017. The global precipitation measurement (GPM) mission for science and Society. Bull. Am. Meteorol. Soc. 98, 1679–1695. https://doi.org/10.1175/BAMS-D-15-00306.1.

Skofronick-Jackson, G., Kirschbaum, D., Petersen, W., Huffman, G., Kidd, C., Stocker, E., Kakar, R., 2018. The global precipitation measurement (GPM) mission's scientific achievements and societal contributions: reviewing four years of advanced rain and snow observations. Q. J. R. Meteorol. Soc. https://doi.org/10.1002/qj.3313.

Sungmin, O., Foelsche, U., Kirchengast, G., Fuchsberger, J., Tan, J., Petersen, W.A., 2017. Evaluation of GPM IMERG early, late, and final rainfall estimates using WegenerNet gauge data in southeastern Austria. Hydrol. Earth Syst. Sci. 21, 6559–6572. https://doi.org/10.5194/hess-21-6559-2017.

Tan, M., Duan, Z., 2017. Assessment of GPM and TRMM precipitation products over Singapore. Remote Sens. 9, 720. https://doi.org/10.3390/rs9070720.

Tan, M.L., Santo, H., 2018. Comparison of GPM IMERG, TMPA 3B42 and PERSIANN-CDR satellite precipitation products over Malaysia. Atmos. Res. 202, 63–76. https://doi.org/10.1016/j.atmosres.2017.11.006.

Tan, J., Petersen, W.A., Kirstetter, P.-E., Tian, Y., 2017. Performance of IMERG as a function of spatiotemporal scale. J. Hydrometeorol. 18, 307–319. https://doi.org/10.1175/JHM-D-16-0174.1.

Tang, G., Ma, Y., Long, D., Zhong, L., Hong, Y., 2016a. Evaluation of GPM Day-1 IMERG and TMPA Version-7 legacy products over mainland China at multiple spatiotemporal scales. J. Hydrol. 533, 152–167. https://doi.org/10.1016/j.jhydrol.2015.12.008.

Tang, G., Zeng, Z., Long, D., Guo, X., Yong, B., Zhang, W., Hong, Y., 2016b. Statistical and hydrological comparisons between TRMM and GPM Level-3 products over a mid-latitude basin: is day-1 IMERG a good successor for TMPA 3B42V7? J. Hydrometeorol. 17, 121–137. https://doi.org/10.1175/JHM-D-15-0059.1.

Tang, G., Behrangi, A., Long, D., Li, C., Hong, Y., 2018. Accounting for spatiotemporal errors of gauges: a critical step to evaluate gridded precipitation products. J. Hydrol. 559, 294–306. https://doi.org/10.1016/j.jhydrol.2018.02.057.

Terink, W., Leijnse, H., van den Eertwegh, G., Uijlenhoet, R., 2018. Spatial resolutions in areal rainfall estimation and their impact on hydrological simulations of a lowland catchment. J. Hydrol. https://doi.org/10.1016/j.jhydrol.2018.05.045.

Toté, C., Patricio, D., Boogaard, H., van der Wijngaart, R., Tarnavsky, E., Funk, C., 2015. Evaluation of satellite rainfall estimates for drought and flood monitoring in Mozambique. Remote Sens. 7, 1758–1776. https://doi.org/10.3390/rs70201758.

Vicente-Serrano, S.M., Saz-Sánchez, M.A., Cuadrat, J.M., 2003. Comparative analysis of interpolation methods in the middle Ebro Valley (Spain): application to annual precipitation and temperature. Clim. Res. 24, 161–180.

Wang, Z., Zhong, R., Lai, C., Chen, J., 2017. Evaluation of the GPM IMERG satellite-based precipitation products and the hydrological utility. Atmos. Res. 196, 151–163. https://doi.org/10.1016/j.atmosres.2017.06.020.

WMO, 1994. Guide to Hydrological Practices: Data Acquisition and Processing, Analysis, Forecasting and Other Applications.

Xavier, A.C., King, C.W., Scanlon, B.R., 2016. Daily gridded meteorological variables in Brazil (1980–2013). Int. J. Climatol. 2659, 2644–2659. https://doi.org/10.1002/joc.4518.

Yang, S., Nesbitt, S.W., 2014. Statistical properties of precipitation as observed by the TRMM precipitation radar. Geophys. Res. Lett. 41, 5636–5643. https://doi.org/10.1002/2014GL060683.

Zad, S.N.M., Zulkafli, Z., Muharram, F.M., 2018. Satellite rainfall (TRMM 3B42-V7) performance assessment and adjustment over Pahang river basin, Malaysia. Remote Sens. 10, 1–24. https://doi.org/10.3390/rs10030388.

Zhang, S., Wang, D., Qin, Z., Zheng, Y., Guo, J., 2018. Assessment of the GPM and TRMM precipitation products using the rain gauge network over the Tibetan Plateau. J. Meteorol. Res. 32, 324–336. https://doi.org/10.1007/s13351-018-7067-0.

244
