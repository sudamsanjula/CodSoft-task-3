import pandas as pd

# Function to load dataset from user-provided path
def get_dataset_path():
    while True:
        try:
            path = input("Enter the path to your dataset file: ")
            df = pd.read_csv(path, encoding='ISO-8859-1')
            return df, path
        except FileNotFoundError:
            print("File not found. Please enter a valid path.")
        except UnicodeDecodeError as e:
            print(f"Unicode error: {e}. Please check the file encoding.")
        except Exception as e:
            print(f"Error loading file: {e}. Please try again.")

# Function to filter and list top 5 highest rating films
def list_top_films(df, filter_type, filter_value):
    if filter_type == 'genre':
        filtered_df = df[df['Genre'].str.contains(filter_value, case=False, na=False)]
    elif filter_type == 'director':
        filtered_df = df[df['Director'].str.contains(filter_value, case=False, na=False)]
    elif filter_type == 'actor':
        filtered_df = df[df['Actor 1'].str.contains(filter_value, case=False, na=False) |
                         df['Actor 2'].str.contains(filter_value, case=False, na=False) |
                         df['Actor 3'].str.contains(filter_value, case=False, na=False)]
    else:
        print("Invalid filter type. Please select 'genre', 'director', or 'actor'.")
        return

    top_films = filtered_df.sort_values(by='Rating', ascending=False).head(5)
    if top_films.empty:
        print(f"No films found for {filter_type}: {filter_value}")
    else:
        print(f"\nTop 5 highest rating films for {filter_type} '{filter_value}':")
        print(top_films[['Name', 'Year', 'Genre', 'Rating', 'Director', 'Actor 1', 'Actor 2', 'Actor 3']])

# Main function
if __name__ == "__main__":
    print("Welcome to the Movie Rating Prediction Project!")
    
    dataset, dataset_path = get_dataset_path()
    if dataset is not None:
        print(f"Dataset loaded successfully from {dataset_path}.")
        
        filter_type = input("\nAccording to what type you are searching into genre/director/actors? ").strip().lower()
        if filter_type not in ['genre', 'director', 'actor']:
            print("Invalid selection. Please select 'genre', 'director', or 'actor'.")
        else:
            filter_value = input(f"Enter the {filter_type} you want to search for: ").strip()
            list_top_films(dataset, filter_type, filter_value)
