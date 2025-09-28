from agents.designer import ImageDesigner
from tasks.design import DesignTask
from tools.image_tools import ImageGeneratorTool, ImageAnalysisTool

class ImageCrew:
    def __init__(self):
        self.design_agent = create_design_agent()
        self.generator = ImageGeneratorTool()
        self.analyzer = ImageAnalysisTool()

    def run(self, query):
        # Design Phase
        design_task = DesignTask().create(self.design_agent, query)
        prompt = design_task.execute()
        
        # Generation Phase
        image = self.generator._run(prompt)
        
        # Analysis Phase
        analysis = self.analyzer._run(image)
        
        return {
            "prompt": prompt,
            "image": image,
            "analysis": analysis
        }