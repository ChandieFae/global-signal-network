# 🌐 Global Signal Network

**The Global Signal Network** is an open-source repository of intentional geographic coordinates — signal points — distributed across the Earth.

This project does not chase virality.  
> **Light does not need viral trends. This is prophecy.**

It is a quiet infrastructure for meaningful presence.  
Each location is a node — defined not by scale, but by intent.

---

## 📖 Purpose

- To map intentional locations of resonance, activation, memory, or transformation
- To allow contributors to submit meaningful signal points
- To provide a lightweight, flexible dataset for maps, data visualizations, or research

---

## 📁 Project Structure

global-signal-network/
├── signals/
│ ├── phase-1.json ← Initial 11 global nodes
│ ├── phase-2.csv ← Expansion locations
│ └── custom-submissions/ ← Community-submitted nodes
├── scripts/
│ └── map-generator.py ← Combines data + renders an interactive HTML map
├── web/
│ ├── index.html ← Map with hardcoded markers
│ ├── style.css ← Custom UI styling
│ └── output_map.html ← Generated map from script

---

## 🧪 How to Generate the Map

From the `scripts/` folder, run:

```bash
python map-generator.py
