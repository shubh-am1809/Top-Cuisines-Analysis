import pandas as pd

df = pd.read_csv("dataset .csv")
df_cuisine = df['Cuisines'].dropna()
all_cuisines = df_cuisine.str.split(', ').explode()
top_cuisines = all_cuisines.value_counts().head(3)
total_restaurants = df.shape[0]

top_cuisine_percentage = (top_cuisines / total_restaurants) * 100
result = pd.DataFrame({
    'Cuisine': top_cuisines.index,
    'Restaurant Count': top_cuisines.values,
    'Percentage (%)': top_cuisine_percentage.round(2)
})
result.to_csv("output/top_cuisines_result.csv", index=False)
print(result)
