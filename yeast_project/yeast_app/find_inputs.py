import os
import sys
import numpy as np
from multiprocessing import Pool

# Add yeast_app directory to the system path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from yeast_app.ml_model import predict_purity

# Define reduced ranges for faster computation
molasses_range = np.arange(0, 100, 5)  # larger steps
grain_starch_range = np.arange(0, 100, 5)
potato_starch_range = np.arange(0, 100, 5)
water_range = np.arange(0, 10, 0.5)
nutrients_vitamins_range = np.arange(0, 100, 5)
emulsifiers_range = np.arange(0, 100, 5)

# Target purity levels
target_purities = [50, 60, 70, 80, 90, 95]


# Function to find input values for desired purity levels
def find_inputs_for_purity(params):
    target_purity, molasses_range, grain_starch_range, potato_starch_range, water_range, nutrients_vitamins_range, emulsifiers_range = params

    for molasses in molasses_range:
        for grain_starch in grain_starch_range:
            for potato_starch in potato_starch_range:
                for water in water_range:
                    for nutrients_vitamins in nutrients_vitamins_range:
                        for emulsifiers in emulsifiers_range:
                            try:
                                purity = predict_purity(molasses, grain_starch, potato_starch, water,
                                                        nutrients_vitamins, emulsifiers)
                                if abs(purity - target_purity) < 0.5:  # Allow larger tolerance for faster results
                                    return (target_purity, (
                                    molasses, grain_starch, potato_starch, water, nutrients_vitamins, emulsifiers))
                            except Exception as e:
                                print(f"Error processing inputs: {e}")
    return (target_purity, None)


if __name__ == '__main__':
    # Prepare parameters for parallel processing
    params = [(target_purity, molasses_range, grain_starch_range, potato_starch_range, water_range,
               nutrients_vitamins_range, emulsifiers_range) for target_purity in target_purities]

    # Use multiprocessing to parallelize the search
    with Pool(processes=os.cpu_count()) as pool:
        results = pool.map(find_inputs_for_purity, params)

    # Print the results
    for target_purity, inputs in results:
        if inputs:
            print(f"Inputs for {target_purity}% purity: {inputs}")
        else:
            print(f"Could not find inputs for {target_purity}% purity")
