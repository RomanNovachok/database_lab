# Auto Scaling для ECS сервісу

resource "aws_appautoscaling_target" "ecs_service" {
  service_namespace  = "ecs"
  scalable_dimension = "ecs:service:DesiredCount"

  # service/<cluster-name>/<service-name>
  resource_id = "service/${aws_ecs_cluster.app.name}/${aws_ecs_service.app.name}"

  min_capacity = 1   # мінімум 1 таска
  max_capacity = 4   # максимум 4 таски (можеш потім поміняти)
}

resource "aws_appautoscaling_policy" "cpu_target" {
  name               = "${var.project_name}-cpu-autoscaling"
  policy_type        = "TargetTrackingScaling"
  service_namespace  = aws_appautoscaling_target.ecs_service.service_namespace
  resource_id        = aws_appautoscaling_target.ecs_service.resource_id
  scalable_dimension = aws_appautoscaling_target.ecs_service.scalable_dimension

  target_tracking_scaling_policy_configuration {
    predefined_metric_specification {
      predefined_metric_type = "ECSServiceAverageCPUUtilization"
    }

    # Цільове завантаження CPU у відсотках
    target_value       = 50
    scale_in_cooldown  = 60  # пауза перед scale-in
    scale_out_cooldown = 60  # пауза перед scale-out
  }
}

output "ecs_autoscaling_resource_id" {
  value       = aws_appautoscaling_target.ecs_service.resource_id
  description = "App Auto Scaling resource id for ECS service"
}
