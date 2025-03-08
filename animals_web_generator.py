"""
Module for generating HTML website from animal data.
"""
import json
import os
from typing import Dict, List, Tuple, Set
import data_fetcher


def serialize_animal(animal: Dict) -> str:
    """
    Serializes a single animal object to HTML format.

    Args:
        animal (Dict): Dictionary containing animal information

    Returns:
        str: HTML formatted string for a single animal
    """
    output = '<li class="cards__item">\n'
    
    if "name" in animal:
        output += f'    <div class="card__title">{animal["name"]}</div>\n'
    
    output += '    <div class="card__text">\n'
    output += '        <ul class="animal__details">\n'
    
    # Check if characteristics exists
    if "characteristics" in animal:
        chars = animal["characteristics"]
        
        # Diet information
        if "diet" in chars:
            output += f'            <li class="detail__item"><strong>Diet:</strong> {chars["diet"]}</li>\n'
        
        # Location information
        if "locations" in animal and animal["locations"]:
            output += f'            <li class="detail__item"><strong>Location:</strong> {animal["locations"][0]}</li>\n'
        
        # Type information
        if "type" in chars:
            output += f'            <li class="detail__item"><strong>Type:</strong> {chars["type"]}</li>\n'
            
        # Skin type information
        if "skin_type" in chars:
            output += f'            <li class="detail__item"><strong>Skin Type:</strong> {chars["skin_type"]}</li>\n'
            
        # Lifespan information
        if "lifespan" in chars:
            output += f'            <li class="detail__item"><strong>Lifespan:</strong> {chars["lifespan"]}</li>\n'
    
    output += '        </ul>\n'
    output += '    </div>\n'
    output += '</li>\n'
    return output


def serialize_animals_list(animals: List[Dict]) -> str:
    """
    Serializes a list of animals to HTML format.

    Args:
        animals (List[Dict]): List of animal dictionaries

    Returns:
        str: Complete HTML formatted string for all animals
    """
    return "".join(serialize_animal(animal) for animal in animals)


def read_template(template_path: str) -> str:
    """
    Reads HTML template file.

    Args:
        template_path (str): Path to template file

    Returns:
        str: Content of template file
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    absolute_path = os.path.join(current_dir, template_path)
    
    with open(absolute_path, "r", encoding='utf-8') as file:
        return file.read()


def write_html(html_content: str, output_path: str) -> None:
    """
    Writes HTML content to file.

    Args:
        html_content (str): HTML content to write
        output_path (str): Path to output file
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    absolute_path = os.path.join(current_dir, output_path)
    
    with open(absolute_path, "w", encoding='utf-8') as file:
        file.write(html_content)


def get_unique_values(animals: List[Dict], field: str) -> Set[str]:
    """
    Gets all unique values for a given field from the animals data.

    Args:
        animals (List[Dict]): List of animal dictionaries
        field (str): Field to get unique values for

    Returns:
        Set[str]: Set of unique values
    """
    values = set()
    for animal in animals:
        if "characteristics" in animal and field in animal["characteristics"]:
            values.add(animal["characteristics"][field])
        elif field == "location" and "locations" in animal and animal["locations"]:
            values.add(animal["locations"][0])
    return values


def filter_animals(animals: List[Dict], filters: Dict[str, str]) -> List[Dict]:
    """
    Filters animals list by multiple criteria.

    Args:
        animals (List[Dict]): List of animal dictionaries
        filters (Dict[str, str]): Dictionary of field:value pairs to filter by

    Returns:
        List[Dict]: Filtered list of animals
    """
    filtered_animals = animals
    for field, value in filters.items():
        if value == "all":
            continue
            
        if field == "location":
            filtered_animals = [
                animal for animal in filtered_animals
                if "locations" in animal 
                and animal["locations"] 
                and animal["locations"][0] == value
            ]
        else:
            filtered_animals = [
                animal for animal in filtered_animals
                if "characteristics" in animal 
                and field in animal["characteristics"]
                and animal["characteristics"][field] == value
            ]
    
    return filtered_animals


def display_filter_menu(animals: List[Dict]) -> Dict[str, str]:
    """
    Displays filter options and gets user selections.

    Args:
        animals (List[Dict]): List of animal dictionaries

    Returns:
        Dict[str, str]: Dictionary of selected filters
    """
    filter_fields = {
        1: ("skin_type", "Skin Type"),
        2: ("diet", "Diet"),
        3: ("type", "Type"),
        4: ("location", "Location")
    }
    
    filters = {}
    print("\nFilter options:")
    for num, (field, display_name) in filter_fields.items():
        print(f"{num}. Filter by {display_name}")
    print("0. Done selecting filters")
    
    while True:
        try:
            choice = int(input("\nSelect a filter option (0 to finish): "))
            
            if choice == 0:
                break
                
            if choice not in filter_fields:
                print("Invalid choice. Please try again.")
                continue
                
            field, display_name = filter_fields[choice]
            
            # Get unique values for selected field
            values = get_unique_values(animals, field)
            print(f"\nAvailable {display_name} values:")
            sorted_values = sorted(values)
            for i, value in enumerate(sorted_values, 1):
                print(f"{i}. {value}")
            print("0. Show all")
            
            # Get user's value choice
            while True:
                try:
                    value_choice = int(input(f"\nSelect {display_name}: "))
                    if value_choice == 0:
                        filters[field] = "all"
                        break
                    if 1 <= value_choice <= len(sorted_values):
                        filters[field] = sorted_values[value_choice - 1]
                        break
                    print("Invalid choice. Please try again.")
                except ValueError:
                    print("Please enter a valid number.")
                    
        except ValueError:
            print("Please enter a valid number.")
    
    return filters


def generate_error_html(animal_name: str) -> str:
    """
    Generates an HTML error message for when no animals are found.

    Args:
        animal_name (str): The animal name that was searched for

    Returns:
        str: HTML formatted error message
    """
    return f'''
    <div class="error-message">
        <h2>Oops! No Results Found</h2>
        <p>We couldn't find any animals matching "{animal_name}".</p>
        <p>Please try searching for a different animal!</p>
        <div class="suggestions">
            <p>Popular searches:</p>
            <ul>
                <li>Fox</li>
                <li>Lion</li>
                <li>Eagle</li>
                <li>Dolphin</li>
            </ul>
        </div>
    </div>
    '''


def process_animals_to_html() -> Tuple[bool, str]:
    """
    Processes animal data and generates HTML file.

    Returns:
        Tuple[bool, str]: Success status and error message if any
    """
    try:
        # Get animal name from user
        animal_name = input("Enter a name of an animal: ")
        
        # Fetch animal data using the data_fetcher module
        animals_data = data_fetcher.fetch_data(animal_name)
        
        # Read template
        template_content = read_template("animals_template.html")
        
        if not animals_data:
            # Generate error message HTML
            error_html = generate_error_html(animal_name)
            final_html = template_content.replace("__REPLACE_ANIMALS_INFO__", error_html)
            write_html(final_html, "animals.html")
            return True, "Website was generated with no results message"
        
        # Get filter selections from user
        filters = display_filter_menu(animals_data)
        
        # Apply filters
        if filters:
            animals_data = filter_animals(animals_data, filters)
            if not animals_data:
                error_html = generate_error_html(animal_name)
                final_html = template_content.replace("__REPLACE_ANIMALS_INFO__", error_html)
                write_html(final_html, "animals.html")
                return True, "Website was generated with no results message (after filtering)"
        
        # Generate animals info string
        animals_info = serialize_animals_list(animals_data)
        final_html = template_content.replace("__REPLACE_ANIMALS_INFO__", animals_info)
        
        # Write to output file
        write_html(final_html, "animals.html")
        
        return True, "Website was successfully generated to the file animals.html"
        
    except Exception as e:
        return False, f"An unexpected error occurred: {str(e)}"


def main() -> None:
    """
    Main function to generate HTML file from animal data.
    """
    success, message = process_animals_to_html()
    print(f"\n{message}")


if __name__ == "__main__":
    mpain()