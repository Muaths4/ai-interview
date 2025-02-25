# AI Development Interview Test

## Introduction
Welcome to the AI development interview test! This task is designed to assess your skills in artificial intelligence, machine learning, and frontend development. You will create a 7-segment display reader model and a user interface that interacts with this model. Follow the instructions carefully and ensure to demonstrate best practices in coding, structure, and version control using Git.

## Project Structure
You will find two main folders in the repository:
- `ai`
- `client`

You are required to implement the following within these folders.

## Task Description

### AI Model Project
1. **Dataset**: Use the [7-segment display dataset](https://www.kaggle.com/datasets/cramatsu/7-segment-display-yolov8) from Kaggle.
2. **Technology**: You are free to choose any technology or framework (such as TensorFlow, PyTorch, etc.) to train your model.
3. **Model Training**:
    - Preprocess the dataset as required for training.
    - Train a model (or tune a pre-trained model) capable of reading 7-segment displays.
    - Save the trained model for later inference.
    - Ensure proper validation, error handling, and logging during training.
4. **Functionality**:
    - Provide a script or API to load the model and perform inference on new images.
    - Implement a way to handle model retraining if needed.
5. **Best Practices**: Follow best practices for AI model training, including data augmentation, proper model evaluation, and optimization.

### Client Project
1. **Technology**: Use [Nuxt 3](https://nuxt.com/docs/getting-started/installation) for the frontend application.
2. **Functionality**:
    - Create a user interface to upload images of 7-segment displays.
    - Display the extracted values from the uploaded images.
    - Maintain a history of the current session where users can view the images and the extracted results.
    - Integrate with the AI model to perform the inference.
3. **UI/UX**: Ensure the interface is user-friendly and visually appealing.

## Git Workflow
1. **Forking**: Fork this repository to your own GitHub account.
2. **Branching**: Use a feature-branch workflow. Create branches for different functionalities (e.g., `feature/ai-model-setup`, `feature/client-setup`).
3. **Commits**: Make frequent, clear, and descriptive commits.
4. **Pull Requests**: Once you've completed a feature, create a pull request to merge it into your main branch. Include descriptive messages with your pull requests.
5. **Git Ignore**: Make sure only the necessary files are saved to the repository. Make proper use of gitignore. 

## Additional Requirements
- **Documentation**: Add comments to your code where necessary and provide a brief documentation on how to set up and run the project.
- **Creativity**: Feel free to add any additional features or improvements that you think would make this project stand out.
- **BONUS: Testing**: Implement unit tests for the client using a framework of your choice.

## Submission
1. Ensure your project is well-documented.
2. Share the link to your forked repository with us.
3. Be prepared to discuss your code, decisions, and any challenges you faced during the development in a follow-up interview.

## Evaluation Criteria
- Adherence to best practices and coding standards.
- Clean and maintainable code.
- Proper use of git and version control best practices.
- User experience and design of the frontend application.
- Effectiveness and accuracy of the AI model.
- Creativity and any additional features implemented.
- Documentation and code comments.

## Getting Started
1. Clone your forked repository to your local machine.
2. Set up the environment for your AI model and run the training scripts.
3. Implement the required functionalities in both the `ai` and `client` folders.
4. Submit your work as described in the submission section.

We look forward to seeing your solution!
