# User Journey Mapper Skill

Automatically creates visual user journey maps in Figma from structured markdown files.

## Folder Structure

```
journey-figma-creator/
├── SKILL.md             # Skill definition with YAML frontmatter
├── implementation.js    # Figma code implementation
├── template.md          # Blank template for new journeys
├── QUICK_START.md       # 3-step quick reference
├── README.md            # This file
└── examples/
    └── README.md        # Example journey maps
```

## Quick Start

1. **Prepare your markdown file** following the format in `template.md`
2. **Connect to Figma** (or have the Figma file URL ready)
3. **Run the command:**
   ```
   Create a journey map from /path/to/your-journey.md
   ```

## Example

```
Create a journey map from DI&A/user-journey-shirley.md
```

This will:
- Parse the markdown structure (created by user-journey skill)
- Extract phases, actions, pain points, and opportunities
- Generate a complete Figma journey map with proper layout and styling
- Validate with a screenshot

## Markdown Format Required

Your markdown file should include these sections:

### Required Sections

```markdown
# User Journey Map: [Title]

## Actor Profile
**Name:** [Name]
**Role:** [Role]
**Organization:** [Org]
**Team:** [Team]
**Key Responsibilities:**
- [Responsibility 1]
- [Responsibility 2]

## Scenario
**Goal:** [Main goal]
**Context:** [Context]
**Expectations:**
- [Expectation 1]

## Journey Map

### Phase 1: [Phase Name]
**Timeline:** [Timeline]

**Actions:**
- [Action 1]
- [Action 2]

**Mindsets:**
> "[Quote]"
- [Thought 1]

**Emotions:** [Description] (rating/5)
- [Detail]

**Pain Points:**
- [Pain point 1]

---

### Phase 2: [Next Phase]
[... repeat structure ...]
```

### Optional Sections

```markdown
## Key Opportunities
### 1. **[Opportunity Name]**
- **Issue:** [Description]
- **Impact:** [Impact]
- **Success Metric:** [Metric]
- **Quote:** "[Quote]"
```

## What Gets Created in Figma

The skill generates a comprehensive journey map with:

✓ **Phase columns** (left-to-right flow)
- Color-coded by phase
- Trigger and timeline cards
- Action items with bullet points
- Data sources used

✓ **Pain points row** (bottom section)
- Red-bordered cards per phase
- Warning icons
- Extracted from Pain Points sections

✓ **Tools & systems row**
- Blue cards showing tools used
- Extracted from actions and context

✓ **Context boxes** (footer)
- User profile and role information
- Key opportunities
- Insights and recommendations

## Customization

### Colors

Phase colors cycle through:
1. Light blue (Initiation)
2. Light green (Data/Research)
3. Light orange (Building)
4. Light purple (Validation)
5. Light pink (Presentation)
6. Light yellow (Tracking)

### Layout

- **Width:** Auto-calculated based on number of phases (~960px per phase)
- **Height:** ~1800px
- **Phase spacing:** 40px padding
- **Card spacing:** 45px vertical between action items

### Typography

- **Title:** Inter Bold 48px
- **Phase headers:** Inter Semi Bold 20px
- **Actions:** Inter Regular 11px
- **Pain points:** Inter Regular 10px with ⚠ icon

## Tips

1. **Keep actions concise** - First 4 actions per phase are shown (to fit layout)
2. **Use specific quotes** - Quotes add authenticity and context
3. **Rate emotions** - Use X/5 scale for emotional journey tracking
4. **Be specific with pain points** - These become the key insights
5. **Include data sources** - Shows research thoroughness

## Troubleshooting

**Issue:** Markdown structure not recognized
- **Fix:** Check that headers use exact format (`### Phase 1:` with space after colon)

**Issue:** Image too large error (>8000px)
- **Fix:** Reduce number of phases or the skill will auto-adjust

**Issue:** Missing sections in output
- **Fix:** Add optional sections like tools or opportunities if needed

**Issue:** Text overflow in cards
- **Fix:** Shorten action descriptions to 1-2 lines

## Advanced Usage

### Multiple Journey Maps

Create multiple journey maps from different personas:

```
Create journey maps from:
- DI&A/user-journey-shirley.md
- DI&A/user-journey-alex.md
- DI&A/user-journey-maria.md
```

### Custom Figma File

Specify the Figma file URL:

```
Create a journey map from user-journey.md in https://figma.com/file/abc123
```

### Export Options

After creation, you can:
- Screenshot at different scales
- Export as PDF
- Share Figma link with stakeholders

## File References

- **Skill definition:** `SKILL.md` (with YAML frontmatter)
- **Implementation code:** `implementation.js`
- **Blank template:** `template.md`
- **Quick start guide:** `QUICK_START.md`
- **Example input:** `DI&A/user-journey-shirley.md` (created by user-journey skill)
- **Example output:** [Shirley_journey Figma file](https://www.figma.com/design/4n4jbHzgnbk6NhfNPF7fME/Shirley_journey)

## Installation

This skill is already available in your `.claude/skills/` directory. No installation needed.

To use it, simply invoke:
```
Create a journey map from [your-file.md]
```

## Version

v1.0.0 - Initial release supporting 6-phase journey maps with full context

## Credits

Created for researcher UX workflows. Based on Nielsen Norman Group journey mapping best practices.
