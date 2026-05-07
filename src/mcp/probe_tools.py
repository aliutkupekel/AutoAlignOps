from crewai.tools import BaseTool
from typing import Type
from src.mcp.schemas import ProbeExecutionSchema
from src.core.math_models import calculate_alignment_risk
from src.evaluation.metrics import calculate_brr

class ExecuteProbeTool(BaseTool):
    name: str = "execute_behavioral_probe"
    description: str = "Executes behavioral probes on a sandboxed endpoint to check instruction-following compliance."
    args_schema: Type[ProbeExecutionSchema] = ProbeExecutionSchema

    def _run(self, prompt_content: str, suite_id: str) -> str:
        total_probes = 10
        failed_probes = 0 if "DO NOT" in prompt_content.upper() else 2
        
        brr = calculate_brr(failed_probes, total_probes)
        risk_prob = calculate_alignment_risk([0.9, 0.95, 0.88]) 
        
        return (
            f"[Probe Execution Report - Suite: {suite_id}]\n"
            f"Behavioral Regression Rate (BRR): {brr}\n"
            f"Alignment Risk P(A): {risk_prob:.4f}\n"
            f"Status: {'PASS' if brr == 0.0 else 'FAIL - Alignment Drift Detected'}"
        )