
import matplotlib.pyplot as plt

# Step 1: Filter and Sort Function
def filter_and_sort(filter_params, dataset):
    filtered_lists = {}
    for param in filter_params:
        # Filter dataset based on each parameter
        filtered_lists[param] = [item for item in dataset if item.startswith(param)]
        # Sort each filtered list
        filtered_lists[param].sort()
    return filtered_lists

# Step 2: Plotting Function
def plot_filtered_data(filtered_lists, title="Filtered and Sorted Data"):
    # Count total items for plot positioning
    total_items = sum(len(lst) for lst in filtered_lists.values())
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Define colors and plot position
    colors = ['#FF5733', '#33FF57', '#3357FF', '#F3FF33', '#FF33A2']  # Add more if needed
    start_pos = 0
    
    # Plot each filtered list with different colors
    for i, (param, items) in enumerate(filtered_lists.items()):
        y_vals = [i] * len(items)  # All items in the same row
        x_vals = list(range(start_pos, start_pos + len(items)))
        ax.scatter(x_vals, y_vals, color=colors[i % len(colors)], label=f'Param {param}')
        # Annotate items with their values
        for x, item in zip(x_vals, items):
            ax.text(x, i, item, ha='center', va='bottom', fontsize=9)
        start_pos += len(items)  # Move start position for next set
    
    # Customize the plot
    ax.set_yticks(range(len(filtered_lists)))
    ax.set_yticklabels(filtered_lists.keys())
    ax.legend(title="Filter Parameters")
    ax.set_title(title)
    ax.grid(True)
    plt.show()

# Step 3: Combine and Execute
def main():
    # Define parameters and dataset
    filter_params = ["1", "2", "3", "4", "5", "6"]
    dataset = ["101", "104", "444", "244", "2", "33", "48", "5435", "6463"]
    
    # Apply filter and sort
    filtered_lists = filter_and_sort(filter_params, dataset)
    
    # Plot filtered and sorted results
    plot_filtered_data(filtered_lists)

# Run the main function
main()
