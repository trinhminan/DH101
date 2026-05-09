---
layout: default
title: How I Use AI
permalink: /pages/how-i-use-ai/
---

# How I Use AI

This page documents **where, how, and why** I used generative AI tools in DH101. My goal is not to hide AI use or to outsource the “thinking” work of the course, but to make AI involvement **legible**, **bounded**, and **verifiable**.

## My Approach (Principles)
1. **Transparency by default.** Every Make has an *Attribution & AI Use* section, and each week has a corresponding AI-use log entry.
2. **Human authorship of claims.** I treat AI as a drafting/ideation tool, not an authority. The critical argument, framing, and final editorial decisions are mine.
3. **Verification before publishing.** Any AI-assisted factual claims, quotations, or numerical estimates must be checked against the primary text, course reading, or cited source.
4. **Minimum necessary automation.** If a task is better served by close reading, manual analysis, or lived experience, I do it myself.

## Tools I Used (and What I Use Them For)

### Writing + Reasoning
- **GPT / ChatGPT (LLM):** brainstorming, outlining, sentence-level clarity edits, generating alternative phrasings, and (in specific weeks) drafting interpretive “first passes” that I then revise.
- **GitHub Copilot (VS Code):** small coding assists (HTML/CSS snippets, quick refactors). I treat suggestions as untrusted drafts and keep only what I understand.

### Images + Media
- **DALL·E / image generators:** creating synthetic images for storytelling and remix assignments (with manual selection and narrative control).
- **LTX Studio (AI video):** generating short visual sequences that I then curate and edit into a loop.
- **Canva / Slides tools:** layout and presentation design; sometimes paired with GPT for draft phrasing.

### Platforms Used as “Artifacts”
- **This Person Does Not Exist (StyleGAN2):** used as a critical object to analyze synthetic identity.
- **Character.AI:** used to create/test a chatbot persona and curate transcripts.

## Concrete Examples (AI Output Included or Modified)

### Example 1 — AI-generated interpretation I edited (Week 6)
In [makes/week06.md]({{ '/makes/week06/' | relative_url }}), I used GPT to generate an initial rhetorical/literary analysis of Shelley’s *Ozymandias*.

- **AI output included:** a draft interpretive breakdown (irony, imagery, symbolism, narrative framing).
- **What I changed:** I reorganized the analysis, removed vague generalities, and kept the interpretation anchored to the poem’s language and the patterns surfaced by Voyant.
- **Verification:** I checked that all quoted lines match the poem and that interpretive claims were defensible from the text (rather than relying on “sounds right” summaries).

### Example 2 — AI-generated visuals I curated/remixed (Week 5)
In [makes/week05.md]({{ '/makes/week05/' | relative_url }}), I used LTX Studio to generate visuals from my prompt, then edited them into a coherent loop.

- **AI output included:** generated frames (typing scene → portrait → grid → blur → return).
- **What I changed:** I selected which frames to keep, set pacing, and constructed the loop so the concept (individual → abstraction) is readable.
- **Verification:** I reviewed the output for unintended stereotypes (e.g., “default” portrait conventions) and adjusted selection/sequence to foreground critique rather than aestheticizing bias.

## Human vs. AI Contributions (Site-wide)

### How I mark it
- **On each Make:** a section titled *Attribution & AI Use* (tools, what AI generated, what I authored/decided).
- **In reflections:** an *AI Use & Verification* note stating whether generative AI was used for drafting, outlining, or editing—and what I checked.
- **Weekly logs:** an AI-use log entry per week in the [ai-log/](../ai-log/) section, so disclosures are centralized and consistent.
- **Weekly logs:** an AI-use log entry per week in the [ai-log/]({{ '/ai-log/' | relative_url }}) section, so disclosures are centralized and consistent.

### What counts as “AI contribution” here
- Draft text, alternative phrasings, outlines, summaries, generated images/video, or any model-produced content that ends up on the site.

### What remains human work
- Selecting the question, defining the argument, deciding what counts as evidence, crafting the final narrative voice, and doing final editorial judgment.

## Verification, Correction, and What I Don’t Trust AI To Do
I assume LLM output can be **confidently wrong**. To avoid “plausible nonsense,” I use a simple checklist:

- **Quotes:** verify against the primary text.
- **Numbers/claims:** verify against a cited source; if I can’t find a source, I don’t publish the claim.
- **Conceptual framing:** align with course readings, not just AI-generated summaries.
- **Images:** review for representational bias and unintended harmful tropes.

## Limits, Bias, and Ethical Considerations (With Specificity)

### “Stochastic parrots” and the illusion of understanding (Bender et al.)
Large language models can produce fluent academic-sounding writing without grounded comprehension. In practice, this shows up when a model:
- invents citations,
- merges concepts from different authors,
- or produces ethical claims as generic “fairness” statements without power analysis.

My response is to treat LLM output as **draft material** and to keep my arguments tied to assigned readings and concrete evidence from my artifacts.

### Power, voice, and whose knowledge counts (D’Ignazio & Klein)
*Data Feminism* stresses that data work is never neutral: it reflects power, standpoint, and exclusion. This shapes how I use AI:
- I don’t treat AI outputs as “objective.”
- I ask who is centered (whose stories, accents, or norms become the default), and who becomes an afterthought.
- When AI produces “universal” language, I revise toward specificity: *who*, *where*, *under what conditions*.

### Material and labor realities (Crawford)
Following *Atlas of AI*, I treat AI systems as material infrastructures with extractive supply chains and hidden labor. This matters ethically because:
- AI costs are distributed unevenly (workers, communities near extraction sites, data center regions).
- Convenience narratives hide coercion and environmental impacts.

So I try to minimize unnecessary prompting, avoid “just for fun” generation when it adds no learning value, and be explicit about the human labor and resources behind “automation.”

## Disclosure Policy
- I do not publish undisclosed AI-generated text or images.
- If AI helped draft, rewrite, generate, or meaningfully shape content, I disclose it in the Make’s attribution section and the weekly AI log.

## Works Referenced
- Bender, Emily M., et al. “On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?” (2021).
- D’Ignazio, Catherine, and Lauren F. Klein. *Data Feminism* (2020).
- Crawford, Kate. *Atlas of AI* (2021).