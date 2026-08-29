

Climate Dynamics (2018) 51:3673–3684
https://doi.org/10.1007/s00382-018-4103-9

CrossMark logo

# Moist convection: a key to tropical wave–moisture interaction in Indian monsoon intraseasonal oscillation

Longtao Wu<sup>1</sup> · Sun Wong<sup>1</sup> · Tao Wang<sup>1,2,3</sup> · George J. Huffman<sup>2</sup>

Received: 25 April 2017 / Accepted: 21 January 2018 / Published online: 29 January 2018
© Springer-Verlag GmbH Germany, part of Springer Nature 2018

## Abstract

Simulation of moist convective processes is critical for accurately representing the interaction among tropical wave activities, atmospheric water vapor transport, and clouds associated with the Indian monsoon Intraseasonal Oscillation (ISO). In this study, we apply the Weather Research and Forecasting (WRF) model to simulate Indian monsoon ISO with three different treatments of moist convective processes: (1) the Betts–Miller–Janjić (BMJ) adjustment cumulus scheme without explicit simulation of moist convective processes; (2) the New Simplified Arakawa–Schubert (NSAS) mass-flux scheme with simplified moist convective processes; and (3) explicit simulation of moist convective processes at convection permitting scale (Nest). Results show that the BMJ experiment is unable to properly reproduce the equatorial Rossby wave activities and the corresponding phase relationship between moisture advection and dynamical convergence during the ISO. These features associated with the ISO are approximately captured in the NSAS experiment. The simulation with resolved moist convective processes significantly improves the representation of the ISO evolution, and has good agreements with the observations. This study features the first attempt to investigate the Indian monsoon at convection permitting scale.

# 1 Introduction

The Indian summer monsoon (ISM) brings 80% of annual precipitation to the Indian continent between June and September (Turner and Annamalai 2012). Substantial component of the ISM precipitation is contributed by its intraseasonal oscillation (ISO), which is characterized by the prolonged wet (active phases) and dry (break phases) spells lasting for 2–3 weeks (Goswami 2005; Rajeevan et al. 2010). Therefore, accurate prediction of the ISM and its variabilities is important for local agriculture, water management and economy.

Northward propagation of convective systems, from the tropical Indian Ocean to the Indian continent and Bay of Bengal (BOB), is generally present associated with the

ISO (Lawrence and Webster 2002; Jiang et al. 2004, 2011; Goswami 2005; Wong et al. 2011). The mechanism of the northward propagation involves a positive vorticity anomaly and the associated low-level moisture convergence, which reduces the stability of the atmosphere to the north of the convective system (Jiang et al. 2004, 2011; Goswami 2005; Wong et al. 2011). The moisture–convection-circulation feedback facilitates the northward propagation of the convection system (Jiang et al. 2004, 2011; Goswami 2005).

For successful simulation of the ISO, it is critical to appropriately represent moisture processes and the associated convection (e.g. Jiang et al. 2004; Del Genio et al. 2012b; Wang et al. 2015). Wong et al. (2016) constructed a water-budget related phase space, spanned by moisture dynamical convergence ($Q_{cnvg}$) and moisture advection ($Q_{advt}$), for studying cloud and precipitation responses to the large-scale circulation. Wang et al. (2015) applied this phase space on ISM to show that the wet/dry spells of the ISO are primarily controlled by $Q_{cnvg}$, while preconditioning by $Q_{advt}$ leading $Q_{cnvg}$ in 4–6 days triggers the development of convection toward ISO peaks. The covariation of $Q_{cnvg}$ and $Q_{advt}$ identifies different phases of the ISO in the water-budget related phase space (Wang et al. 2015).

Benefited from increasing computation capability and improved model physical processes (Murthi et al. 2011),

\* Longtao Wu
Longtao.Wu@jpl.nasa.gov

<sup>1</sup> Jet Propulsion Laboratory, California Institute of Technology, 4800 Oak Grove Dr., Pasadena, CA 91109, USA

<sup>2</sup> NASA Goddard Space Flight Center, Greenbelt, MD 20771, USA

<sup>3</sup> Earth System Science Interdisciplinary Center, University of Maryland, College Park,, MD 20742, USA

Springer logo


---



3674

L. Wu et al.

substantial progresses have been made in recent decades to simulate the ISM (Sabeerali et al. 2013; Sperber et al. 2013; Neena et al. 2017). However, it is still challenging for current state-of-the-art general circulation models (GCMs) to accurately simulate the ISM and its variability (Sabeerali et al. 2013; Sperber et al. 2013; Neena et al. 2017), partly because coarse resolution of the GCMs is unable to resolve small spatial scale of orography and convective processes over the Indian continent (Waliser et al. 2003; Ramu et al. 2016). In recent years, there is increasing interest in using regional climate models (RCMs) to study the ISM at relatively higher (between 15 and 50 km) horizontal resolution (e.g., Ratnam and Krishna Kumar 2005; Mukhopadhyay et al. 2010; Murthi et al. 2011; Taraphdar et al. 2010; Lucas-Picher et al. 2011; Srinivas et al. 2013; Samala et al. 2013; Raju et al. 2015a, b; Unnikrishnan et al. 2015; Umakanth et al. 2016). Previous studies have demonstrated that RCMs can represent spatial and temporal variations of the ISM with some discrepancies. The coupling of land surface and atmosphere has significant impacts on climate variability of the ISM (Unnikrishnan et al. 2015). Simulations can be improved by coupling to an ocean model with improved representation of sea surface temperature (Samala et al. 2013). Moisture advection is a critical factor for correctly capturing northward propagating of the ISO (Umakanth et al. 2016). Simulation of the ISM and its variabilities is quite sensitive to cumulus parameterization (Ratnam and Krishna Kumar 2005; Mukhopadhyay et al. 2010; Srinivas et al. 2013; Raju et al. 2015b; Umakanth et al. 2016). Predictability of active/break phases ranges from 4 to 10 days in the Weather Research and Forecasting (WRF) model, with better predictability during break phases than during active phases (Taraphdar et al. 2010).

The WRF model is one of the frequently used RCMs in simulating the ISM. Raju et al. (2015a) evaluated dynamic and thermodynamic processes associated with the ISM in a 45-km WRF simulation. The cumulus scheme selected was the commonly used Betts–Miller–Janjić (BMJ) scheme (Janjić 1994, 2000), which has better simulation of the ISM climatology than the Grell–Devenyi (Grell and Devenyi 2002) scheme and the Kain–Fritsch (Kain 2004) scheme (Mukhopadhyay et al. 2010; Srinivas et al. 2013). Their simulation reasonably captured seasonal mean precipitation and vertical structures of temperature and moisture (Raju et al. 2015a). Spatial pattern of precipitation and wind associated with the ISO was also reproduced. However, the simulation failed to represent gradual preconditioning in the lower troposphere during active phases of the ISO.

This study extends the framework of using the water-budget related phase space (Wong et al. 2016; Wang et al. 2015) to diagnose the interaction between tropical wave activities and moist convective processes in the ISO simulated by different treatments of cumulus convection in the WRF model. The treatments of cumulus convection include

an adjustment scheme (the BMJ scheme), a mass-flux scheme (New Simplified Arakawa–Schubert, NSAS; Han and Pan 2011), and a simulation with a nested domain at convection permitting scale. To our knowledge, this study represents the first attempt of simulating the ISM at convection permitting scale. Section 2 describes the validation datasets used in this study. Model setup and experiment design are documented in Sect. 3. Model results are presented in Sect. 4. Section 5 is the summary and discussion.

# 2 Validation datasets

The precipitation product used in this study is the daily Tropical Rainfall Measuring Mission (TRMM) multi-satellite precipitation analysis 3B42 V7 at 0.25° × 0.25° spatial resolution (Huffman et al. 2007). Note that the magnitude of the TRMM precipitation is biased low over the Indian continent compared with the daily gridded precipitation data from the India Meteorological Department (IMD), possibly due to fewer station observations used in the TRMM product (Mukhopadhyay et al. 2010; Srinivas et al. 2013). The IMD dataset is not used in this study because it has no coverage over the ocean. Model bias in magnitude of precipitation discussed in this study should be interpreted with caution. Our analysis will focus on relative variation of precipitation. The cloud top pressure (CTP) data are from the Aqua Moderate Resolution Imaging Spectroradiometer (MODIS) product collection 6 at 5 km scenes (King et al. 2013).

The variables to represent large-scale moisture transport ($Q_{cnvg}$ and $Q_{advt}$) are derived as described by Wong et al. (2016) using the Modern Era Retrospective-Analysis for Research and Applications Version 2 (MERRA-2; Bosilovich et al. 2016; GMAO 2015) at 0.625° × 0.5° horizontal resolution. Conservation of atmospheric water budget (Peixoto and Oort 1992) requires

$$ P - E + \frac{\partial Q_{col}}{\partial t} = -\nabla \cdot (Q_{col} \vec{V}) = -\left( Q_{col} \nabla \cdot \vec{V} \right) + \left( -\vec{V} \cdot \nabla Q_{col} \right) \equiv Q_{cnvg} + Q_{advt} \quad (1) $$

where $P$ is precipitation, $E$ is surface evaporation, $Q_{col} = \int_{P_{top}}^{P_{surf}} q \frac{dp}{g}$ represents the column-integrated specific humidity $q$, $\vec{V} = \frac{1}{Q_{col}} \int_{P_{top}}^{P_{surf}} (\vec{u}q) \frac{dp}{g}$ is the column-integrated horizontal winds, $\vec{u}$, weighted by the specific humidity vertical profiles, and $g$ is the gravitational acceleration.

Springer logo

Springer
1 3


---



Moist convection: a key to tropical wave–moisture interaction in Indian monsoon intraseasonal…

3675

# 3 Model setup and experiment design

The Advanced Research WRF version V3.6 (Skamarock et al. 2008) is used in this study. The WRF model integrates non-hydrostatic, compressible dynamic equations on an Arakawa C-grid using a terrain-following hydrostatic pressure vertical coordinate. Various selections of physical parameterizations are available in the WRF model. The physical parameterizations used in this study are similar to the regional climate study of Wu et al. (2015), including the WRF Single-Moment 6-class (WSM-6) microphysical scheme (Hong and Lim 2006), the Yonsei University (YSU) planetary boundary layer scheme (Hong et al. 2006), the Community Atmosphere Model (CAM) shortwave and longwave schemes (Collins et al. 2004), and the unified Noah land surface scheme (Chen et al. 1996).

The BMJ cumulus scheme mostly used in the WRF simulations of the ISM (e.g. Mukhopadhyay et al. 2010; Srinivas et al. 2013) is applied in this study in a set of simulations at 0.2° horizontal resolution (this set of experiments is referred to as “BMJ” hereafter). The BMJ cumulus scheme is a column moist adjustment scheme without explicitly simulating convective processes (Janjić 1994122%3C0927:TSASCO%3E2.0.CO;2), 2000128%3C3605:COTCBM%3E2.0.CO;2); Lackmann 2016). The preconditioning of convective environment is simulated in the shallow convection component of the BMJ scheme by moving moisture upward without precipitating, leading to drying at the cloud base and moistening at the cloud top. The deep convection component relaxes temperature and moisture profiles to a well-mixed reference state, and produces precipitation with a conservation of enthalpy. The reference temperature and moisture profiles and relaxation time are functions of cloud efficiency. Because the BMJ scheme does not explicitly predict cloud processes except modifying relative humidity, propagation of organized convections may not be properly represented in the model (Lackmann 2016).

As shown in Raju et al. (2015a) and our following analyses, the evolution of the ISO is not correctly simulated in experiments with the BMJ scheme. Another set of simulations is performed at 0.2° horizontal resolution using the NSAS cumulus scheme (this set of experiments is referred to as “NSAS” hereafter). The NSAS cumulus parameterization (Han and Pan 2011) is a bulk mass-flux scheme with explicit representation of convective processes at each grid point. The mass, moist static energy and moisture in shallow and deep convections are simulated in a 1-D cloud model. In order to reduce excessive heavy precipitation simulated in the old Simplified Arakawa–Schubert scheme, stronger and deeper convection is produced in the NSAS scheme to deplete more atmospheric instability.

For further assessing the impacts of model resolution and moist convective processes, a third set of simulations is run with a mother domain the same as the NSAS run, and

Coverage of the model domains with terrain height (m) in color shading.

Fig. 1 Coverage of the model domains with terrain height (m) in color shading. The outer box covers the model domain of the BMJ and NSAS runs and the outer domain of the Nest run. The inner black box shows the nested domain of the Nest simulation with terrain height at 0.04° horizontal resolution. The blue dashed box represents the interested region over the Indian subcontinent sector discussed in this paper

a nested domain at 0.04° horizontal resolution covering the Indian subcontinent sector and the surrounding regions (this set of experiments is referred to as “Nest” hereafter). The coverage of the model domains is shown in Fig. 1. The NSAS cumulus scheme is used in the mother domain, while convective clouds are resolved in the nested domain. The nested domain provides feedbacks to the mother domain through a two-way nesting method. For a fair comparison, we focus on the simulations in the mother domain for all the experiments.

For each set of the experiments, we run five ensembles of simulations from 2011 to 2015, with the model initialized on May 1 and ended on October 1 of each year. There are 40 vertical model levels with a top at 100 hPa. The initial and boundary conditions for the model simulations are provided by the 6-hourly European Center for Medium-Range Weather Forecasts (ECMWF) Interim reanalysis (ERA-Interim) data (Dee et al. 2011).

# 4 Results

## 4.1 Mean monsoon precipitation

Figure 2 features the WRF simulated precipitation over the ISM regions comparing to TRMM observations averaged in May–September for 2011–2015. All of the simulations

Springer logo

3


---



3676

L. Wu et al.

**Fig. 2** Mean precipitation (mm day<sup>−1</sup>) in May–September for 2011–2015 from **a** TRMM; **b** BMJ; **c** NSAS; **d** Nest

Four maps showing mean precipitation in South Asia and the Indian Ocean for TRMM, BMJ, NSAS, and Nest models, with a color scale from 1 to 30 mm day−1.

roughly capture the distribution patterns, including heavy precipitation over the Western Ghats, moderate precipitation over the BOB and the northeast India, and relatively dry regions over the central India. Excessive precipitation compared with TRMM is simulated over ocean in all the WRF runs, consistent with other WRF studies (e.g. Mukhopadhyay et al. 2010; Srinivas et al. 2013; Wu et al. 2013). The BMJ run (Fig. 2b) produces the highest precipitation among the simulations, while the simulated rainfall maximum over the BOB shifts to the west of that in the observations. Comparing to the BMJ run, the NSAS run (Fig. 2c) exhibits more intense precipitation over the Western Ghats with sharp contrast between land and ocean, and less precipitation over the

BOB with the precipitation center closer to the observation. Spurious precipitation is shown over the central India in the NSAS run. Due to the identical model settings in the mother domain, the large-scale distribution of precipitation in the Nest run (Fig. 2d) is largely similar to that of the NSAS run. The better resolved topography and convective processes in the nested domain leads to gradual variation of precipitation from the Western Ghats to the ocean. The spurious precipitation over the central Indian is also eliminated, with comparable precipitation amount to TRMM. However, the magnitude of precipitation is underestimated over the northeast India compared to TRMM.

Springer logo Springer


---



Moist convection: a key to tropical wave–moisture interaction in Indian monsoon intraseasonal…

3677

<table>
  <thead>
    <tr>
        <th>Month</th>
        <th>TRMM</th>
        <th>BMJ</th>
        <th>NSAS</th>
        <th>Nest</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>May</td>
<td>2</td>
<td>2</td>
<td>1</td>
<td>1</td>
    </tr>
<tr>
        <td>Jun</td>
<td>8</td>
<td>8</td>
<td>4</td>
<td>4</td>
    </tr>
<tr>
        <td>Jul</td>
<td>10</td>
<td>15</td>
<td>8</td>
<td>8</td>
    </tr>
<tr>
        <td>Aug</td>
<td>8</td>
<td>22</td>
<td>16</td>
<td>16</td>
    </tr>
<tr>
        <td>Sep</td>
<td>10</td>
<td>14</td>
<td>12</td>
<td>11</td>
    </tr>
<tr>
        <td>Oct</td>
<td>5</td>
<td>10</td>
<td>8</td>
<td>7</td>
    </tr>
  </tbody>
</table>

Fig. 3 Time series of five-ensemble mean daily precipitation (mm day<sup>−1</sup>) over the Indian subcontinent sector (blue dashed box in Fig. 1). Fifteen-day smoothing is applied to the time series

Based on TRMM observations, a small amount of precipitation appears over the Indian subcontinent sector (10°–25°N, 71°–89°E; blue dashed box in Fig. 1) in early May (Fig. 3). Then a rapid increase of precipitation starts in late May. From June to September, three peaks with precipitation between 8 and 12 mm day<sup>−1</sup> are evident from TRMM in mid-June, mid-July and early September, respectively. The ISM starts to decay in late September. All of the simulations roughly capture the variation of the observed ISM precipitation. The BMJ run exhibits similar magnitude and increasing rate of precipitation to TRMM from late May to mid-June. However, precipitation in the BMJ run continues increasing until early August, then a sharp decrease in mid-August, and starts to decrease slowly in September. Only one local peak is clearly evident in early August in the BMJ run. Before July, both the NSAS and Nest experiments produce smaller amount of precipitation than TRMM. The first peak and trough in June are reproduced in the NSAS and Nest runs. A sharp increase of precipitation from late June to early August is simulated in both the NSAS and Nest runs. The second local peak in the NSAS and Nest runs presents in early August, about 20 days later than the one observed in TRMM. The NSAS experiment produces a third local peak in early September, but the precipitation variation in August and September is rather small. The Nest run nicely reproduces the third local peak and decay of the ISM observed by TRMM. On average, all the simulations have a wet bias compared with TRMM, with the largest wet bias of 5.71 mm day<sup>−1</sup> in the BMJ run and the smallest wet bias of 0.18 mm day<sup>−1</sup> in the Nest run.

Overall, all of the experiments roughly simulate the horizontal distribution and temporal variations of the ISM precipitation, but with some discrepancies comparing to TRMM. The BMJ run simulates the highest precipitation amount, with too much precipitation over the BOB. The sharp increase of the ISM precipitation in late May is reproduced in the BMJ run, but the increase of precipitation is unable to stop until early August. The NSAS run has

spurious precipitation produced over the central India. The temporal variation of precipitation is simulated in the NSAS run, with lower (higher) precipitation before (after) July than TRMM. The Nest simulation fixes the spurious precipitation over the central India in the NSAS run, and produces a better horizontal distribution of precipitation. The temporal variation of precipitation is also better simulated in the Nest run.

## 4.2 ISO and associated large‑scale atmospheric water budgets

The model performance on simulating the ISO evolution and the associated large-scale atmospheric water budgets are investigated in this section. Daily precipitation time series averaged over the Indian subcontinent sector (10°–25°N, 71°–89°E) from TRMM and the model experiments are used to identify their ISO phases, respectively. A 15–90 day band pass filter is applied to the daily precipitation time series and other interested quantities (such as $Q_{cnvg}$ and $Q_{advt}$) to retain their ISO features. Then, the ISO peaks and troughs are singled out as maxima and minima larger than 1$\sigma$ of the filtered precipitation anomalies, respectively. A total of 15 (14) ISO peaks (troughs) are identified in the 5-year TRMM data, while the model experiments simulate 18–19 (14–19) ISO peaks (troughs). Time-lag composites of anomalies relative to the ISO peaks are constructed for the observations and the WRF simulations, and discussed in the following.

The TRMM dataset (upper panel of Fig. 4a) observed a positive precipitation anomaly near the equator between day − 20 and day − 10 relative to the ISO peaks. The positive precipitation anomalies gradually move northward and reach maximum over the Indian subcontinent (10°–25°N) at the ISO peaks. The BMJ experiment produces a northward propagation of the positive precipitation anomalies within day ± 10 (upper panel of Fig. 4b), with a similar magnitude of precipitation anomalies to that of TRMM. However, the simulated positive precipitation anomalies are initiated around 10°N on day − 20, earlier than the observed. Moreover, the northward propagation in the BMJ run is weaker and slower than the observed. Both the NSAS and Nest runs capture the observed northward propagation (upper panel of Fig. 4c, d), with maximum precipitation anomalies slightly to the south of the observation. Larger magnitude of precipitation anomalies is evident in the Nest run than the NSAS run.

The precipitation anomaly is primarily controlled by the $Q_{cnvg}$ anomaly in both the observations and the simulations (lower panel of Fig. 4). On a particular day, the positive $Q_{advt}$ anomaly is observed to the north of the positive $Q_{cnvg}$ anomaly with partial overlapping (lower panel of Fig. 4a), which results in a north–south asymmetric moisture distribution around the precipitation center and leads to the northward propagation of the ISO (Jiang et al. 2004017%3C1022:NPOTIS%3E2.0.CO;2)). The simulated

Springer logo
1 3


---



3678

L. Wu et al.

Hovmöller diagrams showing composite anomalies of precipitation, Qcnvg, and Qadvt for OBS, BMJ, NSAS, and Nest models.

**Fig. 4** Hovmöller diagrams of composite anomalies as functions of latitudes and lagging days relative to the ISO peak dates (day 0), averaged over the 71°–89°E sector for (upper panel) precipitation (mm day<sup>−1</sup>), (lower panel) $Q_{cnvg}$ (shading; mm day<sup>−1</sup>) and $Q_{advt}$ (contour; from − 2 to 2 mm day<sup>−1</sup> with 0.5 mm day<sup>−1</sup> interval) for **a** observations (OBS); **b** BMJ; **c** NSAS; and **d** Nest, respectively

$Q_{advt}$ anomaly in the BMJ run is out of phase with the $Q_{cnvg}$ anomaly (lower panel of Fig. 4b), while the NSAS and Nest runs reproduce the reanalysis phase relationship between the $Q_{cnvg}$ and $Q_{cnvg}$ anomalies (lower panel of Fig. 4c, d).

The responses of clouds to the large-scale water vapor transport over the Indian subcontinent are described in Fig. 5. The phase-lag relationship between $Q_{cnvg}$ and $Q_{cnvg}$ is effectively illustrated in the phase space in Fig. 6. The positive $Q_{advt}$ anomaly is observed 4–6 days ahead of the positive $Q_{cnvg}$ anomaly over the Indian subcontinent (lower panel of Figs. 5a, 6a). Once the $Q_{advt}$ anomaly becomes positive, the negative $Q_{col}$ anomaly starts to increase around day − 12, providing a favorable environment for the development of deep convection (Wang et al. 2015). When the $Q_{col}$ anomaly increases from negative to positive values around day − 5, a transition from shallow clouds to deep clouds is observed by MODIS (upper panel of Fig. 5a; Wang et al. 2015). In the following days, the $Q_{advt}$ anomaly keeps positive to maintain the increase of the $Q_{col}$ anomaly (Fig. 5a). Meanwhile, the $Q_{cnvg}$ anomaly becomes positive and continues increasing associated with the increasing frequency of deep convective clouds. The maximum of the $Q_{cnvg}$ anomaly occurs when deep convective clouds occur most frequently, lagging the maximum precipitation (in phase with $Q_{cnvg} + Q_{advt}$) by ~ 3 days. This is also observed with precipitation and outgoing long wave radiative flux (an indicator of high, thick clouds) anomalies associated with the MJO in West Pacific (Del Genio and Chen 2015). When the $Q_{advt}$ anomaly

becomes negative on day 4, both the $Q_{advt}$ and precipitation anomalies act to decrease the $Q_{col}$ anomaly and stabilize the atmosphere (Fig. 5a). Decrease of the $Q_{cnvg}$ anomaly further strengthens the decrease of the $Q_{col}$ anomaly. A transition of deep convective clouds to shallow clouds is evident during the decay of the ISO (Wang et al. 2015). The evolution of the ISM is further illustrated by the covariation of the $Q_{cnvg}$ and $Q_{cnvg}$ anomalies (Fig. 6a). The preconditioning for deep convection is characterized by positive $Q_{advt}$ and negative $Q_{cnvg}$ anomalies, while the decaying phase of the ISO presents negative $Q_{advt}$ and positive $Q_{cnvg}$ anomalies (Wang et al. 2015).

The BMJ experiment simulates a different relationship between $Q_{advt}$ and $Q_{cnvg}$ anomalies from that shown in the MERRA-2 reanalysis dataset. The $Q_{advt}$ anomaly is anti-correlated with the $Q_{cnvg}$ anomaly over the Indian subcontinent (Figs. 5b, 6b). Precipitation anomaly is primarily supported by the strong $Q_{cnvg}$ anomaly in the BMJ simulation. Excessively frequent high clouds are simulated throughout the ISO in the BMJ run.

The NSAS experiment roughly reproduces the phase-lag relationship of the $Q_{advt}$ and $Q_{cnvg}$ anomalies (Figs. 5c, 6c). The preconditioning (decaying) process lasts for 6 (6) days in the MERRA-2 datasets, while the NSAS experiment simulates faster processes with 3 (4) days of the preconditioning (decaying). This indicates that deep convection in the NSAS experiment responds faster to local water vapor increase than that in the real world. The simulated $Q_{advt}$ anomaly

Springer logo


---



Moist convection: a key to tropical wave–moisture interaction in Indian monsoon intraseasonal…

3679

<table>
  <thead>
    <tr>
        <th colspan="13">Evolution of anomalies following the monsoon ISO over the Indian subcontinent</th>
    </tr>
<tr>
        <th rowspan="2">Lagging Days</th>
        <th colspan="3">(a) OBS</th>
        <th colspan="3">(b) BMJ</th>
        <th colspan="3">(c) Nest</th>
        <th colspan="3">(d) NSAS</th>
    </tr>
<tr>
        <th>Rain</th>
        <th>Qcol</th>
        <th>Qadvt</th>
        <th>Rain</th>
        <th>Qcol</th>
        <th>Qadvt</th>
        <th>Rain</th>
        <th>Qcol</th>
        <th>Qadvt</th>
        <th>Rain</th>
        <th>Qcol</th>
        <th>Qadvt</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>-20</td>
<td>0.0</td>
<td>-0.5</td>
<td>-0.2</td>
<td>0.0</td>
<td>-0.8</td>
<td>-0.5</td>
<td>0.0</td>
<td>-0.5</td>
<td>-0.2</td>
<td>0.0</td>
<td>-0.5</td>
<td>-0.2</td>
    </tr>
<tr>
        <td>-15</td>
<td>0.2</td>
<td>-0.2</td>
<td>0.1</td>
<td>0.1</td>
<td>-0.5</td>
<td>-0.2</td>
<td>0.1</td>
<td>-0.3</td>
<td>0.0</td>
<td>0.1</td>
<td>-0.4</td>
<td>-0.1</td>
    </tr>
<tr>
        <td>-10</td>
<td>0.5</td>
<td>0.5</td>
<td>0.8</td>
<td>0.3</td>
<td>0.0</td>
<td>0.2</td>
<td>0.4</td>
<td>0.2</td>
<td>0.5</td>
<td>0.3</td>
<td>0.1</td>
<td>0.3</td>
    </tr>
<tr>
        <td>-5</td>
<td>1.5</td>
<td>2.0</td>
<td>1.5</td>
<td>1.0</td>
<td>1.5</td>
<td>0.8</td>
<td>1.2</td>
<td>1.8</td>
<td>1.2</td>
<td>1.2</td>
<td>2.0</td>
<td>1.0</td>
    </tr>
<tr>
        <td>0</td>
<td>5.5</td>
<td>4.0</td>
<td>0.5</td>
<td>4.5</td>
<td>5.0</td>
<td>0.2</td>
<td>4.8</td>
<td>4.5</td>
<td>0.4</td>
<td>5.0</td>
<td>5.5</td>
<td>0.3</td>
    </tr>
<tr>
        <td>5</td>
<td>2.5</td>
<td>1.5</td>
<td>-1.5</td>
<td>2.0</td>
<td>2.0</td>
<td>-1.0</td>
<td>2.2</td>
<td>1.8</td>
<td>-1.2</td>
<td>2.5</td>
<td>2.2</td>
<td>-1.5</td>
    </tr>
<tr>
        <td>10</td>
<td>0.5</td>
<td>-0.5</td>
<td>-1.0</td>
<td>0.5</td>
<td>-0.2</td>
<td>-0.8</td>
<td>0.6</td>
<td>-0.4</td>
<td>-0.8</td>
<td>0.8</td>
<td>-0.2</td>
<td>-1.0</td>
    </tr>
<tr>
        <td>15</td>
<td>0.1</td>
<td>-1.0</td>
<td>-0.5</td>
<td>0.2</td>
<td>-0.8</td>
<td>-0.5</td>
<td>0.2</td>
<td>-0.8</td>
<td>-0.4</td>
<td>0.2</td>
<td>-1.0</td>
<td>-0.5</td>
    </tr>
<tr>
        <td>20</td>
<td>0.0</td>
<td>-0.8</td>
<td>-0.2</td>
<td>0.0</td>
<td>-1.0</td>
<td>-0.3</td>
<td>0.0</td>
<td>-1.0</td>
<td>-0.2</td>
<td>0.0</td>
<td>-1.2</td>
<td>-0.2</td>
    </tr>
  </tbody>
</table>

**Fig. 5** Evolution of occurrence frequencies of cloud top pressure (color shading) with the associated anomalies in $Q_{col}$ (mm), rain (mm day<sup>−1</sup>), $Q_{cnvg}$ (mm day<sup>−1</sup>) and $Q_{advt}$ (mm day<sup>−1</sup>) following the monsoon ISO over the Indian subcontinent (10°–25°N, 71°–89°E) for **a** observations (OBS); **b** BMJ; **c** NSAS; **d** nest

responsible for the moistening process during preconditioning is much weaker than that in MERRA-2. Largest positive $Q_{col}$ anomaly and frequent high clouds are simulated in the NSAS experiment, possibly related to stronger and deeper convection in the modification of the NSAS scheme (Han and Pan 2011).

The covariation between $Q_{advt}$ and $Q_{cnvg}$ in the Nest simulation has improved comparing to the two simulations with cumulus parameterization, and is rather similar to that in MERRA-2 (Figs. 5, 6). Compared to the NSAS run, the Nest run exhibits a better representation of the phase lag and magnitude of the $Q_{advt}$ and $Q_{cnvg}$ anomalies during the preconditioning, albeit with a longer preconditioning of 9 days

(Figs. 5d, 6d), probably because of the weaker $Q_{advt}$ anomaly responsible for moistening the atmosphere. The transition of shallow and deep clouds is better simulated in the Nest run than the other two simulations. The weak $Q_{advt}$ anomaly also results in a shorter phase lag between precipitation and $Q_{cnvg}$ (~ 2 days compared to 3 days in MERRA-2).

In summary, all the experiments simulate the northward propagation of the ISO with some discrepancies. The covariation of $Q_{advt}$ and $Q_{cnvg}$ in MERRA-2 is not captured in the BMJ experiment, while it is approximately simulated in the NSAS run. The simulated ISO in the Nest experiment with resolved convective processes has better agreement with the MODIS cloud variations, TRMM precipitation, and the

Springer logo


---



3680

L. Wu et al.

<table>
  <thead>
    <tr>
        <th colspan="9">Fig. 6: Orbits of dynamical states in two-dimensional phase space (Qcnvg vs Qadvt)</th>
    </tr>
<tr>
        <th>Panel</th>
        <th>(a) OBS</th>
        <th> </th>
        <th>(b) BMJ</th>
        <th> </th>
        <th>(c) NSAS</th>
        <th> </th>
        <th>(d) Nest</th>
        <th> </th>
    </tr>
<tr>
        <th>State</th>
        <th>Qcnvg</th>
        <th>Qadvt</th>
        <th>Qcnvg</th>
        <th>Qadvt</th>
        <th>Qcnvg</th>
        <th>Qadvt</th>
        <th>Qcnvg</th>
        <th>Qadvt</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>Preconditioning (Blue)</td>
<td>-1.5</td>
<td>0.2</td>
<td>-2.5</td>
<td>0.4</td>
<td>-1.0</td>
<td>0.2</td>
<td>-2.0</td>
<td>0.6</td>
    </tr>
<tr>
        <td>Monsoon Peak (Red)</td>
<td>1.5</td>
<td>0.8</td>
<td>7.0</td>
<td>-1.0</td>
<td>4.0</td>
<td>0.6</td>
<td>5.0</td>
<td>0.2</td>
    </tr>
<tr>
        <td>20 days before (Green)</td>
<td>0.0</td>
<td>-0.5</td>
<td>-2.0</td>
<td>0.3</td>
<td>-0.5</td>
<td>-0.8</td>
<td>-0.5</td>
<td>-0.5</td>
    </tr>
<tr>
        <td>20 days after (Magenta)</td>
<td>2.0</td>
<td>0.8</td>
<td>-1.5</td>
<td>0.5</td>
<td>0.0</td>
<td>0.4</td>
<td>0.0</td>
<td>0.7</td>
    </tr>
  </tbody>
</table>

**Fig. 6** The orbits of dynamical states in two-dimensional phase space over the Indian subcontinent from **a** observations (OBS); **b** BMJ; **c** NSAS; **d** nest. Blue dots identify the preconditioning phase, which has positive $Q_{advt}$ and negative $Q_{cnvg}$ anomalies during $Q_{col}$ increase. Red dots mark the monsoon peaks; Green (magenta) dots mark 20 days before (after) the monsoon peaks

corresponding covariance between $Q_{advt}$ and $Q_{cnvg}$ compared to other experiments.

## 4.3 Wave activity and water vapor transport during the ISO

Discrepancies in water vapor transport among different experiments from the MERRA-2 reanalysis seen in Figs. 5 and 6 are related to different tropical wave activities realized in the WRF experiments. We further investigate ISO wave activities in a lag-composite analysis with respective to the ISO peaks. On day − 15, convection (illustrated by positive precipitation anomaly) is observed over the equatorial ocean (Fig. 7a). A vortex center (positive vorticity associated with

equatorial Rossby wave) at 850 hPa is located to the north of the convection, indicating a northward tilting structure associated with the convection, which contributes to the northward propagating of the ISO (Jiang et al. 2004017%3C1022:NPOISO%3E2.0.CO;2), 2011). While the vortex moves northward for 3 days, a second vortex is generated to the east over the Maritime Continent on day − 12. On day − 9, the western vortex reaches the Indian continent with intensified convection to the west of the Western Ghats, while the eastern vortex strengthens and moves northwestward towards BOB. From day − 12 to day − 6, the movement of the two vortices is associated with positive $Q_{advt}$ anomalies in Figs. 5a and 6a over the Indian continent for the preconditioning period. The horizontal moisture advection anomalies associated with these vortices

Springer logo


---



Moist convection: a key to tropical wave–moisture interaction in Indian monsoon intraseasonal… 3681

are consistent with the moisture flux anomalies reported in Wong et al. (2011). The two vortices start to merge on day − 6. In the following days, the two partially-merged vortices continue to strengthen and move northward, bringing heavy precipitation to the Indian subcontinent, with one precipitation maximum at the west slope of Western Ghats and the other over the BOB. As the vortex centers move towards the Indian subcontinent, positive $Q_{advt}$ anomaly decreases while positive $Q_{cnvg}$ anomaly increases together with frequent occurrence of deep convection (Figs. 5a, 6a).

In the BMJ experiment, the equatorial Rossby wave propagations from day − 15 to day − 9 are not as clear and evident as those in MERRA-2. On day − 6, the vortex near BOB strengthens while another vortex is approaching from the west at around 15°N. This western vortex connects with the vortex over the BOB in the following days, resulting in positive precipitation anomalies over the Western Ghats and the BOB. The BMJ experiment produces a different propagation feature from that in MERRA-2, and only reproduces the observed spatial precipitation pattern during the peak phase of the ISO (day 0), consistent with the Hovmöller diagram in Fig. 4b. This inability to simulate the proper equatorial Rossby wave activity associated with the ISO in the BMJ experiment is also reflected in the misrepresentation of the phase relationship of $Q_{advt}$ and $Q_{cnvg}$ (Figs. 5b, 6b).

The NSAS experiment shows a vortex to the southwest of the Indian continent (around 5°N and 68°E) on day − 12 (Fig. 7c). On day − 9, this vortex is strengthening and another vortex is present over the BOB, instead of west of Indonesia seen in MERRA-2. During day − 9 and day − 3, the western vortex moves northward while the eastern vortex moves westward, and they merge over Indian as in MERRA-2. The weaker vorticity over the Indian continent compared to MERRA-2 from day − 12 to day − 9 is associated with the much weaker positive $Q_{advt}$ anomalies seen in Figs. 5c and 6c. The western vortex edge tangentially touches the Indian continent around day − 6, while at this time the western vortex center in MERRA-2 is already on the Indian continent. This explains why the peak of $Q_{advt}$ in the NSAS experiment is a couple of days lagging the peak in MERRA-2 (comparing Fig. 5a with Fig. 5c). This difference is also reflected in the shape of their orbits on the $Q_{advt} \cdot Q_{cnvg}$ phase space (Fig. 6a, c). How equatorial Rossby wave propagations help water vapor transport to the Indian continent is approximately captured in the NSAS run, and the detailed discrepancies are reflected in the covariance of $Q_{advt}$ and $Q_{cnvg}$ and the corresponding shapes in the phase space.

In the Nest run, the vortex near the southern tip of the Indian continent touches the land about the same time as the vortex in MERRA-2 during the preconditioning period, this is reflected by the similarity of the variation of $Q_{advt}$ between Fig. 5a, d or between Fig. 6a, d. A second vortex is generated near the Maritime Continent on day − 12. The propagation and merging of the two vortices during the ISO are also well reproduced in the Nest run. The precipitation maximum at the Western Ghats is located several degrees south to the observation at the ISO peaks. The weaker $Q_{advt}$ and stronger $Q_{cnvg}$ after day − 6, compared to those in MERRA-2, could be related to the relative locations of the vortices from the Indian continent and the magnitudes of their vorticity (the larger the vorticity, the stronger the $Q_{cnvg}$). These detailed discrepancies from MERRA-2 are reflected in the phase space as an orbit of a more horizontally oriented ellipsoid for the Nest run. Note that the Nest run has the same large-scale dynamics and thermodynamics as the NSAS run at the mother domain. High resolution with resolved convection (and possibly better representation of topography) leads to the improved simulation of the ISO.

## 5 Summary and discussion

This study investigates the impacts of moist convective processes on the simulations of the Indian monsoon intraseasonal oscillation (ISO) from the perspective of interactions among equatorial Rossby waves, atmospheric water vapor transport, and convection. Sensitivity tests are carried out by applying two different cumulus parameterizations and a nested simulation at cloud-resolving horizontal resolution in the regional Weather Research and Forecasting (WRF) model. Results show that the model simulation with the Betts–Miller–Janjić (BMJ) cumulus scheme can capture horizontal distribution of the Indian Summer Monsoon (ISM) precipitation. However, the preconditioning and decaying of the ISO contributed by moisture advection ($Q_{advt}$) are not properly represented in this simulation (Figs. 5b, 6b), consistent with previously report by Raju et al. (2015a). The BMJ scheme somewhat produces a weaker and slower northward propagation of the ISO precipitation associated with a different tropical wave activity compared to the observations (Figs. 4b, 7). This misrepresentation may be due to the intrinsic limitation in the moist adjustment scheme, which does not explicitly represent convective cloud processes (Lackmann 2016). First, occurrence of deep convection (as indicated by anomalies of moisture dynamical convergence $Q_{cnvg}$ becoming positive) does not respond to atmospheric water vapor accumulation by moisture advection properly, resulting in an anti-correlated pattern between $Q_{cnvg}$ and $Q_{advt}$ in the water-budget phase space (Fig. 6b). Second, variation of cloud top heights does not properly respond to deep convection (Fig. 5b), implying a misrepresentation of cloud radiative feedback to moist convective processes.

The New Simplified Arakawa–Schubert (NSAS) scheme, a bulk mass-flux scheme with simplified convective cloud processes, approximately captures the coherency among atmospheric water transport, cloud top heights, and

Springer logo
3681


---



3682

L. Wu et al.

Geographical maps showing atmospheric data (OBS, BMJ, NSAS, Nest) at different time lags (-15D to 0D) with a color scale from -16 to 16.

Springer logo


---



Moist convection: a key to tropical wave–moisture interaction in Indian monsoon intraseasonal…

3683

◂**Fig. 7** Lag composite of 15–90 day band pass filtered precipitation (color shading; mm day<sup>−1</sup>), 850-hPa vorticity (purple contour; from 0 to $6 \times 10^{-6} \text{ s}^{-1}$, with $3 \times 10^{-6} \text{ s}^{-1}$ interval) and 850-hPa wind (vector; m s<sup>−1</sup>) with respect to the ISO peaks at lag day − 15, day − 12, day − 9, day − 6, day − 3 and day 0 for **a** OBS; **b** BMJ; **c** NSAS; **d** nest

equatorial Rossby wave activity (Figs. 5c, 6c). As a result, the northward propagation of precipitation is close to what is observed (Fig. 4c). Relative location of the equatorial Rossby wave from the Indian continent and its exact timing of landing are responsible for much smaller positive $Q_{advt}$ anomaly during preconditioning (Fig. 7). Transition from shallow to deep convection in the NSAS simulation exists (Fig. 5c), but not as evident as that in the observation or the simulation with a nested domain. High cloud frequency is higher than observation, perhaps related to the enhancement of convective mass flux.

The sensitivity to horizontal resolution is investigated by having a domain at 0.04° horizontal resolution nested to the outer domain with the NSAS scheme. Convective cloud processes are resolved in the nested domain, and with a better representation of the topography over the Indian continent. The high resolution experiment significantly improves the simulation of interactions among equatorial Rossby waves, atmospheric water transport, and clouds for the ISO, compared to the NSAS experiment. The high resolution run reasonably reproduces northward propagation of precipitation, transition of shallow to deep convection, and equatorial Rossby wave activities associated with the ISO. The phase-space orbit for ($Q_{cnvg} \cdot Q_{advt}$) anomalies over the Indian continent has the closest resemblance to that of MERRA-2, although the $Q_{advt}$ anomaly is weaker and the $Q_{cnvg}$ anomaly is stronger. More accurate representation of topography helps improve the spatial pattern of precipitation over the central Indian inform that in the NSAS run.

This study provides the first convection-permitting simulation of the ISM. Sensitivity experiments prove that moist convective processes (and possibly high resolution topography) are primary factors contributing to the proper simulation of interactions among tropical waves, large-scale moisture transport, and cloud variations associated with the ISO. The water-budget phase space is an effective tool to diagnose such interactions. This study demonstrates that cloud resolving simulation is the future direction for correctly representation of the ISO in the models. Due to the limitation of available computation capability, it may not be feasible to run general circulation models (GCMs) at resolution as in our nested experiment in the near future. Improvement of the ISM simulation can be achieved by better representation of moist convective processes in cumulus parameterizations (e.g., Del Genio et al. 2012a; Del Genio and Chen 2015).

**Acknowledgements** The work is conducted at the Jet Propulsion Laboratory, California Institute of Technology, under contract with NASA. The authors thank the funding support from the NASA Precipitation Measurement Missions Science Team (PMM, NNH15ZDA001N-PMM). We thank Xianan Jiang for providing comments on this manuscript.

# References

Bosilovich MG, Lucchesi R, Suarez M (2016) MERRA-2: File Specification. GMAO Office Note No. 9 (Version1.1), 73 pp. [http://gmao.gsfc.nasa.gov/pubs/office_notes](http://gmao.gsfc.nasa.gov/pubs/office_notes). Accessed 26 Jan 2018

Chen F, Mitchell K, Schaake J, Xue Y, Pan H, Koren V, Duan QY, Ek M, Betts A (1996) Modeling of land surface evaporation by four schemes and comparison with FIFE observations. J Geophys Res 101(D3):7251–7268. [https://doi.org/10.1029/95JD02165](https://doi.org/10.1029/95JD02165)

Collins WD et al (2004) Description of the NCAR community atmosphere model (CAM3). National Center for Atmospheric Research, Boulder

Dee DP et al (2011) The ERA-Interim reanalysis: configuration and performance of the data assimilation system. Q J R Meteorol Soc 137:553–597. [https://doi.org/10.1002/qj.828](https://doi.org/10.1002/qj.828)

Del Genio AD, Chen Y (2015) Cloud-radiative driving of the Madden–Julian oscillation as seen by the A-Tran. J Geophys Res Atmos 120:5344–5356. [https://doi.org/10.1002/2015JD023278](https://doi.org/10.1002/2015JD023278)

Del Genio AD, Wu J, Wolf AB, Chen Y, Yao M, Kim D (2012a) Constraints on cumulus parameterization from simulations of observed MJO events. J Clim 25:6419–6442. [https://doi.org/10.1175/JCLI-D-14-00832.1](https://doi.org/10.1175/JCLI-D-14-00832.1)

Del Genio AD, Chen Y, Kim D, Yao MS (2012b) The MJO transition from shallow to deep convection in CloudSat/CALIPSO data and GISS GCM simulations. J Clim 25(11):3755–3770

Global Modeling and Assimilation Office (2015) inst3_3d_asm_Np:MERRA-2 3D IAU State, Meteorology Instantaneous 3-hourly (p-coord, 0.625 × 0.5 L42), version 5.12.4. Goddard Space Flight Center Distributed Active Archive Center (GSFC DAAC), Greenbelt. [https://doi.org/10.5067/VJAFPLI1CSIV](https://doi.org/10.5067/VJAFPLI1CSIV)

Goswami BN (2005) Intraseasonal variability (ISV) of south Asian summer monsoon. In: Lau K, Waliser D (eds) Intraseasonal variability of the atmosphere–ocean climate system. Springer, Chichester, pp 19–61

Grell G, Devenyi D (2002) A generalized approach to parameterizing convection combining ensemble and data assimilation techniques. Geophys Res Lett. [https://doi.org/10.1029/2002GL015311](https://doi.org/10.1029/2002GL015311)

Han J, Pan H-L (2011) Revision of convection and vertical diffusion schemes in the NCEP global forecast system. Weather Forecast 26:520–533. [https://doi.org/10.1175/WAF-D-10-05038.1](https://doi.org/10.1175/WAF-D-10-05038.1)

Hong S-Y, Lim JJ (2006) The WRF single-moment microphysics scheme (WSM6). J Korean Meteorol Soc 42:129–151

Hong S-Y, Noh Y, Dudhia J (2006) a new vertical diffusion package with an explicit treatment of entrainment processes. Mon Weather Rev 134:2318–2341. [https://doi.org/10.1175/MWR3199.1](https://doi.org/10.1175/MWR3199.1)

Huffman GJ, Adler RF, Bolvin DT, Gu G, Nelkin EJ, Bowman KP, Hong Y, Stocker EF, Wolff DB (2007) The TRMM multi-satellite precipitation analysis: quasi-global, multi-year, combined-sensor precipitation estimates at fine scale. J Hydrometeorol 8:38–55

Janjic ZI (1994) The step-mountain eta coordinate model. Further developments of the convection, viscous sublayer and turbulence closure schemes. Mon Weather Rev 122:927–945

Janjić ZI (2000) Comments on Development and evaluation of a convection scheme for use in climate models. J Atmos Sci 57(21):3686–3686. [https://doi.org/10.1175/1520-0469(2000)057<3686:CODAEO>2.0.CO;2](https://doi.org/10.1175/1520-0469(2000)057<3686:CODAEO>2.0.CO;2)057<3686:CODAEO>2.0.CO;2)

Springer logo

3


---



3684

L. Wu et al.

Jiang X, Li T, Wang B (2004) Structures and mechanisms of the northward propagating boreal summer intraseasonal oscillation. J Clim 17:1022–1039. [https://doi.org/10.1175/1520-0442(2004)017<1022:SAMOTN>2.0.CO;2](https://doi.org/10.1175/1520-0442(2004)017<1022:SAMOTN>2.0.CO;2)017%3C1022:SAMOTN%3E2.0.CO;2)

Jiang X, Waliser DE, Li J-L, Woods C (2011) Vertical structures of cloud water associated with the boreal summer intraseasonal oscillation based on CloudSat observations and ERA-Interim reanalysis. Clim Dyn 36:2219–2232. [https://doi.org/10.1007/s00382-010-0853-8](https://doi.org/10.1007/s00382-010-0853-8)

Kain J (2004) The Kain–Fritsch convective parameterization: an update. J Appl Meteorol 43:170–181

King MD, Platnick S, Menzel WP, Ackerman SA, Hubanks PA (2013) Spatial and temporal distribution of clouds observed by MODIS onboard the Terra and Aqua satellites. IEEE Trans Geosci Remote Sens 51:3826–3852. [https://doi.org/10.1109/TGRS.2012.2227333](https://doi.org/10.1109/TGRS.2012.2227333)

Lackmann GM (2016) MEA 716 Exercise, BMJ CP scheme. [http://www4.ncsu.edu/~gary/mea716/2016_716_bmjlab.pdf](http://www4.ncsu.edu/~gary/mea716/2016_716_bmjlab.pdf). Accessed 26 Jan 2018

Lawrence DM, Webster PJ (2002) The boreal summer intraseasonal oscillation: relationship between northward and eastward movement of convection. J Atmos Sci 59:1593–1606

Lucas-Picher P, Christensen JH, Saeed F, Kumar P, Asharaf S, Ahrens B, Wiltshire AJ, Jacob D, Hagemann S (2011) Can regional climate models represent the Indian monsoon? J Hydrometeorol 12(5):849–868. [https://doi.org/10.1175/2011jhm1327.1](https://doi.org/10.1175/2011jhm1327.1)

Mukhopadhyay P, Taraphdar S, Goswami BN, Krishnakumar K (2010) Indian summer monsoon precipitation climatology in a high resolution regional climate model: impact of convective parameterization on systematic biases. Weather Forecast 25:369–387

Murthi A, Kenneth P, Bowman L, Leung R (2011) Simulation of precipitation using NRCM and comparisons with satellite observations and CAM: annual cycle. Clim Dyn 36:1659–1679. [https://doi.org/10.1007/s00382-010-0878-z](https://doi.org/10.1007/s00382-010-0878-z)

Neena JM, Waliser D, Jiang X (2017) Model performance metrics and process diagnostics for boreal summer intraseasonal variability. Clim Dyn 48:1661. [https://doi.org/10.1007/s00382-016-3166-8](https://doi.org/10.1007/s00382-016-3166-8)

Peixóto JP, Oort AH (1992) Physics of climate. American Institute of Physics, New York

Rajeevan M, Gadgil S, Bhate J (2010) Active and break spells of the Indian summer monsoon. J Earth Syst Sci 119(3):229–247

Raju A, Parekh A, Chowdary JS, Gnanaseelan C (2015a) Assessment of the Indian summer monsoon in the WRF regional climate model. Clim Dyn 44:3077–3100

Raju PVS, Bhatla R, Almazrouiand M, Assiri M (2015b) Performance of convection schemes on the simulation of summer monsoon features over the South Asia CORDEX domain using RegCM-4.3. Int J Climatol. [https://doi.org/10.1002/joc.4317](https://doi.org/10.1002/joc.4317)

Ramu DA, Sabeerali CT, Chattopadhyay R, Rao DN, George G, Dhakate AR, Salunke K, Srivastava A, Rao SA (2016) Indian summer monsoon rainfall simulation and prediction skill in the CFSv2 coupled model: impact of atmospheric horizontal resolution. J Geophys Res Atmos 121:2205–2221. [https://doi.org/10.1002/2015JD024629](https://doi.org/10.1002/2015JD024629)

Ratnam JV, Krishna Kumar K (2005) Sensitivity of the simulated monsoons of 1987 and 1988 to convective parameterization schemes in MM5. J Clim 18:2724–2743

Sabeerali CT, Dandi AR, Dhakate A, Salunke K, Mahapatra S, Rao SA (2013) Simulation of boreal summer intraseasonal oscillations in the latest CMIP5 coupled GCMs. J Geophys Res 118:4401–4420. [https://doi.org/10.1002/jgrd.50403](https://doi.org/10.1002/jgrd.50403)

Samala BK, Banerjee S, Kaginalkar A, Dalvi M (2013) Study of the Indian summer monsoon using WRF–ROMS regional coupled model simulations. Atmos Sci Let 14:20–27

Skamarock WC, Klemp J, Dudhia J, Gill DO, Barker DM, Wang W, Powers JG (2008) A description of the advanced research WRF version 2. NCAR technical note, NCAR/TN-468 + STR. Mesoscale and Microscale Meteorology Division, National Center for Atmospheric Research, Boulder

Sperber KR, Annamalai H, Kang I-S, Kitoh A, Moise A, Turner A, Wang B, Zhou T (2013) the asian summer monsoon: an intercomparison of CMIP5 vs. CMIP3 simulations of the late century. Clim Dyn 41(9–10):2711–2744

Srinivas CV, Hariprasad D, Bhaskar Rao DV, Anjaneyulu Y, Baskarana R, Venkataramana B (2013) Simulation of the Indian summer monsoon regional climate using advanced research WRF model. Int J Climatol. [https://doi.org/10.1002/joc.3505](https://doi.org/10.1002/joc.3505)

Taraphdar S, Mukhopadhyay P, Goswami BN (2010) Predictability of Indian summer monsoon weather during active and break phases using a high resolution regional model. Geophys Res Lett 37:1–6

Turner AG, Annamalai H (2012) Climate change and the south Asian summer monsoon. Nat Clim Change 2:1–9. [https://doi.org/10.1038/NCLIMATE1495](https://doi.org/10.1038/NCLIMATE1495)

Umakanth U, Kesarkar AP, Raju A, Vijaya Bhaskar Rao S (2016) Representation of monsoon intraseasonal oscillations in regional climate model: sensitivity to convective physics. Clim Dyn 47:895. [https://doi.org/10.1007/s00382-015-2878-5](https://doi.org/10.1007/s00382-015-2878-5)

Unnikrishnan CK, Rajeevan M, Vijaya Bhaskara Rao S (2015) A study on the role of land–atmosphere coupling on the south Asian monsoon climate variability using a regional climate model. Theor Appl Climatol. [https://doi.org/10.1007/s00704-015-1680-y](https://doi.org/10.1007/s00704-015-1680-y)

Waliser DE, Jin K, Kang I-S, Stern WF, Schubert SD, Wu MLC, Lau K-M, Lee M-I, Krishnamurty V, Kitoh A, Meehl GA, Galin VY, Satyan V, Mandke SK, Wu G, Liu Y, Park C-K (2003) AGCM simulations of intraseasonal variability associated with the Asian summer monsoon. Clim Dyn 21:423–446. [https://doi.org/10.1007/s00382-003-0337-1](https://doi.org/10.1007/s00382-003-0337-1)

Wang T, Wong S, Fetzer EJ (2015) Cloud regime evolution in the Indian monsoon intraseasonal oscillation: connection to large-scale dynamical conditions and the atmospheric water budget. Geophys Res Lett 42:9465–9472. [https://doi.org/10.1002/2015GL066353](https://doi.org/10.1002/2015GL066353)

Wong S, Fetzer EJ, Tian B, Lambrigtsen B, Ye H (2011) The apparent water vapor sinks and heat sources associated with the intraseasonal oscillation of the Indian summer monsoon. J Clim 24:4466–4479. [https://doi.org/10.1175/2011JCLI4076.1](https://doi.org/10.1175/2011JCLI4076.1)

Wong S, Del Genio AD, Wang T, Kahn BH, Fetzer EJ, L’Ecuyer TS (2016) Responses of tropical ocean clouds and precipitation to the large-scale circulation: atmospheric-water-budget-related phase space and dynamical regimes. J Clim 29:7127–7143. [https://doi.org/10.1175/JCLI-D-15-0712.1](https://doi.org/10.1175/JCLI-D-15-0712.1)

Wu L, Su H, Jiang JH (2013) Regional simulation of aerosol impacts on precipitation during the East Asian summer monsoon. J Geophys Res Atmos 118:6454–6467. [https://doi.org/10.1002/jgrd.50527](https://doi.org/10.1002/jgrd.50527)

Wu L, Li JLF, Pi CJ, Yu JY, Chen JP (2015) An observationally based evaluation of WRF seasonal simulations over the Central and Eastern Pacific. J Geophys Res Atmos 120:10664–10680. [https://doi.org/10.1002/2015JD023561](https://doi.org/10.1002/2015JD023561)

Springer logo 3
