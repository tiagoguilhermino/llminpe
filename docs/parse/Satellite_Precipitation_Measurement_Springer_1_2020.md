# Advances in Global Change Research

Volume 67

**Series Editor**

Markus Stoffel, Institute of Geological Sciences, University of Geneva, Geneva, Switzerland

**Advisory Editors**

Wolfgang Cramer, IMEP, Bâtiment Villemin, Europole de l’Arbois, Aix-en-Provence, France

Urs Luterbacher, University of Geneva, Geneva, Switzerland

F. Toth, International Institute for Applied Systems Analysis (IIASA), Laxanburg, Austria

---

More information about this series at [http://www.springer.com/series/5588](http://www.springer.com/series/5588)

---

Vincenzo Levizzani • Christopher Kidd
Dalia B. Kirschbaum • Christian D. Kummerow
Kenji Nakamura • F. Joseph Turk

Editors

# Satellite Precipitation Measurement

Volume 1

Springer logo

---

*Editors*

Vincenzo Levizzani
CNR-ISAC
Bologna, Italy

Dalia B. Kirschbaum
Code 617
NASA Goddard Space Flight Center
Greenbelt, MD, USA

Kenji Nakamura
Department of Economics on Sustainability
Dokkyo University
Saitama, Japan

Christopher Kidd
Earth System Science Interdisciplinary Center
University of Maryland and NASA Goddard Space Flight Center
Greenbelt, MD, USA

Christian D. Kummerow
Department of Atmospheric Science
Colorado State University
Fort Collins, CO, USA

F. Joseph Turk
Jet Propulsion Laboratory
California Institute of Technology
Pasadena, CA, USA

ISSN 1574-0919 ISSN 2215-1621 (electronic)

Advances in Global Change Research

ISBN 978-3-030-24567-2 ISBN 978-3-030-24568-9 (eBook)

[https://doi.org/10.1007/978-3-030-24568-9](https://doi.org/10.1007/978-3-030-24568-9)

© Springer Nature Switzerland AG 2020

This work is subject to copyright. All rights are reserved by the Publisher, whether the whole or part of the material is concerned, specifically the rights of translation, reprinting, reuse of illustrations, recitation, broadcasting, reproduction on microfilms or in any other physical way, and transmission or information storage and retrieval, electronic adaptation, computer software, or by similar or dissimilar methodology now known or hereafter developed.

The use of general descriptive names, registered names, trademarks, service marks, etc. in this publication does not imply, even in the absence of a specific statement, that such names are exempt from the relevant protective laws and regulations and therefore free for general use.

The publisher, the authors, and the editors are safe to assume that the advice and information in this book are believed to be true and accurate at the date of publication. Neither the publisher nor the authors or the editors give a warranty, expressed or implied, with respect to the material contained herein or for any errors or omissions that may have been made. The publisher remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Cover illustration: Courtesy of NASA

This Springer imprint is published by the registered company Springer Nature Switzerland AG.
The registered company address is: Gewerbestrasse 11, 6330 Cham, Switzerland

---

*Sognatore è un uomo con i piedi fortemente appoggiati sulle nuvole<sup>\*</sup>*

*Ennio Flaiano (1910–1972)*

\* *Dreamer is a man with his feet firmly resting on the clouds*

---

*In memory of*
*Arthur Y. Hou (1947–2013)*

---

# Preface

This book is published 13 years after the book *Measuring Precipitation from Space: EURAINSAT and the Future* (V. Levizzani, P. Bauer, and F. J. Turk, Eds., Springer, ISBN 978-1-4020-5835-6), but it is not a revised edition of the previous. It is a new book that aims to construct a quasi-complete picture of the science and applications of satellite-derived precipitation measurements at the present time.

The book comes out at the end of a very exciting era of precipitation measurements from space. The Tropical Rainfall Measuring Mission (TRMM), launched in November 1997, ended its long life in space in April 2015 providing an unprecedented 17-year-long dataset of tropical precipitation and lightning. The Global Precipitation Measurement (GPM) mission, launched in February 2014, is now in space as TRMM’s natural successor with a more global perspective that extends precipitation radar observations to the Arctic and Antarctic circles. At the same time, the CloudSat mission, launched in April 2006, is in its 13<sup>th</sup> year in space and focuses on cloud structure, which is essential for improving precipitation retrievals. These are just a few examples of precipitation-oriented missions that continuously provide data from geostationary and low Earth orbits in a truly cooperative effort worldwide. This effort involves many agencies and a broad range of countries who collaborate in a genuine way to observe global precipitation.

It is by realizing the significance of this historical moment and the need to think about what is important for the future that the community joined in the effort of writing a book with the goal of serving the precipitation community itself, the scholars, the students, the stakeholders, the end users, and all the readers interested in knowing the progress of satellite precipitation studies. The most recent achievements in precipitation monitoring from space drive us into the future of measuring not only heavy rainfall but less intense rainfall, snowfall, and even hailfall. Such a scientific framework would not have even been conceivable 13 years ago and is only possible thanks to the relentless effort of the worldwide space and precipitation communities.

Naturally, we realize that at the time of the printing of this book, the field will already have made advances and thus part of the material may already be a bit

ix


---



x

Preface

outdated. However, in this era of rapidly evolving technological developments, sensors that take years to design, build, and launch are already considered old. This is particularly true nowadays when the progress in approaching new scientific challenges is particularly fast.

Since 2007, science has made substantial progresses toward transforming satellite rainfall “estimates” into accurate “measurements” and producing operational rainfall products readily available for a wide field of applications ranging from climate research and numerical weather prediction to hydrology, agriculture, health, civil protection, and much more. Satellite-derived precipitation products are now being considered as a valuable tool for a number of applications that benefit society and save lives. This is perhaps the most important achievement of all.

This book represents a significant effort, and each author has provided high-quality material in the topics of current and future mission contributions, observations of precipitation using the suite of precipitation satellites, retrieval techniques, validation, and applications. The result is a book that not only photographs the state of the art of the discipline but also projects it into the future.

<table>
  <tbody>
    <tr>
        <td>Bologna, Italy</td>
<td>Vincenzo Levizzani</td>
    </tr>
<tr>
        <td>Greenbelt, MD, USA</td>
<td>Christopher Kidd</td>
    </tr>
<tr>
        <td>Greenbelt, MD, USA</td>
<td>Dalia B. Kirschbaum</td>
    </tr>
<tr>
        <td>Fort Collins, CO, USA</td>
<td>Christian D. Kummerow</td>
    </tr>
<tr>
        <td>Saitama, Japan</td>
<td>Kenji Nakamura</td>
    </tr>
<tr>
        <td>Pasadena, CA, USA</td>
<td>F. Joseph Turk</td>
    </tr>
<tr>
        <td colspan="2">9 March 2020</td>
    </tr>
  </tbody>
</table>



---

# Acknowledgments

The first acknowledgment goes to Springer Nature for asking us to start this project and for being very patient with us for the considerable amount of time it took to put the material together.

All the colleagues who spent their precious time contributing their ideas and results deserve special gratitude. They are all very busy scientists, and this is why their contribution is particularly valuable. We deem the book to be a first-hand image of the achievements of the whole community at this time while also providing an important glimpse into future developments.

Then we feel that we need to thank the readers who have already made the previous 2007 Springer book a success, thus de facto making it possible to start writing the new one. We hope you will get from this new book even more inspiration than you got from its predecessor. While some concepts and details will surely become outdated as time goes by, it is our hope that the material contained herein is sufficiently broad that it will always serve as a springboard to understand and put into context the latest research and findings.

It would be almost impossible to thank all the people and organizations behind this effort. You realize this simple truth by looking at the list of contributors and seeing the very long list of institutes, research organizations, university departments, and operational agencies that allowed their members to spend a substantial amount of time writing and correcting the chapters of the book. We thank, in particular, our home institutions that were very supportive in understanding the importance of our work for the community: CNR, Colorado State University, Dokkyo University, JPL-Caltech, NASA, and University of Maryland.

It is very important to remember all the colleagues who are no longer with us and who worked very hard until the last minute providing an essential contribution. This book is dedicated to the memory of a friend of all of us, Arthur Y. Hou (1947–2013). Arthur was not only the US Project Scientist of the Global Precipitation Measurement (GPM) mission, he was a man of a truly global vision who now is in place with the GPM constellation. More than that, he made great efforts to establish an international science cooperation through his gentle and unique way of approaching

xi


---



xii

Acknowledgments

each one of us. Other colleagues left us in recent times, and we want to honor them as well: David (Dave) H. Staelin (1938–2011), David I. F. Grimes (1951–2011), and James (Jim) A. Weinman (1930–2012). They all left us much too soon, and we miss them, but their work is here to testify to their essential contribution to the advancement of science and to meet the needs of mankind.

Two major international organizations gave us the opportunity to work together with a global strategy for the future: the International Precipitation Working Group (IPWG) and the World Meteorological Organization (WMO).

The senior editor (Vincenzo Levizzani) would like to recognize the ceaseless work of his coeditors in effectively putting together the material of their respective sections: F. Joseph (Joe) Turk for Section 1, Christian (Chris) D. Kummerow for Sections 2 and 3, Christopher (Chris) Kidd for Section 4, Kenji Nakamura for Section 5, and Dalia B. Kirschbaum for Section 6. Their commitment and competence largely influenced the quality level of this book.

Finally, our families are part of the project through their understanding and their moral and practical support. Without them, the writing of this book would have never even started.

<table>
  <tbody>
    <tr>
        <td>Bologna, Italy</td>
<td>Vincenzo Levizzani</td>
    </tr>
<tr>
        <td>Greenbelt, MD, USA</td>
<td>Christopher Kidd</td>
    </tr>
<tr>
        <td>Greenbelt, MD, USA</td>
<td>Dalia B. Kirschbaum</td>
    </tr>
<tr>
        <td>Fort Collins, CO, USA</td>
<td>Christian D. Kummerow</td>
    </tr>
<tr>
        <td>Saitama, Japan</td>
<td>Kenji Nakamura</td>
    </tr>
<tr>
        <td>Pasadena, CA, USA</td>
<td>F. Joseph Turk</td>
    </tr>
<tr>
        <td colspan="2">9 March 2020</td>
    </tr>
  </tbody>
</table>



---

# Contents of Volume 1

## Part I Status of Observations and Satellite Programs

**1** **The Global Precipitation Measurement (GPM) Mission** 3
Christopher Kidd, Yukari N. Takayabu, Gail M. Skofronick-Jackson,
George J. Huffman, Scott A. Braun, Takuji Kubota,
and F. Joseph Turk

**2** **Status of the CloudSat Mission** 25
Matthew D. Lebsock, Tristan S. L’Ecuyer, Norman B. Wood,
John M. Haynes, and Mark A. Smalley

**3** **The Megha-Tropiques Mission After Seven Years in Space** 45
Rémy Roca, Michel Dejus, Philippe Chambon, Sophie Cloché,
and Michel Capderou

**4** **Microwave Sensors, Imagers and Sounders** 63
Kazumasa Aonashi and Ralph R. Ferraro

**5** **Microwave and Sub-mm Wave Sensors:**
**A European Perspective** 83
Christophe Accadia, Vinia Mattioli, Paolo Colucci, Peter Schlüssel,
Salvatore D’Addio, Ulf Klein, Tobias Wehr, and Craig Donlon

**6** **Plans for Future Missions** 99
Christian D. Kummerow, Simone Tanelli, Nobuhiro Takahashi,
Kinji Furukawa, Marian Klein, and Vincenzo Levizzani

**Part II Retrieval Techniques, Algorithms and Sensors**

**7** **Introduction to Passive Microwave Retrieval Methods** 123
Christian D. Kummerow

xiii


---



xiv Contents of Volume 1

**8 The Goddard Profiling (GPROF) Precipitation Retrieval Algorithm** 141
David L. Randel, Christian D. Kummerow, and Sarah Ringerud

**9 Precipitation Estimation from the Microwave Integrated Retrieval System (MiRS)** 153
Christopher Grassotti, Shuyan Liu, Quanhua Liu, Sid-Ahmed Boukabara, Kevin Garrett, Flavio Iturbide-Sanchez, and Ryan Honeyager

**10 Introduction to Radar Rain Retrieval Methods** 169
Toshio Iguchi and Ziad S. Haddad

**11 Dual-Frequency Precipitation Radar (DPR) on the Global Precipitation Measurement (GPM) Mission's Core Observatory** 183
Toshio Iguchi

**12 DPR Dual-Frequency Precipitation Classification** 193
V. Chandrasekar and Minda Le

**13 Triple-Frequency Radar Retrievals** 211
Alessandro Battaglia, Simone Tanelli, Frederic Tridon, Stefan Kneifel, Jussi Leinonen, and Pavlos Kollias

**14 Precipitation Retrievals from Satellite Combined Radar and Radiometer Observations** 231
Mircea Grecu and William S. Olson

**15 Scattering of Hydrometeors** 249
Stefan Kneifel, Jussi Leinonen, Jani Tyynelä, Davide Ori, and Alessandro Battaglia

**16 Radar Snowfall Measurement** 277
Guosheng Liu

**17 A 1DVAR-Based Snowfall Rate Algorithm for Passive Microwave Radiometers** 297
Huan Meng, Cezar Kongoli, and Ralph R. Ferraro

**18 X-Band Synthetic Aperture Radar Methods** 315
Saverio Mori, Frank S. Marzano, and Nazzareno Pierdicca

### Part III Merged Precipitation Products

**19 Integrated Multi-satellite Retrievals for the Global Precipitation Measurement (GPM) Mission (IMERG)** 343
George J. Huffman, David T. Bolvin, Dan Braithwaite, Kuo-Lin Hsu, Robert J. Joyce, Christopher Kidd, Eric J. Nelkin, Soroosh Sorooshian, Erich F. Stocker, Jackson Tan, David B. Wolff, and Pingping Xie

---



Contents of Volume 1 xv

**20 Global Satellite Mapping of Precipitation (GSMaP) Products in the GPM Era** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 355
Takuji Kubota, Kazumasa Aonashi, Tomoo Ushio, Shoichi Shige, Yukari N. Takayabu, Misako Kachi, Yoriko Arai, Tomoko Tashima, Takeshi Masaki, Nozomi Kawamoto, Tomoaki Mega, Munehisa K. Yamamoto, Atsushi Hamada, Moeka Yamaji, Guosheng Liu, and Riko Oki

**21 Improving PERSIANN-CCS Using Passive Microwave Rainfall Estimation** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 375
Kuo-Lin Hsu, Negar Karbalee, and Dan Braithwaite

**22 TAMSAT** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 393
Ross Maidment, Emily Black, Helen Greatrex, and Matthew Young

**23 Algorithm and Data Improvements for Version 2.1 of the Climate Hazards Center’s InfraRed Precipitation with Stations Data Set** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 409
Chris Funk, Pete Peterson, Martin Landsfeld, Frank Davenport, Andreas Becker, Udo Schneider, Diego Pedreros, Amy McNally, Kristi Arsenault, Laura Harrison, and Shraddhanand Shukla

**24 Merging the Infrared Fleet and the Microwave Constellation for Tropical Hydrometeorology (TAPEER) and Global Climate Monitoring (GIRAFE) Applications** . . . . . . . . . . . . . . . . . . 429
Rémy Roca, Adrien Guérou, Rômulo A. Jucá Oliveira, Philippe Chambon, Marielle Gosset, Sophie Cloché, and Marc Schröder

---

# Contents of Volume 2

**Part IV Validation**

**25 The IPWG Satellite Precipitation Validation Effort** . . . . . . . . . . . . . 453
Christopher Kidd, Shoichi Shige, Daniel Vila, Elena Tarnavsky,
Munehisa K. Yamamoto, Viviana Maggioni, and Bathobile Maseko

**26 The GPM Ground Validation Program** . . . . . . . . . . . . . . . . . . . . . . 471
Walter A. Petersen, Pierre-Emmanuel Kirstetter, Jianxin Wang,
David B. Wolff, and Ali Tokay

**27 The GPM DPR Validation Program** . . . . . . . . . . . . . . . . . . . . . . . . 503
Riko Oki, Toshio Iguchi, and Kenji Nakamura

**28 Error and Uncertainty Characterization** . . . . . . . . . . . . . . . . . . . . . 515
Christian Massari and Viviana Maggioni

**29 Multiscale Evaluation of Satellite Precipitation Products:
Effective Resolution of IMERG** . . . . . . . . . . . . . . . . . . . . . . . . . . . . 533
Clément Guilloteau and Efi Foufoula-Georgiou

**30 Remote Sensing of Orographic Precipitation** . . . . . . . . . . . . . . . . . . 559
Ana P. Barros and Malarvizhi Arulraj

**31 Integrated Multi-satellite Evaluation for the Global Precipitation
Measurement: Impact of Precipitation Types on Spaceborne
Precipitation Estimation** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 583
Pierre-Emmanuel Kirstetter, Walter A. Petersen,
Christian D. Kummerow, and David B. Wolff

**32 Hydrologic Validation and Flood Analysis** . . . . . . . . . . . . . . . . . . . . 609
Witold F. Krajewski, Felipe Quintero, Mohamed El Saadani,
and Radoslaw Goska

xvii


---



xviii Contents of Volume 2

**33 Global-Scale Evaluation of 22 Precipitation Datasets Using Gauge Observations and Hydrological Modeling** 625
Hylke E. Beck, Noemi Vergopolan, Ming Pan, Vincenzo Levizzani, Albert I. J. M. van Dijk, Graham P. Weedon, Luca Brocca, Florian Pappenberger, George J. Huffman, and Eric F. Wood

**34 OceanRAIN – The Global Ocean Surface-Reference Dataset for Characterization, Validation and Evaluation of the Water Cycle** 655
Christian Klepp, Paul A. Kucera, Jörg Burdanowitz, and Alain Protat

## Part V Observed Characteristics of Precipitation

**35 GPCP and the Global Characteristics of Precipitation** 677
Robert F. Adler, Guojun Gu, George J. Huffman, Mathew R. P. Sapiano, and Jian-Jian Wang

**36 Global Snowfall Detection and Measurement** 699
Mark S. Kulie, Lisa Milani, Norman B. Wood, and Tristan S. L’Ecuyer

**37 Snowfall Detection by Spaceborne Radars** 717
Atsushi Hamada, Toshio Iguchi, and Yukari N. Takayabu

**38 On the Duration and Life Cycle of Precipitation Systems in the Tropics** 729
Rémy Roca, Dominique Bouniol, and Thomas Fiolleau

**39 Observational Characteristics of Warm-Type Heavy Rainfall** 745
Byung-Ju Sohn, Geun-Hyeok Ryu, and Hwan-Jin Song

**40 Satellite Precipitation Measurement and Extreme Rainfall** 761
Olivier P. Prat and Brian R. Nelson

**41 Rainfall Trends in East Africa from an Ensemble of IR-Based Satellite Products** 791
Elsa Cattani, Andrés Merino, and Vincenzo Levizzani

**42 Heavy Precipitation Systems in the Mediterranean Area: The Role of GPM** 819
Giulia Panegrossi, Anna Cinzia Marra, Paolo Sanò, Luca Baldini, Daniele Casella, and Federico Porcù

**43 Dryland Precipitation Climatology from Satellite Observations** 843
Efrat Morin, Francesco Marra, and Moshe Armon

**44 Hailfall Detection** 861
Ralph R. Ferraro, Daniel Cecil, and Sante Laviola

**45 Improving High-Latitude and Cold Region Precipitation Analysis** 881
Ali Behrangi

---



Contents of Volume 2

xix

**46 Latent Heating Retrievals from Satellite Observations** 897
Yukari N. Takayabu and Wei-Kuo Tao

## Part VI Applications

**47 Operational Applications of Global Precipitation Measurement Observations** 919
Anita LeRoy, Emily Berndt, Andrew Molthan, Bradley Zavodsky, Matthew Smith, Frank LaFontaine, Kevin McGrath, and Kevin Fuell

**48 Assimilation of Precipitation Observations from Space into Numerical Weather Prediction (NWP)** 941
Sid-Ahmed Boukabara, Erin Jones, Alan Geer, Masahiro Kazumori, Kevin Garrett, and Eric Maddy

**49 Precipitation Ensemble Data Assimilation in NWP Models** 983
Takemasa Miyoshi, Shunji Kotsuki, Koji Terasaki, Shigenori Otsuka, Guo-Yuan Lien, Hisashi Yashiro, Hirofumi Tomita, Masaki Satoh, and Eugenia Kalnay

**50 PERSIANN-CDR for Hydrology and Hydro-climatic Applications** 993
Phu Nguyen, Hamed Ashouri, Mohammed Ombadi, Negin Hayatbini, Kuo-Lin Hsu, and Soroosh Sorooshian

**51 Soil Moisture and Precipitation: The SM2RAIN Algorithm for Rainfall Retrieval from Satellite Soil Moisture** 1013
Luca Ciabatta, Stefania Camici, Christian Massari, Paolo Filippucci, Sebastian Hahn, Wolfgang Wagner, and Luca Brocca

**52 Drought Risk Management Using Satellite-Based Rainfall Estimates** 1029
Elena Tarnavsky and Rogerio Bonifacio

**53 Two Decades of Urban Hydroclimatological Studies Have Yielded Discovery and Societal Benefits** 1055
J. Marshall Shepherd, Steven J. Burian, Menglin Jin, Chuntao Liu, and Bradford Johnson

**54 Validation of Climate Models** 1073
Francisco J. Tapiador

**55 Extreme Precipitation in the Himalayan Landslide Hotspot** 1087
Thomas Stanley, Dalia B. Kirschbaum, Salvatore Pascale, and Sarah Kapnick

**56 The Value of Satellite Rainfall Estimates in Agriculture and Food Security** 1113
Tufa Dinku

---



xx Contents of Volume 2

**57 Using Satellite Estimates of Precipitation for Fire Danger Rating** 1131
Robert D. Field

**58 Variability of Satellite Sea Surface Salinity Under Rainfall** 1155
Alexandre Supply, Jacqueline Boutin, Gilles Reverdin, Jean-Luc Vergely, and Hugo Bellenger

---

# List of Figures

Fig. 1.1 Schematic of the Global Precipitation Measurement (GPM) mission Core Observatory (CO; left) and the GPM international partner constellation (right). Note that as of 21 May 2018 the KaPR swath width has been increased to 245 km to match that of the KuPR. (Note that the GPM-CO alternates flight directions to keep the canted solar panel towards the Sun: half the time the flight direction is 180° from that shown) 5

Fig. 1.2 An infrared image from Himawari 8 of the "lake effect" clouds over the Japan Sea (top), and three-dimensional snapshot of shallow precipitation from those clouds observed by the effective radar reflectivity at Ku band of the GPM/DPR at 0955 UTC 2 December 2014 (bottom) 7

Fig. 1.3 Hail detection in the thunderstorm near Fort Worth, Texas, on 26 May 2015. **(a)** Hydrometeor identification by a ground-based polarimetric radar and **(b)** the output from the "flagHeavyIcePrecip" from the DPR product. (Adapted from Iguchi et al. 2018; see the reference for details) 8

Fig. 2.1 Highlights several of the unique features of the CloudSat data. The image shows an example of a tropical deep convective system with obvious heavy attenuation and multiple scattering effects. Attenuation can be so heavy at times that the surface reflection is not observed. The convective core area is identifiable through the lack of a radar bright band and elevated reflectivity maximum. Also notice the frequent detection of shallow isolated light showers with reflectivity generally <8 dBZ 27

xxi


---



xxii

List of Figures

Fig. 2.2 Panel **(a)** shows an estimate of effect of CloudSat fixed diurnal sampling on the annual mean Probability of Precipitation (PoP). The map shows the difference of the full CMORPH dataset from 2007 to 2010 from the CMORPH dataset subsampled at the CloudSat ground track. In most regions the effect causes an underestimate of the PoP that can be as large as 6%. Panel **(b)** shows an estimate of the effect of non-scanning sampling on the PoP again using CMORPH. The CMORPH data is restricted to the CloudSat sampling times at each latitude and compared to that calculated from a single cross section at a random longitude 28

Fig. 2.3 The fraction of total (rain & no-rain) pixels in which the surface signal is saturated by heavy attenuation 28

Fig. 2.4 The frequency of occurrence of surface precipitation of any phase. Occurrence is estimated using the certain precipitation flag in the 2C-Precip-Column product described below using data from 2007 to 2010 29

Fig. 2.5 The global frequency of occurrence of convective cores identified in CloudSat’s 2C-Precip-Column product using data from 2007 to 2010 31

Fig. 2.6 Variation of clear-sky surface backscatter with wind speed as derived from matched AMSR-E and CloudSat wind observations over the ocean, for a multi-month period and a fixed sea surface temperature range of 15 to 25 °C. Colors indicate normalized frequency of occurrence; the red line is the mean, and the dashed black lines are one standard deviation either side of the mean 34

Fig. 2.7 (panel a) the accumulate rainfall from the CloudSat 2C-Rain Profile product for the years 2007–2010; (panel b) the same from the DRP Ku band algorithm for a 2-year period from 2014 to 2016; (panel c) the difference between panels a and b; (panel d) the scatter plot of the rate difference shown in panel c with the saturation occurrence fraction from CloudSat 40

Fig. 3.1 Two-years times series of the flip maneuver schedule based on the beta solar angle (the angle between the sun direction and the orbital plan; see Capderou 2014 for details) 48

Fig. 3.2 Schematic of the effect of the relaxed control of the yaw 48

Fig. 3.3 Time series of maximum (red) and minimum (blue) latitude of the scan of the SAPHIR instrument 50

Fig. 3.4 Time series of the noise (NEΔT) for each channel of the SAPHIR sounder 51

Fig. 3.5 Zonal mean of the fraction of time for which the baseline product and the No-meghatropiques products differs by more than 50% of the daily accumulation. Summer 2012 conditions are considered. (Adapted from Roca et al. 2018) 52

---



List of Figures

xxiii

Fig. 3.6 Brightness temperatures from SAPHIR channel 6 over the Tropical Atlantic on 6 September, 2017. The four scans correspond to consecutive orbits and show the developments of the two hurricanes IRMA and JOSE. These two hurricanes were observed within the same orbit, illustrating the unique feature of this observing system 54

Fig. 3.7 Fraction of SAPHIR observations per month which have been received and used a Météo-France before the cutoff times of the Météo-France global data assimilation system (4–5 h depending on the assimilation cycle) (Courtesy of Hervé Benichou, Météo-France DIROP/COMPAS/COM). The period starts in June 2015, which corresponds to the beginning of the operational assimilation of Megha-Tropiques data at Météo-France. The dashed red line refers to the averaged fraction over this 4-year period 56

Fig. 4.1 A time sequence of the microwave images of the super-typhoon NANGKA from 0540 to 1731 UTC 12 July 2015, superimposed on MTSAT IR images. (From NRL Tropical Cyclone page – https://www.nrlmry.navy.mil/TC.html, last accessed 21 Oct 2018) 64

Fig. 4.2 Scan geometries of the SSM/I sensors. (The COMET Program – https://www.meted.ucar.edu/index.php, last accessed 21 Oct. 2018) 68

Fig. 4.3 Scan geometries of the TRMM PR, TMI and VIRS. (Adapted from Kummerow et al. 1998) 69

Fig. 4.4 Scan geometries of the AMSU-A and AMSU-B sensors. (The COMET Program – https://www.meted.ucar.edu/index.php, last accessed 21 Oct 2018) 76

Fig. 5.1 MWI and ICI accommodation on Metop-SG 84

Fig. 6.1 State-of-the-art microwave monolithic integrated circuits low noise amplifiers’ noise figure 108

Fig. 6.2 A deployable reflector antenna concept for the small satellites. The antenna reflector surface can fit to less than 1.5 U volume and it is designed to operate up to ~100 GHz 108

Fig. 6.3 Roadmap of spaceborne precipitation radar 112

Fig. 7.1 Demonstrative atmospheric transmittances (total, H<sub>2</sub>O and O<sub>2</sub>) as a function of frequency and wavelength in the microwave region. (Adapted from Liou 2002, p. 415) 125

Fig. 7.2 Example of brightness temperatures as a function of column averaged rain rate at 19 GHz used to illustrate the “beamfilling” or non-homogeneous rain distribution effect 127

---



xxiv List of Figures

<table>
  <tbody>
    <tr>
        <td>Fig. 8.1</td>
<td>Schematic for the GPROF Processing Algorithm. The three main components are the Sensor Profile Database, the Preprocessor, and the GPROF 2017 Processing Engine</td>
<td>143</td>
    </tr>
<tr>
        <td>Fig. 8.2</td>
<td>GPROF database distribution of Total Precipitable Water (TPW) and Two-Meter Temperature (T2M) profiles included in the a priori database year. These represent the number of database profiles in each TPW/T2 m and Surface Type category</td>
<td>146</td>
    </tr>
<tr>
        <td>Fig. 8.3</td>
<td>GPROF GMI retrieval of surface rain for hurricane Harvey, 25 August 2017 shortly before making landfall on the Texas coast. Over 60 inches (1500 mm) of precipitation was recorded near Houston over the next 5 days</td>
<td>149</td>
    </tr>
<tr>
        <td>Fig. 8.4</td>
<td>Solid (Snow) vs. Liquid Precipitation and Wet Bulb for both ocean and land locations. (Adapted from Sims and Liu 2015)</td>
<td>150</td>
    </tr>
<tr>
        <td>Fig. 8.5</td>
<td>GPROF zonal averaged precipitation retrieval for Total (left) and Frozen precipitation (right) for five GPM constellation sensors</td>
<td>151</td>
    </tr>
<tr>
        <td>Fig. 9.1</td>
<td>Schematic of MiRS processing components and data flow showing MiRS core retrieval and post-processing components. Core products are retrieved simultaneously as part of the state vector. Post-processing products are derived through vertical integration (water vapor, hydrometeors), catalogs (SIC, SWE), or fast regressions (rain rate). Post-processed hydrometeor retrieval products are indicated in red: Rain Rate, Graupel Water Path, Rain Water Path and Cloud Liquid Water</td>
<td>155</td>
    </tr>
<tr>
        <td>Fig. 9.2</td>
<td>Example of rain water (left) and graupel water (right) retrieval evolution for a single vertical profile based on NOAA-18 AMSU-MHS measurements. Top panels show rain and graupel water profile retrieval as function of iteration (3 iterations total). The remaining panels show the CRTM Jacobians with respect to rain and graupel at channels 15, 17, 18, 19, 20 (89, 157, 183 ± 1, 183 ± 3, and 190 GHz), for each iteration. In this case, the retrieval converged in 3 iterations. Rain and graupel particle effective radii were assumed to be 500 microns</td>
<td>159</td>
    </tr>
<tr>
        <td>Fig. 9.3</td>
<td>Comparison of global rain rate maps on 21 June 2016 from MiRS when applied to GPM/GMI (left) and SNPP/ATMS measurements (right). Examples of weather systems detected by both satellites are circled</td>
<td>160</td>
    </tr>
  </tbody>
</table>



---



List of Figures

xxv

<table>
  <tbody>
    <tr>
        <td>Fig. 9.4</td>
<td>MiRS retrievals of hydrometeor and temperature structure around Typhoon Soudelor from Suomi-NPP/ATMS valid 0445 UTC on 6 August 2015. Panels show surface rain rate (top left), rain water 0.01 mm isosurface with temperature profile superimposed (top right), graupel water 0.05 mm isosurface with temperature profile superimposed (bottom left), and a vertical cross-section along 21°N of both rain and graupel water (bottom right)</td>
<td>161</td>
    </tr>
<tr>
        <td>Fig. 9.5</td>
<td>Comparison of MiRS SNPP/ATMS instantaneous rain rate (mm/h) (top) with operational NWS Stage IV rain rate (bottom) over the conterminous US for two different dates, 16 March 2016 (left), and 28 July 2016 (right)</td>
<td>162</td>
    </tr>
<tr>
        <td>Fig. 9.6</td>
<td>Example of impact of using retrieved CLW over land in the land precipitation estimation from SNPP/ATMS on 01 May 2016. Shown are <strong>(a)</strong> MiRS operational rain rate (mm/h), <strong>(b)</strong> MiRS rain rate using CLW, <strong>(c)</strong> MRMS Q3 radar-gauge analysis valid at 1900 UTC (units in inches), <strong>(d)</strong> MiRS Liquid Water Path (LWP = RWP + CLW, mm), and <strong>(e)</strong> visible satellite image from GOES-East valid at 1915 UTC</td>
<td>164</td>
    </tr>
<tr>
        <td>Fig. 9.7</td>
<td>Probability distribution functions of MIRS ATMS vs. Stage IV baseline (operational, no CLW included in rain rate estimation) and experimental rain rate (CLW included) over land during September–November 2016. Note improved frequency distribution and agreement with Stage IV in experimental rain rate. Distributions are for all points with Stage IV rain rate greater than 0 mm h<sup>-1</sup></td>
<td>165</td>
    </tr>
<tr>
        <td>Fig. 11.1</td>
<td>DPR’s scan pattern before May 21 2018 (left) and after May 21 2018 (right). KaHS beams scan in the inner swath before May 21 2018, but now they scan in the outer swath and match with KuPR’s beams. Numbers in color indicate angle bin numbers for KuPR (blue), KaMS (yellow), and KaHS (red)</td>
<td>184</td>
    </tr>
<tr>
        <td>Fig. 11.2</td>
<td>DPR L2 algorithm flow</td>
<td>186</td>
    </tr>
<tr>
        <td>Fig. 12.1</td>
<td>Schematic plot of DFR<sub>m</sub> profile with key points A, B, C, and D. Point A: slope of DFR<sub>m</sub> has peak value. Point B: local maximum of DFR<sub>m</sub>. Point C: local minimum of DFR<sub>m</sub>. Point D: DFR<sub>m</sub> value near surface</td>
<td>194</td>
    </tr>
<tr>
        <td>Fig. 12.2</td>
<td>Histogram of DFR<sub>m</sub> index V3 and CDFs (cumulative density function) using total of 121,859 vertical profiles from GPM real data. <strong>(a)</strong> Histogram and 1-CDF of V3 for Stratiform rain. Red dashed line represents 1-CDF. <strong>(b)</strong> Histogram and CDF of V3 for Convective rain. Red dashed line represents CDF</td>
<td>196</td>
    </tr>
<tr>
        <td>Fig. 12.3</td>
<td>Block diagram of precipitation type classification model</td>
<td>197</td>
    </tr>
<tr>
        <td>Fig. 12.4</td>
<td>Block diagram of melting layer detection for DFR<sub>m</sub> method</td>
<td>198</td>
    </tr>
  </tbody>
</table>



---



xxvi

List of Figures

Fig. 12.5 Left column (from top to bottom): comparison of melting layer top height (in km) between dual-frequency classification method and Ku only method for cyclone, hurricane and typhoons shown in Table 12.2. Right column illustrates similar results for melting layer bottom height (in km) ......................................... 200
Fig. 12.6 **(a)** GPM DPR overpass of rainfall rate on March 17, 2014 (#000272). Circled A, B and C represents snow, stratiform rain, and convective rain. **(b)** Averaged reflectivity profiles as well as dual-frequency ratio profile for snow. **(c)** Same as **(b)** for stratiform rain. **(d)** Same as **(b)** for convective rain ............... 202
Fig. 12.7 Vertical cross section at nadir of DPR overpass shown in Fig. 12.6a ............................................................ 203
Fig. 12.8 GPM DPR overpass of rainfall rate on March 17, 2014. Scan # from 4894 to 5142. **(a)** Histogram of mean DFR<sub>m</sub> slope in absolute value. **(b)** Histogram of maximum reflectivity at Ku band. **(c)** Histogram of storm top height ........................... 204
Fig. 12.9 Large scale study of the snow index using GPM DPR profiles. Histograms of the snow index are shown for rain (blue) and snow (red). The blue dashed curve is the cumulative density function (CDF) for rain. The red dashed curve is 1-CDF for snow ........ 205
Fig. 12.10 Flowchart to perform surface snowfall identification in profile classification module of GPM DPR level 2 algorithm ............ 206
Fig. 12.11 Match ratio for 16 validation cases during the years 2014–2018 ............................................................ 208
Fig. 13.1 CloudSat and GPM coincident overpass observations of a convective precipitation system developed over the Banda Sea in the Maluku Islands of Indonesia. Measurements from a suite of microwave sensors are shown. Top row: CloudSat W-band reflectivity; second row: GPM Ka-band reflectivities for the high sensitivity (HS) scan; third row: GPM Ku-band reflectivity for the normal scan (NS). The dataset of coincident overpasses is from the GPM product 2B-CSATGPM from the NASA Precipitation Processing System developed by J. Turk, JPL ..... 213
Fig. 13.2 Left: effective DFR<sub>Ka-W</sub> vs DFR<sub>Ku-Ka</sub> for population of raindrops at 15 °C with Γ DSDs with different m as indicated in the legend and with color-coded mean mass-weighted diameter. Right: extinction coefficient vs rain rate for exponential DSDs with intercept parameters as indicated in the legend. Scattering properties are computed using T-matrix ........................... 216
Fig. 13.3 Effective DFR<sub>Ka-W</sub> vs DFR<sub>Ku-Ka</sub> for population of ice crystals computed different scattering tables. The density plots show the distribution measured by a triple-frequency radar during one of the GPM field campaigns ............................................ 218

---



List of Figures

xxvii

Fig. 13.4 Left: gas-corrected Ka-band reflectivity (top), DFR<sub>Ku-Ka</sub> (center) and DFR<sub>Ka-W</sub> (bottom) for a flight on the 1 December 2016. Right top: flight tracks across the Olympic Peninsula from the Olympic Mountains range toward and beyond the NPOL radar (black dot) on the Pacific coastline. The UTC time of DC-8 (external contour) and Citation (internal contour) aircraft paths are modulated in color (see color bar). The position of the Citation is shown in the top left panel. Right bottom: hydrometeor classification according to the multi-frequency method of Tridon et al. (2019) 220

Fig. 13.5 Retrieved parameters for the leg shown in Fig. 13.4: mean mass-weighted maximum size (top), IWC (center) and flux (bottom). The right bottom panel shows the bulk ice density as defined in Leinonen et al. (2018) 221

Fig. 13.6 Comparison between in-situ and retrieved microphysical properties as sample by the Citation aircraft in the ice part corresponding to the upper leg as shown in Fig. 13.4. Left column: mean mass weighted particle size (top) and ice water content (bottom) for the in-situ and for the two retrievals considered in this paper. The blue lines and the blue bands correspond to the a-priori and its standard deviation. Right panel: scatterplot of IWC vs D<sub>m</sub> for the in-situ and for the two retrievals. Note that the in-situ D<sub>m</sub> and IWC are derived from the PSD measurements based on the assumption that the mass-size follows that of lightly rimed B-model of Leinonen and Szyrmer (2015) 222

Fig. 13.7 Shift of the retrieved particle size distributions towards lower sizes. Figure prepared by L. Pfitzenmaier (see Pfitzenmaier et al. 2019 for details) 224

Fig. 14.1 Illustration of two possible strategies to mitigate the large mismatches between the radar and radiometer footprint sizes in satellite combined retrievals 234

Fig. 14.2 (Left) Example of combined surface precipitation estimates for GPM orbit 605 on 1 October 2014. (Right) The associated Multi-Radar/Multi-Sensor (MRMS) estimates 238

Fig. 14.3 Density scatterplot of GPM combined V06 vs reference MRMS convective precipitation (mm h<sup>−1</sup>) at the footprint scale over the period April 2014–October 2014 239

Fig. 14.4 (Left) Example of liquid water path (LWP) derived from GMI observations over oceans for orbit 003351 on 1 October 2014. (Right) The associated combined surface precipitation. The magnitude of the LWP suggests that light precipitation is undetected by the DPR 240

---



xxviii

List of Figures

Fig. 14.5 (Left) Example of Ku-band PIA derived by the combined algorithm for orbit 003539 on 13 October 2014. (Right) The associated Ku-band PIA estimated exclusively from GMI observations 242

Fig. 14.6 (Left) Ku-band PIA derived by the combined algorithm for orbit 003351 on 1 October 2014. (Right) The associated Ku-band PIA derived from GMI brightness temperatures using the extended formulation described in the text 244

Fig. 15.1 Extinction (left) and backscattering (right) cross sections for spheres (continuous lines), perfectly oriented spheroids (dashed) and Rayleigh spheres (dotted) for single raindrops at 9.6 (red), 35.5 (green) and 94 (blue) GHz 260

Fig. 15.2 Reflectivity per unit mass for an exponential drop size distribution vs mean mass-weighted equi-volume diameter for spheres (continuous lines), perfectly oriented spheroids (dashed) at 9.6 (red), 35.5 (green) and 94 (blue) GHz 260

Fig. 15.3 Backscattering ($Q_{bk}$, left) and extinction ($Q_{ext}$, right) efficiencies defined as $Q = \sigma / \pi r_{eff}^2$ with $r_{eff}$ being the radius of the equal mass ice sphere and $\sigma$ the corresponding cross section. The size parameter x combines the dependence of the scattering variables on particle mass and wavelength. Spheroid approximations include spheres of solid ice (continuous black line), spheres with an ice-air mixture (black long-dashed) representing the mass-size relation of Brown and Francis (1995), and spheroids with the same mass-size relation but with and aspect ratio of 0.6 (black dotted). Scattering properties for unrimed (gray dots) and rimed (black dots) calculated with DDA in Leinonen and Szyrmer (2015) (results shown are for particle model B and the second most rimed particles). The SSRGA (gray solid line) has been derived for the same ensemble of unrimed aggregates (Leinonen et al. 2018a, b). The vertical lines denote the size parameter for X, Ka and W Band assuming a particle mass of 10 mg which corresponds for example for the unrimed aggregates to a maximum snowflake size of 3 cm 263

Fig. 15.4 Extinction (left) and backscattering (right) cross sections for partially melted snow aggregates at 10% (dark) and 50% (gray) melted fractions. Results are from DDA scattering simulations (Ori et al. 2014) at 9.6 (continuous), 35.5 (dashed) and 94 (dash-dotted) GHz 269

Fig. 16.1 The spread of Z-S relations under different assumptions of particle shapes. (Adapted from Hiley et al. 2011) 280

---



List of Figures

xxix

Fig. 16.2 Z-S relation for three nonspherical snowflakes. A least square fitting curve and relation by Matrosov (2007) are also shown. (Adapted from Liu 2008b) .......................................... 281

Fig. 16.3 Scatterplot of coincident CloudSat CPR and GPM/DPR Ku-band reflectivities for snowing cases. Data in the green box are those above the minimum detection for both Ku and CPR radars ...... 282

Fig. 16.4 PDFs and cumulative PDFs of snowfall occurrence and snowfall rate derived by coincident CPR and DPR observations using Z-S relations as discussed in the text. Data period for these plots is from March 2014 to December 2015 ............................... 283

Fig. 16.5 CloudSat CPR radar reflectivity for 2 snowfall cases on 21 August 2007 (top) and 17 July 2006 (bottom) over 50–60°S. The top case is associated with deep snowing clouds cross a frontal system and the bottom case is associated with very shallow snowing cloud cells next to moderate deep snowing clouds . . . . . 284

Fig. 16.6 Frequency of total precipitation (rain and snow, left), frequency of snowfall (middle) and mean snowfall rate (right) for northern (top) and southern (bottom) hemispheres derived from CloudSat observations from July 2006 to June 2008. The diagrams cover the area from the Poles to 40°N/S. Detailed descriptions of the retrieval method can be found in Liu (2008b) ..................... 285

Fig. 16.7 Zonally averaged frequency of occurrence of rainfall (blue), frequency of snowfall (gray, stacked above blue) and snowfall rate (red). Derived using CPR -15 dBZ as precipitation threshold, rain-snow separation scheme of Sims and Liu (2015), and Z-S relation of Liu (2008b) ..................................... 286

Fig. 16.8 Number and volume frequency distributions of snowfall rate derived from CloudSat observations. Note the frequencies are calculated in a snowfall rate interval on logarithm scale . . . . . . . . . 286

Fig. 16.9 Mean profiles for a given near surface snowfall rate for **(a)** over ocean and **(b)** over land environments. CloudSat observations from July 2006 to June 2007 are used. (Adapted from Liu 2008b) ............................................................... 287

Fig. 16.10 Relation between near surface snowfall rate and cloud top height as expressed by snowfall profiles frequency distributions for snowfall events over **(a)** ocean and **(b)** land. The frequency values are normalized so that the maximum frequency is 100. (Adapted from Liu 2008b) .......................................... 288

---



xxx List of Figures

Fig. 16.11 Mean liquid water path as a function of cloud top temperature and near surface radar reflectivity for different snowing cloud types: **(a)** Isolated shallow clouds, **(b)** Isolated deep clouds, **(c)** extended shallow clouds, and **(d)** Extended deep clouds. Coincident CloudSat CPR and Aqua AMSR-E observations from June 2006 to June 2010 are used. Note that the LWP color scales for isolated and extended clouds are different. (Adapted from Wang et al. 2013) 289

Fig. 16.12 Mean snowfall rate maps derived from multiple years of CloudSat (2007–2010), GMI (March 2014–Feb 2018), and MHS (2007–2010). GMI algorithm is trained by combined CloudSat and DPR radar data. No observations in blank areas. MHS algorithm is trained by CloudSat CPR 291

Fig. 17.1 CloudSat derived ice water content (IWC) profiles. The values have been normalized 306

Fig. 17.2 Stage IV vs. S-NPP SFR scatter plot from **(a)** before calibration, and **(b)** after calibration 307

Fig. 17.3 PDFs of S-NPP SFR and Stage IV **(a)** before, and **(b)** after calibration 308

Fig. 17.4 S-NPP ATMS SFR using **(a)** satellite-only SD algorithm, and **(b)** hybrid SD algorithm during a major snowfall event on 5 February 2014 in the US Image **(c)** is the near coincident radar reflectivity which covers both snowfall and rainfall (in the southern part of CONUS). The noted oval areas in **(a)** and **(b)** show legitimate snowfall that was missed by the satellite-only algorithm but captured by the hybrid algorithm 309

Fig. 17.5 **(a)** Scatter plot of Stage IV vs. collocated S-NPP SFR validation data, and **(b)** PDFs of the same data sets 310

Fig. 17.6 Comparison of **(a)** S-NPP SFR 3-month average from January - March 2017 and **(b)** the corresponding Stage IV data 310

Fig. 18.1 (Lower left image) Synoptic view of Hurricane Gustav over south eastern Louisiana on September 2, 2008 12:00 UTC taken from NEXRAD weather radar reflectivity mosaic. The white box shows an outer rain band around 30.5° N × 89.5° W. (Central image) Geographic representation of the NEXRAD image at 0.86° elevation, acquired by the S-band radar (KMOB, in figure) near Mobile (Alabama). The semi-transparent rectangular box represents the scene of interest, acquired by TSX X-SAR on 2 September 2008 12:00 UTC in HH polarization and ScanSAR mode (100 km swath). (Upper right image) TSX quicklook of the acquisition in arbitrary units at 100-m resolution; flight direction is indicated. (Adapted from Marzano et al. 2010) 319

---



List of Figures

xxxi

Fig. 18.2 Correlation diagram between NRCS values X-band $\sigma_{SAR}$ against co-located and co-registered S-band NEXRAD weather-radar reflectivity Z, for a selected region of interest (ROI) of the scene. The upper axis provides the estimated rain-rate from NEXRAD data using the Marshall-Palmer relation (Bringi and Chandrasekar 2001). The best-fitting curve is also plotted. (Adapted from Marzano et al. 2010) 320

Fig. 18.3 TRMM observations, at 15:30 UTC, for the case study of Hurricane Gustav. (Top panels) TRMM 1B11 brightness temperature (TB) product relative to TMI channel 7 (37 GHz horizontal polarization, left), beam effective field-of-view (EFOV) of $16 \times 9\text{ km}^2$, and TMI channel 9 (85.5 GHz horizontal polarization, right) with a main-beam EFOV of $7 \times 5\text{ km}^2$. The cyclonic cell indicated in Fig. 18.2 is well captured. (Bottom panels) The TRMM 1C21 radar reflectivity (dBZ) product, relative to PR normal sample (left) range bin 75, and PR rain oversample (right), range bin 16. Note that the PR swath is 220 km wide (reduced in the oversampled product) and the range resolution is 0.25 km; TMI swath is 760 km wide. (Adapted from Marzano et al. 2011) 321

Fig. 18.4 Schematic SAR NRCS (in dB) as a function of cross-track scanning distance $x$, showing enhanced values on the left of the cross-over point caused by scattering from the cloud top and attenuation from rain in the lower cloud on the right. The viewing angle with respect to nadir (incidence angle) is $\theta$, while the cloud extension is w. The symbol $\Delta r$ indicates the width of the slant slice of the atmosphere representing the SAR side-looking resolution volume. The figure also shows the energy fluxes and the e.m. parameters of the model according to Marzano et al. (2012) and Mori et al. (2017a) 323

Fig. 18.5 Example of System for Atmospheric Model (SAM) vertical slice for a Compact Medium Single Cell cloud. Values indicate water content $W$ in $\text{g m}^{-3}$ of the simulated distributions of snow, rain, ice and cloud particles 326

Fig. 18.6 SAR simulated response in terms of normalized Radar cross section $\sigma_{SARhh}$ (horizontal transmitted and received), co-polar ratio $Z_{SARco}$ and complex correlation coefficient $\rho_{SARco}$ for the SAM realistic cell of Fig. 18.5. Four SAR frequencies evaluated (5.4, 9, 14 and 35 GHz). Considered background are Spheres, Dihedrals, Cylinders, and a semi-empirical bare soil (SEM) 327

Fig. 18.7 Flowchart of the procedure described in Mori et al. (2016) for detecting flooded and cloud areas in X-SAR images and estimating the relative precipitation rate 332

---



xxxii List of Figures

Fig. 18.8 Voghera case study. Left image is a geocoded quicklook of the CSK acquisition (at 05:18 UTC). Right figure shows the corresponding Italian National Mosaic Vertical Maximum Intensities (VMI) at 05:30 UTC (~15 min acquisition time); the ellipse approximately encloses the case study area. (Adapted from Mori et al. 2017b) 334

Fig. 18.9 Precipitation maps for the case study of Fig. 18.8. Left map is obtained from X-SAR data with the procedure of Sect. 18.5.1 (filtered and smoothed to WR resolution), right map is obtained by WR VMI data and a Marshall-Palmer formula. (Adapted from Mori et al. 2017b) 334

Fig. 18.10 Right plot shows the analysis of the position error between the WR precipitation map (shaded background) and the SAR one (foreground) for the case study of Fig. 18.8. Values have been normalized to the maximum of the dataset. Note that the WR data precedes the SAR data by ~12 min. Left plot shows Complementary Cumulative Distribution Function (CCDF) for the same case study. Blue lines represent SAR data degraded at WR resolution (1000 m); red lines represent WR data. (Adapted from Mori et al. 2017b) 335

Fig. 19.1 PMW sensor Equator-crossing times for 12-24 Local Time (LT; 0000-1200 LT is the same) for the modern PMW sensor era. These are all ascending passes, except F08 is descending. Shading indicates that the precessing TRMM, Megha-Tropiques, and GPM cover all times of day with changes that are too rapid to depict at this scale. (Image by Eric Nelkin (SSAI; GSFC), 12 July 2018; https://pmm.nasa.gov/sites/default/files/imce/times_allsat.jpg holds the current version, last accessed 1 Apr. 2019) 345

Fig. 19.2 Rainfall accumulations for the week of 25-31 August 2017 over the US Gulf Coast for NOAA Multi-Radar Multi-Sensor (MRMS) data (left) and IMERG V05 Late estimates (right). Houston, Texas is just west of Area 1 350

Fig. 19.3 Time series of area-average rainfall for the week of 25-31 August 2017 over the US Gulf Coast for the near-coastal Area 1 (top) and the more inland Area 2 (bottom). Houston, Texas is just west of Area 1. The IMERG Late averages are labeled precipitationCal, and the IR-based precipitation time series is IRprecipitation 351

Fig. 20.1 Image of "JAXA Global Rainfall Watch" website (http://sharaku.eorc.jaxa.jp/GSMaP/, last accessed 15 Oct. 2018) 357

Fig. 20.2 Process flowchart for the GSMaP product 359

Fig. 20.3 Distribution of the daily rain amount around Japan on June 25, 2017 for **(a)** JMA radar-AMeDAS, **(b)** GC V6, **(c)** MVK V6, **(d)** NRT V6, **(e)** NOW V6, and **(f)** Hydro-Estimator (H-E) 365

---



List of Figures

xxxiii

Fig. 20.4 Time series of the correlation coefficient (CC) for the GSMaP products and the H-E with reference to the JMA’s Radar-AMeDAS around Japan in 0.25 deg lat/lon grid and daily accumulation from Apr. 1, 2017 to Dec. 31, 2018. Monthly mean was applied to the daily CC values. Open circles denote the GA; closed circles denote the MVK; plusses denote the NRT; crosses denote the NOW; and triangles denote the H-E 365

Fig. 20.5 Time series of the root mean square error (RMSE) for the GSMaP products and the H-E with reference to the JMA’s Radar-AMeDAS around Japan in 0.25 deg lat/lon grid and daily accumulation from Apr. 1, 2017 to Dec. 31, 2018. Monthly mean was applied to the daily RMSE values. Open circles denote the GA; closed circles denote the MVK; plusses denote the NRT; crosses denote the NOW; and triangles denote the H-E 366

Fig. 20.6 Accumulated rainfall (mm year<sup>−1</sup>) over 3 months: June to August 2015 for **(a)** MRMS, **(b)** MVK V6, and **(c)** GA V6. The MRMS was analyzed over areas where the RQI was more than 50 367

Fig. 20.7 Two-dimensional distribution function of daily precipitation over 3 months from June to August 2015. Horizontal axis shows the rain rate of the MRMS, and vertical axis shows rain rates of **(a)** MVK and **(b)** GA. Hatch color shows the sample number of occurrences. The average value (squares) and the standard deviation (1 sigma, bars) are shown for bins of 0.2 mm h<sup>−1</sup> of the MRMS with the horizontal axis as a reference. The broken line is a one-to-one line 368

Fig. 21.1 The major processing modules and data flows in IMERG. The blocks are organized by contributing institution; the final code package is an integrated system. (Adapted from Huffman et al. 2018) 378

Fig. 21.2 Cloud image segmentation, feature extraction, classification, and rainfall estimation of the PERSIANN-CCS algorithm 379

Fig. 21.3 **(a)** The Tb-R relationship of $20 \times 20$ SOFM cloud patch groups and **(b)** the Tb-R curves with respect to the SOFM groups G0~G6 379

Fig. 21.4 PMW sensor Equator-crossing time for 1200–2400 local time for the modern PMW sensor era. Image by Eric Nelkin (SSAI/GSFC, 5 july 2017; current version at https://precip.gsfc.nasa.gov/times_allsat.jpg, last accessed 5 Apr. 2019; also see Huffman et al. 2018) 380

Fig. 21.5 Matching rainfall from PMW satellites with the rainfall from PERSIANN-CCS using PMM rainfall. (Adapted from Karbalaee et al. 2017) 381

---



xxxiv

List of Figures

Fig. 21.6 **(a)** PERSIANN-CCS rainfall, **(b)** PMW recalibrated PERSIANN rainfall and **(c)** PMW rainfall maps at 0330 UTC, 9 March 2012. (rain rate: mm h<sup>−1</sup>) 382

Fig. 21.7 **(a)** cloud image from longwave infrared channel; **(b)** segmentation of IR cloud image at Tb = 253 K, **(c)** segmentation of cloud image at Tb = 260 K, and **(d)** segmentation of cloud image at Tb = 280 K 385

Fig. 21.8 PERSIANN-CCS mapping curves using IR Tb thresholds at **(a)** 253 and **(b)** 280 K 386

Fig. 21.9 Rainfall map at 1600 UTC time 3 July 2012, from **(a)** Q2 radar map, **(b)** satellite image of IR brightness temperature, and the rainfall maps estimated from segmentation using thresholds from Tb = **(c)** 253, **(d)** 260, and **(e)** 280 K 386

Fig. 22.1 The WMO World Weather Watch global distribution of the Regional Basis Synoptic Network weather stations providing SYNOP (surface synoptic observations) reports during October 2002. (WMO 2003). The colour denotes each station's reporting rate 394

Fig. 22.2 Schematic summarising the TAMSAT calibration and rainfall estimation process. Squares denote inputs or outputs and ovals denote processes. (Adapted from Maidment et al. 2017) 397

Fig. 22.3 TAMSAT v3.0 rainfall total (left) and rainfall anomaly (right) for August 2017 398

Fig. 22.4 Full disc (background) Meteosat-8 thermal-infrared image captured at 1800 UTC on 12 August 2005. The grey scale assigned signifies warmer (colder) surfaces as the darker (whiter) regions. A subset (foreground) of this image projected onto a longitude-latitude grid over West Africa giving the brightness temperature (scale in K) of the scene observed 399

Fig. 22.5 Schematic illustrating the assumptions in the TAMSAT algorithm. Clouds with tops colder than the threshold temperature (T<sub>t</sub>) are assumed to be raining, while clouds with tops warmer than T<sub>t</sub> are assumed not to be raining (schematic by David Grimes) 399

Fig. 22.6 TAMSAT v3.0 threshold temperature (T<sub>t</sub>) maps for January (left) and August (right) respectively 401

Fig. 23.1 The number of monthly station data used in the production of the CHIRPS Final precipitation data 411

Fig. 23.2 CHIRPS2.1 schema 415

Fig. 23.3 Map of 14,197 stations used in the validation analysis 419

Fig. 23.4 Plots of station means (x-axis) and IRP (red diamonds), CHIRP2.0 (blue skinny diamonds) and CHIRP2.1 (yellow circles) means (y-axis). Data stratified binned by CHIRP2.0 values 420

---



List of Figures

xxxv

Fig. 23.5 Empirical correction factors obtained from the station data and IRP averages (yellow circles) along with regression estimates based on the IRP means 420

Fig. 23.6 Change in standard deviation (CHIRPS2.1 minus 2.0). Red circles indicate a decline of $-2$ mm or more, orange circles indicate decreases of between $-1$ and $-2$ mm, grey circles indicate change values between $-1$ and 1 mm, cyan circles had changes between $+1$ and $+2$ mm, blue circles had changes greater than $+2$ mm 422

Fig. 23.7 Top – CHIRP POD for events with at least 20 mm of precipitation and change in $+20$ mm POD (CHIRPS2.1 minus 2.0). Middle – Map of changes in $20 +$ mm POD (CHIRPS2.1 minus 2.0). Cyan circles indicate POD increases between 5 and 10 percent, blue circles had changes greater than 10 percent. Average increase in POD was 11%. Bottom – Map of changes in FAR (CHIRPS2.1 minus 2.0). Orange circles indicate POD increases between 0 and 5 percent, red circles had changes greater than 5 percent. Average increase in FAR was 4% 424

Fig. 24.1 The relative uncertainty in % as a function of daily rain accumulation for land (left) and ocean (right) conditions for July 2012 all over the Tropics 435

Fig. 24.2 Flow chart of the merging algorithm 436

Fig. 24.3 Map of the July–September 2012–2016 average daily precipitation from TAPEER 1.5 438

Fig. 24.4 Hydrological application of TAPEER 1.5 over the Niger River basin. The left figure shows the total rainfall accumulated over the Niger river basin in 2016 (1 January–31 December), the right plot illustrates the simulation of the discharge in Niamey based on the hydrological model MGB (Fleischmann et al. 2018) with TAPEER rainfall as forcing 439

Fig. 24.5 Map of the monthly precipitation accumulation in mm for August 2016 from the full run of GIRAFE 442

Fig. 24.6 Map of the monthly mean difference between the two runs of GIRAFE with or without the sounders in the constellation (mm day<sup>-1</sup>) 443

Fig. 24.7 GPM imagers and sounders (in blue) and GPM imagers only (in red) precipitation volume distributions over all the region (top), over land (middle) and ocean (bottom) 444

Fig. 24.8 Zonal mean number of overpass of the full-blown microwave constellation including imagers, sounders and SAPHIR. Computations realized using the IXION package. (Capderou 2014) 446

---

# List of Tables

Table 1.1 Satellites and sensors contributing to the GPM constellation 6
Table 3.1 MADRAS channel frequency and noise levels 49
Table 3.2 Noise and difference with simulations in K for each SAPHIR channels 50
Table 3.3 List of weather prediction agencies which are assimilating SAPHIR observations within an operational framework 57
Table 4.1 Typical MWI channels used for the retrieval of the physical variables ⊚ and ◯ denotes necessary and important channels, respectively. S and L denotes over-sea and over-land retrievals, respectively 65
Table 4.2 Major satellite MWIs from the 1970s to the present 66
Table 4.3 Radiometric performance characteristics of ESMR on NIMBUS-5 67
Table 4.4 Radiometric performance characteristics of ESMR on NIMBUS-6 67
Table 4.5 Radiometric performance characteristics of SMMR on NIMBUS-7, SEASAT 67
Table 4.6 Radiometric performance characteristics of SSM/I on DMSP 5D satellites 68
Table 4.7 Radiometric performance characteristics of TMI on TRMM 69
Table 4.8 Radiometric performance characteristics of WindSat on Coriolis 70
Table 4.9 Radiometric performance characteristics of AMSR-E on Aqua 71
Table 4.10 Radiometric performance characteristics of AMSR2 on GCOMW1 71
Table 4.11 Radiometric performance characteristics of GMI on GPM 71
Table 4.12 Major MWS satellite and instruments from the 1970's to present 72
Table 4.13 Radiometric performance of the MSU sensor on NOAA satellites 73

xxxvii


---



xxxviii

List of Tables

Table 4.14 Radiometric performance of the SSM/T sensor on DMSP satellites ................................................. ............. 74
Table 4.15 Radiometric performance of the SSMT/2 sensor on DMSP satellites ................................................. ............. 74
Table 4.16 Radiometric performance of the SSMIS sensor on the DMSP satellites ................................................. ............. 75
Table 4.17 Radiometric performance of the SAPHIR sensor on the M-T Satellite ................................................. .............. 77
Table 4.18 Radiometric performance of the AMSU-A sensor on NOAA and MetOp satellites ................................................. ..... 77
Table 4.19 Radiometric performance of the AMSU-B sensor on NOAA satellites ................................................. ............. 77
Table 4.20 Radiometric performance of the MHS sensor on NOAA satellites ................................................. ............. 78
Table 4.21 Radiometric performance of the ATMS sensor on the S-NPP and NOAA-20 satellites ............................................. 79
Table 5.1 Payload complement of EPS and EPS-SG satellites .............. 85
Table 5.2 Required MWI performance ........................................ 86
Table 5.3 Required ICI performance .......................................... 88
Table 5.4 CIMR channels complement and required performance according to current requirements (2018) ......................... 94
Table 7.1 Channel combinations and correlations against radar reflectivity (dBZ) (Alishouse et al. 1990) ...................................... 129
Table 9.1 Summary of MiRS precipitation rate performance relative to Stage IV measurements over the CONUS for the period 1–30 March 2016 ................................................. ......... 163
Table 9.2 Summary of MiRS precipitation rate performance relative to Stage IV measurements over the CONUS for the period 1–31 July 2016 ................................................. ............ 163
Table 9.3 Categorical scores (Probability of Detection (%), Probability of False Detection (%), and Heidke Skill Score) of MiRS ATMS (Oper: operational version; Test: experimental test version) rain rates relative to Stage IV for a rain rate threshold of 0.5 mm h<sup>−1</sup> ................................................... ........ 165
Table 9.4 Categorical scores (Probability of Detection (%), Probability of False Detection (%), and Heidke Skill Score) of MiRS ATMS (Oper: operational version; Test: experimental test version) rain rates relative to Stage IV for a rain rate threshold of 3.0 mm h<sup>−1</sup> ................................................... .... 166
Table 12.1 Comparisons of melting layer boundaries between different criteria for NAMMA, GRIP and Wakasa Bay data ............... 198

---



List of Tables

xxxix

Table 12.2 Comparison of stratiform, convective and other rain types between dual-frequency classification method and Ku only method 199
Table 12.3 Count of melting layer top match between dual-frequency method of DPR and Ku only method using GPM DPR data from tropical storms including cyclones, typhoons and hurricanes 200
Table 12.4 Count of melting layer bottom match between dual-frequency method and Ku only method using GPM DPR data from tropical storms including cyclones, typhoons and hurricanes 201
Table 12.5 Information on snow validation cases 207
Table 12.6 Meaning of abbreviation used for ground radar hydrometeor identification 207
Table 12.7 Average match ratio for validation cases under different surface types 208
Table 15.1 Databases of scattering properties for snow particles at microwave frequencies 258
Table 17.1 S-NPP SFR metrics before and after calibration 307
Table 17.2 S-NPP SD Metrics from satellite-only and hybrid algorithms 309
Table 17.3 S-NPP SFR validation metrics 310
Table 17.4 Metrics of S-NPP SFR 3-month (Jan–Mar 2017) average 311
Table 19.1 Lists of data field variable names and definitions to be included in each of the output datasets. Primary fields for users are in *italics* 348
Table 20.1 GSMaP product list in the GPM era 357
Table 20.2 Brief summary of evolutions in the algorithms from V6 to V7 363
Table 20.3 Values of the CC and RMSE averaged during 21 months: April 2017 to December 2018 366
Table 21.1 Statistical parameters used for global validation calculated for 8 zones (December, January, and February 2012). Statistics is provided based on the concurrent samples of test data over the 3-month period. Bias & corr (no unit); RMSE (mm/3-month) 383
Table 21.2 Statistical parameters used for global validation calculated for 8 zones (June, July, and August 2012). Statistics is provided based on the concurrent samples of test data over the 3-month period. Bias & corr (no unit); RMSE (mm/3-month) 383
Table 21.3 Comparison between PERSIANN-CCS and MA-PERSIANN-CCS with PMW satellite data over CONUS during winter and summer 2012. Statistics is provided based on the concurrent samples of test data over the 3-month period. Bias & corr (no unit); RMSE (mm/3-month) 384



---



xl

List of Tables

Table 21.4 Comparison between PERSIANN-CCS, MA-PERSIANN-CCS, and PMW with Q2 ground based radar over CONUS during winter and summer 2012. Statistics is provided based on the concurrent samples of test data over the 3-month period. Bias & corr (no unit); RMSE (mm/3-month) 384

Table 22.1 Summary of widely used satellite rainfall datasets providing coverage for Africa 396

Table 22.2 Contingency table for determining T<sub>t</sub>. The occurrence threshold is set at zero for both rainfall (mm) and CCD (hours). All gauge-CCD pairs are split into one of four possible groups (n<sub>11</sub>:n<sub>22</sub>) with the counts for each group recorded 400

Table 23.1 Counts of CHC station climate normals added to the GPCC and FAO archive 413

Table 23.2 Mean Bias Error (MBE) and Mean Absolute Error (MAE) by precipitation stratification. All statistics in mm per pentad 420

Table 23.3 Pentad validation statistics for events when stations observed at least 1 mm of rainfall 422

Table 24.1 The configuration of the geostationary infrared fleet for August 2016 used in the precipitation products 437

Table 24.2 The configuration of the passive microwave constellation (imagers and sounders) used for the various TAPEER and GIRAFE products 438

---

# Contributors

**Christophe Accadia** European Organization for the Exploitation of Meteorological Satellites (EUMETSAT), Darmstadt, Germany

**Robert F. Adler** Earth System Science Interdisciplinary Center (ESSIC), University of Maryland, College Park, MD, USA

**Kazumasa Aonashi** Meteorological Research Institute (MRI), Japan Meteorological Agency (JMA), Tsukuba, Japan

**Yoriko Arai** Remote Sensing Technology Center of Japan (RESTEC), Tokyo, Japan

**Moshe Armon** The Fredy & Nadine Herrmann Institute of Earth Sciences, Hebrew University of Jerusalem, Jerusalem, Israel

**Kristi Arsenault** SAIC, Inc., McLean, VA, and National Aeronautics and Space Administration (NASA), Goddard Space Flight Center (GSFC), Greenbelt, MD, USA

**Malarvizhi Arulraj** Pratt School of Engineering, Civil & Environmental Engineering, Duke University, Durham, NC, USA

**Hamed Ashouri** Department of Civil and Environmental Engineering, Center for Hydrometeorology and Remote Sensing (CHRS), University of California, Irvine, CA, USA

**Luca Baldini** Institute of Atmospheric Sciences and Climate (ISAC), National Research Council (CNR), Roma, Italy

**Ana P. Barros** Pratt School of Engineering, Civil & Environmental Engineering, Duke University, Durham, NC, USA

**Alessandro Battaglia** Department of Physics and Astronomy, University of Leicester, Leicester, UK

xli


---



xlii Contributors

**Hylke E. Beck** Department of Civil and Environmental Engineering, Princeton University, Princeton, NJ, USA

**Andreas Becker** Global Precipitation Climatology Center (GPCC), Deutscher Wetterdienst (DWD), Offenbach, Germany

**Ali Behrangi** Department of Hydrology and Atmospheric Sciences, University of Arizona, Tucson, AZ, USA

**Hugo Bellenger** Laboratoire de Météorologie Dynamique/IPSL, CNRS, Sorbonne Université, École Normale Supérieure, École Polytechnique, Paris, France
Japan Agency for Marine-Earth Science and Technology (JAMSTEC), Yokosuka, Japan

**Emily Berndt** NASA, Marshall Space Flight Center (MSFC), Huntsville, AL, USA

**Emily Black** Department of Meteorology, University of Reading, Reading, UK

**David T. Bolvin** Science Systems and Applications, Inc., Lanham, MD, and NASA/GSFC, Greenbelt, MD, USA

**Rogerio Bonifacio** World Food Programme, Vulnerability Assessment and Mapping Unit, Roma, Italy

**Sid-Ahmed Boukabara** NOAA/NESDIS/STAR, College Park, MD, USA

**Dominique Bouniol** Météo France, Centre National de Recherches Météorologiques (CNRM), Groupe de Modélisation et d’Assimilation pour la Prévision (GMAP), OBS, Toulouse, France

**Jacqueline Boutin** Sorbonne Université, CNRS, Institut de Recherche pour le Développement (IRD), Muséum National d’Histoire Naturelle (MNHN), Laboratoire d'Océanographie et du Climat, Expérimentations et Approches Numériques (LOCEAN), Paris, France

**Dan Braithwaite** Department of Civil and Environmental Engineering/CHRS, University of California, Irvine, CA, USA

**Scott A. Braun** NASA/GSFC, Greenbelt, MD, USA

**Luca Brocca** Research Institute for Geo-Hydrological Protection (IRPI), National Research Council (CNR), Perugia, Italy

**Jörg Burdanowitz** Institute for Meteorology, University of Hamburg, Hamburg, Germany

**Steven J. Burian** Department of Civil and Environmental Engineering, University of Utah, Salt Lake City, UT, USA

**Stefania Camici** CNR/IRPI, Perugia, Italy

**Michel Capderou** CNRS/LMD, Palaiseau, France

**Daniele Casella** CNR/ISAC, Roma, Italy

---



Contributors xliii

**Elsa Cattani** CNR/ISAC, Bologna, Italy

**Daniel Cecil** NASA/MSFC, Huntsville, AL, USA

**Philippe Chambon** Météo France, CNRM/GMAP/OBS, Toulouse, France

**Venkatachalam Chandrasekar** Department of Electrical and Computer Engineering, Colorado State University, Ft. Collins, CO, USA

**Luca Ciabatta** CNR/IRPI, Perugia, Italy

**Sophie Cloché** CNRS/IPSL, Palaiseau, France

**Paolo Colucci** EUMETSAT, Darmstadt, Germany

**Salvatore D’Addio** European Space Agency (ESA), European Space Research and Technology Centre (ESTEC), Noordwijk, The Netherlands

**Frank Davenport** Climate Hazards Group (CHG), University of California, Santa Barbara, CA, USA

**Michel Dejus** Centre National d'Études Spatiales (CNES), Toulouse, France

**Tufa Dinku** International Research Institute for Climate and Society (IRI), The Earth Institute at Columbia University, Palisades, NY, USA

**Craig Donlon** ESA/ESTEC, Noordwijk, The Netherlands

**Mohamed El Saadani** Department of Civil Engineering, University of Louisiana Lafayette, Lafayette, LA, USA

**Ralph R. Ferraro** NOAA/NESDIS/STAR, College Park, MD, USA

**Robert D. Field** Department of Applied Physics and Applied Mathematics, Columbia University, and NASA Goddard Institute for Space Studies, New York, NY, USA

**Paolo Filippucci** CNR/IRPI, Perugia, Italy

**Thomas Fiolleau** CNRS, Laboratoire d’Études en Géophysique et Océanographie Spatiales (LEGOS), Toulouse, France

**Efi Foufoula-Georgiu** Department of Civil and Environmental Engineering and Department of Earth Science, University of California, Irvine, CA, USA

**Kevin Fuell** Earth System Science Center (ESSC), University of Alabama in Huntsville, Huntsville, AL, USA

**Chris Funk** United States Geological Survey (USGS), Earth Resources Observation and Science (EROS) Center, Sioux Falls, SD, and CHG, University of California, Santa Barbara, CA, USA

**Kinji Furukawa** Japan Aerospace Exploration Agency (JAXA), Tokyo, Japan

**Kevin Garrett** NOAA/NESDIS/STAR, College Park, MD, USA

---



xliv Contributors

**Alan Geer** European Centre for Medium-range Weather Forecasts (ECMWF), Reading, UK

**Radoslaw Goska** Iowa Institute of Hydraulic Research (IIHR) – Hydroscience & Engineering, University of Iowa, Iowa City, IA, USA

**Marielle Gosset** Geoscience Environnement, Toulouse, France

**Christopher Grassotti** Cooperative Institute for Satellite Earth System Studies (CISESS), ESSIC, University of Maryland, College Park, MD, USA

**Helen Greatrex** Department of Meteorology, University of Reading, Reading, UK

**Mircea Grecu** Morgan State University, Baltimore, MD, and NASA/GSFC, Greenbelt, MD, USA

**Guojun Gu** ESSIC, University of Maryland, College Park, MD, USA

**Adrien Guérou** CNRS/LEGOS, Toulouse, France

**Clément Guilloteau** Department of Civil and Environmental Engineering, University of California, Irvine, CA, USA

**Ziad S. Haddad** Jet Propulsion Laboratory (JPL), California Institute of Technology (Caltech), Pasadena, CA, USA

**Sebastian Hahn** Department of Geodesy and Geoinformation, Research Group Remote Sensing, TU Wien, Vienna, Austria

**Atsushi Hamada** Faculty of Sustainable Design, University of Toyama, Toyama, Japan

**Laura Harrison** CHG, University of California, Santa Barbara, CA, USA

**Negin Hayatbini** Department of Civil and Environmental Engineering/CHRS, University of California, Irvine, CA, USA

**John M. Haynes** Cooperative Institute for Research in the Atmosphere (CIRA), Colorado State University, Ft. Collins, CO, USA

**Ryan Honeyager** UCAR, College Park, MD, USA

**Kuo-Lin Hsu** Department of Civil and Environmental Engineering/CHRS, University of California, Irvine, CA, USA

**George J. Huffman** NASA/GSFC, Greenbelt, MD, USA

**Toshio Iguchi** National Institute of Information and Communications Technology (NICT), Koganei, Japan

**Flavio Iturbide-Sanchez** NOAA/NESDIS/STAR, College Park, MD, USA



---



Contributors xlv

**Menglin Jin** Department of Atmospheric and Oceanic Science, University of Maryland, College Park, MD, USA

**Bradford Johnson** Department of Geography, University of Georgia, Athens, GA, USA

**Erin Jones** NOAA/NESDIS/STAR, College Park, MD, USA

**Robert J. Joyce** Innovim, Greenbelt, MD, and NOAA, National Weather Service (NWS), Climate Prediction Center (CPC), College Park, MD, USA

**Rômulo A. Jucá Oliveira** Geoscience Environnement, Toulouse, France

**Misako Kachi** Earth Observation Research Center (EORC), JAXA, Ibaraki, Japan

**Eugenia Kalnay** Department of Atmospheric and Oceanic Science, University of Maryland, College Park, MD, USA

**Sarah Kapnick** NOAA, Geophysical Fluid Dynamics Laboratory (GFDL), Princeton, NJ, USA

**Negar Karbalee** Department of Civil and Environmental Engineering/CHRS, University of California, Irvine, CA, USA

**Nozomi Kawamoto** RESTEC, Tokyo, Japan

**Masahiro Kazumori** JMA, Tokyo, Japan

**Christopher Kidd** ESSIC, University of Maryland, College Park, MD, and NASA/GSFC, Greenbelt, MD, USA

**Dalia B. Kirschbaum** NASA/GSFC, Greenbelt, MD, USA

**Pierre-Emmanuel Kirstetter** School of Meteorology and School of Civil Engineering and Environmental Sciences and Advanced Radar Research Center, University of Oklahoma and NOAA/National Severe Storms Laboratory, Norman, OK, USA

**Marian Klein** Boulder Environmental Sciences and Technology, Boulder, CO, USA

**Ulf Klein** ESA/ESTEC, Noordwijk, The Netherlands

**Christian Klepp** Max Planck Institute for Meteorology, Hamburg, Germany

**Stefan Kneifel** Institute for Geophysics and Meteorology, University of Cologne, Cologne, Germany

**Pavlos Kollias** School of Marine and Atmospheric Sciences, Stony Brook University, Stony Brook, NY, USA

**Cezar Kongoli** University of Maryland, College Park, MD, USA

**Shunji Kotsuki** RIKEN Center for Computational Science, Kobe, Japan
Center for Environmental Remote Sensing, Chiba University, Chiba, Japan

---



xlvi Contributors

**Witold F. Krajewski** IIHR-Hydroscience & Engineering, University of Iowa, Iowa City, IA, USA

**Takuji Kubota** EORC/JAXA, Ibaraki, Japan

**Paul A. Kucera** University Corporation for Atmospheric Research (UCAR), Boulder, CO, USA

**Mark S. Kulie** NOAA/NESDIS/STAR, Advanced Satellite Products Branch, Madison, WI, USA

**Christian D. Kummerow** Department of Atmospheric Science, Colorado State University, Ft. Collins, CO, USA

**Frank Lafontaine** Jacobs, Engineering Services and Science Capability Augmentation (ESSCA), NASA/MSFC, Huntsville, AL, USA

**Martin Landsfeld** CHG, University of California, Santa Barbara, CA, USA

**Sante Laviola** CNR/ISAC, Bologna, Italy

**Minda Le** Department of Electrical and Computer Engineering, Colorado State University, Ft. Collins, CO, USA

**Matthew D. Lebsock** JPL/Caltech, Pasadena, CA, USA

**Tristan S. L’Ecuyer** Department of Atmospheric and Oceanic Sciences, University of Wisconsin-Madison, Madison, WI, USA

**Jussi Leinonen** JPL/Caltech, Pasadena, CA, USA

**Anita LeRoy** ESSC, University of Alabama in Huntsville, Huntsville, AL, USA

**Vincenzo Levizzani** CNR/ISAC, Bologna, Italy

**Guo-Yuan Lien** Research and Development Center, Central Weather Bureau, Taipei, Taiwan

**Chuntao Liu** Texas A&M University, Department of Physical and Environmental Sciences, Corpus Christi, TX, USA

**Guosheng Liu** Department of Earth, Ocean and Atmospheric Science, Florida State University, Tallahassee, FL, USA

**Quanhua Liu** NOAA/NESDIS/STAR, College Park, MD, USA

**Shuyan Liu** CIRA, Colorado State University, Ft. Collins, CO, USA

**Eric Maddy** NOAA/NESDIS/STAR, College Park, MD, USA

**Viviana Maggioni** Sid and Reva Dewberry Department of Civil, Environmental, and Infrastructure Engineering, George Mason University, Fairfax, VA, USA

**Ross Maidment** Department of Meteorology, University of Reading, Reading, UK

---



Contributors xlvii

**Anna Cinzia Marra** CNR/ISAC, Roma, Italy

**Francesco Marra** The Fredy & Nadine Herrmann Institute of Earth Sciences, Hebrew University of Jerusalem, Jerusalem, Israel, and CNR/ISAC, Bologna, Italy

**Frank S. Marzano** Department of Information Engineering, Electronics and Telecommunications (DIET), Sapienza University of Roma, Roma, Italy

**Takeshi Masaki** RESTEC, Tokyo, Japan

**Bathobile Maseko** South African Weather Service, Pretoria, South Africa

**Christian Massari** CNR/IRPI, Perugia, Italy

**Vinia Mattioli** EUMETSAT, Darmstadt, Germany

**Kevin McGrath** Jacobs/ESSCA, NASA/MSFC, Huntsville, AL, USA

**Amy McNally** ESSIC, University of Maryland, College Park, MD, and NASA/GSFC, Greenbelt, MD, USA

**Tomoaki Mega** Tokyo Metropolitan University, Tokyo, Japan

**Huan Meng** NOAA/NESDIS/STAR, College Park, MD, USA

**Andrés Merino** Department of Chemistry and Applied Physics, University of León, León, Spain

**Lisa Milani** University of Maryland, College Park, MD, and NASA/GSFC, Greenbelt, MD, USA

**Takemasa Miyoshi** RIKEN Center for Computational Science, Kobe, Japan

**Andrew Molthan** NASA/MSFC, Huntsville, AL, USA

**Saverio Mori** DIET, Sapienza University of Roma, Roma, Italy

**Efrat Morin** The Fredy & Nadine Herrmann Institute of Earth Sciences, Hebrew University of Jerusalem, Jerusalem, Israel

**Kenji Nakamura** Dokkyo University, Saitama, Japan

**Eric J. Nelkin** Science Systems and Applications, Inc., Lanham, MD, and NASA/GSFC, Greenbelt, MD, USA

**Brian R. Nelson** NOAA/NESDIS, National Centers for Environmental Information (NCEI), Asheville, NC, USA

**Phu Nguyen** Department of Civil and Environmental Engineering/CHRS, University of California, Irvine, CA, USA

**Riko Oki** Earth Observation Research Center (EORC)/Japan Aerospace Exploration Agency (JAXA), Ibaraki, Japan

**William S. Olson** University of Maryland Baltimore County, Baltimore, MD, and NASA/GSFC, Greenbelt, MD, USA

---



xlviii Contributors

**Mohammed Ombadi** Department of Civil and Environmental Engineering/CHRS, University of California, Irvine, CA, USA

**Davide Ori** Institute for Geophysics and Meteorology, University of Cologne, Cologne, Germany

**Shigenori Otsuka** RIKEN Center for Computational Science, Kobe, Japan

**Ming Pan** Department of Civil and Environmental Engineering, Princeton University, Princeton, NJ, USA

**Giulia Panegrossi** CNR/ISAC, Roma, Italy

**Florian Pappenberger** ECMWF, Shinfield Park, Reading, UK

**Salvatore Pascale** Department of Earth System Science, Stanford University, Stanford, CA, USA

**Diego Pedreros** USGS/EROS, Sioux Falls, SD, USA

**Walter A. Petersen** NASA/MSFC, Huntsville, AL, USA

**Pete Peterson** CHG, University of California, Santa Barbara, CA, USA

**Nazzareno Pierdicca** DIET, Sapienza University of Roma, Roma, Italy

**Federico Porcù** Department of Physics and Astronomy, University of Bologna, Bologna, Italy

**Olivier P. Prat** Cooperative Institute for Satellite Earth System Studies (CISESS), North Carolina State University, Asheville, NC, USA

**Alain Protat** Bureau of Meteorology (BoM), Melbourne, VIC, Australia

**Felipe Quintero** IIHR-Hydroscience & Engineering, University of Iowa, Iowa City, IA, USA

**David L. Randel** Department of Atmospheric Science, Colorado State University, Ft. Collins, CO, USA

**Gilles Reverdin** Sorbonne Université, CNRS/IRD/MNHN/LOCEAN, Paris, France

**Sarah Ringerud** ESSIC, University of Maryland, College Park, MD, and NASA/GSFC, Greenbelt, MD, USA

**Rémy Roca** CNRS/LEGOS, Toulouse, France

**Geun-Hyeok Ryu** National Meteorological Satellite Center, Korea Meteorological Administration, Seoul, South Korea

**Paolo Sanò** CNR/ISAC, Roma, Italy

**Mathew R. P. Sapiano** Sapiano Statistical Services, Atlanta, GA, USA

---



Contributors xlix

**Masaki Satoh** Atmosphere and Ocean Research Institute (AORI), The University of Tokyo, Chiba, Japan

**Peter Schlüssel** EUMETSAT, Darmstadt, Germany

**Udo Schneider** GPCC/DWD, Offenbach, Germany

**Marc Schröder** DWD, Offenbach, Germany

**J. Marshall Shepherd** Department of Geography, University of Georgia, Athens, GA, USA

**Shoichi Shige** Division of Earth and Planetary Sciences, Graduate School of Science, Kyoto University, Kyoto, Japan

**Shraddhanand Shukla** CHG, University of California, Santa Barbara, CA, USA

**Gail M. Skofronick-Jackson** NASA, Headquarters, Science Mission Directorate, Washington, DC, USA

**Mark A. Smalley** JPL/Caltech, Pasadena, CA, USA

**Matthew Smith** Information Technology and Systems Center, University of Alabama in Huntsville, Huntsville, AL, USA

**Byung-Ju Sohn** School of Earth and Environmental Sciences, Seoul National University, Seoul, South Korea

**Hwan-Jin Song** National Institute of Meteorological Sciences, Korea Meteorological Administration, Seoul, South Korea

**Soroosh Sorooshian** Department of Civil and Environmental Engineering/CHRS, University of California, Irvine, CA, USA

**Thomas Stanley** Universities Space Research Association (USRA), Columbia, MD, and NASA/GSFC, Greenbelt, MD, USA

**Erich F. Stocker** NASA/GSFC, Greenbelt, MD, USA

**Alexandre Supply** Sorbonne Université, CNRS/IRD/MNHN/LOCEAN, Paris, France

**Nobuhiro Takahashi** Institute for Space-Earth Environmental Research, Nagoya University, Nagoya, Japan

**Yukari N. Takayabu** Atmosphere and Ocean Research Institute, The University of Tokyo, Tokyo, Japan

**Jackson Tan** USRA, Columbia, MD, and NASA/GSFC, Greenbelt, MD, USA

**Simone Tanelli** JPL/Caltech, Pasadena, CA, USA

**Wei-Kuo Tao** NASA/GSFC, Greenbelt, MD, USA

---



l Contributors

1

**Francisco J. Tapiador** University of Castilla-La Mancha, Toledo, Spain

**Elena Tarnavsky** Department of Meteorology, University of Reading, Reading, UK

**Tomoko Tashima** EORC/JAXA, Ibaraki, Japan

**Koji Terasaki** RIKEN Center for Computational Science, Kobe, Japan

**Ali Tokay** University of Maryland Baltimore County, Baltimore, MD, and NASA/GSFC, Greenbelt, MD, USA

**Hirofumi Tomita** RIKEN Center for Computational Science, Kobe, Japan

**Frederic Tridon** Earth Observation Science, Department of Physics and Astronomy, University of Leicester, Leicester, UK

**F. Joseph Turk** JPL/Caltech, Pasadena, CA, USA

**Jani Tyynelä** Finnish Meteorological Institute (FMI), Helsinki, Finland

**Tomoo Ushio** Tokyo Metropolitan University, Tokyo, Japan

**Albert I. J. M. van Dijk** Fenner School of Environment & Society, The Australian National University, Canberra, Australia

**Jean-Luc Vergely** ACRI-st, Guyancourt, France

**Noemi Vergopolan** Department of Civil and Environmental Engineering, Princeton University, Princeton, NJ, USA

**Daniel Vila** Instituto Nacional de Pesquisas Espaciais (IPE), Centro de Previsão de Tempo e Estudos Climaticos (CPTEC), Cachoeira Paulista, Brazil

**Wolfgang Wagner** Department of Geodesy and Geoinformation, Research Group Remote Sensing, TU Wien, Vienna, Austria

**Jian-Jian Wang** ESSIC, University of Maryland, College Park, MD, USA

**Jianxin Wang** Science Systems Applications International and NASA/GSFC, Greenbelt, MD, USA

**Graham P. Weedon** Joint Centre for Hydro-Meteorological Research, Met Office, Wallingford, UK

**Tobias Wehr** ESA/ESTEC, Noordwijk, The Netherlands

**David B. Wolff** NASA/GSFC, Wallops Flight Facility, Wallops Island, VA, USA

**Eric F. Wood** Department of Civil and Environmental Engineering, Princeton University, Princeton, NJ, USA

---



Contributors li

**Norman B. Wood** Space Science and Engineering Center (SSEC), University of Wisconsin-Madison, Madison, WI, USA

**Pingping Xie** NOAA/NWS/CPC, College Park, MD, USA

**Moeka Yamaji** EORC/JAXA, Ibaraki, Japan

**Munehisa K. Yamamoto** Division of Earth and Planetary Sciences, Graduate School of Science, Kyoto University, Kyoto, Japan

**Hisashi Yashiro** Satellite Observation Center, National Institute for Environmental Studies, Tsukuba, Japan

**Matthew Young** Department of Meteorology, University of Reading, Reading, UK

**Bradley Zavodsky** NASA/MSFC, Huntsville, AL, USA

---

# Acronyms

<table>
  <tbody>
    <tr>
        <td>ABI</td>
<td>Advanced Baseline Imager (GOES)</td>
    </tr>
<tr>
        <td>ACE</td>
<td>Aerosol-Clouds-Ecosystem Mission (NASA)</td>
    </tr>
<tr>
        <td>AD</td>
<td>Analog-to-Digital converter</td>
    </tr>
<tr>
        <td>ADDA</td>
<td>Amsterdam DDA</td>
    </tr>
<tr>
        <td>AET</td>
<td>Actual Evapotranspiration</td>
    </tr>
<tr>
        <td>AGL</td>
<td>Above Ground Level</td>
    </tr>
<tr>
        <td>AHPS</td>
<td>Advanced Hydrologic Prediction Service (NWS)</td>
    </tr>
<tr>
        <td>AI</td>
<td>Aridity Index</td>
    </tr>
<tr>
        <td>AIP</td>
<td>Algorithm Intercomparison Programme</td>
    </tr>
<tr>
        <td>Air-MSPI</td>
<td>Airborne Multi-angle SpectroPolarimetric Imager (NASA)</td>
    </tr>
<tr>
        <td>AIRS</td>
<td>Atmospheric Infrared Sounder (NASA)</td>
    </tr>
<tr>
        <td>AKDT</td>
<td>Alaska Daylight Time</td>
    </tr>
<tr>
        <td>ALEXI</td>
<td>Atmosphere-Land Exchange Inverse</td>
    </tr>
<tr>
        <td>AMeDAS</td>
<td>Automated Meteorological Data Acquisition System (JMA)</td>
    </tr>
<tr>
        <td>AMIE/DYNAMO</td>
<td>ARM Madden-Julian Oscillation Investigation Experiment/<br/>Dynamics of the Madden-Julian Oscillation</td>
    </tr>
<tr>
        <td>AMIP</td>
<td>Atmospheric Model Intercomparison Project (WCRP)</td>
    </tr>
<tr>
        <td>AMMA</td>
<td>African Monsoon Multidisciplinary Analysis experiment</td>
    </tr>
<tr>
        <td>AMO</td>
<td>Atlantic Meridional Oscillation</td>
    </tr>
<tr>
        <td>AMPR</td>
<td>Advanced Microwave Precipitation Radiometer (NASA)</td>
    </tr>
<tr>
        <td>AMS</td>
<td>Annual Maximum Series (of rainfall)</td>
    </tr>
<tr>
        <td>AMSL</td>
<td>Above Mean Sea Level</td>
    </tr>
<tr>
        <td>AMSR</td>
<td>Advanced Microwave Scanning Radiometer (JAXA)</td>
    </tr>
<tr>
        <td>AMSR-E</td>
<td>AMSR-EOS (NASA)</td>
    </tr>
<tr>
        <td>AMSU</td>
<td>Advanced Microwave Sounding Unit (NOAA and EUMETSAT)</td>
    </tr>
<tr>
        <td>AMW</td>
<td>Active Microwave</td>
    </tr>
<tr>
        <td>APHRODITE</td>
<td>Asian Precipitation—Highly Resolved Observational Data Integration Towards Evaluation of Water Resources (Japan)</td>
    </tr>
  </tbody>
</table>

liii


---



liv

Acronyms

**APR-3**: Airborne Third Generation Precipitation Radar (NASA)

**APSIM**: Agricultural Production Systems sIMulator

**AR**: Atmospheric River

**ARC (1)**: Africa Rainfall Climatology (NOAA)

**ARC (2)**: Active Radar Calibrator

**ARM**: Atmospheric Radiation Measurement (DoE)

**ARM-SGP**: ARM Southern Great Plains (DoE)

**ARMAR**: Airborne Rain-Mapping Radar (NASA and JPL)

**ASCAT**: Advanced SCATterometer (ESA)

**ASCII**: American Standard Code for Information Interchange

**ASI**: Italian Space Agency

**ASL**: Above Sea Level (a.s.l.)

**ASTRAIA**: Analyse Stereoscopique par Radar Aeroporte (CNRS)

**ATBD**: Algorithm Theoretical Basis Document

**ATMS**: Advanced Technology Microwave Sounder (NASA/NOAA)

**AWARE**: ARM West Antarctic Radiation Experiment

**AWIPS**: Advanced Weather Interactive Processing System (NWS and UNIDATA)

**BAECC**: Biogenic Aerosols-Effects on Clouds and Climate Experiment (ARM)

**BB**: Bright Band

**BC**: British Columbia

**BCS**: Bias Correction Scheme

**BMKG**: Badan Meteorologi, Klimatologi, dan Geofisika (Indonesia)

**BoM**: Bureau of Meteorology (Australia)

**BRAIN**: Bayesian Rain Algorithm Including Neural Networks (Megha-Tropiques)

**BSA**: Backscatter Alignment

**BUFR**: Binary Universal Form for the Representation of Meteorological Data

**BUI**: Buildup Index (FWI)

**CAPE**: Convective Available Potential Energy

**CAPRICORN**: Clouds, Aerosols, Precipitation, Radiation, and Atmospheric Composition over the Southern Ocean

**CARE**: Centre for Atmospheric Research Experiments (Environment Canada)

**CATDS**: Centre Aval de Traitement des Données SMOS

**CC**: Correlation Coefficient

**CCD**: Cold Cloud Duration

**CCDF**: Complementary Cumulative Distribution Function

**CCI**: Climate Change Initiative (ESA)

**CCl**: Commission for Climatology (WMO)

**CCP (1)**: Clouds, Convection, and Precipitation

**CCP (2)**: Cloud and Precipitation Process Mission

---



Acronyms

lv

**CCZ**: Continent-Climate Zone

**CDD**: Consecutive Dry Days Index (ETCCDI)

**CDF**: Cumulative Density Function

**CDR**: Climate Data Record

**CDRD**: Cloud Dynamics and Radiation Database

**CEMADEN**: Centro Nacional de Monitoramento e Alertas de Desastres Naturais (Brazil)

**CEOS**: Committee on Earth Observation Satellites

**CERES**: Clouds and the Earth’s Radiant Energy System (NASA)

**CESM**: Community Earth System Model

**CFAD**: Contoured Frequency by Altitude Diagram

**CG**: Cloud-to-Ground Lightning

**CGMS**: Coordination Group for Meteorological Satellites

**CHC**: Climate Hazards Center (University of California, Santa Barbara)
**CHIRPS**: Climate Hazards center InfraRed Precipitation with Stations

**CHPcli**: Climate Hazards Group’s Precipitation Climatology

**CIMR**: Copernicus Imaging Microwave Radiometer Mission (EU)

**CIndO**: Central Equatorial Indian Ocean index

**CIRA**: Cooperative Institute for Research in the Atmosphere (CSU)

**CLC**: Corine Land Cover

**CLIVAR**: Climate Variability and Predictability (WMO)

**CLW**: Cloud Liquid Water

**CLWC**: Cloud Liquid Water Content

**CMA**: China Meteorological Administration

**CMAP**: CPC Merged Analysis of Precipitation

**CMIP**: Coupled Model Intercomparison Project (WCRP)

**CMIP-5**: CMIP Phase 5

**CMORPH**: CPC MORPHing algorithm

**CMORPH-CRT**: CMORPH Bias Corrected

**CMORPH-KF**: CMORPH-Kalman Filter

**CM-SAF**: Climate Monitoring-SAF (EUMETSAT)

**CNES**: Centre National D’Études Spatiales (France)
**CNRM/GAME**: Centre National de Recherches Météorologiques—Groupe d’études de l’Atmosphère Météorologique (Météo France)

**CNR**: Consiglio Nazionale delle Ricerche (Italy)

**CNR-IRPI**: CNR-Istituto di Ricerca per la Protezione Idrogeologica

**CNR-ISAC**: CNR-Istituto di Scienze dell'Atmosfera e del Clima

**CNRS**: Centre National de la Recherche Scientifique (France)

**CNTL**: Control Run

**COADS**: Comprehensive Ocean Atmosphere Data Set

**ConQ**: Moisture Flux Convergence

**CONUS**: Conterminous US

**CORRA**: Combined Radar-Radiometer Product (GPM)



---



lvi

Acronyms

<table>
  <tbody>
    <tr>
        <td>CoSMIR</td>
<td>Conical Scanning Millimeter-wave Imaging Radiometer (NASA)</td>
    </tr>
<tr>
        <td>CPC</td>
<td>Climate Prediction Center (NOAA)</td>
    </tr>
<tr>
        <td>CPI</td>
<td>Convective Percent Index</td>
    </tr>
<tr>
        <td>CPL</td>
<td>Cloud Physics Lidar (NASA)</td>
    </tr>
<tr>
        <td>CPR</td>
<td>Cloud Profiling Radar (NASA)</td>
    </tr>
<tr>
        <td>CRS</td>
<td>Cloud Remote Sensing Radar (NASA)</td>
    </tr>
<tr>
        <td>CrIS</td>
<td>Cross-Track Infrared Sounder (NASA)</td>
    </tr>
<tr>
        <td>CRM</td>
<td>Cloud-Resolving Model</td>
    </tr>
<tr>
        <td>CRS</td>
<td>Cloud Radar System (NASA)</td>
    </tr>
<tr>
        <td>CRTM</td>
<td>Community Radiative Transfer Model</td>
    </tr>
<tr>
        <td>CRU</td>
<td>Climate Research Unit (Univ. of East Anglia)</td>
    </tr>
<tr>
        <td>CSA</td>
<td>Climate Service for Agriculture (Rwanda)</td>
    </tr>
<tr>
        <td>CSH</td>
<td>Convective and Stratiform Heating</td>
    </tr>
<tr>
        <td>CSI</td>
<td>Critical Success Index</td>
    </tr>
<tr>
        <td>CSK</td>
<td>COSMO-SkyMed (ASI)</td>
    </tr>
<tr>
        <td>CSP</td>
<td>Climate Services Partnership</td>
    </tr>
<tr>
        <td>CSU</td>
<td>Colorado State University</td>
    </tr>
<tr>
        <td>CSPP</td>
<td>Community Satellite Processing Package</td>
    </tr>
<tr>
        <td>CT</td>
<td>Cloud Thickness</td>
    </tr>
<tr>
        <td>CTH</td>
<td>Cloud Top Height</td>
    </tr>
<tr>
        <td>CWD</td>
<td>Consecutive Wet Days (ETCCDI)</td>
    </tr>
<tr>
        <td>CWV</td>
<td>Columnar Water Vapor</td>
    </tr>
<tr>
        <td>CYGNSS</td>
<td>Cyclone Global Navigation Satellite System (NASA)</td>
    </tr>
<tr>
        <td>DA</td>
<td>Data Assimilation</td>
    </tr>
<tr>
        <td>DAR</td>
<td>Differential Absorption Radar</td>
    </tr>
<tr>
        <td>DB</td>
<td>Dark Band</td>
    </tr>
<tr>
        <td>DBNet</td>
<td>Direct Broadcast Network</td>
    </tr>
<tr>
        <td>DC</td>
<td>Drought Code (FWI)</td>
    </tr>
<tr>
        <td>DD</td>
<td>Downward Decreasing</td>
    </tr>
<tr>
        <td>DDA</td>
<td>Discrete Dipole Approximation</td>
    </tr>
<tr>
        <td>DDSCAT</td>
<td>Discrete Dipole Scattering</td>
    </tr>
<tr>
        <td>DEM</td>
<td>Digital Elevation Model</td>
    </tr>
<tr>
        <td>DFR</td>
<td>Dual-Frequency Ratio</td>
    </tr>
<tr>
        <td>DI</td>
<td>Downward Increasing</td>
    </tr>
<tr>
        <td>DJF</td>
<td>December-January-February</td>
    </tr>
<tr>
        <td>DKRZ</td>
<td>Deutsches Klimarechenzentrum (Germany)</td>
    </tr>
<tr>
        <td>DLR</td>
<td>Deutschen Zentrums für Luft- und Raumfahrt (Germany)</td>
    </tr>
<tr>
        <td>DMC</td>
<td>Duff Moisture Code (FWI)</td>
    </tr>
<tr>
        <td>DMIP2</td>
<td>Distributed Hydrologic Model Intercomparison Project–Phase 2 (NWS)</td>
    </tr>
<tr>
        <td>DMSP</td>
<td>Defense Meteorological Satellite Program (US Navy)</td>
    </tr>
<tr>
        <td>DNN</td>
<td>Deep Neural Network</td>
    </tr>
  </tbody>
</table>



---



Acronyms

lvii

**DoE**: Department of Energy

**DO-Op**: Daylight Only Operations (CloudSat)

**DoW**: Doppler on Wheels (Center for Severe Weather Research)

**DP**: Dual Polarimetric Radar

**DPC (1)**: Data Processing Center (CloudSat)

**DPC (2)**: Department of Civil Protection of Italy

**DPCA**: Displaced Phase Center Antenna

**DPR**: Dual-frequency Precipitation Radar (GPM)

**DRC**: Democratic Republic of the Congo

**DryMOD**: Dryland hydrological MODel (University of Reading)

**DSD**: Drop Size Distribution

**DSI**: Drought Severity Index

**DSSAT**: Decision Support System for Agrotechnology Transfer

**DWR**: Dual-Wavelength Ratio

**DYNAMO**: Dynamics of the MJO experiment

**D3R**: Dual-Frequency Dual-Polarized Doppler Radar (NASA)

**EA**: East Africa

**EAF**: East Africa

**EarthCARE**: Earth Clouds, Aerosols, and Radiation Explorer (ESA-JAXA)

**EASE**: Equal-Area Scalable Earth

**EBCM**: Extended Boundary Condition Method

**EC**: European Commission

**ECCC**: Environment and Climate Change Canada

**ECDI**: Enhanced Combined Drought Index

**ECMWF**: European Centre for Medium-Range Weather Forecasts

**EDF**: Environmental Data Fusion

**EDOP**: ER-2 Doppler Radar

**EDR**: Environmental Data Record

**EEA**: Eastern East Africa

**EIA**: Earth Incident Angle

**ELDORA**: Electra Doppler Radar (NCAR)

**EM**: Electromagnetic

**EMA**: Effective Medium Approximations

**eMAs**: extended MODIS Airborne Simulator (NASA)

**EMSR**: Electronically Scanning Microwave Radiometer (NOAA)

**ENACTS**: Enhancing National Climate Services

**ENSO**: El Niño Southern Oscillation

**EOF**: Empirical Orthogonal Function

**EOS**: Earth Observing System (NASA)

**EPD2**: Extreme Precipitation Day > 2 in day<sup>-1</sup>

**EPD4**: Extreme Precipitation Day > 4 in day<sup>-1</sup>

**EPS**: EUMETSAT Polar System

**EPSAT-SG**: Estimation of Precipitation by Satellite Second Generation (CNRS-LMD)

---



lviii

Acronyms

**EPS-SG**: EPS Second Generation

**ERA**: ECMWF Reanalysis

**ESA**: European Space Agency

**ESA-CCI**: ESA Climate Change Initiative

**ESMR**: Electronically Scanned Microwave Radiometer (NOAA)

**ESPC**: Environmental Satellite Processing Center (NESDIS)

**ESSIC**: Earth System Science Interdisciplinary Center

**ET**: Evapotranspiration

**ETCCDI**: Expert Team on Climate Change Detection and Indices

**EU**: European Union

**EUMETCast**: EUMETSAT’s Multicast Distribution System

**EUMETSAT**: European Organization for the Exploitation of Meteorological Satellites

**EVI-3**: Earth Venture Instrument-3 program (NASA)

**EVT**: Extreme Value Theory

**EWFN**: Energy-Water-Food Nexus

**EWS**: Early Warning System

**EXRAD**: ER-2 X-band Radar (NASA)

**FAO**: Food and Agriculture Organization (UN)

**FAR**: False Alarm Rate

**FAS**: Foreign Agricultural Service (USDA)

**FB**: Frequency Bias

**FCDR**: Fundamental Climate Data Record

**FD**: Frost Days

**FDRS**: Fire Danger Rating Systems

**FEWS NET**: Famine Early Warning Systems Network

**FFMC**: Fine Fuel Moisture Code (FWI)

**FL**: Freezing Level

**FLDAS**: FEWS NET Land Data Assimilation System

**FLOR**: Forecast-oriented Low Ocean Resolution model (GFDL)

**FMI**: Finnish Meteorological Institute

**FNMOC**: Fleet Numerical Meteorology and Oceanography Center (US Navy)

**FoV**: Field of View

**FP**: Forward Processing (GMAO)

**FRMSE**: Fractional RMSE

**FSOI**: Forecast Sensitivity Observation Impact

**FWI**: Fire Weather Index

**GAGES**: Geospatial Attributes of Gages for Evaluating Streamflow (USGS)

**GANAL**: Global Analysis (JMA)

**GATE**: Global Atmospheric Research Program Atlantic Tropical Experiment

**GC**: Ground Clutter

---



Acronyms

lix

GCEM	Goddard Cumulus Ensemble Model (NASA)

GCM	General Circulation Model

GCOM	Global Change Observation Mission (JAXA)

GCOM-W	GCOM-Water

GCOS	Global Climate Observing System (WMO)

GCPEx	GPM Cold Season Precipitation Experiment

GDAP	GEWEX Data and Assessment Panel

GDAS/GFS	Global Data Assimilation System/Global Forecast System (NOAA)

GEC	Geocoded Ellipsoid Corrected

GEO (1)	Geostationary orbit

GEO (2)	Group on Earth Observations

GEOGLAM	GEO Global Agricultural Monitoring

GEOS	Goddard Earth Observing System (NASA)

GEOS FP	Global Earth Observing System Forward Processing

GEOSS	Group on Earth Observation System of Systems

GeoSTAR	Geostationary Synthetic Thinned Aperture Radiometer (NASA)

GES DISC	Goddard Earth Sciences Data and Information Services Center

GEV	Generalized Extreme Value Distribution

GEWEX	Global Energy and Water Exchanges (WCRP)

GFCS	Global Framework for Climate Services (WMO)

GFDL	Geophysical Fluid Dynamics Laboratory (NOAA and Princeton University)

GFS	Global Forecast System (NCEP)

GFWED	Global Fire Weather Database (NASA GISS)

GHA	Greater Horn of Africa

GHCN-D	Global Historical Climatology Network-Daily (NOAA)

GHM	Global Hydrological Model

GHRC	Global Hydrology Resource Center (NASA)

GIRAFE	Global Interpolated RAinFall Estimation

GIS	Geographic Information System

GISS	Goddard Institute for Space Studies (NASA)

GLC	Global Landslide Catalog (NASA)

GMa	Gulf of Mexico area

GMAO	Global Modeling and Assimilation Office (NASA)

GMI	GPM Microwave Imager

GMM	Generalized Multiparticle Mie-solution

GoAMAZON	Green Ocean Amazon Experiment

GOES	Geostationary Operational Environmental Satellite (NOAA)

GOSAT-3	Greenhouse Gases Observing Satellite (JAXA)

GOTM	General Ocean Turbulence Model

GPC	Global Precipitation Climatology Center (DWD)

GPCP	Global Precipitation Climatology Project (GEWEX)

---



lx

Acronyms

**GPI**: GOES Precipitation Index

**GPM**: Global Precipitation Measurement mission (NASA and JAXA)

**GPM-CO**: GPM Core Observatory

**GPP**: Gross Primary Production

**GPROF**: Goddard Profiling Algorithm (NASA)

**GPS**: Global Positioning System

**GRACE**: Gravity Recovery and Climate Experiment (NASA and DLR)

**GRACE-FO**: GRACE Follow-On

**GRDC**: Global Runoff Data Centre

**Grid-Sat**: Gridded Satellite Data (NOAA)

**GRIP**: Genesis and Rapid Intensification Processes (NASA)

**GRISO**: Rainfall Generator of Spatial Interpolation from Observation

**GS**: Grain Size

**GSFC**: Goddard Space Flight Center (NASA)

**GSI**: Gridpoint Statistical Interpolation

**GSM**: Global Spectral Model

**GSMaP**: Global Satellite Mapping of Precipitation (Japan)

**GSMaP-MVK**: GSMaP Motion Vector Kalman

**GSMaP-NRT**: GSMaP Near Real Time

**GSOD**: Global Surface Summary of the Day (NOAA)

**GT**: Gaussian Transformation

**GTC**: Geocoded Terrain Corrected

**GTS**: Global Telecommunication System

**GV**: Ground Validation

**GW**: Global Warming

**GWIS**: Global Wildfire Information System

**GWP**: Graupel Water Path

**G5NR**: GEOS-5 Nature Run (NASA)

**HADS**: Hydrometeorological Automated Data System (NWS)

**HAMSR**: High-Altitude MMIC Sounding Radiometer (JPL)

**HDF**: Hierarchical Data Format

**HEMT**: High Electron Mobility Transistor

**HEPEX**: Hydrological Ensemble Prediction Experiment

**HID**: Hydrometeor Identification algorithms

**HIRS**: High-Resolution Infrared Radiation Sounder (NOAA)

**HISA**: Hurricane Intensity and Structure Algorithm

**HIWRAP**: High-Altitude Imaging Wind and Rain Airborne Profiler (NASA)

**HLM**: Hillslope-Link Model

**HMA**: High Mountain Asia

**HOAPS**: Hamburg Ocean Atmosphere Parameters and Fluxes from Satellite Data (University of Hamburg)

**HQPrecip**: High-Quality Precipitation (GPM)

---



Acronyms

lxi

**HR**: 

 Hit Rate
**HRPP**: 

 High-Resolution Precipitation Product
**HRWS**: 

 High-Resolution Wide Swath
**H-SAF**: 

 Support to Operational Hydrology and Water Management (EUMETSAT)
**HSS**: 

 Heidke Skill Score
**HyMeX**: 

 Hydrological Cycle in Mediterranean Experiment
**IC**: 

 Intra-cloud Lightning
**ICDC**: 

 Integrated Climate Data Center (University of Hamburg)
**ICE-POP**: 

 International Collaborative Experiment for the PyeongChang Olympics and Paralympics Experiment 2018
**ICHARM**: 

 International Centre for Water Hazard and Risk Management
**ICI**: 

 Ice Cloud Imager (EUMETSAT)
**ICO-LETKF**: 

 Icosahedral LETKF
**IDF**: 

 Intensity-Duration-Frequency Curve
**IDW**: 

 Inverse Distance Weighting
**IFAS**: 

 Integrated Flood Analysis System
**IFM**: 

 Index Flood Method
**IMERG**: 

 Integrated Multi-satellitE Retrievals for GPM
**IMERG_E**: 

 IMERG Early Run (near real time with a latency of 6 h)
**IMERG_F**: 

 IMERG Final Run (gauged-adjusted with a latency of 4 months)
**IMERG_L**: 

 IMERG Late Run (reprocessed near real time with a latency of 18 h)
**IOD**: 

 Indian Ocean Dipole
**IPHEx**: 

 Integrated Precipitation and Hydrology Experiment (GPM)
**IPS**: 

 Institut Pierre Simon Laplace (CNRS)
**IPWG**: 

 International Precipitation Working Group (CGMS)
**IR**: 

 Infrared
**IRI**: 

 International Research Institute for Climate and Society (Columbia University)
**IRP**: 

 Infrared Precipitation Estimate
**ISI**: 

 Initial Spread Index (FWI)
**ISRO**: 

 Indian Space Research Organisation
**ISS**: 

 International Space Station
**ITCZ**: 

 Intertropical Convergence Zone
**IWP**: 

 Ice Water Path
**I&Q**: 

 In-Phase and Quadrature Signal
**JAXA**: 

 Japan Aerospace Exploration Agency
**JCOMM**: 

 Joint Technical Commission for Oceanography and Marine Meteorology (WMO)
**JCSDA**: 

 Joint Center for Satellite Data Assimilation (NOAA)
**JERD**: 

 JPSS NESDIS ESPC Requirements Document
**JF**: 

 January-February

---



lxii

Acronyms

**JJA**: June-July-August

**JJAS**: June-July-August-September

**JMA**: Japan Meteorological Agency

**JPL**: Jet Propulsion Laboratory

**JPSS**: Joint Polar Satellite System

**JRA55**: Japanese 55-year Reanalysis

**JRC**: Joint Research Centre (EC)

**KGE**: Kling-Gupta Efficiency

**KMA**: Korea Meteorological Administration

**KWAJEX**: Kwajalein Experiment

**LACA&D**: Latin American Climate Assessment & Dataset

**LDM**: Local Data Manager (UNIDATA)

**LDR**: Linear Depolarization Ratio

**LEGOS**: Laboratoire d'Études en Géophysique et Océanographie Spatiales

**LEO**: Low Earth Orbit

**LETKF**: Local Ensemble Transform Kalman Filter (RIKEN)

**LFM**: Local Forecast Model

**LH**: Latent Heating

**LHASA**: Landslide Hazard Assessment for Situational Awareness (NASA)

**LIA**: Local Incidence Angle

**LLCF**: Low-Level Clouds and Fog

**LL-LETKF**: Latitude-Longitude LETKF

**LMD**: Laboratoire de Météorologie Dynamique (CNRS)

**LMODEL**: Lagrangian Model (UC Irvine and University of Hull)

**LPVEx**: Light Precipitation Validation Experiment (GPM)

**LR**: Logistic Regression

**LST**: Land Surface Temperature

**LUT**: Lookup Table

**LWP**: Liquid Water Path

**LZA**: Local Zenith Angle

**L1SR**: Level 1 Science Requirements (GPM)

**MADRAS**: Microwave Analysis and Detection of Rain and Atmospheric Structures (Megha-Tropiques)

**MAE**: Mean Absolute Error

**MAFF**: Ministry of Agriculture, Forestry and Fisheries (Japan)

**MAM**: March-April-May

**MARSOP**: Monitoring Agricultural ResourceS Operational (JRC)

**MBE**: Mean Bias Error

**MCS**: Mesoscale Convective System

**MCTA**: Merged CloudSat, TRMM, and AMSR product

**MC3E**: Mid-latitude Continental Convective Clouds Experiment

**ME**: Mean Error

---



Acronyms

lxiii

**Medicane**: Mediterranean hurricane

**MERRA**: Modern-Era Retrospective analysis for Research and Applications (NASA)

**MGD**: Multilook Ground Detected

**MGDSST**: Merged Satellite and In Situ Data Global Daily SST (JMA)

**MHEMT**: Metamorphic HEMT

**MHOPrEx**: Monsoon Himalaya Orographic Precipitation Experiment

**MHS**: Microwave Humidity Sounder (EUMETSAT)

**MicroMAS-2**: Micro-sized Microwave Atmospheric Satellite-2

**MIIDAPS**: Multi-instrument Inversion and Data Assimilation Preprocessing System (NOAA)

**MIR**: Middle IR

**MIRA**: Microwave/Infrared Rainfall Algorithm

**MIRAS**: Microwave Imaging Radiometer using Aperture Synthesis

**MiRS**: Microwave Integrated Retrieval System (NOAA)

**MISDc**: Modello Idrologico Semi-Distribuito in continuo (CNR-IRPI)

**MLP**: Melting Level Precipitation

**MLS**: Microwave Limb Sounder (EOS)

**MMIC**: Millimeter-Wave Monolithic Integrated Circuits

**MODIS**: Moderate Resolution Imaging Spectroradiometer (NASA)

**MPE**: Multisensor Precipitation Estimator

**MP-M**: Max-Planck-Institut für Meteorologie (Germany)

**MRR**: Micro Rain Radar

**MREA**: Modified Regression Empirical Algorithm

**MRMS**: Multi-Radar/Multisensor Precipitation Data

**MREA**: Modified Regression Empirical Algorithm

**MRMS**: Multi-Radar Multisensor system (NOAA)

**MS**: Multiple Scattering

**MSG**: Meteosat Second Generation (EUMETSAT)

**MSG-CPP**: MSG Cloud Physical Properties (EUMETSAT)

**MSLP**: Mean Sea-Level Pressure

**MSPPS**: Microwave Surface and Precipitation Products System (NOAA)

**MSU**: Microwave Sounding Unit (NOAA)

**MSWEP**: Multisource Weighted-Ensemble Precipitation

**MTSAT**: Multifunctional Transport Satellites (JMA)

**MW**: Microwave

**MWCC**: Microwave Cloud Classification

**MWCOMB**: Combined MW Rainfall Retrieval (CPC)

**MWHS-2**: Microwave Humidity Sounder-2 (CMA)

**MWI**: Microwave Imager (EUMETSAT)

**MWR (1)**: Microwave Radiometer

**MWR (2)**: Moving Window Regression

---



lxiv

Acronyms

**MWS**: Microwave Sounder

**NAa**: North Atlantic Area

**NAMMA**: NASA African Monsoon Multidisciplinary Analyses

**NAS**: National Academies of Sciences (US)

**NASA**: National Aeronautics and Space Administration

**NCA**: North and Central America

**NCAR**: National Center for Atmospheric Research

**NCE**: National Centers for Environmental Information (NOAA)

**NCEI**: National Centers for Environmental Information

**NCEP**: National Centers for Environmental Prediction (NOAA)

**NCEP-CFSR**: Climate Forecast System Reanalysis

**NCL**: NCAR Command Language

**NDVI**: Normalized Difference Vegetation Index

**NESDIS**: National Environmental Satellite, Data, and Information Service (NOAA)

**netCDF**: Network Common Data Form

**NEWS**: NASA Energy and Water Cycle Study

**NEXRAD**: Next-Generation Weather Doppler Radar (NOAA/NWS)

**NH**: Northern Hemisphere

**NHM**: National Hydrometeorological Service

**NICAM**: Nonhydrostatic Icosahedral Atmospheric Model (RIKEN)

**NIR**: Near IR

**NM**: National Meteorology Agency

**NMAE**: Normalized Mean Absolute Error

**NMHS**: National Meteorological and Hydrological Service

**NMQ**: National Mosaic Quantitative Precipitation Estimation (NOAA/NSSL)

**NU-WRF**: NASA-Unified WRF

**NPP**: Net Primary Production

**NRCS**: Normalized Radar Cross Section

**NOAA**: National Oceanic and Atmospheric Administration

**NOP**: Numerical Ocean Prediction

**NPOL**: NASA S-Band Dual Polarimetric

**NRL**: Naval Research Laboratory (US Navy)

**NRMSE**: Normalized Root Mean Square Error

**NRT**: Near Real Time

**NSE**: Nash-Sutcliffe Efficiency

**NSMC**: National Satellite Meteorological Center (CMA)

**NSSL**: National Severe Storms Laboratory (NOAA)

**NTPa**: North Tropical Pacific Area

**NUBF**: Nonuniform Beam Filling

**NU-WRF**: NASA-Unified Weather Research and Forecasting

**NWP**: Numerical Weather Prediction

**NWS**: National Weather Service (NOAA)

---



Acronyms

lxv

**OBCT**: On-Board Calibration Target

**OCE**: Oceania

**OceanRain**: Ocean Rainfall And Ice-Phase Precipitation Measurement Network

**OE**: Optimal Estimation

**OI**: Optimal Interpolation

**OLYMPEX**: Olympic Mountains Experiment

**OM**: Observatoire Midi-Pyrénées

**OND**: October-November-December

**OSCAR**: Observing Systems Capability Analysis and Review (WMO)

**OSPO**: Office of Satellite and Product Operations (NOAA)

**OSSE**: Observing Systems Simulation Experiment

**OZA**: Observation Zenith Angle

**PAW**: Percentage Available Water

**PCT**: Polarization Corrected Temperature

**PDF (1)**: Probability Density Function

**PDF (2)**: Particle Distribution Function

**PDO**: Pacific Decadal Oscillation

**PDSI**: Palmer Drought Severity Index

**PERHPP**: Program for the Evaluation of High-Resolution Precipitation Products

**PERSIANN**: Precipitation Estimation from Remotely Sensed Information using Artificial Neural Networks (UC Irvine)

**PERSIANN-CCS**: PERSIANN-Cloud Classification System

**PERSIANN-CDR**: PERSIANN-Climate Data Records

**PERSIANN-MSA**: PERSIANN-Multispectral Analysis

**PF**: Precipitation Feature

**PHEMT**: Pseudomorphic HEMT

**PHIVOLCS**: Philippine Institute of Volcanology and Seismology

**PIA**: Path-Integrated Attenuation

**PICSA**: Participatory Integrated Climate Services

**PIP**: Precipitation Imaging Package

**PMA**: Probability Matching Algorithm

**PMI**: Polarimetric Microwave Imager (CMA)

**PMM (1)**: Precipitation Measurement Mission (NASA)

**PMM (2)**: Probability Matching Method

**PMP**: Probable Maximum Precipitation

**PMW**: Passive Microwave

**PNPR**: Passive Microwave Neural Network Precipitation Retrieval (CNR-ISAC)

**POD**: Probability of Detection

**POES**: Polar Operational Environmental Satellites (NOAA)

**POFD**: Probability of False Detection

**PoP**: Probability of Precipitation

---



lxvi Acronyms

**POS**: Probability of Snowfall

**PPI**: Plan Position Indicator

**PPP**: Precipitation Per Person

**PPS**: Precipitation Processing System (IMERG)

**PQPE**: Probabilistic Quantitative Precipitation Estimation

**PR**: Precipitation Radar (TRMM)

**PRCPTOT**: Total Rainfall Amount (ETCCDI)

**PRISM**: Parameter-Elevation Regressions on Independent Slopes Model (Oregon State University)

**PRPS**: Precipitation Retrieval and Profiling Scheme

**PSD**: Particle Size Distribution

**PSS**: Practical Salinity Scale

**PTH**: Precipitation Top Height

**PUSH**: Precipitation Uncertainties for Satellite Hydrology

**PV**: Physical Validation (GPM)

**PW**: Precipitable Water

**PWC**: Precipitable Water Content

**QA**: Quality Assurance

**QC**: Quality Control

**QCLCD**: Quality Controlled Local Climatological Data

**QI**: Quality Index

**QPE**: Quantitative Precipitation Estimation

**RADAP**: Radar Data Processor (NOAA)

**RADAR**: Radio Detection and Ranging

**RADEX**: Radar Definition Experiment (OLYMPEX)

**RCM**: Regional Climate Model

**RCS**: Radar Cross Section

**REA**: Regressive Empirical Algorithm

**REFAME**: Rain Estimation Using Forward Adjusted-Advection of Microwave Estimates (UC Irvine)

**RFC**: River Forecast Center (NWS)

**RFE**: Rainfall Estimate (FAO)

**RFI**: Radio Frequency Interference

**RGA**: Rayleigh-Gans Approximation

**RGB**: Red Green Blue

**RH**: Relative Humidity

**RHI**: Range Height Indicator

**RICO**: Rain in Cumulus over the Ocean

**RIM**: Rain Impact Model (salinity)

**RMS**: Root Mean Square

**RMSD**: RMS Deviation

**RMSE**: RMS Error

**RoF**: Rain on Fog

**RoFCC**: RoF and Cap Clouds

---



Acronyms

lxvii

**ROI**: Region of Interest

**RoLLC**: Rain on Low-Level Clouds

**ROSA**: Radio Occultation Sensor for Atmosphere

**RQI**: Radar Quality Index

**RR**: Rain Rate

**RRFA-S**: Regional Rainfall Frequency Analysis using Satellite Precipitation

**RSS**: Remote Sensing Systems Inc.

**RTH**: Rain Top Height

**RTM**: Radiative Transfer Model

**RTTOV**: Radiative Transfer for TOVS

**RV (or (R/V)**: Research Vessel

**RWH**: Rainwater Harvesting

**RW**: Rainwater Path

**R2O/O2**: Research-to-Operations/Operations-to-Research paradigm (SPoRT)

**SAa**: South Atlantic Area

**SAF**: Satellite Application Facility (EUMETSAT)

**SAM (1)**: System for Atmospheric Modeling

**SAM (2)**: Southern Appalachian Mountains

**SAPHIR**: Sondeur Atmosphérique du Proᶠⁱle d’Humidité Intertropicale par Radiométrie (Megha-Tropiques)

**SAR**: Synthetic Aperture Radar

**SARRA-H**: Systéme d’Analyse Régional des Risques Agroclimatiques-Habillé

**SBA**: Split-Based Approach

**SCA**: Scatterometer (ESA)

**SCaMPR**: Self-Calibrating Multivariate Precipitation Retrieval (NESDIS)

**ScaRaB**: Scanner for Radiation Budget (Megha-Tropiques)

**scPDSI**: Self-Calibrated PDSI

**SCS**: Single-Look Complex Slant Products

**SCSMEX**: South China Sea Monsoon Experiment

**SCSMEX/NESA**: SCSMEX Northern Enhanced Sounding Array

**SCSMEX/SESA**: SCSMEX Southern Enhanced Sounding Array

**SD (1)**: Snowfall Detection

**SD (2)**: Standard Deviation

**SDCI**: Scaled Drought Condition Index

**SDG**: Sustainable Development Goal

**SDII**: Simple Daily Intensity Index (ETCCDI)

**SEA**: Southeast and East Asia

**SEAK**: Southeast Alaska

**SEM**: Semiempirical Model

---



lxviii

Acronyms

**SEVIRI**: Spinning Enhanced Visible and Infrared Imager (EUMETSAT)

**SFI**: Seeder-Feeder Interactions

**SFR**: Snowfall Rate (NOAA)

**SH**: Southern Hemisphere

**SI**: Snow Index

**SIA**: Sea Ice Age

**SIC**: Sea Ice Concentration

**SID**: Sea Ice Drift

**SIDOC**: SAR Images Dark Object Classifier

**SIT**: Sea Ice Thickness

**SLH**: Spectral Latent Heating

**SM**: Soil Moisture

**SMA**: Soil Moisture Anomaly

**SMAP**: Soil Moisture Active Passive (NASA)

**SMMR**: Scanning Multichannel Microwave Radiometer (NOAA)

**SMOS**: Soil Moisture and Ocean Salinity (ESA)

**SM2RAIN**: Soil Moisture to Rain Algorithm (CNR-IRPI)

**S-NPP**: Suomi National Polar-Orbiting Partnership (NASA/NOAA)

**SNR**: Signal-to-Noise Ratio

**SON**: September-October-November

**SOS**: Start of Season

**SPA**: Specific Power Attenuation

**SPCZ**: South Pacific Convergence Zone

**SPEI**: Standardized Precipitation Evapotranspiration Index

**SPI**: Standardized Precipitation Index

**SPICE**: Solid Precipitation Intercomparison Experiment (WMO)

**SPoRT**: Short-term Prediction Research and Transition Center (NASA)

**SPP (1)**: Satellite Precipitation Product

**SPP (2)**: Seasonal Performance Probability

**SPS**: Special Weather Statement (NWS)

**SPURS**: Salinity Processes in the Upper Ocean Regional Study

**SR**: Success Ratio

**SRE**: Satellite-Based Rainfall Estimate

**SREM2D**: Two-Dimensional Satellite Rainfall Error Model

**SRI**: Surface Rainfall Intensity

**SRT**: Surface Reference Technique

**SSA (1)**: Space Situational Awareness

**SSA (2)**: Sub-Saharan Africa

**SSN**: Spatial Stream Network

**SSM/I**: Special Sensor Microwave/Imager (DMSP)

**SSMIS**: Special Sensor Microwave Imager Sounder (DMSP)

**SSM/T**: Special Sensor Microwave Temperature (DMSP)

**SSP**: Surface Salinity Profiler

---



Acronyms

lxix

<table>
  <tbody>
    <tr>
        <td>SSRGA</td>
<td>Self-Similar Rayleigh-Gans Approximation</td>
    </tr>
<tr>
        <td>SSS</td>
<td>Sea Surface Salinity</td>
    </tr>
<tr>
        <td>SST</td>
<td>Sea Surface Temperature</td>
    </tr>
<tr>
        <td>SSU</td>
<td>Stratospheric Sounding Unit (NOAA)</td>
    </tr>
<tr>
        <td>SSW</td>
<td>Sea Surface Wind</td>
    </tr>
<tr>
        <td>STAR</td>
<td>Center for Satellite Applications and Research (NOAA-NESDIS)</td>
    </tr>
<tr>
        <td>STDV</td>
<td>Standard Deviation</td>
    </tr>
<tr>
        <td>STH</td>
<td>Storm-Top Height</td>
    </tr>
<tr>
        <td>STIa</td>
<td>South Tropical Indian Area</td>
    </tr>
<tr>
        <td>STPa</td>
<td>South Tropical Pacific Area</td>
    </tr>
<tr>
        <td>SWA</td>
<td>South and West Asia</td>
    </tr>
<tr>
        <td>SWB</td>
<td>Soil Water Balance</td>
    </tr>
<tr>
        <td>SWE</td>
<td>Snow Water Equivalent</td>
    </tr>
<tr>
        <td>SWER</td>
<td>Snow Water Equivalent Rate</td>
    </tr>
<tr>
        <td>SYNOP</td>
<td>Surface Synoptic Observation (WMO)</td>
    </tr>
<tr>
        <td>TAMSAT</td>
<td>Tropical Applications of Meteorology Using Satellite and Ground-Based Observations</td>
    </tr>
<tr>
        <td>TAPEER</td>
<td>Tropical Amount of Precipitation with an Estimate of Errors</td>
    </tr>
<tr>
        <td>TARCAT</td>
<td>TAMSAT African Rainfall Climatology and Time Series</td>
    </tr>
<tr>
        <td>TB</td>
<td>Brightness Temperature</td>
    </tr>
<tr>
        <td>TC</td>
<td>Tropical Cyclone</td>
    </tr>
<tr>
        <td>TCA</td>
<td>Triple Collocation Analysis</td>
    </tr>
<tr>
        <td>TCC</td>
<td>TRMM Composite Climatology</td>
    </tr>
<tr>
        <td>TC4</td>
<td>Tropical Composition, Cloud and Climate Coupling Experiment</td>
    </tr>
<tr>
        <td>TDTS</td>
<td>Time-Dependent Two-Stream Method</td>
    </tr>
<tr>
        <td>TEMPEST</td>
<td>Temporal Experiment for Storms and Tropical Systems</td>
    </tr>
<tr>
        <td>TEMPEST-D</td>
<td>TEMPEST Technology Demonstration</td>
    </tr>
<tr>
        <td>TIR</td>
<td>Thermal Infrared</td>
    </tr>
<tr>
        <td>TLC</td>
<td>Tropical-Like Cyclone</td>
    </tr>
<tr>
        <td>TMD</td>
<td>Thai Meteorological Department (Thailand)</td>
    </tr>
<tr>
        <td>TMI</td>
<td>TRMM Microwave Imager</td>
    </tr>
<tr>
        <td>TMPA</td>
<td>TRMM Multisatellite Precipitation Analysis (NASA)</td>
    </tr>
<tr>
        <td>TOOCAN</td>
<td>Tracking Of Organized Convection Algorithm through a 3-D segmentatioN</td>
    </tr>
<tr>
        <td>TOGA-COARE</td>
<td>Tropical Ocean Global Atmosphere Coupled Ocean-Atmosphere Response Experiment</td>
    </tr>
<tr>
        <td>TOVS</td>
<td>TIROS Operational Vertical Sounder</td>
    </tr>
<tr>
        <td>TPW</td>
<td>Total Precipitable Water</td>
    </tr>
<tr>
        <td>TQV</td>
<td>Total Precipitable Water Vapor</td>
    </tr>
<tr>
        <td>TRMM</td>
<td>Tropical Rainfall Measuring Mission</td>
    </tr>
<tr>
        <td>TROPICS</td>
<td>Time-Resolved Observations of Precipitation structure and storm Intensity with a Constellation of Smallsats (NASA)</td>
    </tr>
  </tbody>
</table>



---



lxx

Acronyms

**TSX**: TerraSAR-X (DLR)

**TVA**: Tennessee Valley Authority

**TWP-ICE**: Tropical Warm Pool – International Cloud Experiment

**TWSA**: Terrestrial Water Storage Anomaly

**T2M**: Two-Meter Temperature

**UCA**: Urban Climate Archipelago

**UCLM**: Universidad de Castilla-La Mancha

**UH**: University of Helsinki

**UHI**: Urban Heat Island

**UMORA**: Unified Microwave Ocean Retrieval Algorithm

**UN**: United Nations

**UNEP**: United Nations Environment Programme (UN)

**UNESCO**: United Nations Educational, Scientific and Cultural Organization (UN)

**US**: United States of America

**USCRN**: US Climate Reference Network

**USDA**: US Department of Agriculture

**USDM**: US Drought Monitor

**USGS**: US Geological Survey

**UTC**: Universal Time Coordinated

**UWSI**: Urban Water Stress Index per Individual

**VAM**: Vulnerability Assessment and Mapping (WFP)

**VarBC**: Variable Bias Correction

**VI**: Vegetation Index

**VMI**: Vertical Maximum Intensity

**VN**: Validation Network (GPM)

**WATCH**: Water and Global Change (EU)

**WCOM**: Water Cycle Observation Mission (CMA)

**WCRP**: World Climate Research Programme (WMO)

**WDCC**: World Data Center for Climate (DKRZ)

**WDM6**: WRF Double-Moment 6-Class

**WEA**: Western East Africa

**WFF**: Wallops Flight Facility (NASA)

**WFO**: Weather Forecast Office (NWS)

**WFP**: World Food Programme

**WFDEI-CRU**: WATCH Forcing Data ERA Interim-CRU

**WII**: Weather Index-Based Insurance

**WMMD**: Wet Millimeter Days

**WMO**: World Meteorological Organization (UN)

**WR**: Weather Radar

**WRF**: Weather Research and Forecasting Model

**WRF-ARW**: WRF-Advanced Research WRF

**WRSI**: Water Requirements Satisfaction Index

**WS**: Wind Speed

---



Acronyms lxxi

<table>
  <tbody>
    <tr>
        <td>WSR-57</td>
<td>Weather Surveillance Radar 1957 (NWS)</td>
    </tr>
<tr>
        <td>WV</td>
<td>Water Vapor</td>
    </tr>
<tr>
        <td>XCAL</td>
<td>Intersatellite Calibration Working Group (GPM)</td>
    </tr>
<tr>
        <td>ZAR</td>
<td>Zones À Risque model</td>
    </tr>
<tr>
        <td>2DVD</td>
<td>2D Video Disdrometer</td>
    </tr>
  </tbody>
</table>

