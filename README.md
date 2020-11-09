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
 <img src="https://latex.codecogs.com/gif.latex?n_{comp}=\frac{1}{2}\sum_{i=1}^{n_{teams}}\sum_{k\ne{i}}^{n_{teams}}n_i*n_k=\sum_{i=1}^{n_{teams}} \sum_{k=i+1}^{n_{teams}}n_i*n_k"/>  


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

If the size of the two teams is chosen uniformly at random then for teams between 10 and 50 players <p align="center">	
<img src="https://latex.codecogs.com/gif.latex?n_i\in[1..250]\rightarrow{P(s_{f}>1.0)} = 0.6625"/>.

(A uniform distribution is a terrible choice here, a [multivariate Gaussian](https://en.wikipedia.org/wiki/Multivariate_normal_distribution) would be more appropriate and result in a lower probability).  

As the maximum potential size of the two teams increases so does the probablility that a randomly selected set of team sizes will have <img src="https://latex.codecogs.com/gif.latex?s_{f}>1.0"/>. Here are two more examples.

<p align="center">	
<img src="https://latex.codecogs.com/gif.latex?n_i\in[1..250]\rightarrow{P(s_{f}>1.0)}=0.8844"/>
<p align="center">	
<img src="https://latex.codecogs.com/gif.latex?n_i\in[1..500]\rightarrow{P(s_{f}>1.0)}=0.9176"/>

The asymptotic curve [plotted previously](https://github.com/WyattJordan/comp_vs_coop#general-case) for two equal size teams should be hidden in the purple region here where <img src="https://latex.codecogs.com/gif.latex?s_{f}<1.0"/>. Zooming in to this region proves it's still there (it's the lowest edge along the surface).  
<p align="center">
<img src="/img/2teams_uncooperative.gif" width=600, height=375/>
     

