
![](https://github.com/igemsoftware2020/IIT_Roorkee_India/blob/main/light%20blueAsset%201%404x.png)




# IIT_Roorkee_India
Machine Learning model for detecting Antibiotic Resistance genes and Django based REST API for predicting secondary structure of our novel engineered protein.

## About
Therapeutic-strategies targeting antibiotic resistance can be aimed at sensitizing pathogens to conventional antibiotics, or developing novel antimicrobials to treat infections. 
 
We have developed a machine learning approach called DARG, i.e. Detection of Antibiotic Resistant Genes, utilising support vector machines-based algorithm. The algorithm uses pan-genome information of pathogen strains along with their resistant phenotype to find genes important for conferring antibiotic resistance. The resulting list of genes consisted of previously validated target-genes and novel hits uncovered by the algorithm. For perspective experiments, these genes can be knocked out as an attempt to make bacterial strain susceptible to a particular antibiotic and validate their function.

Alternatively, we developed TailScout, a webserver for assembly and secondary-structure prediction of novel Seekercins. Seekercins are novel protein-based antimicrobials inspired from R-Type Pyocins and bacteriophages, that can target resistant pathogens. TailScout helps researchers in designing Seekercins specific for antimicrobial resistant pathogens by detecting the best combination of Pyocin and bacteriophage-tail fiber. As a final result, the software produces the sequence of engineered Seekercin that can be readily ordered as DNA products for cloning and further experiments.

### Contribution
Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are greatly appreciated.

   1. Fork the Project.
   2. Create all meaningful chnages in a new Branch. 
   3. Commit your Changes. 
   4. Push to the Branch. 
   5. Open a Pull Request.
   
### Tech Stack
#### Frontend
- React
- Bootstrap
- jQuery

#### Backend
- Django
- Django REST Framework
   
### Steps to Run Locally
1. Fork the Project.
2. Clone the Repository
3. Change the working directory to **frontend**.

```
npm run build
```
4. Move to the previous directory.
```
python -m venv env
```
```
source env/bin/activate
```
```
pip install -r requirements.txt
```
```
python manage.py makemigrations
```
```
python manage.py migrate
```
```
python manage.py runserver
```
5. Head over to localhost:8000. 

### License
Distributed under the MIT License. See ![LICENSE](https://github.com/igemsoftware2020/IIT_Roorkee_India/blob/main/LICENSE.md) for more information.



shi hai?
