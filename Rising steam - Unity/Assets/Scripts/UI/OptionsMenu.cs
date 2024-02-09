using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI; 

public class OptionsMenu : MonoBehaviour
{
    public void VideoHigh()
    {
        QualitySettings.SetQualityLevel(6, true);
    }
    public void VideoMed()
    {
        QualitySettings.SetQualityLevel(2, true);
    }
    public void VideoLow()
    {
        QualitySettings.SetQualityLevel(0, true);
    }
}
