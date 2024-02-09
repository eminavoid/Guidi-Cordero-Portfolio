using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class InGamePause : MonoBehaviour
{
    public void Pause()
    {
        Time.timeScale = 0;
    }
    public void Continue()
    {
        Time.timeScale = 1;

    }
    public void MainMenu()
    {
        GameManager.Instance.ResetCharacterPos();
        SceneLoader.Load(SceneLoader.Scene.MainMenu);
        Time.timeScale = 1;

    }
    private void Start()
    {
        
    }
}
