import generate_validation_data
import generate_production_data
import generate_surrogate_model
import generate_training_data

if __name__ == '__main__':
    generate_training_data.main()
    generate_validation_data.main()
    generate_production_data.main()
    generate_surrogate_model.main()
