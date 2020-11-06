# Is the world in harmony or discord?
# Are humans inherently good or evil?
In order to find out let's accept some absurd premises:
1. Goodness is embodied by partnering with others regardless of motivation (i.e. cooperation)
2. Evil is embodied by resisting others regardless of motivation (i.e. competition)
3. Relationships between
3. If there is more cooperation in the world than competition

good intro  
"some of us lie awake at night wondering different things..."  
"is the world more friendly or aggressive?"  
Let's do some data visualization to find out (PSA: the methods used are a gross oversimplification).

# How
Let's begin by calculating the number of competitive and cooperative relationships between a set of teams.The number of cooperative relationships in team <img src="https://latex.codecogs.com/gif.latex?i"/> with size <img src="https://latex.codecogs.com/gif.latex?n_i"/> is <img src="https://latex.codecogs.com/gif.latex?n_{i\_coop}"/> which can be calculated as the number of links in the network of team members where every member is a node connected to all other members (a perfectly dense graph).  

<p align="center">
 <img src="https://latex.codecogs.com/gif.latex?n_{i\_coop}=\frac{n_i*(n_i-1)}{2}"/>
<\p>


Note: this formula is a specific case (<img src="https://latex.codecogs.com/gif.latex?k=2"/>) of the general combination formula for taking <img src="https://latex.codecogs.com/gif.latex?k"/> elements out of a set of <img src="https://latex.codecogs.com/gif.latex?n"/> which is
<p align="center">
 <img src="https://latex.codecogs.com/gif.latex?\binom{n}{k} = \frac{n!}{k!*(n-k)!"/>
<\p>

The total number of cooperative links is therefore:
<p align="center">
 <img src="https://latex.codecogs.com/gif.latex?n_{coop} = \sum_{i=1}^{n_{teams}} n_{i\_coop}"/>
<\p>


Now to count the number of competitive relationships let's again assume both teams are fully connected graphs, meaning every team member has a competitive relationship with every member of an opposing team. Therefore the number of competitve relationships for team <img src="https://latex.codecogs.com/gif.latex?i"/> is the summation of the product of <img src="https://latex.codecogs.com/gif.latex?n_i"/> with every other team size:


<p align="center">
 <img src="https://latex.codecogs.com/gif.latex?n_{i\_comp} = \sum_{k \ne i}^{n_{teams}} n_i*n_k"/>
<\p>  

And again we sum this summation for every team but don't count relationships twice. The equivalent double summation on the right is how this formula is actully implemented on line 21 of calc.py.
<p align="center">
 <img src="https://latex.codecogs.com/gif.latex?n_{comp}  =  \frac{1}{2} \sum_{i=1}^{n_{teams}} \sum_{k \ne i}^{n_{teams}} n_i*n_k  =  \sum_{i=1}^{n_{teams}} \sum_{k=i+1}^{n_{teams}} n_i*n_k"/>
<\p>  


For indicating if the set of teams is more cooperative or competitive we will simply use a "friendly" score set by:

<p align="center">
 <img src="https://latex.codecogs.com/gif.latex?s_{f} = \frac{n_{coop}}{n_{comp}}"/>
<\p>


# Two Equal Size Teams
Let's examine some special cases for two equal size teams before generalizing.
### Perfectly Competitive
If each team has only one player then there is only one relationship and that relationship is competitive. This is the "unhappy marriage" case.
### Twice as Competitive as Cooperative
If each team has two players there are only 2 cooperative links (one per team) and 4 total competitive links which results in <img src="https://latex.codecogs.com/gif.latex?s_{f} = 0.5"/>. Think spikeball.
<p align="center">
 <img src="https://cdn.shopify.com/s/files/1/0152/1325/files/SPIKEBALL_2016_COMBO_0878.jpg?v=1576690897" width="480" height="320"/>
<\p>

### General Case
With two teams of equal size the friendly score asymptotically approaches 1 as the team size increases but it will never be greater than 1. If you simplify the equations above with two teams of equal size you end up with a friendly score:  
<p align="center">  
 <img src="https://latex.codecogs.com/gif.latex?s_{f} = \frac{n*(n-1)}{n^2}"/>  
<\p>  

In a world of equal size teams there will always be more competition than cooperation.
<p align="center">
<img src="/img/2teams_equal.png" />
<\p>

## But what happens with differing team sizes?
With teams of 
Teams between 10 and 50 players have a 66.25% chance of being more coop than comp (using uniform distribution even though we should use gaussian if we actually cared about trying to model this accurately)

Teams between 1 and 500 players have a 91.76% chance of being more coop than comp. Again this is probably unrealistic since real-world teams would probably be close to the same size. I can't think of a sport with a team of 2 facing 500.

Teams 1-250 have 88.44% chance


