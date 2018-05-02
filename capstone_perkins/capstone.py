
# coding: utf-8

# In[1]:


from matplotlib import pyplot as plt
import pandas as pd


# In[2]:


species = pd.read_csv(r'C:\Users\Ethan\Desktop\biodiversity\species_info.csv')


# In[3]:


species.head()


# In[4]:


species.scientific_name.nunique()


# In[5]:


species.category.unique()


# In[6]:


species.conservation_status.unique()


# In[7]:


species.groupby('conservation_status').scientific_name.nunique().reset_index()


# In[8]:


species.fillna('No Intervention', inplace=True)


# In[9]:


species.groupby('conservation_status').scientific_name.nunique().reset_index()


# In[17]:


protection_counts = species.groupby('conservation_status')    .scientific_name.count().reset_index()    .sort_values(by='scientific_name')


# In[21]:


plt.figure(figsize=(10,4))
ax=plt.subplot()
plt.bar(range(len(protection_counts)),
        protection_counts.scientific_name.values)
ax.set_xticks(range(len(protection_counts))) 
ax.set_xticklabels(protection_counts.conservation_status.values)
plt.ylabel('Number of Species')
plt.xlabel('Conservation Status by Species')


# In[22]:


species['is_protected'] = species.conservation_status != 'No Intervention'


# In[23]:


category_counts = species.groupby(['category', 'is_protected']).scientific_name.nunique().reset_index()


# In[24]:


category_counts.head()


# In[25]:


category_pivot = category_counts.pivot(columns='is_protected',
                                      index='category',
                                      values='scientific_name').reset_index()


# In[26]:


category_pivot


# In[28]:


category_pivot.columns = ['category', 'not_protected', 'protected']


# In[29]:


category_pivot['percent_protected'] = category_pivot.protected / (category_pivot.protected + category_pivot.not_protected)


# In[30]:


category_pivot


# In[31]:


#Mammals/Birds
contingency = [[30, 146],
              [75, 413]]


# In[32]:


from scipy.stats import chi2_contingency


# In[33]:


chi2_contingency(contingency)


# In[34]:


#Mammals/Reptiles
contingency = [[30, 146],
              [5, 73]]


# In[35]:


chi2_contingency(contingency)


# In[3]:


from scipy.stats import chi2_contingency


# In[1]:


#Amphibian/Fish
contingency = [[7, 72],
              [11, 115]]


# In[4]:


chi2_contingency(contingency)


# In[5]:


#Nonvascular Plant/Vascular Plant
contingency = [[5,328],
              [46, 4216]]


# In[6]:


chi2_contingency(contingency)


# In[7]:


#Reptile/Fish
contingency = [[5, 73],
              [11, 115]]


# In[8]:


chi2_contingency(contingency)


# In[13]:


#Bird/Reptile
contingency = [[75, 413],
              [5, 73]]


# In[14]:


chi2_contingency(contingency)


# In[9]:


#Birds/Vascular Plants
contingency = [[75, 413],
              [46, 4216]]


# In[10]:


chi2_contingency(contingency)


# In[37]:


observations = pd.read_csv(r'C:\Users\Ethan\Desktop\biodiversity\observations.csv')
observations.head()


# In[38]:


species['is_sheep'] = species.common_names.apply(lambda x: 'Sheep' in x)
species.head()


# In[39]:


species[species.is_sheep]


# In[41]:


sheep_species = species[(species.is_sheep) & (species.category == 'Mammal')]
sheep_species


# In[42]:


sheep_observations = observations.merge(sheep_species)
sheep_observations


# In[43]:


obs_by_park = sheep_observations.groupby('park_name').observations.sum().reset_index()
obs_by_park


# In[44]:


plt.figure(figsize=(16, 4))
ax=plt.subplot()
plt.bar(range(len(obs_by_park)), obs_by_park.observations.values)
ax.set_xticks(range(len(obs_by_park)))
ax.set_xticklabels(obs_by_park.park_name.values)
plt.ylabel('Number of Observations')
plt.title('Observations of Sheep per week')
plt.show()

        


# In[45]:


minimum_detectable_effect = 100 * 0.05 / 0.15
minimum_detectable_effect


# In[46]:


baseline = 15


# In[1]:


sample_size_per_variant = 510


# In[2]:


bryce_obs_time = 510 / 250
yellowstone_obs_time = 510 / 507

