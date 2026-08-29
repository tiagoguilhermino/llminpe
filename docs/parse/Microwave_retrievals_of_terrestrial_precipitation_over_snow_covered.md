AGU PUBLICATIONS logo

# Geophysical Research Letters

## RESEARCH LETTER

10.1002/2017GL073451

# Microwave retrievals of terrestrial precipitation over snow-covered surfaces: A lesson from the GPM satellite

**Key Points:**

* Microwave signals of precipitation show transitions from a scattering to an emission regime from summer to winter due to evolution of snow

* Combination of low- and high-frequency channels provide the maximum amount of information for microwave snowfall detection

* The probability of microwave snowfall detection can even be higher than rainfall

**A. M. Ebtehaj<sup>1</sup> ORCID icon and C. D. Kummerow<sup>2</sup> ORCID icon**

<sup>1</sup>Saint Anthony Falls Laboratory, Department of Civil, Environmental, and Geo-Engineering, University of Minnesota, Minneapolis, Minnesota, USA, <sup>2</sup>Cooperative Institute for Research in the Atmosphere, Department of Atmospheric Science, Colorado State University, Fort Collins, Colorado, USA

**Correspondence to:**

A. M. Ebtehaj,
ebtehaj@umn.edu

**Abstract** Satellites are playing an ever-increasing role in estimating precipitation over remote areas. Improving satellite retrievals of precipitation requires increased understanding of its passive microwave signatures over different land surfaces. Snow-covered surfaces are notoriously difficult to interpret because they exhibit both emission from the land below and scattering from the ice crystals. Using data from the Global Precipitation Measurement (GPM) satellite, we demonstrate that microwave brightness temperatures of rain and snowfall transition from a scattering to an emission regime from summer to winter, due to expansion of less emissive snow cover. Evidence suggests that the combination of low- (10–19 GHz) and high-frequency (89–166 GHz) channels provides the maximum amount of information for snowfall detection. The results demonstrate that, using a multifrequency matching method, the probability of snowfall detection can even be higher than rainfall—chiefly because of the information content of the low-frequency channels that respond to the (near) surface temperature.

**Citation:**

Ebtehaj, A. M., and C. D. Kummerow (2017), Microwave retrievals of terrestrial precipitation over snow-covered surfaces: A lesson from the GPM satellite, *Geophys. Res. Lett.*, 44, 6154–6162, doi:10.1002/2017GL073451.

Received 16 MAR 2017
Accepted 6 JUN 2017
Accepted article online 12 JUN 2017
Published online 27 JUN 2017

## 1. Introduction

Snowfall is the main input for glaciers and snowpack accumulation processes. Observational evidence suggests that, due to increased global mean temperatures, the mass of the glaciers has been reduced worldwide [*Radić et al.*, 2013; Arendt et al., 2014] and the areal extent [*Brown and Robinson*, 2011] and seasonal duration [*Choi et al.*, 2010] of the Northern Hemisphere snow cover have continued to shrink in the past 30 years. Improved understanding of the hydrologic cycle and long-term dynamics of cryosphere requires deeper knowledge about the global patterns in precipitation phase change using satellite observations. However, unlike successful track records in passive infrared [e.g., *Hsu et al.*, 1997; *Kuligowski*, 2002; *Joyce et al.*, 2004] and microwave [e.g., *Kummerow et al.*, 2001; *Petty and Li*, 2013; *Kummerow et al.*, 2015] satellite rainfall retrievals, the problem of microwave precipitation phase detection and snowfall retrieval is still at its early stage of development [e.g., *Liu and Seo*, 2013; *Kongoli et al.*, 2015; *You et al.*, 2017, and references therein]—despite previous operational efforts [*Ferraro et al.*, 2005].

In microwave bands, both snow cover [*Stiles and Ulaby*, 1980; *Ulaby and Stiles*, 1980] and precipitation particles [*Ebert et al.*, 1996] scatter the upwelling surface radiation, enabling remote sensing of their physical characteristics from space. Volume scattering of fresh snow becomes significant over frequencies $\ge$20 GHz [*Stiles and Ulaby*, 1980; *Ulaby and Stiles*, 1980] and monotonically increases up to 150 GHz [*Mätzler*, 1994; *Grody*, 2008]; however, it varies markedly depending on the snow depth, density, particle size, and liquid water content. For example, a small percentage of liquid water ($\sim$1%) content increases the dielectric constant of snow significantly and transforms it into a more emitting medium. Scattering by ice particles in raining clouds often gives rise to depressions in the field of brightness temperatures at high-frequency channels from 80 to 90 GHz [*Grody*, 1991]. This scattering signal has been widely used for operational retrievals of overland rainfall [*Ferraro*, 1997; *Kummerow et al.*, 2001; *Gopalan et al.*, 2010]. Radiative transfer modeling shows that snowfall scattering increases with frequency and approaches its maximum around 150 GHz before strong absorption by water vapor at 183 GHz masks its signal [*Bennartz and Bauer*, 2003; *Skofronick-Jackson and Johnson*, 2011]. Thus, frequencies around 90 and 160 GHz are very useful for snowfall retrievals [e.g., *Noh et al.*, 2006]. However, as explained, both precipitation and snow cover scatter the upwelling radiation over the same

©2017. American Geophysical Union. All Rights Reserved.

EBTEHAJ AND KUMMEROW PRECIPITATION MICROWAVES OVER SNOW COVER 6154


---



19448007, 2017, 12, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1002/2017GL073451 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU logo # Geophysical Research Letters 10.1002/2017GL073451

high frequencies. Proper separation of their signals is often challenging and one of the main sources of large errors in passive microwave retrievals of rain [*Ebtehaj et al.*, 2015, 2016] and snowfall [*Noh et al.*, 2009].

The Tropical Rainfall Measuring Mission [*Kummerow et al.*, 1998] provided invaluable rainfall data within 35° south-north latitudes for two decades from 1997 to 2014. The launch of the Global Precipitation Measurement (GPM) [*Hou et al.*, 2014] satellite, which carries a dual-frequency precipitation radar (DPR, 13 and 35 GHz) and a multifrequency microwave imager (GMI, 10–183 GHz), provides extended coverage within 65° south-north latitudes and thus new avenues for deeper understanding of the precipitation phase change in midlatitudes. This new opportunity comes with scientific and technical challenges for passive precipitation retrievals, chiefly due to complexity of land surface radiometric properties in temperate and cold climate regimes [*Kummerow et al.*, 2015]. This paper uses a year of overland GPM and other ancillary data to provide new insights about radiometric interactions of land and precipitating clouds in microwave bands between 10 and 200 GHz, with particular emphasis on precipitation types and seasonal dynamics of snow cover.

In summary, it is found that the upwelling passive microwave signal of precipitating atmosphere exhibits a transitional regime from emission (warmer than surface) in winter to scattering (colder than surface) in summer in response to snow cover dynamics and precipitation types. It is demonstrated that the snowfall can exhibit emission-like signals over snow cover largely due to reduced surface emission and not because of increased atmospheric liquid water content—commonly observed in snowing clouds over ocean [*Wang et al.*, 2013]. The results denote that the combination of horizontally polarized 10 and 166 GHz channels provides the highest skill for snowfall detection over ground with no snow cover. However, when snow is on ground the most effective high-frequency channel is the horizontal polarization of 89 GHz. Using a multifrequency *k*-nearest neighbor matching method, we show that the probability of snowfall detection may be even higher than the rainfall, chiefly because the snowfall occurrence depends on (near) surface temperature, the variability of which is partly captured by the low- to middle-frequency channels.

## 2. Data

This paper uses the operational GPM Dual-Frequency Radar precipitation product (2A-DPR) and calibrated passive brightness temperatures (1B-GMI) of all orbits in 2015. The radar data provide information about precipitation rates and phases throughout the atmospheric column using dual-wavelengths information at Ku (13 GHz) and Ka (35 GHz) bands [*Iguchi et al.*, 2010]. The ancillary snow cover fraction (MOD10C1 [*Hall et al.*, 2002]) and its skin temperature (MOD11C1 [*Wan*, 2014]) are obtained from the Moderate Resolution Imaging Spectroradiometer (MODIS) sensor on board the Terra satellite at 0.05°. For the GPM orbits, the surface skin temperature, 2 m air temperature, total integrated atmospheric vapor, liquid, and ice water content are acquired from the 1-hourly single-level diagnostic products by the second version of the Modern-Era Retrospective analysis for Research and Applications (MERRA-2-M2I1NXASM) [*Rienecker et al.*, 2011] at resolution 0.625°×0.5°.

## 3. Methodology and Results

The brightness temperatures and all the ancillary data with different spatial resolutions are mapped onto the DPR grids at nominal resolution of 0.05°, using the nearest neighbor interpolation and box averaging. As a result, the radar information remains intact; however, some information of the higher-resolution MODIS data will be lost. The 1-hourly MERRA-2 data are first interpolated linearly onto the GPM radar scanning times and then interpolated onto the radar spatial grids. The snowfall pixels are those that are labeled with solid phase in 2A-DPR product, and their 2 m air temperatures are below 2°C [*Liu*, 2009]. The skin temperatures are used to confine the study to dry snow, which is loosely defined as those snow-covered surfaces with subfreezing skin temperatures. All collocated data are then stratified into a set of six disjoint land-atmosphere classes of interest $\mathcal{C}=\{c_s\}_{s=1}^6$ including ground ($c_1$), rain over ground ($c_2$), snowfall over ground ($c_3$), snow cover ($c_4$), rainfall over snow cover ($c_5$), and snowfall over snow cover ($c_6$). We finally narrow down the data set to almost 25 million randomly sampled pixels that contain layers of GPM observations and the ancillary data over the Northern Hemisphere.

Throughout, we generally explain the patterns in the vector of brightness temperatures based on the mean and variability of their cross-frequency features over the low- (<30 GHz) and high-frequency (>80 GHz) channels. The information content of the low-frequency channels largely encodes the combined effects of

EBTEHAJ AND KUMMEROW PRECIPITATION MICROWAVES OVER SNOW COVER 6155


---



19448007, 2017, 12, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1002/2017GL073451 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

# AGU Geophysical Research Letters

10.1002/2017GL073451

Line charts showing seasonal class mean GMI brightness temperatures for different surface and precipitation conditions.

**Figure 1.** The seasonal class mean GMI brightness temperatures in 2015 for ground ($c_1$), rain over ground ($c_2$), snowfall over ground ($c_3$), snow cover ($c_4$), rainfall over snow cover ($c_5$), and snowfall over snow cover ($c_6$). At the lower left of each subplot, the mean values of surface skin temperatures ($T_s^{c_i}$) and the Euclidean distances between the class mean brightness temperatures ($d_{i,j}$) are shown. The classes are identified using the information from GPM precipitation radar, MODIS snow cover, and ancillary information of the 2 m air temperature from the MERRA-2 reanalysis.

ground surface emissivity and temperature while the high-frequency bands respond primarily to the atmospheric constituents. However, scattering from snow-covered surfaces alters the upwelling radiation over the entire observed spectrum from 20 to 200 GHz. We use the Euclidean distance $d_{i,j} = \|\vec{Tb}_{c_i} - \vec{Tb}_{c_j}\|_2$ to characterize similarity between the $c_i$ and $c_j$'s land-atmosphere classes of interest—where for a column vector of brightness temperatures $\vec{Tb} = (Tb_1, Tb_2, \dots, Tb_p)^T$ at $p$ channels, the Euclidean norm is $\|\vec{Tb}\|_2 = \Sigma_{p=1}^n Tb_p^2$. Clearly, a smaller distance represents a more similar pair of brightness temperatures. It is important to note that the goal is not to exactly quantify the emission or scattering signal of precipitation but rather to better understand the differences between the patterns of brightness temperatures at the top of the atmosphere and provide new insights for improving prognostic microwave snowfall detection algorithms over snow cover.

## 3.1. Precipitation Signal Over Snow Cover

Figure 1 shows the seasonal class mean brightness temperatures in 2015. Figure 1 (left columns) compares the brightness temperatures of snow cover with ground under a nonprecipitating atmosphere. As expected, the snow cover is always radiometrically cooler than the ground because of colder surface temperatures and lower emissivity values. During the winter, the depression in the middle-frequency channels due to snow cover volume scattering reaches to its maximum with 35 K cooling signal at horizontally polarized 89 GHz channel and then decreases over the higher frequencies. While the temperature increases from winter to summer, the snow cover scattering weakens significantly and the snow cover and ground emission become very similar—as the snow ages and its wetness increase throughout the depth. The explained similarity pattern is well captured by the Euclidean metric, which decreases from winter to summer and suggests that the separation of dry snow cover and ground signal might be easier in the winter.

EBTEHAJ AND KUMMEROW

PRECIPITATION MICROWAVES OVER SNOW COVER

6156


---



19448007, 2017, 12, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1002/2017GL073451 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU logo

# Geophysical Research Letters

10.1002/2017GL073451

Figure 1 (middle columns) focuses on the seasonal signatures of precipitation over the ground with no snow cover. Here there are a few important observations. First, while the low-frequency rainfall emission is generally considered to be negligible in passive microwave retrieval algorithms, a significant emission signal is observed from 10 to 36 GHz during the winter—with an average warming effect from 16 to 19 K. Second, the mean snowfall signal is radiometrically cooler than the mean ground emission across all frequencies largely because of colder (near) surface temperatures. Some snowfall scattering signatures are observed at frequencies $\ge$36 GHz, which can be broken down into some minor reduction in brightness temperatures, especially during the summer when the surface emissivity is high, and some degradation of cross-frequency variability or the polarization signal due to diffused scattering of snowfall. Third, due to the temporal dynamics of surface emission, there is a seasonally varying depression frequency (DF) above which the rainfall brightness temperatures are cooler than their ground counterparts. The DF can be as low as 23 GHz in summer and as high as 166 GHz in winter. The Euclidean distance between the snowfall brightness temperatures and the ground is minimum during the winter and gradually increases toward summer. This observation indicates that detection of snowfall during the summer can be more accurate than during the winter, largely because of a notable difference between the summertime surface temperatures in snowing and nonsnowing atmospheres.

In Figure 1 (right columns), an assessment of the precipitation signal over snow cover reveals a more pronounced transition from a wintertime emission to a summertime scattering not only for the rainfall but also for the snowfall. The rainfall and snowfall brightness temperatures are significantly warmer than the ground emission during the winter when the surface temperature and emissivity are low due to fresh snow cover. The MERRA-2 data show that this emission-like signal is not due to a specific increase of the liquid water content during the wintertime precipitation events. In effect, the mean total precipitable liquid water content of the snowfall pixels over snow cover in summer (95 g m<sup>−2</sup>) is higher than that of winter (65 g m<sup>−2</sup>), when no emission signal is detected. Clearly, in winter, the rainfall emission is more pronounced than the snowfall as the reanalysis data indicate that the mean total precipitable liquid water content for the raining pixels (140 g m<sup>−2</sup>) is more than twice that of the snowing ones (65 g m<sup>−2</sup>). For both rain and snowfall, the maximum wintertime emission (warming) and summertime scattering (cooling) occur at horizontally polarized 89 and 166 GHz channel, respectively. The Euclidean distance between the snowfall brightness temperatures and snow cover is maximum during the winter and summer and minimum during the fall and spring, which indicates that the detection of terrestrial snowfall over snow cover may be more accurate during the winter and summer than the other seasons. It appears that during the spring and fall, because of an increase in snow cover emissivity, the low-frequency signatures of snowing and nonsnowing atmospheres become very similar, which may reduce the accuracy of snowfall detection. Interestingly, the magnitude of the Euclidean metric between the snowfall and the snow cover brightness temperatures is greater than that of snowfall and other surface types during the winter, which implies that the wintertime snowfall detection might be more accurate over snow cover than other surfaces.

## 3.2. Channel Importance

To better understand multifrequency distribution of rain and snowfall spectral signatures, we visualize the grouped scatterplots of the brightness temperatures at different channel pairs in Figure 2. This figure shows that the frequency distance is a key for proper separation of different land-atmosphere classes. In other words, visual inspection shows that as the frequency distance begins to increase and the channel pairs become less correlated, the spread of the scatterplots increases and different classes become more distinguishable. To quantify this observation in a 2-D sense, we divide the two-dimensional space of the pairs of the brightness temperatures ($T_{b_p}$, $T_{b_q}$) between channels $p$ and $q$ into differential areas $a^{pq}(i, j)$ of size 2.5 by 2.5 K. Then, we compute the number of pairs of brightness temperatures that fall within $a^{pq}(i, j)$ and assign that area to the class with the highest probability of occurrence. For example, the inset in Figure 2 depicts the highest probability areas of each class, using horizontally polarized 36 and 166 GHz channels. Here we assume that the detection skill of each channel pair is proportional to the total area $A_{c_s}(p, q) = \sum_{i,j \in c_s} a^{pq}(i, j)$ that those channels can discern. For brevity, Figure 3 illustrates the relative importance weight $w_{c_s}(p, q) = A_{c_s}^{pq} / \max_{p,q} (A_{c_s}^{pq})$ only for those classes with a precipitating atmosphere.

Figure 3 (first panel from the left) reveals that for rainfall over the ground, the combinations of horizontally polarized 89 GHz channel with higher-frequency bands provide the maximum separability. This separation skill can be realized because the scattering from ice in the raining atmosphere (cooling) can be captured by channels 89 and 166 GHz, while the sounding channels contain emission signals (warming) of integrated

EBTEHAJ AND KUMMEROW

PRECIPITATION MICROWAVES OVER SNOW COVER

6157


---



19448007, 2017, 12, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1002/2017GL073451 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU logo

# Geophysical Research Letters

10.1002/2017GL073451

Grouped scatterplots of GMI brightness temperatures with inset showing spectral regions for land-atmosphere classes

Figure 2. Grouped scatterplots of the GMI brightness temperatures based on the defined land-atmosphere classes. The inset demonstrates the 2-D spectral regions, spanned by the horizontally polarized 36 and 166 GHz channels, over which the probability of a specific land-atmosphere class is maximum.

precipitable water content. It appears that this anticorrelated response spans a larger space than those by other channel pairs. For detection of snowfall over the ground (Figure 3, second panel from the left), the pair of horizontally polarized 166 and 10 GHz channels provides the maximum separability. It is important to note that, contrary to the rainfall case, the low-frequency channels play an important role in snowfall detection primarily because the occurrence of snowfall depends on (near) surface temperature, which can be partially captured by the middle to lower frequencies. When snow is on the ground, the importance of the middle-frequency channels also increases (e.g., 19 GHz), due to snow cover scattering. For rainfall over the snow cover (Figure 3, third panel from the left) the horizontally polarized 10 and 19 GHz channels paired with 89 GHz band provide the maximum separability. It is seen that the weight of 89 GHz becomes more important

Heatmap panels showing relative importance weights of GMI channel pairs for land-atmosphere classes

Figure 3. (first to fourth panels) Relative importance weights $w_{c_s} (p, q) \in [0, 1]$ of the GMI channel pairs $(p, q)$ for passive separation of the land-atmosphere classes of interest with a precipitating atmosphere. The weights are proportional to the area of spectral regions over which a specific class exhibits the highest probability of occurrence.

EBTEHAJ AND KUMMEROW

PRECIPITATION MICROWAVES OVER SNOW COVER

6158
6158


---



AGU logo Geophysical Research Letters 10.1002/2017GL073451

19448007, 2017, 12, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1002/2017GL073451 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

Table 1. The Conditional Probability of Detection (False Alarm), Using the Proposed *k*-Nearest Neighbor Approach for Detection of Ground ($c_1$), Rain Over Ground ($c_2$), Snowfall Over Ground ($c_3$), Snow Cover ($c_4$), Rainfall Over Snow Cover ($c_5$), and Snowfall Over Snow Cover ($c_6$)<sup>a</sup>

<table>
  <thead>
    <tr>
        <th> </th>
        <th colspan="4">Predicted</th>
    </tr>
<tr>
        <th> </th>
        <th>c1</th>
        <th>c2</th>
        <th colspan="2">c3</th>
    </tr>
<tr>
        <th rowspan="3">Actual</th>
        <th>c1</th>
        <th>0.88(0.05)</th>
        <th>0.05</th>
        <th>0.07</th>
    </tr>
<tr>
        <th>c2</th>
        <th>0.08</th>
        <th>0.87(0.03)</th>
        <th>0.05</th>
    </tr>
<tr>
        <th>c3</th>
        <th>0.01</th>
        <th>0.01</th>
        <th>0.98(0.06)</th>
    </tr>
  </thead>
</table>

<table>
  <thead>
    <tr>
        <th> </th>
        <th colspan="4">Predicted</th>
    </tr>
<tr>
        <th> </th>
        <th>c4</th>
        <th>c5</th>
        <th colspan="2">c6</th>
    </tr>
<tr>
        <th rowspan="3">Actual</th>
        <th>c4</th>
        <th>0.82(0.05)</th>
        <th>0.05</th>
        <th>0.13</th>
    </tr>
<tr>
        <th>c5</th>
        <th>0.06</th>
        <th>0.89(0.04)</th>
        <th>0.05</th>
    </tr>
<tr>
        <th>c6</th>
        <th>0.04</th>
        <th>0.03</th>
        <th>0.93(0.09)</th>
    </tr>
  </thead>
</table>

<sup>a</sup>The probabilities are obtained knowing that whether snow cover exists or not.

than 166 GHz for detection of rainfall over the snow cover, likely this frequency contains more information about the snow cover signatures. The patterns of channel importance for snowfall over snow cover are very similar to the snowfall over the ground. However, 89 GHz channels gain more weights due to their sensitivity to the snow cover scattering. These normalized weights can be used to form a symmetric class specific weight matrix **W**$_{c_s} = [w_{c_s}(p, q)]$, where $w_{c_s}(p, q) = w_{c_s}(q, p)$ and $w_{c_s}(p, p) = \sum_q w_{c_s}(p, q)$. This matrix is positive semidefinite based on the Gershgorin circle theorem [*Gershgorin*, 1931] and can be used to represent the relative importance of channel pairs for prognostic passive precipitation phase detection.

## 3.3. Precipitation Phase Detection

So far, we have revealed the seasonal patterns of the class mean brightness temperatures, their similarity in terms of the Euclidean distance, and quantified the importance of each channel pair in detection of six different land-atmosphere classes of interest. Now the question is how we may exploit the produced information for prognostic precipitation phase detection with and without the snow cover. Here we provide preliminary evidence that a *k*-nearest neighbor matching that uses a weighted Euclidean distance metric can be used for this purpose with unprecedented accuracy—without relying on any online ancillary data. To this end, let us reduce the data set to a library $\mathcal{L} = \left\{ \left( \vec{Tb}^m, c_s^m \right) \right\}_{m=1}^M$, where each pair $\left( \vec{Tb}^m, c_s^m \right)$ represents the $m^{th}$ pixel-level vector of brightness temperatures and its associated land-atmosphere class of interest. Here $M$ represents 80% of the entire data set, and we consider the remainder for the validation purpose and stored them in $\mathcal{L}^V = \left\{ \left( \vec{y}^n, x_s^n \right) \right\}_{n=1}^N$, in which the vector of brightness temperatures and their associated land-atmosphere classes are denoted by $\vec{y}^n$ and $x_s^n$—for notational convenience. For each $\vec{y}$, we first isolate its *k*-nearest neighbors in $\left\{ \vec{Tb}^m \right\}_{m=1}^M$ using the weighted Euclidean distance $d_{c_s}^m = \left( \vec{y} - \vec{Tb}^m \right)^T \mathbf{W}_{c_s} \left( \vec{y} - \vec{Tb}^m \right)$. Then, we look into the land-atmosphere class of those *k*-nearest neighbors $\left\{ c_s^m \right\}_{m=1}^k$ and estimate the class $\hat{x}_s$ of $\vec{y}$ using a majority vote rule. By comparing $\hat{x}_s^n$ and $x_s^n$ for all $n = 1, \dots, N$ number of validation pairs, Table 1 summarizes the probability of detection and false alarm for $k = 20$. The computed probabilities are not excessively sensitive to the values of $k$ greater than 20, but certainly further investigations are needed for any operational implementation.

Perhaps, the most important message from Table 1 is that the detection of terrestrial snowfall can be even more accurate than the rainfall using the *k*-nearest neighbor method. The main reason is that the snowfall brightness temperatures can be distinguished from the surface emission slightly better than the rainfall when all-frequency channels are properly used. In Figure 1, we can see across multiple seasons, the total distance of snowfall signatures from the ground emission is greater than its rainfall counterpart, largely due to the role of the low-frequency channels. Figure 4 shows the preliminary results of the proposed approach for two different storms captured by GPM overpasses. The results can be visually compared with reference observations obtained from coincident ground-based Multiradar/Multisensor System (MRMS). Even though, a thorough investigation is needed to fully characterize the performance of the explained approach, the initial results are certainly promising for prognostic precipitation phase detection over snow cover.

EBTEHAJ AND KUMMEROW PRECIPITATION MICROWAVES OVER SNOW COVER 6159


---



19448007, 2017, 12, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1002/2017GL073451 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU logo

# Geophysical Research Letters

10.1002/2017GL073451

Precipitation phase detection maps comparing DPR, MRMS, and KNN methods over snow cover for two GPM overpasses.

Figure 4. Results of precipitation phase detection over snow cover for two GPM overpasses (top row: 21 November 2016, orbit #10412 and bottom row: 28 December 2015, #9833) by the standard 2A-DPR product, ground-based Multiradar/Multisensor System (MRMS), and the proposed nearest neighbor (KNN) approach. The snow cover maps in the fourth column are from the standard 2A-GPROF-GMI product [Kummerow et al., 2015], which uses the NOAA’s AutoSnow product [Romanov et al., 2000].

## 4. Discussion and Conclusions

It is important to note that the data set used and the results presented are not free of error, and thus the following discussion should be interpreted accordingly, especially with respect to the uncertainties that may arise as a result of data projection at different resolutions onto the radar grids.

One of the most important observations was the temporal dependence of the depression frequencies to snow cover dynamics and precipitation types. As a result, any effort to design new thresholding methods for precipitation phase detection *Seto et al.*, 2005 [see 2005] shall account for this temporal variability. We also found that during the winter, the warm precipitation signal can be better distinguished from the emission of fresh snow cover than the emission of other surface types. We demonstrated that the combinations of low- and high-frequency channels are critical for snowfall detection. Further understanding of this observation certainly requires in depth physical modeling of land surface structural characteristics and atmospheric radiative transfer properties. However, from a data science point of view, when the nearby channel pairs (e.g., 10 and 19 GHz) are strongly correlated, they cannot provide proper detection capabilities. When the frequency distance becomes larger (i.e., 10 and 166 GHz), the channels begin to respond in a less correlated way and thus provide improved detection skills. Among the low-frequency channels, the horizontally polarized 10 GHz channel seems to encode important surface information for snowfall detection. This might be due to the fact that this channel partly captures variability of (near) surface temperatures, but the surface emissivity does not drastically vary as a function snow cover metamorphism at this frequency. It is worth nothing that the channel weights may also exhibit some seasonal dependencies to the changes of land surface radiometric properties. Moreover, maximum probability of occurrence was used to characterize the channel importance, which can be extended to a weighted mixture of probabilities for better addressing the relative importance of those channel pairs with significant spectral overlapping. The preliminary results of the *k*-nearest neighbor method for snowfall detection seem very promising and calls for more detailed studies that might help to develop future generation of operational microwave snowfall retrieval algorithms.

EBTEHAJ AND KUMMEROW

PRECIPITATION MICROWAVES OVER SNOW COVER

6160
6160


---



19448007, 2017, 12, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1002/2017GL073451 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU logo

# Geophysical Research Letters

10.1002/2017GL073451

## Acknowledgments

The authors acknowledge the support (NNX16AO56G) from the NASA Precipitation Measurement Missions through R. Kakar. GPM data (version 4) are provided courtesy of the NASA Precipitation Processing System at the Goddard Space Flight center ([https://pmm.nasa.gov/data-access/](https://pmm.nasa.gov/data-access/)). The MERRA-2 and MODIS data are from the Goddard Earth Sciences and Information Service Center ([https://disc.sci.gsfc.nasa.gov/mdisc/](https://disc.sci.gsfc.nasa.gov/mdisc/)) and the Land Processes Distributed Active Archive Center by the USGS ([https://lpdaac.usgs.gov/data_access/data_pool](https://lpdaac.usgs.gov/data_access/data_pool)). The authors would like to thank Zeinab Takbiri for her help, Pierre Kirstetter at the University of Oklahoma for providing us the MRMS data, and Efi Foufoula-Georgiou at the University of California-Irvine for her support and offered insights.

## References

Arendt, A. A., et al. (2014), Randolph glacier inventory—A dataset of global glacier outlines: Version 4.0, *Tech. Rep.*, Global Land Ice Meas. from Space, Boulder, Colo., doi:10.1017/CBO9781107415324.004.

Bennartz, R., and P. Bauer (2003), Sensitivity of microwave radiances at 85–183 GHz to precipitating ice particles, *Radio Sci.*, *38*(4), 8075, doi:10.1029/2002RS002626.

Brown, R. D., and D. A. Robinson (2011), Northern Hemisphere spring snow cover variability and change over 1922–2010 including an assessment of uncertainty, *Cryosphere*, *5*(1), 219–229, doi:10.5194/tc-5-219-2011.

Choi, G., D. A. Robinson, and S. Kang (2010), Changing Northern Hemisphere snow seasons, *J. Clim.*, *23*(19), 5305–5310, doi:10.1175/2010JCLI3644.1.

Ebert, E. E., M. J. Manton, P. A. Arkin, R. J. Allam, G. E. Holpin, and A. Gruber (1996), Results from the GPCP algorithm intercomparison programme, *Bull. Am. Meteorol. Soc.*, *77*(12), 2875–2887, doi:10.1175/1520-0477(1996)077<2875:RFTGAI>2.0.CO;2077%3C2875:RFTGAI%3E2.0.CO;2).

Ebtehaj, A. M., R. L. Bras, and E. Foufoula-Georgiou (2015), Shrunken locally linear embedding for passive microwave retrieval of precipitation, *IEEE Trans. Geosci. Remote Sens.*, *53*(7), 3720–3736, doi:10.1109/TGRS.2014.2382436.

Ebtehaj, A. M., R. L. Bras, and E. Foufoula-Georgiou (2016), Evaluation of ShARP passive rainfall retrievals over snow-covered land surfaces and coastal zones, *J. Hydrometeorol.*, *17*, 1013–1029, doi:10.1175/JHM-D-15-0164.1.

Ferraro, R. R. (1997), Special sensor microwave imager derived global rainfall estimates for climatological applications, *J. Geophys. Res.*, *102*, 16,715–16,735, doi:10.1029/97JD01210.

Ferraro, R. R., F. Weng, N. C. Grody, L. Zhao, H. Meng, C. Kongoli, P. Pellegrino, S. Qiu, and C. Dean (2005), NOAA operational hydrological products derived from the advanced microwave sounding unit, *IEEE Trans. Geosci. Remote Sens.*, *43*, 1036–1048, doi:10.1109/TGRS.2004.843249.

Gershgorin, S. (1931), Ueber die Abgrenzung der Eigenwerte einer Matrix, *Izv. Akad. Nauk. SSSR Ser. Mat.*, *1*, 749–754.

Gopalan, K., N. Y. Wang, R. Ferraro, and C. Liu (2010), Status of the TRMM 2A12 land precipitation algorithm, *J. Atmos. Oceanic Technol.*, *27*(8), 1343–1354, doi:10.1175/2010JTECHA1454.1.

Grody, N. (2008), Relationship between snow parameters and microwave satellite measurements: Theory compared with advanced microwave sounding unit observations from 23 to 150 GHz, *J. Geophys. Res.*, *113*, D22108, doi:10.1029/2007JD009685.

Grody, N. C. (1991), Classification of snow cover and precipitation using the special sensor microwave imager, *J. Geophys. Res.*, *96*(D4), 7423–7435, doi:10.1029/91JD00045.

Hall, D. K., G. A. Riggs, V. V. Salomonson, N. E. DiGirolamo, and K. J. Bayr (2002), MODIS snow-cover products, *Remote Sens. Environ.*, *83*(1–2), 181–194, doi:10.1016/S0034-4257(02)00095-000095-0).

Hou, A. Y., R. K. Kakar, S. Neeck, A. A. Azarbarzin, C. D. Kummerow, M. Kojima, R. Oki, K. Nakamura, and T. Iguchi (2014), The global precipitation measurement mission, *Bull. Am. Meteorol. Soc.*, *95*(5), 701–722, doi:10.1175/BAMS-D-13-00164.1.

Hsu, K.-l., X. Gao, S. Sorooshian, and H. V. Gupta (1997), Precipitation estimation from remotely sensed information using artificial neural networks, *J. Appl. Meteorol.*, *36*(9), 1176–1190, doi:10.1175/1520-0450(1997)036<1176:PEFRSI>2.0.CO;2036%3C1176:PEFRSI%3E2.0.CO;2).

Iguchi, T., S. Seto, R. Meneghini, N. Yoshida, J. Awaka, and T. Kubota, (2010), GPM/DPR level-2 algorithm theoretical basis document, *Tech. Rep.* Available at [https://pmm.nasa.gov/sites/default/files/document_files/ATBD_GPM_DPR_n3_dec15.pdf.]

Joyce, R. J., J. E. Janowiak, P. A. Arkin, and P. Xie (2004), CMORPH: A method that produces global precipitation estimates from passive microwave and infrared data at high spatial and temporal resolution, *J. Hydrometeorol.*, *5*(3), 487–503, doi:10.1175/1525-7541(2004)005<0487:CAMTPG>2.0.CO;2005%3C0487:CAMTPG%3E2.0.CO;2).

Kongoli, C., H. Meng, J. Dong, and R. Ferraro (2015), A snowfall detection algorithm over land utilizing high-frequency passive microwave measurements—Application to ATMS, *J. Geophys. Res. Atmos.*, *120*, 1918–1932, doi:10.1002/2014JD022427.

Kuligowski, R. J. (2002), A self-calibrating real-time goes rainfall algorithm for short-term rainfall estimates, *J. Hydrometeorol.*, *3*(2), 112–130, doi:10.1175/1525-7541(2002)003<0112:ASCRTG>2.0.CO;2003%3C0112:ASCRTG%3E2.0.CO;2).

Kummerow, C., W. Barnes, T. Kozu, J. Shiue, and J. Simpson (1998), The Tropical Rainfall Measuring Mission (TRMM) sensor package, *J. Atmos. Oceanic Technol.*, *15*(3), 809–817, doi:10.1016/0273-1177(94)90210-090210-0).

Kummerow, C., Y. Hong, W. S. Olson, S. Yang, R. F. Adler, J. McCollum, R. Ferraro, G. Petty, D.-B. Shin, and T. T. Wilheit (2001), The evolution of the Goddard Profiling Algorithm (GPROF) for rainfall estimation from passive microwave sensors, *J. Appl. Meteorol.*, *40*(11), 1801–1820, doi:10.1175/1520-0450(2001)040<1801:TEOTGP>2.0.CO;2040%3C1801:TEOTGP%3E2.0.CO;2).

Kummerow, C. D., D. L. Randel, M. Kulie, N.-Y. Wang, R. Ferraro, S. Joseph Munchak, and V. Petkovic (2015), The evolution of the Goddard Profiling Algorithm to a fully parametric scheme, *J. Atmos. Oceanic Technol.*, *32*(12), 2265–2280, doi:10.1175/JTECH-D-15-0039.1.

Liu, G. (2009), Deriving snow cloud characteristics from CloudSat observations, *J. Geophys. Res.*, *114*, DO0A09, doi:10.1029/2007JD009766.

Liu, G., and E.-K. Seo (2013), Detecting snowfall over land by satellite high-frequency microwave observations: The lack of scattering signature and a statistical approach, *J. Geophys. Res. Atmos.*, *118*, 1376–1387, doi:10.1002/jgrd.50172.

Mätzler, C. (1994), Passive microwave signatures of landscapes in winter, *Meteorol. Atmos. Phys.*, *54*(1–4), 241–260, doi:10.1007/BF01030063.

Noh, Y.-J., G. Liu, E.-K. Seo, J. R. Wang, and K. Aonashi (2006), Development of a snowfall retrieval algorithm at high microwave frequencies, *J. Geophys. Res.*, *111*, D22216, doi:10.1029/2005JD006826.

Noh, Y. J., G. Liu, A. S. Jones, and T. H. V. Haar (2009), Toward snowfall retrieval over land by combining satellite and in situ measurements, *J. Geophys. Res. Atmos.*, *114*, D24205, doi:10.1029/2009JD012307.

Petty, G. W., and K. Li (2013), Improved passive microwave retrievals of rain rate over land and Ocean. Part I: Algorithm description, *J. Atmos. Oceanic Technol.*, *30*(11), 2493–2508, doi:10.1175/JTECH-D-12-00144.1.

Radic, V., A. Bliss, A. C. Beedlow, R. Hock, E. Miles, and J. G. Cogley (2013), Regional and global projections of twenty-first century glacier mass changes in response to climate scenarios from global climate models, *Clim. Dyn.*, *42*, 37–58, doi:10.1007/s00382-013-1719-7.

Rienecker, M. M., et al. (2011), MERRA: NASA’s Modern-Era Retrospective analysis for Research and Applications, *J. Clim.*, *24*(14), 3624–3648, doi:10.1175/JCLI-D-11-00015.1.

Romanov, P., G. Gutman, and I. Csiszar (2000), Automated monitoring of snow cover over North America with multispectral satellite data, *J. Appl. Meteorol.*, *39*(11), 1866–1880, doi:10.1175/1520-0450(2000)039<1866:AMOSCO>2.0.CO;2039%3C1866:AMOSCO%3E2.0.CO;2).

Seto, S., N. Takahashi, and T. Iguchi (2005), Rain/no-rain classification methods for microwave radiometer observations over land using statistical information for brightness temperatures under no-rain conditions, *J. Appl. Meteorol.*, *44*(8), 1243–1259, doi:10.1175/JAM2263.1.

Skofronick-Jackson, G., and B. T. Johnson (2011), Surface and atmospheric contributions to passive microwave brightness temperatures for falling snow events, *J. Geophys. Res.*, *116*, D02213, doi:10.1029/2010JD014438.

Stiles, W. H., and F. T. Ulaby (1980), The active and passive microwave response to snow parameters: 1. Wetness, *J. Geophys. Res.*, *85*(C2), 1037–1044, doi:10.1029/JC085iC02p01037.

EBTEHAJ AND KUMMEROW

PRECIPITATION MICROWAVES OVER SNOW COVER

6161


---



19448007, 2017, 12, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1002/2017GL073451 by Capes, Wiley Online Library on [16/07/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

AGU logo

# 

 Geophysical Research Letters 

 10.1002/2017GL073451

Ulaby, F. T., and W. H. Stiles (1980), The active and passive microwave response to snow parameters: 2. Water equivalent of dry snow, *J. Geophys. Res.*, *85*(C2), 1045–1049, doi:10.1029/JC085iC02p01045.

You, Y., N. Wang, R. Ferraro, and S. Rudlosky (2017), Quantifying the snowfall detection performance of the GPM microwave imager channels over land, *J. Hydrometeorol.*, *18*(3), 729–751, doi:10.1175/JHM-D-16-0190.1.

Wan, Z. (2014), New refinements and validation of the collection-6 MODIS land-surface temperature/emissivity product, *Remote Sens. Environ.*, *140*, 36–45, doi:10.1016/j.rse.2013.08.027.

Wang, Y., G. Liu, E.-K. Seo, and Y. Fu (2013), Liquid water in snowing clouds: Implications for satellite remote sensing of snowfall, *Atmos. Res.*, *131*, 60–72, doi:10.1016/j.atmosres.2012.06.008.

EBTEHAJ AND KUMMEROW

PRECIPITATION MICROWAVES OVER SNOW COVER

6162
