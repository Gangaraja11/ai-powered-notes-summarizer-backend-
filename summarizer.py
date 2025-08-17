def generate_summary(transcript, prompt):
    if not transcript:
        return "No transcript provided."
    
    # Simple summarizer (first 3 lines only)
    lines = transcript.split(". ")
    summary = ". ".join(lines[:3]) + "..."
    
    if prompt:
        summary = f"Prompt: {prompt}\n\n{summary}"
    
    return summary