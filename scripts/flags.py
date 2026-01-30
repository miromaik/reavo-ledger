FLAGS = {
    # CRITICAL (weight 4-5) - most problematic clauses
    "AI_TRAINING": {
        "keywords": ["train", "training", "machine learning", "artificial intelligence",
                    "ml model", "algorithm", "develop model", "improve service",
                    "analyze content", "automated systems"],
        "severity": "critical",
        "description": "Your content may be used to train AI models"
    },
    "PERPETUAL_LICENSE": {
        "keywords": ["perpetual", "irrevocable", "permanent", "indefinite",
                    "survives termination", "continues after"],
        "severity": "critical",
        "description": "License to your content never expires"
    },
    "BROAD_IP_GRANT": {
        "keywords": ["worldwide", "royalty-free", "sublicensable", "transferable",
                    "derivative works", "modify", "adapt", "translate"],
        "severity": "critical",
        "description": "Very broad rights granted to your intellectual property"
    },
    "WAIVE_MORAL_RIGHTS": {
        "keywords": ["waive moral rights", "moral rights", "attribution waive",
                    "integrity waive", "paternity rights"],
        "severity": "critical",
        "description": "You waive moral rights to your content"
    },
    
    # HIGH (weight 3) - serious concerns
    "THIRD_PARTY_SHARING": {
        "keywords": ["third party", "third-party", "share with", "partners",
                    "affiliates", "service providers", "contractors", "vendors"],
        "severity": "high",
        "description": "Data may be shared with third parties"
    },
    "MANDATORY_ARBITRATION": {
        "keywords": ["arbitration", "class action waiver", "jury trial", "binding arbitration",
                    "dispute resolution", "waive right to sue"],
        "severity": "high",
        "description": "Forced arbitration instead of court"
    },
    "UNLIMITED_LIABILITY": {
        "keywords": ["indemnify", "hold harmless", "defend against", "liable for",
                    "responsible for all", "you agree to pay"],
        "severity": "high",
        "description": "Unlimited user liability"
    },
    "AUTO_RENEWAL": {
        "keywords": ["auto-renew", "automatic renewal", "automatically renew",
                    "subscription continues", "recurring charge", "auto-pay"],
        "severity": "high",
        "description": "Automatic subscription renewal"
    },
    "SELL_YOUR_DATA": {
        "keywords": ["sell", "monetize", "commercial purposes", "advertising purposes",
                    "marketing purposes", "sell information"],
        "severity": "high",
        "description": "May sell or monetize your data"
    },
    
    # MEDIUM (weight 2) - notable issues
    "EXTENSIVE_TRACKING": {
        "keywords": ["tracking", "cookies", "analytics", "pixel", "web beacon",
                    "device information", "browsing", "fingerprint"],
        "severity": "medium",
        "description": "Extensive activity tracking"
    },
    "DATA_RETENTION": {
        "keywords": ["retain data", "store indefinitely", "backup", "archive",
                    "reasonable time", "retain information"],
        "severity": "medium",
        "description": "Long-term data retention"
    },
    "UNILATERAL_CHANGES": {
        "keywords": ["modify terms", "change without notice", "sole discretion",
                    "update terms", "revise", "amend at any time"],
        "severity": "medium",
        "description": "Can change terms unilaterally"
    },
    "ACCOUNT_TERMINATION": {
        "keywords": ["suspend", "terminate", "close account", "disable",
                    "ban", "remove access", "revoke"],
        "severity": "medium",
        "description": "Account can be suspended or terminated"
    },
    "GEOFENCING": {
        "keywords": ["geographic restriction", "region", "country", "location-based",
                    "not available in", "geo-block"],
        "severity": "medium",
        "description": "Geographic restrictions"
    },
    "NO_REFUND": {
        "keywords": ["no refund", "non-refundable", "no money back", "final sale",
                    "cannot cancel"],
        "severity": "medium",
        "description": "No refund policy"
    },
    "BROAD_CONTENT_LICENSE": {
        "keywords": ["use your content", "display publicly", "distribute", "reproduce",
                    "publicly perform", "make available"],
        "severity": "medium",
        "description": "Broad license to use your content"
    },
    
    # LOW (weight 1) - less critical but worth noting
    "AGE_RESTRICTION": {
        "keywords": ["age 13", "age 16", "age 18", "minor", "parental consent",
                    "years of age"],
        "severity": "low",
        "description": "Age restrictions apply"
    },
    "NO_WARRANTY": {
        "keywords": ["no warranty", "as is", "as available", "without guarantee",
                    "disclaim", "no representations"],
        "severity": "low",
        "description": "Service provided without warranty"
    },
    "LIMITED_LIABILITY": {
        "keywords": ["limit liability", "not liable for", "maximum liability",
                    "exclude liability", "not responsible"],
        "severity": "low",
        "description": "Limited company liability"
    },
    "FOREIGN_LAW": {
        "keywords": ["california law", "delaware law", "united states law",
                    "governed by", "jurisdiction", "exclusive venue"],
        "severity": "low",
        "description": "Governed by foreign law"
    },
    "USER_CONTENT_RESPONSIBILITY": {
        "keywords": ["responsible for content", "your responsibility", "you are liable",
                    "user-generated content", "your submissions"],
        "severity": "low",
        "description": "You're responsible for your content"
    },
    
    # POSITIVE (bonus) - actually good things
    "GDPR_COMPLIANT": {
        "keywords": ["gdpr", "right to deletion", "data portability", "right to access",
                    "data protection", "privacy by design", "legitimate interest"],
        "severity": "positive",
        "description": "GDPR compliant (good for users)"
    },
    "TRANSPARENT_PRACTICES": {
        "keywords": ["transparent", "clear notice", "inform you", "notify users",
                    "specific purposes", "limited purposes"],
        "severity": "positive",
        "description": "Transparent data practices"
    },
    "EASY_DELETION": {
        "keywords": ["delete account", "remove data", "export data", "download data",
                    "account deletion", "data erasure"],
        "severity": "positive",
        "description": "Easy account and data deletion"
    },
    "OPT_IN": {
        "keywords": ["opt-in", "explicit consent", "prior consent", "ask permission",
                    "you control", "your choice"],
        "severity": "positive",
        "description": "Opt-in consent model"
    },
    "LIMITED_DATA_COLLECTION": {
        "keywords": ["minimal data", "only necessary", "limited collection",
                    "data minimization", "essential data"],
        "severity": "positive",
        "description": "Collects only necessary data"
    },
}

WEIGHTS = {
    # Negative weights
    "AI_TRAINING": -5,
    "PERPETUAL_LICENSE": -5,
    "BROAD_IP_GRANT": -4,
    "WAIVE_MORAL_RIGHTS": -5,
    "THIRD_PARTY_SHARING": -3,
    "MANDATORY_ARBITRATION": -3,
    "UNLIMITED_LIABILITY": -4,
    "AUTO_RENEWAL": -3,
    "SELL_YOUR_DATA": -4,
    "EXTENSIVE_TRACKING": -2,
    "DATA_RETENTION": -2,
    "UNILATERAL_CHANGES": -2,
    "ACCOUNT_TERMINATION": -2,
    "GEOFENCING": -2,
    "NO_REFUND": -2,
    "BROAD_CONTENT_LICENSE": -2,
    "AGE_RESTRICTION": -1,
    "NO_WARRANTY": -1,
    "LIMITED_LIABILITY": -1,
    "FOREIGN_LAW": -1,
    "USER_CONTENT_RESPONSIBILITY": -1,
    
    # Positive weights
    "GDPR_COMPLIANT": +3,
    "TRANSPARENT_PRACTICES": +2,
    "EASY_DELETION": +2,
    "OPT_IN": +2,
    "LIMITED_DATA_COLLECTION": +2,
}

# Grading system A-F
GRADE_THRESHOLDS = {
    "A": (3, float('inf')),      # 3+ points (has positive flags)
    "B": (-3, 3),                 # -3 to 3 points
    "C": (-8, -3),                # -8 to -3 points
    "D": (-15, -8),               # -15 to -8 points
    "E": (-22, -15),              # -22 to -15 points
    "F": (float('-inf'), -22),    # below -22 points
}

def detect_flags(text: str) -> dict:
    """
    Detects flags in ToS text
    
    Args:
        text: ToS text to analyze
        
    Returns:
        dict with found_flags, details, total_score, and grade
    """
    import re
    text = text.lower()
    found = []
    details = {}
    
    for flag, config in FLAGS.items():
        matches = []
        for keyword in config["keywords"]:
            # Use word boundaries for better matching
            pattern = r'\b' + re.escape(keyword) + r'\b'
            if re.search(pattern, text, re.IGNORECASE):
                matches.append(keyword)
        
        if matches:
            found.append(flag)
            details[flag] = {
                "severity": config["severity"],
                "description": config["description"],
                "matched_keywords": matches[:3],  # Limit to first 3 matches
                "weight": WEIGHTS[flag]
            }
    
    # Calculate total score
    total_score = sum(WEIGHTS[flag] for flag in found)
    
    # Determine grade
    grade = "F"
    for grade_letter, (min_score, max_score) in GRADE_THRESHOLDS.items():
        if min_score <= total_score < max_score:
            grade = grade_letter
            break
    
    return {
        'found_flags': found,
        'details': details,
        'total_score': total_score,
        'grade': grade,
        'flag_count': len(found),
        'critical_count': sum(1 for f in found if FLAGS[f]["severity"] == "critical"),
        'positive_count': sum(1 for f in found if FLAGS[f]["severity"] == "positive")
    }

def get_grade_color(grade: str) -> str:
    """Returns color code for grade"""
    colors = {
        "A": "#22c55e",  # green
        "B": "#84cc16",  # lime
        "C": "#eab308",  # yellow
        "D": "#f97316",  # orange
        "E": "#ef4444",  # red
        "F": "#dc2626",  # dark red
    }
    return colors.get(grade, "#6b7280")

def get_grade_explanation(grade: str) -> str:
    """Returns explanation for given grade"""
    explanations = {
        "A": "Excellent terms - very user-friendly",
        "B": "Good terms - minor concerns",
        "C": "Fair terms - some notable issues",
        "D": "Poor terms - several concerning clauses",
        "E": "Very poor terms - many problematic clauses",
        "F": "Terrible terms - highly unfavorable to users"
    }
    return explanations.get(grade, "Unknown grade")