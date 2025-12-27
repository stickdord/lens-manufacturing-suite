"""
Quality control measurements for contact lens manufacturing.
"""

import numpy as np

def measure_center_thickness(lens_data, method='optical'):
    """
    Measure the center thickness of a soft lens.
    
    Args:
        lens_data: array of thickness measurements
        method: 'optical' or 'mechanical'
    
    Returns:
        float: center thickness in microns
    """
    if method == 'optical':
        # Use optical interferometry algorithm
        if len(lens_data) < 3:
            raise ValueError("Insufficient data points")
        # Simple average of central region
        center_idx = len(lens_data) // 2
        thickness = np.mean(lens_data[center_idx-1:center_idx+2])
    elif method == 'mechanical':
        # Use mechanical probe measurement
        thickness = np.median(lens_data)
    else:
        raise ValueError(f"Unknown method: {method}")
    
    # Convert to microns if needed
    if thickness > 1000:  # assume nm
        thickness /= 1000
    
    return thickness