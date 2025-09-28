from typing import Dict

class InputCollector:
    def collect_inputs(self) -> Dict:
        print("\n=== Image Requirements Collection ===")
        return {
            'description': input("Image description: "),
            'required': input("Required elements (comma-separated): ").split(','),
            'excluded': input("Excluded elements (comma-separated): ").split(','),
            'style': input("Art style (e.g., realistic, cartoonish): "),
            'color_palette': input("Color preferences: ")
        }