# Are humans inherently good or evil?
In order to find out let's accept some absurd premises:
1. Goodness is embodied by partnering with others regardless of motivation (i.e. cooperation)
2. Evil is embodied by resisting others regardless of motivation (i.e. competition)
3. There is an even distribution of cooperative and competitive relationships in a population (i.e. if there is more cooperation than competition in the whole population then most individuals also have more cooperation than competition).
4. A person is considered "good" if they are more cooperative than competitive with others and evil otherwise.

# How can we calculate this?
Let's begin by calculating the number of competitive and cooperative relationships between a set of teams.The number of cooperative relationships in team <img src="https://latex.codecogs.com/gif.latex?i"/> with size <img src="https://latex.codecogs.com/gif.latex?n_i"/> is <img src="https://latex.codecogs.com/gif.latex?n_{i\_coop}"/> which can be calculated as the number of links in the network of team members where every member is a node connected to all other members (a perfectly dense graph).  

<p align="center">
<img src="https://latex.codecogs.com/gif.latex?n_{i\_coop}=\frac{n_i*(n_i-1)}{2}"/>



Note: this formula is a specific case (<img src="https://latex.codecogs.com/gif.latex?k=2"/>) of the general combination formula for taking <img src="https://latex.codecogs.com/gif.latex?k"/> elements out of a set of <img src="https://latex.codecogs.com/gif.latex?n"/> which is
<p align="center">
 <img src="https://latex.codecogs.com/gif.latex?\binom{n}{k}=\frac{n!}{k!*(n-k)!"/>


The total number of cooperative links is therefore:
<p align="center">
 <img src="https://latex.codecogs.com/gif.latex?n_{coop}=\sum_{i=1}^{n_{teams}}n_{i\_coop}"/>


Now to count the number of competitive relationships let's again assume both teams are fully connected graphs, meaning every team member has a competitive relationship with every member of an opposing team. Therefore the number of competitve relationships for team <img src="https://latex.codecogs.com/gif.latex?i"/> is the summation of the product of <img src="https://latex.codecogs.com/gif.latex?n_i"/> with every other team size:


<p align="center">
 <img src="https://latex.codecogs.com/gif.latex?n_{i\_comp}=\sum_{k\ne{i}}^{n_{teams}}n_i*n_k"/>

And again we sum this summation for every team but don't count relationships twice. The equivalent double summation on the right is how this formula is actully implemented on line 21 of calc.py.
<p align="center">
 <img src="https://latex.codecogs.com/gif.latex?n_{comp}=\frac{1}{2}\sum_{i=1}^{n_{teams}}\sum_{k\ne{i}}^{n_{teams}}n_i*n_k=\sum_{i=1}^{n_{teams}}\sum_{k=i+1}^{n_{teams}}n_i*n_k"/>  


For indicating if the set of teams is more cooperative or competitive we will simply use a "friendly" score set by:

<p align="center">
 <img src="https://latex.codecogs.com/gif.latex?s_{f}=\frac{n_{coop}}{n_{comp}}"/>  


# Two Equal Size Teams
Let's examine some special cases for two equal size teams before generalizing.
### Perfectly Competitive
If each team has only one player then there is only one relationship and that relationship is competitive. This is the "unhappy marriage" case.
### Twice as Competitive as Cooperative
If each team has two players there are only 2 cooperative links (one per team) and 4 total competitive links which results in <img src="https://latex.codecogs.com/gif.latex?s_{f}=0.5"/>. Think spikeball.
<p align="center">
 <img src="https://cdn.shopify.com/s/files/1/0152/1325/files/SPIKEBALL_2016_COMBO_0878.jpg?v=1576690897" width="480" height="320"/>  

### General Case
With two teams of equal size the friendly score asymptotically approaches 1 as the team size increases but it will never be greater than 1. If you simplify the equations above with two teams of equal size you end up with a friendly score:  
<p align="center">  
 <img src="https://latex.codecogs.com/gif.latex?s_{f}=\frac{n*(n-1)}{n^2}"/>  

In a world of two roughly equal size teams there will always be more competition than cooperation. Yay politics.  
<p align="center">
<img src="/img/2teams_equal.png" width=600, height=375/>  

# What About Two Variable Size Teams? 
Modeling for two teams, between 10 and 50 members each, results in the following graph.
<p align="center">
<img src="/img/2variable_teams.jpeg" width=600, height=375/>  

A better visualization with a different color mapping for instances where <img src="https://latex.codecogs.com/gif.latex?s_{f}<1.0"/>
<p align="center">
<img src="/img/2teams.gif" width=600, height=375/>

If the size of the two teams is chosen uniformly at random (which is a gross oversimplification, really a [multivariate Gaussian](https://en.wikipedia.org/wiki/Multivariate_normal_distribution) would be more appropriate) then for teams between 10 and 50 players <p align="center">	
<img src="https://latex.codecogs.com/gif.latex?P(s_{f}>1.0)=0.6625\leftarrow{n_i\in[1..50],i\in[1..2]}"/>

As the maximum potential size of the two teams increases so does the probablility that a randomly selected set of team sizes will have <img src="https://latex.codecogs.com/gif.latex?s_{f}>1.0"/>. Here are two more examples.

<p align="center">	
<img src="https://latex.codecogs.com/gif.latex?P(s_{f}>1.0)=0.8844\leftarrow{n_i\in[1..250],i\in[1..2]}"/>
<p align="center">	
<img src="https://latex.codecogs.com/gif.latex?P(s_{f}>1.0)=0.9176\leftarrow{n_i\in[1..500],i\in[1..2]}"/>

The asymptotic curve [plotted previously](https://github.com/WyattJordan/comp_vs_coop#general-case) for two equal size teams should be hidden in the purple region here where <img src="https://latex.codecogs.com/gif.latex?s_{f}<1.0"/>. Zooming in to this region proves it's still there (it's the lowest edge along the surface).  
<p align="center">
<img src="/img/2teams_uncooperative.gif" width=600, height=375/>
     
# What About Three Variable Size Teams?
<p align="center">
Ask and you shall receive. Higher friendliness scores are lighter color points.
<p align="center">
<img src="/img/three_teams_formatted.jpeg" width=600, height=429/>

<p align="center">
The tesseract in motion.
<p align="center">  
<img src="/img/three_teams_comp.gif" width=600, height=429/>

The probability of a randomly selected set of team sizes such that <img src="https://latex.codecogs.com/gif.latex?s_{f}>1.0"/> drops drastically when three teams are involved. In this case the probability becomes
<p align="center">	
<img src="https://latex.codecogs.com/gif.latex?P(s_{f}>1.0)=0.00188\leftarrow{n_i\in[10..50],i\in[1..3]}"/>
 
<p align="center">	
Plotting only instances where <img src="https://latex.codecogs.com/gif.latex?s_{f}>1.0"/>
<p align="center">  
<img src="/img/three_teams_coop.jpeg" width=600, height=429/>

Increasing the potential team size for three different teams also increases the probability that a randomly selected set of team sizes will have <img src="https://latex.codecogs.com/gif.latex?s_{f}>1.0"/> 
<p align="center">	
<img src="https://latex.codecogs.com/gif.latex?P(s_{f}>1.0)=0.04101\leftarrow{n_i\in[10..100],i\in[1..3]}"/>
<p align="center">	
<img src="https://latex.codecogs.com/gif.latex?P(s_{f}>1.0)=0.10054\leftarrow{n_i\in[10..250],i\in[1..3]}"/>


# What About Real World Data?
If we use the size of each fanbase for various sports leagues we can rank which have the highest amount of cooperation relative to competition. Sources gathered from [stadium-maps](http://www.stadium-maps.com) based on social media data.
| Sports League   | Friendliness Score | Number of Teams |
| -------------   | ------------------ | --------------- |
|Premier  Soccer  | 0.1989             | 20      |
|MLS              | 0.1023             | 26      |
|NBA              | 0.0716             | 30      |
|NHL              | 0.0538             | 31      |
|NFL              | 0.0446             | 32      |

The friendliness score decreases as the number of teams increases which is consistent with the probabilities calculated above.  

# What About Partial Cooperation Between Competing Teams?
But even in competition there can be cooperation. Tournaments often provide opportunities for competiting teams to support one another via cheering or other means in defeating a more formidable opponent. So let's edit our equations to account for this. Let's say there is one main goal every team is striving for or against and they have a normalized score value which indicates their cooperation or hostility towards this goal (<img src="https://latex.codecogs.com/gif.latex?s_{i}"/>). If we have a vector <img src="https://latex.codecogs.com/gif.latex?S"/> containing <img src="https://latex.codecogs.com/gif.latex?s_{i}"/> for every team we can generate an appropriate relationship table <img src="https://latex.codecogs.com/gif.latex?R"/> between all teams. 

<p align="center">	
<img src="https://latex.codecogs.com/gif.latex?R=S\times{S^{T}}"/>

Our calc.py expects relationships between 0 and 1 so let's scale this table and then multiply by 1/2 because teams are still primarily in competition and only in cooperation when it benefits them.  
<p align="center">	
<img src="https://latex.codecogs.com/gif.latex?R=\frac{1}{2}*(R-min(R))/max(R)"/>

The new way to calculate the number of competitive connections is now:
<p align="center">
 <img src="https://latex.codecogs.com/gif.latex?n_{comp}=\sum_{i=1}^{n_{teams}}\sum_{k\ne{i}}^{n_{teams}}n_i*n_k*r_{i,k}"/>  

# What About a Real World Example?
Let's use countries as teams with size equal to their population and scores based on their democracy index ([population data](https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population), [democracy data](https://en.wikipedia.org/wiki/Democracy_Index), [convert wiki tables to csv](https://wikitable2csv.ggor.de/)). Crunching these numbers we get a world friendliness score of:

<p align="center">
 <img src="https://latex.codecogs.com/gif.latex?s_f=0.3257"/>  

# What About a Conclusion
Clearly this result about the world's cooperation vs competition based on democracy is accurate and should have a major impact on your life. I did this more for the visualizations and because I thought the process was intriguing. There are many improvements that could be made if an accurate estimate of the world friendliness score was desired. The first would be using multiple indices for gauging relationships rather than just democracy score. This would also lead to multiple sets of teams based on the indices chosen (we only used nations here due to our chosen democracy index). Finally we would have to scale the strength of each relationship for each index based on the value structure of the individuals involved. Someone might not mind you adhere to their opposing political party if they value which sports team you support more than politics. To each their own.