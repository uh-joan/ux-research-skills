# User Journey Mapper - Quick Start Guide

## 🚀 Get Started in 3 Steps

### Step 1: Prepare Your Markdown
Copy `template.md` or use this minimal structure:

```markdown
# User Journey Map: [Title]

## Actor Profile
**Name:** [Name]
**Role:** [Role]
**Organization:** [Org]

## Scenario
**Goal:** [Goal]

## Journey Map

### Phase 1: [Phase Name]
**Timeline:** [When]
**Actions:**
- [Action 1]
- [Action 2]
**Emotions:** [Description] (X/5)
**Pain Points:**
- [Pain 1]
```

### Step 2: Run the Command
```bash
Create a journey map from DI&A/my-journey.md
```

Or with a specific Figma file:
```bash
Create a journey map from DI&A/my-journey.md in https://figma.com/design/YOUR_FILE_KEY
```

### Step 3: Review in Figma
The skill will:
1. ✅ Parse your markdown
2. ✅ Create the journey map layout
3. ✅ Take a validation screenshot
4. ✅ Return the Figma link

## 📋 What You Need

**Minimum markdown sections:**
- Actor Profile (name, role)
- At least 2 phases with actions and pain points

**Optional but recommended:**
- Emotions with ratings (adds depth)
- Mindset quotes (adds authenticity)
- Key Opportunities (actionable insights)
- Tools/data sources (workflow context)

## 🎨 What You Get

A professional Figma journey map with:
- ✅ Color-coded phase columns
- ✅ Action cards with bullet points
- ✅ Pain points section (red cards)
- ✅ Tools & systems row
- ✅ Context boxes with user profile
- ✅ Opportunities section

## 💡 Pro Tips

1. **Quote liberally** - Add `> "User quotes"` for authenticity
2. **Rate emotions** - Use 1-5 scale: 1=frustrated, 5=delighted
3. **Be specific** - "Data source deviations cause 2hr delays" > "Data issues"
4. **Limit actions** - First 4 actions per phase are shown (keeps it readable)
5. **Use validation screenshot** - Check alignment before sharing

## 🔗 Resources

- **Full docs:** See `README.md`
- **Template:** Copy `template.md`
- **Examples:** Check `examples/README.md`
- **Implementation:** Review `implementation.js` for customization

## ⚡ Example

```bash
# Use markdown created by user-journey skill
Create a journey map from DI&A/user-journey-shirley.md
```

**Output:** [Shirley's Journey Map](https://www.figma.com/design/4n4jbHzgnbk6NhfNPF7fME/Shirley_journey)

## ❓ Common Issues

**"Markdown structure not recognized"**
→ Check phase headers: `### Phase 1: Name` (space after colon)

**"Image too large (>8000px)"**
→ Skill auto-adjusts, or reduce phase count

**"Missing Figma connection"**
→ Provide Figma URL: `... in https://figma.com/design/abc123`

---

**Need help?** See full documentation in `README.md`
