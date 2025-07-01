# Install Robyn package with !pip install robynpy

from robynpy import Robyn
import pandas as pd

# Load your marketing dataset (with date, sales/KPI, media spend/impressions, and other variables)
df = pd.read_csv('your_marketing_data.csv')

# Initialize Robyn model
robyn = Robyn(data=df)

# Define your variables:
# - Dependent variable (e.g., sales)
# - Paid media variables (e.g., TV impressions, digital clicks)
# - Organic variables (e.g., newsletters, social media posts without spend)
# - Context variables (e.g., seasonality, holidays, competitor activity)

robyn.set_target_variable('sales')
robyn.set_paid_media_vars(['TV_impressions', 'Digital_clicks', 'Radio_GRPs'])
robyn.set_organic_vars(['Newsletter_sends', 'Social_media_posts'])
robyn.set_context_vars(['Competitor_sales', 'Holiday'])

# Configure adstock and saturation transformations for paid media
robyn.set_adstock_type('geometric')  # or 'weibull'
robyn.set_saturation_model('hill')   # models diminishing returns

# Set bounds and constraints for hyperparameters (optional, can use defaults)
robyn.set_hyperparameter_bounds({
    'adstock_rate': (0.1, 0.9),
    'saturation_alpha': (0.1, 3),
    # Add other hyperparameters as needed
})

# Run hyperparameter optimization using evolutionary algorithms (Nevergrad)
robyn.optimize_models(
    iterations=500,  # Number of optimization iterations
    objectives=['NRMSE', 'ROI'],  # Multi-objective optimization
    population_size=50
)

# Select the best model based on fit and business metrics
best_model = robyn.select_best_model()

# Extract and analyze model outputs
print("Model coefficients and media effectiveness:")
print(best_model.coefficients_)

# Visualize channel contribution, ROI, saturation curves, and adstock effects
robyn.plot_channel_contribution(best_model)
robyn.plot_saturation_curves(best_model)
robyn.plot_adstock_effects(best_model)

# Use the model to simulate budget allocation for ROI maximization
optimal_budget = robyn.optimize_budget_allocation(best_model, total_budget=1000000)
print("Recommended budget allocation:", optimal_budget)
